from flask import Flask, render_template, request, redirect, url_for
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Firebase 초기화
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')  # 서비스 계정 키 파일 경로
initialize_app(cred)
db = firestore.client()

# 썸네일 업로드 경로 설정
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 허용되는 파일 확장자
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# 파일 확장자 확인 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 메인 페이지: 저장된 기사들을 보여주는 페이지
@app.route('/')
def main():
    articles_ref = db.collection('articles')
    articles = articles_ref.order_by('created_at', direction=firestore.Query.DESCENDING).stream()
    articles_list = [article.to_dict() for article in articles]
    return render_template('main.html', articles=articles_list)

# 에디터 페이지: 기사를 작성하는 페이지
@app.route('/editor')
def editor():
    return render_template('editor.html')

# 기사 발행 처리
@app.route('/publish', methods=['POST'])
def publish():
    title = request.form['title']
    content = request.form['content']
    created_at = datetime.now()

    # 썸네일 파일 처리
    file = request.files['thumbnail']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # 썸네일 URL을 웹 경로로 변환
        thumbnail_url = url_for('static', filename='uploads/' + filename)
    else:
        thumbnail_url = None

    # Firestore에 데이터 저장
    db.collection('articles').add({
        'title': title,
        'thumbnail_url': thumbnail_url,
        'content': content,
        'created_at': created_at
    })

    return redirect(url_for('main'))

# 기사 상세 페이지
@app.route('/article/<article_id>')
def article_detail(article_id):
    article_ref = db.collection('articles').document(article_id)
    article = article_ref.get()
    if not article.exists:
        return '기사 없음', 404
    return render_template('article_detail.html', article=article.to_dict())

if __name__ == '__main__':
    app.run(debug=True)
