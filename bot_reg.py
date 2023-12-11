from telethon.sync import TelegramClient

api_id = 'n'
api_hash = 'n'

with TelegramClient('kasta', api_id, api_hash) as client:
    print(client.session.save())
