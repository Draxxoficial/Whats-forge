import requests
import os
import random
import webbrowser

whats = str(input('Digite o NUMERO: '))
url = ("https://api.whatsapp.com/send?phone={}&text={}".format(whats))

webbrowser.open(url)
