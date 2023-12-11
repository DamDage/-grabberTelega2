from telethon import TelegramClient, events


api_id = n
api_hash = 'n'
my_channel_id = -n
channels = [-n, -n]

client = TelegramClient('myGrab', api_id, api_hash)


print("GRAB - Started")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
    if event.message:
        await client.send_message(my_channel_id, event.message)

client.start()
client.run_until_disconnected()
