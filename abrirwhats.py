import requests
import os
import webbrowser

new=2
whats = str(input('Digite o NUMERO: '))
msg = str(input('Digite a Mensagem: '))
url = ("https://api.whatsapp.com/send?phone={}&text={}".format(whats, msg))

os.system('clear')

webbrowser.open(url,new=new)