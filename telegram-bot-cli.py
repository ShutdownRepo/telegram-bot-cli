#!/usr/bin/env python3

import telegram
import config
from optparse import OptionParser

def get_options():
    parser = OptionParser()
    parser.add_option("-j", "--job", dest="job", type="string", help="select a job name (required)")
    parser.add_option("-d", "--details", dest="details", type="string", help="add details to the job (50 characters max)")
    parser.add_option("-u", "--username", dest="username", type="string", help="add your username if you want the bot to highlight you")
    (options, args) = parser.parse_args()
    if not options.job:
        parser.error('Job name not given')
    elif options.details:
        if len(options.details) > 50:
            parser.error('Details too long')
    return options

def prepare_bot():
    # We need the telegram bot token and group id to send the message. I think this check can be done more gracefully.
    try:
        if config.BOT_TOKEN == "" or not config.BOT_TOKEN:
            print('Error: BOT_TOKEN is not set')
            quit()
        if config.BOT_TOKEN == "" or not config.GROUP_ID:
            print('Error: GROUP_ID is not set')
            quit()
        return telegram.Bot(token=config.BOT_TOKEN)
    except:
        print('Error: parsing config file, BOT_TOKEN or GROUP_ID may be missing')
        quit()

def send_message(bot, message):
    bot.send_message(config.GROUP_ID, message, parse_mode=telegram.ParseMode.MARKDOWN)

if __name__ == "__main__":
    bot = prepare_bot()
    options = get_options()
    message = "*[CLI Job]* the command-line job *" + options.job + "* has ended"
    if options.details:
        message += " (" + options.details + ")"
    if options.username:
        message += " for @" + options.username
    send_message(bot, message)
