import random
import telebot
from dotenv import load_dotenv
import os
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

print(TELEGRAM_TOKEN)


filenames = [
    "GS1_Questions.txt",
    "GS2_Questions.txt",
    "GS3_Questions.txt",
]

def send_message(question):
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    bot.send_message(CHAT_ID, question)
# ""
if __name__ == '__main__':
    question = ""
    cnt = 1
    for filename in filenames:
        with open(filename, 'r',encoding="utf-8") as file:
            lines = file.readlines()
            q = random.choice(lines).strip()
            question += f"{cnt}. {q}\n"
            cnt += 1
        file.close()
    send_message(question)
    print(question)
    
    
