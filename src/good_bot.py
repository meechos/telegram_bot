import argparse
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def greet_new_user(update: Update, context: CallbackContext):
    # Get the new user's name
    new_user = update.message.new_chat_members[0]
    new_user_name = new_user.first_name

    # Get the greeting message from the context
    bot_message = "Blip blop"
    greeting_message = context.chat_data.get('greeting_message', 'Hello')

    # Send the greeting message to the chat
    update.message.reply_text(f"[{bot_message}] {greeting_message}, {new_user_name}!")


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Autobot for Telegram')
    parser.add_argument('--greeting', type=str, help='The greeting message to send to new users')
    parser.add_argument('--bot_id', type=str, help='The bot ID for the Telegram bot')
    parser.add_argument('--chat_id', type=str, help='The chat ID for the Telegram channel')
    args = parser.parse_args()

    # Create the bot instance
    updater = Updater(token=args.bot_id, use_context=True)

    # Set the maximum number of connections
    updater.bot._max_connections = 20

    # Set up the greet_new_user handler
    updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet_new_user), group=1)

    # Add the greeting message to the chat data
    updater.dispatcher.chat_data['greeting_message'] = args.greeting

    # Start the bot
    updater.start_polling()

    # Run the bot until it is stopped
    updater.idle()


if __name__ == '__main__':
    main()
