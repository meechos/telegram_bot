import argparse

from good_bot import Args, server


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Autobot for Telegram")
    parser.add_argument("--greeting", type=str, help="The greeting message to send to new users")
    parser.add_argument("--bot_id", type=str, help="The bot ID for the Telegram bot")
    parser.add_argument("--chat_id", type=str, help="The chat ID for the Telegram channel")

    args = Args()

    parser.parse_args(namespace=args)

    server(args)
