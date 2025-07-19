import json

with open('config.json', 'r') as f:
    config = json.load(f)

username = config.get('username', 'Guest')
print(f'Hello, {username}!')
