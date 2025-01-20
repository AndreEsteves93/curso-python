import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://worldofwarcraft.blizzard.com/pt-br/')
except urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site está acessível!')
    # para pegar o conteudo html. print(site.read())
