import os
import requests


def main():
    base_url = 'https://api.telegram.org/bot'
    # Get the API key. If OS var not set, checks for key.txt. If no file then error.
    try:
        key = os.environ['WEBBOTAPIKEY']
        if key is None:
            raise OSError('API key not set as environment variable')
    except OSError:
        try:
            file = open('key.txt')
            key = file.readline()
        except FileNotFoundError:
            raise FileNotFoundError("No key set, no key file found")
    messages_url = base_url + key + '/getUpdates'
    # Check unread messages
    response = requests.get(url=messages_url).json()
    if response['ok']:
        messages = response['result']
    else:
        raise Exception("Telegram returned not ok")
    # Parse and resolve each message
    for message in messages:
        pass


if __name__ == '__main__':
    main()