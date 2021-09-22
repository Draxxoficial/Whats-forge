import requests
import os
import random
import webbrowser

whats = str(input('Digite o NUMERO: '))
print()
msg = str(input('Digite a Mensagem: '))
url = ("https://api.whatsapp.com/send?phone={}&text={}".format(whats, msg))

webbrowser.open(url)
