from loader import db


async def on_startup(dp):
    try:
        db.create_table()
    except Exception as err:
        print(err)

    print(db.select_all_users())


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
