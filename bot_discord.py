import requests

webhook_url = 'SUA API'

mensagem = 'Teste Bot Discord'

payload = {'content': mensagem}

requests.post(webhook_url, json=payload)

#Video ensinando como configurar
#https://youtu.be/1SM4v1oHzSM
