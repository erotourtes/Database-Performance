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
