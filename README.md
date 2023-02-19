# Good Bot

🤖 A Telegram bot that welcomes new users to a specific chat with a custom greeting message.

## Description

Good Bot is a Python module that can be used to create a Telegram bot that automatically sends a welcome message to new users who join a specific chat. The bot can be customized with a greeting message and supports the latest version of the Telegram API. Good Bot uses the python-telegram-bot library to interact with the Telegram API.

## Usage

To use Good Bot, you'll need to have Python 3 installed on your computer. Follow these steps to set up and run the bot:

1. Clone the repository and navigate to the project directory:

```
git clone https://github.com/meechos/good-bot.git
cd good-bot
```

2. Install the required packages using pip:

```
pip install -r requirements.txt
```

3. Create a new bot on Telegram and obtain its API token.

4. Find the ID of the chat where you want the bot to welcome new users.

5. Start the bot with the following command:

```
python3 good_bot.py --bot_id <API_TOKEN> --chat_id <CHAT_ID> --greeting "Welcome to the chat, "
```

Replace `<API_TOKEN>` with your bot's API token and `<CHAT_ID>` with the ID of the chat where you want the bot to welcome new users. You can customize the greeting message by changing the value of the `--greeting` option.

That's it! The bot will now automatically send a welcome message to new users who join the specified chat.

