import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('articles.db')

# 커서 생성
cur = conn.cursor()

# articles 테이블에서 모든 데이터 가져오기
cur.execute("SELECT * FROM articles")

# 결과 출력
rows = cur.fetchall()

for row in rows:
    print(row)

# 연결 종료
conn.close()
