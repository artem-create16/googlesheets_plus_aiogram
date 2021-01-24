from utils.db_api.sqlite import Database

db = Database()

def test():
    db.create_table()
    # db.add_user(8, 20, "123456")
    # db.add_user(2, 200, "12-22")
    # db.add_user(3, 2, "13-22")
    users = db.select_all_users()

    print(f'All users: {users}')

test()