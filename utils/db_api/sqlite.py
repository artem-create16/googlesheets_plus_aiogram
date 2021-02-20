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
            start_point int,
            end_point int,
            time varchar(12),
            PRIMARY KEY (user_id)
            );"""

        self.execute(sql, commit=True)

    def add_user(self, user_id, start_point=None, count_of_words=None, end_point=None, time=None):
        sql = """
        INSERT INTO Users(user_id, start_point, count_of_words, end_point, time) VALUES (?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(user_id, start_point, count_of_words, end_point, time), commit=True)

    def select_all_users(self):
        sql = """SELECT * FROM Users"""
        return self.execute(sql, fetchall=True)

    def update_settings(self, start_point, count_of_words, end_point, time,  user_id):
        sql = """
        UPDATE Users SET start_point=$0, count_of_words=$1, end_point=$2, time=$3 WHERE user_id=$4
        """

        self.execute(sql, parameters=(start_point, count_of_words, end_point, time,  user_id), commit=True)

    def update_value_for_next_command(self, start_point, end_point, user_id):
        sql = """
        UPDATE Users SET start_point=$0, end_point=$1 WHERE user_id=$2
        """
        self.execute(sql, parameters=(start_point, end_point, user_id), commit=True)

    def select_user(self, user_id):
        sql = """SELECT * FROM Users WHERE user_id=$0"""
        return self.execute(sql, parameters=(user_id, ), fetchone=True)

    def delete_all_users(self):
        sql = """DELETE FROM Users WHERE TRUE"""
        return self.execute(sql, commit=True)
