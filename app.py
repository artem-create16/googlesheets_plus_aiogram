from loader import db


async def on_startup(dp):
    # db.delete_all_users()
    try:
        db.create_table()
        print(db.select_all_users())
    except Exception as err:
        pass

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
