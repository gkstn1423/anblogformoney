import sqlite3

# SQLite 데이터베이스 연결
conn = sqlite3.connect('articles.db')

# 커서 생성
cur = conn.cursor()

# articles 테이블 생성
cur.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        thumbnail_url TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL
    )
''')

# 샘플 데이터 삽입 (원하는 경우)
cur.execute('''
    INSERT INTO articles (title, thumbnail_url, content, created_at)
    VALUES (?, ?, ?, ?)
''', ('정치: 차기 총리의 전망과 도전 과제', 
      'https://via.placeholder.com/300x150',
      '이곳은 기사 본문 내용입니다. 여러 문단으로 구성될 수 있으며, 각 문단은 독자가 이해하기 쉽게 작성되어야 합니다.',
      '2024-10-03'))

# 커밋하고 데이터베이스 닫기
conn.commit()
conn.close()

print("articles.db 데이터베이스가 생성되고 초기 데이터가 추가되었습니다.")
