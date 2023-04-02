from os import system


def chatbot():
    response = None
    try:
        while True:
            request = yield response
            match request:
                case None:
                    response = 'generator initialised'      # NOTE: never returned
                case 'hello':
                    response = 'Hi, how are ya?'
                case 'how are you':
                    response = 'Good thanks, you?'
                case 'bye':
                    response = 'Have a good'
                case _:
                    response = 'Sorry didn''t get that'
    finally:
        print(f"Exiting yield_func")

    return 0


def chatbot_demo():
    bot = chatbot()
    print(bot.send(None))
    print(bot.send('hello'))
    print(bot.close())


if __name__ == '__main__':
    chatbot_demo()
