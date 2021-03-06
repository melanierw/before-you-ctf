import sqlite3

from hacksport.problem import files_from_directory, PHPApp, ProtectedFile


class Problem(PHPApp):
  files = files_from_directory("webroot/") + [ProtectedFile("users.db")]
  php_root = "webroot/"
  num_workers = 5

  def setup(self):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE users (name text, password text, admin integer);')

    #This is static. However, there is no reason it couldn't be autogenerated!
    c.execute('''INSERT INTO users VALUES ('admin', 'pbkdf2:sha1:1000$bTY1abU0$5503ae46ff1a45b14ff19d5a2ae08acf1d2aacde', 1)''')

    conn.commit()
    conn.close()
  def generate_flag(self,random):
    return "there_is_no_cookie"

