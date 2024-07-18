#
# telepyscrape: telegram bot to download latest messages and save to text file
# author:       l0g
#


## requirements ##

from datetime import datetime
import asyncio
from telethon import TelegramClient
from deep_translator import GoogleTranslator

## variables

interesting_channels = ['itarmyofukraine2022', 'CyberArmyofRussia', 'dark_school_killnet_Eng', 'killnet_reservs'] # initialized the interesting channel list
now = str(datetime.today().strftime('%Y-%m-%d %H:%M'))
api_id = # number
api_hash = # string

## begin script

print(f'Executing script at {now} \n')
client = TelegramClient('getthis', api_id, api_hash)

async def main():
        #me = await client.get_me()
        #await client.send_message('me', '# SCRAPE RUN @ ' + now + ' #')

        lookup = {}

        for i in interesting_channels:

            index = 0
            msg_ids = []
            msg_txt = []

            async for message in client.iter_messages(i, reverse=False, limit=5):
                #translated = GoogleTranslator(source='auto', target='en').translate(str(message.text))

                msg_ids.insert(index, message.id)
                msg_txt.insert(index, message.text)
                index = index + 1
                lookup[message.id] = message.text

        for x, y in lookup.items():
            #print(f'{x} :::: {y}')
            print(f'Message ID: {x}')
            print(f'Message TXT: {y}\n\n')

        print(f'Information above written to log file')

with client:
    client.loop.run_until_complete(main())
