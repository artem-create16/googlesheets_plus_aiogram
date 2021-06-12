from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.users.get_words import get_message


scheduler = AsyncIOScheduler()

scheduler.add_job(get_message, "interval", seconds=5)
