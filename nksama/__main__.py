from nksama import bot, darbot
import logging

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    filemode="a",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
)


def main():
    bot.run()
    darbot.start()


if __name__ == "__main__":
    main()
