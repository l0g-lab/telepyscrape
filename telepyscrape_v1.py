#
# telepyscrape: telegram bot to download latest messages and save to text file
# author:       l0g
#


## requirements ##

from datetime import datetime
import asyncio
from telethon import TelegramClient
from deep_translator import GoogleTranslator
from colorama import init, Fore, Back, Style

## variables

interesting_channels = ['itarmyofukraine2022', 'CyberArmyofRussia', 'dark_school_killnet_Eng', 'killnet_reservs']
now = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
api_id = ##
api_hash = ##
init(autoreset=True)
f = open("chat_log.txt", "w")
g = open("chat_log_translated.txt", "w")

## begin script

print(Style.BRIGHT + Fore.GREEN + 'Executing script at ' + now)
client = TelegramClient('getthis', api_id, api_hash)

async def main():
        me = await client.get_me()
        await client.send_message('me', '# SCRAPE RUN @ ' + now + ' #')

        for i in interesting_channels:

            line0 = 'Telegram Channel Name: ' + str(i)
            print(Style.BRIGHT + Fore.RED + line0)
            f.writelines(line0)
            f.writelines("\n\n\n")

            async for message in client.iter_messages(i, reverse=False, limit=5):
                #translated = GoogleTranslator(source='auto', target='en').translate(str(message.text))
                
                line1 = 'Message ID ' + str(message.id)
                f.writelines(line1)
                f.writelines("\n")
                #g.writelines(line1)
                #g.writelines("\n")
                
                line2 = 'Message TXT ' + str(message.text)
                #line2_tr = 'Message TXT ' + str(translated)
                f.writelines(line2)
                f.writelines("\n\n")
                #g.writelines(line2_tr)
                #g.writelines("\n\n")

        print(Style.BRIGHT + Fore.GREEN + 'Information above written to log file')

with client:
    client.loop.run_until_complete(main())
