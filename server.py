import sqlite3

db = sqlite3.connect('d.db', check_same_thread=False)
cursor = db.cursor()

class Data():
    def __init__(self):
        pass

    def reg(self, user_id, refer_id=0):
        try:
            
            cursor.execute('INSERT INTO "users" (user_id, refer_id) VALUES (?, ?)', (user_id, refer_id))
            db.commit()
            print('reg() is True')
            return True
            
        except Exception as exc: 
            print(exc)
            return False

    def return_refer(self, user_id):
        data = cursor.execute(f"SELECT refer_id FROM users WHERE user_id = {user_id}").fetchall()
        return data[0][0]

ds = Data()
ds.reg(234432, 234)