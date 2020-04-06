# The bot
  This is a command line tool I use when I want to get notified, on Telegram (on my phone), that something has finished running (on my laptop).
  For instance, let's say I'm in an engagement scanning assets and waiting for my nmap scan to finish, I can now receive a text message on Telegram from my bot.

# Usage
```
Usage: telegram-bot-cli.py [options]

Options:
  -h, --help                          show this help message and exit
  -j JOB, --job=JOB                   select a job name (required)
  -d DETAILS, --details=DETAILS       add details to the job (50 characters max)
  -u USERNAME, --username=USERNAME    your username if you want the bot to highlight you
```

# Quick start
  First of all, clone this git : `git clone https://github.com/ShutdownRepo/telegram-bot-cli`
  If you already know your bot token and the group ID in which you want to get notified, add those in the `sample-config.py` file and rename it `config.py`.
  If you don't know these information, follow these steps "Full instructions".

  Once the config file is setup, install the requirements and test the script
  ```
  pip3 install --user requirements.txt
  echo "Testing" | python3 telegram-bot-cli.py --job testing
  ```

  If you love aliases like I do, you can something like
  `alias telegram-bot-cli='python3 /PATH/TO/telegram-bot-cli/telegram-bot-cli.py -u username'`

# Full instructions
  Create a bot and find the token
  1. Open a Telegram client
  2. Start a conversation with @BotFather
  3. Send the following command : /newbot`
  4. Send the name of your bot (anything you want)
  5. Send the username of your bot (must be unique, and end with 'bot')
  6. The bot is created and the token to access the HTTP API is sent to you

  Create a group, add the bot and find the group ID
  1. Create the group your want the bot to send messages to
  2. Add the bot to the group with its username (@unique_username_bot)
  3. Send the following message in the group : `/my_id @unique_username_bot`
  4. Go to `https://api.telegram.org/bot<bot_token>/getUpdates` and replace `<bot_token>` with yours
  5. In the JSON array, find the message/chat/id negative integer composed of 9 figures, this is your group ID

  Now that you have the bot, the token, the group and the group ID, add those in the `sample-config.py` file and rename it `config.py`.

# TODO
  - find a way to trigger this cli bot by grepping something in commands output. For instance, let's say I want to get notified when my `ntlmrelayx` has successfully relayed authentication during an engagement, I would grep on "SUCCESS"
  - **any ideas?**
