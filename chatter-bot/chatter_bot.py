from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    "Chappie",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database="./db.sqlite3",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_first_response"
        }
    ]
)


with open("../chatter-bot/chatter_bot_messages.txt") as f:
    conversation = f.readlines()
    bot.set_trainer(ListTrainer)
    bot.train(conversation)


while True:
    try:
        user_input = input("msg: ")
        response = bot.get_response(user_input)
        print("bot:", response)
    except(KeyboardInterrupt, SystemExit):
        print("goodbye!")
        break
