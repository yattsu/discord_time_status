from tendo import singleton
me = singleton.SingleInstance()

import requests
import time
import os
import random

while True:
  seconds = time.ctime().replace('  ', ' ').split(' ')[3].split(':')[2]
  if seconds == '00':
    break

  time.sleep(0.1)

while True:
  clocks = [
  '🕐',
  '🕙',
  '🕥',
  '🕚',
  '🕦',
  '🕛',
  '🕧',
  '🕜'
  ]
  clock = random.choice(clocks)
  current_time = ':'.join(time.ctime().replace('  ', ' ').split(' ')[3].split(':')[:2])
  
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'YOUR TOKEN',
  }

  data = '{"custom_status": {"text": "' + current_time + '", "emoji_id": null, "emoji_name": "' + clock + '", "expires_at": null}}'

  response = requests.patch('https://discordapp.com/api/v6/users/@me/settings', headers = headers, data = data.encode('utf-8'))

  seconds = time.ctime().replace('  ', ' ').split(' ')[3].split(':')[2]

  time.sleep(60 - int(seconds))