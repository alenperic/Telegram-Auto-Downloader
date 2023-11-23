from telethon import TelegramClient, events
import os
import requests

# Your Telegram API credentials
api_id = 'your_api_id'
api_hash = 'your_api_hash'

# Pushover API credentials
pushover_user_key = 'your_pushover_user_key'
pushover_api_token = 'your_pushover_api_token'

# Download location
download_location = 'path/to/download_folder'  # Update this path

client = TelegramClient('session_name', api_id, api_hash)

def send_pushover_notification(message):
    data = {
        'token': pushover_api_token,
        'user': pushover_user_key,
        'message': message
    }
    response = requests.post('https://api.pushover.net/1/messages.json', data=data)
    return response.status_code

@client.on(events.NewMessage(chats='your_group_name'))
async def handler(event):
    if event.message.media:
        # Downloading media to specified location
        file_path = await client.download_media(event.message, file=download_location)
        # Sending notification
        if file_path:
            send_pushover_notification(f'File downloaded: {file_path}')

with client:
    client.run_until_disconnected()
