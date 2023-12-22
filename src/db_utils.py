from dotenv import load_dotenv

import os
import re
import mysql.connector

def load_env():
  path = os.path.dirname(os.path.abspath(__file__))
  env_path = os.path.join(path, ".local.env")
  load_dotenv(env_path)

def connect():
  config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB_NAME"),
    'raise_on_warnings': True
  }

  print(config)
  
  try:
    return mysql.connector.connect(**config)
  except mysql.connector.Error as err:
    print(err)
    exit(1)

def initial_state_sql():
  path = os.path.dirname(os.path.abspath(__file__))
  sql = os.path.join(path, "../sql/schema.sql")
  with open(sql, "r") as f:
    file = f.read()
    # remove comments
    file = re.sub(r"--.*", "", file)
    # remove empty lines
    file = re.sub(r"\n\s*\n", "\n", file)
  return file

class User:
  def __init__(self, id, name, email, password):
    self.user_id = id
    self.name = name
    self.email = email
    self.password = password

class Post:
  def __init__(self, id, content, created_at, user_id):
    self.post_id = id
    self.message = content
    self.created_at = created_at
    self.user_id = user_id

class Comment:
  def __init__(self, id, content, created_at, user_id, post_id):
    self.comment_id = id
    self.message = content
    self.created_at = created_at
    self.user_id = user_id
    self.post_id = post_id

