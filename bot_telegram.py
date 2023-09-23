import requests

token = "SEU TOKEN"
chat_id = "SEU CHAT ID"
url = f'https://api.telegram.org/bot{token}/sendMessage'
   
mensagem = "Teste bot telegram"
params = {'chat_id': chat_id, 'text': mensagem}
requests.get(url, params=params)
