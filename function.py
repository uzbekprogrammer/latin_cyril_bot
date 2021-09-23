from transliterate import to_latin,to_cyrillic
from aiogram import Bot, Dispatcher, executor, types

def trans(msg):
    javob = lambda msg: to_cyrillic(msg) if  msg.isascii() else to_latin(msg)
    answer=javob(msg)
    return answer