import data_generate as data
import sqlite3

class SQL(data.SQLTableValues):
    def __init__(self,db_file = 'mymeet.db', ):
        super().__init__()
        self.db_file = db_file

    def create_connection(self):
        ''' create a database connection to the SQLite database specified by db_file '''
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def create_user_table(self):
        drop_table_sql = '''DROP TABLE IF EXISTS user;'''
        create_table_sql = '''CREATE TABLE user(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR,
            username VARCHAR CHECK ((LENGTH(password) >= 8) AND (LENGTH(password) <= 14)) UNIQUE NOT NULL,
            password VARCHAR CHECK ((LENGTH(password) >= 8) AND (LENGTH(password) <= 14) AND (username != password)) UNIQUE NOT NULL        
        );'''
        self.create_connection()
        try:
            self.cur.execute(drop_table_sql)
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        else:
            print('user_table created')

    def insert_user_record(self):
        self.create_connection()

        insert_user_sql = '''INSERT INTO user (first_name,last_name,username,password)
            VALUES (?,?,?,?)'''
        self.create_user_dict()
        try:
            for user_id in self.user_dict:
                record = self.user_dict[user_id]
                self.cur.execute(insert_user_sql, record)    
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('user_table: values inserted')    
    
    def create_friend_table(self):
        drop_table_sql = '''DROP TABLE IF EXISTS friend;'''
        create_table_sql = '''CREATE TABLE friend (
            user_id INTEGER,
            friend_id INTEGER CHECK (friend_id != user_id),
            FOREIGN KEY (user_id)
            REFERENCES user (user_id),
            FOREIGN KEY (friend_id)
            REFERENCES user (user_id) 
        );'''
        self.create_connection()
        try:
            self.cur.execute(drop_table_sql)
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        else:
            print('friend_table created')
        
    def insert_friend_record(self):
        self.create_connection()

        insert_friend_sql = '''INSERT INTO friend (user_id, friend_id)
            VALUES (?,?)'''
        self.create_friend_dict()
        try:
            for user_id in sorted(self.friend_dict):
                for friend_id in sorted(set(self.friend_dict[user_id])):
                    record = (user_id, friend_id)
                    self.cur.execute(insert_friend_sql, record)    
                    self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('friend_table: values inserted')

    def create_note_table(self):
        drop_table_sql = '''DROP TABLE IF EXISTS note;'''
        create_table_sql = '''CREATE TABLE note(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT (DATETIME('now','localtime')),    
            title VARCHAR CHECK (LENGTH(title <= 50)),
            text VARCHAR CHECK (LENGTH(text <= 250)),
            visible_to VARCHAR CHECK (visible_to = 'public' or visible_to = 'friends'),
            FOREIGN KEY (user_id)
            REFERENCES user (user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE        
        );'''
        self.create_connection()
        try:
            self.cur.execute(drop_table_sql)
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        else:
            print('note_table created')

    def insert_note_record(self):
        self.create_connection()

        insert_note_sql = '''INSERT INTO note (user_id, title, text, visible_to)
            VALUES (?,?,?,?)'''
        self.create_note_dict()
        try:
            for note_id  in self.note_dict:
                record = self.note_dict[note_id]
                self.cur.execute(insert_note_sql, record)    
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('note_table: values inserted')

    def create_event_table(self):
        drop_table_sql = '''DROP TABLE IF EXISTS event;'''
        create_table_sql = '''CREATE TABLE event (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            note_id INTEGER NOT NULL,
            timestamp TIMESTAMP 
                DEFAULT (DATETIME(DATETIME('now','localtime'),'+' 
                || CAST((ABS(RANDOM()) % (300-1) + 1) AS TEXT) || ' minutes')),
            x_cordinate REAL,
            y_cordinate REAL,
            notification_range INT,
            FOREIGN KEY (note_id)
            REFERENCES note (note_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );'''
        self.create_connection()
        try:
            self.cur.execute(drop_table_sql)
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        else:
            print('event_table created')

    def insert_event_record(self):
        self.create_connection()

        insert_event_sql = '''INSERT INTO event (note_id, x_cordinate, y_cordinate, notification_range)
            VALUES (?,?,?,?)'''
        self.create_event_dict()
        try:
            for event_id in self.event_dict:
                record =self.event_dict[event_id]
                self.cur.execute(insert_event_sql, record)    
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('event_table: values inserted')


    def create_comment_table(self):
        drop_table_sql = '''DROP TABLE IF EXISTS comment;'''
        create_table_sql = '''CREATE TABLE comment (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            note_id INTEGER NOT NULL,
            commenter_id INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT (DATETIME('now','localtime')),
            text VARCHAR,
            FOREIGN KEY (note_id)
            REFERENCES note (note_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE, 
            FOREIGN KEY (commenter_id)
            REFERENCES user (user_id)
                ON UPDATE CASCADE
                ON DELETE CASCADE     
        );'''
        self.create_connection()
        try:
            self.cur.execute(drop_table_sql)
            self.cur.execute(create_table_sql)
        except sqlite3.Error as e:
            print(e)
        else:
            print('comment_table created')

    def insert_comment_record(self):
        self.create_connection()

        insert_comment_sql = '''INSERT INTO comment (note_id, commenter_id, text)
            VALUES (?,?,?)'''
        self.create_comment_dict()
        try:
            for comment_id  in self.comment_dict:
                record = self.comment_dict[comment_id]
                self.cur.execute(insert_comment_sql, record)    
                self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('comment_table: values inserted')
    
    def integrity_check(self):
        try:
            check = self.cur.execute('PRAGMA integrity_check;')
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        else:
            print('Integrity Check:', check.fetchall())

DB = SQL()
DB.create_user_table()
DB.create_friend_table()
DB.create_note_table()
DB.create_event_table()
DB.create_comment_table()
print()
DB.integrity_check()
print()
DB.insert_user_record()
DB.insert_friend_record()
DB.insert_note_record()
DB.insert_event_record()
DB.insert_comment_record()

















def select_tasks(self):
        sql = 'SELECT * FROM user;'
        
        self.create_connection()
        try:
            self.cur.execute(sql)
        except sqlite3.Error as e:
            print(e)
        rows = self.cur.fetchall()
        for record in rows:
            print(record)

