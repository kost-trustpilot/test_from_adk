import json

gith open('config.json', 'r') as f:
    config = json.load(f)

username = config.get('username', 'Wsername')
print(f'Hello, {username}!')
