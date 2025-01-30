
from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

token = config('TOKEN')


bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())
admins = [5576961334, ]