from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table()

    db.add_user(5, 2, 1, 0, "13-22")
    db.add_user(6, start_point=1)

    users = db.select_all_users()

    print(f'All users: {users}')


test()
