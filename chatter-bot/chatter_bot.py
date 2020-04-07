from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance

import logging

logging.basicConfig(level=logging.CRITICAL)

bot = ChatBot(
    "Chappie",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./db.sqlite3",
    logic_adapters=[
        "chatterbot.logic.BestMatch"
    ],
    statement_comparison_function=levenshtein_distance,
    response_selection_method=get_first_response
)

conversation = [
    "ciao",
    "come stai?",
    "come ti chiami?",
    "quanti anni hai?",
    "sei un maschio o una femmina?",
    "chi è il tuo creatore?",
    "che lavoro fai?",
    "come procede la quarantena?"
]

trainer = ListTrainer(bot)
trainer.train(conversation)


if __name__ == "__main__":
    while True:
        try:
            user_input = input("Tu: ")
            bot_response = bot.get_response(user_input)
            print("Bot: ", bot_response)
        except(KeyboardInterrupt, EOFError, SystemExit):
            print("GoodBye!")
            break


def open_file_conversation():
    with open("/path-of-file/chatter_bot_messages.txt") as f:
        conversation_file = f.readlines()
        trainer_mode = ListTrainer(bot)
        trainer_mode.train(conversation_file)
