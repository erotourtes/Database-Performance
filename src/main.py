import db_utils as u
from faker import Faker

AMOUNT_OF_USERS = 10_000
AMOUNT_OF_POSTS = 20_000
AMOUNT_OF_COMMENTS = 100_000

u.load_env()

fake = Faker()

with u.connect() as conn:
  with conn.cursor() as cursor:
    insert_query = 'INSERT INTO users (first_name, second_name, email, password) VALUES (%s, %s, %s, %s)'
    users_data = [(fake.first_name(), fake.last_name(), fake.unique.email(), fake.password()) for _ in range(AMOUNT_OF_USERS)]
    cursor.executemany(insert_query, users_data)
    conn.commit()

    insert_query = 'INSERT INTO posts (content, created_at, user_id) VALUES (%s, %s, %s)'
    posts_data = [(fake.text(), fake.date_time(), fake.random_int(1, AMOUNT_OF_USERS)) for _ in range(AMOUNT_OF_POSTS)]
    cursor.executemany(insert_query, posts_data)
    conn.commit()

    insert_query = 'INSERT INTO comments (content, user_id, post_id) VALUES (%s, %s, %s)'
    comments_data = [(fake.text(), fake.random_int(1, AMOUNT_OF_USERS), fake.random_int(1, AMOUNT_OF_POSTS)) for _ in range(AMOUNT_OF_COMMENTS)]
    cursor.executemany(insert_query, comments_data)
    conn.commit()
