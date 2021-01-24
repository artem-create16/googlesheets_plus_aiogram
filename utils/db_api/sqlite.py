import sqlite3


class Database:
    def __init__(self, path_to_db='data/main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql, parameters: tuple = None, fetchone=False,
                fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Users (
            user_id int NOT NULL,
            count_of_words int,
            time varchar(12),
            PRIMARY KEY (user_id)
            );"""

        self.execute(sql, commit=True)

    def add_user(self, user_id, count_of_words=None, time=None):
        sql = """
        INSERT INTO Users(user_id, count_of_words, time) VALUES (?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, count_of_words, time), commit=True)

    def select_all_users(self):
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def delete_all_users(self):
        sql = "DELETE FROM Users WHERE TRUE"
        return self.execute(sql, commit=True)

