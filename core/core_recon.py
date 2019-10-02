#!/usr/bin/python3

import GreenLib

#green_gethostname
import socket,sys
#green_checkrobots
import requests
#green_urlparse
from urllib.parse import urlparse

#Traceroute
# HIDE (https://stackoverflow.com/questions/24812604/hide-scapy-warning-message-ipv6)
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#archive
import json

#Whatcms
#pip install pywhatcms
from pywhatcms import whatcms

#Shodan
from shodan import Shodan

#Google Hacking
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from random import randint

# Sharingmyip
#import requests
#from bs4 import BeautifulSoup

# ---------------------
# Funções usadas Recon
# -------
# OK
def green_sharingmyip(url,save):
    #TODO - usar variavel save para gerar saida/output
    rec_site = requests.get('http://sharingmyip.com/?site='+url)

    soup = BeautifulSoup(rec_site.text,'html.parser')

    qt_textarea = len(soup('textarea'))
    msg_list = ['Site (s) neste endereço','DNS para ','Entradas de DNS relacionadas para']
    #for msg in range(msg_list):
    for i in range(qt_textarea):
        if (i == 0):
            print(msg_list[0]+" ")
            print(soup('textarea')[i].string)
        elif i == 1:
            print(msg_list[1]+" "+url)
            print(soup('textarea')[i].string)
        elif i == 2:
            print(msg_list[2]+" "+url)
            print(soup('textarea')[i].string)
        else:
            print("Aconteceu algo errado :D")

# OK
def green_whatcms(site,chave):
    whatcms(chave, site)
    print("Nome:",whatcms.name)
    print("CMS CODE:",whatcms.code)
    #print(whatcms.confidence)
    print("CMS URL:",whatcms.cms_url)
    print("Versão:",whatcms.version)
    #print(whatcms.msg)
    #print(whatcms.id)
    #print(whatcms.request)
    #print(whatcms.request_web)

#OK
def green_checkrobots(url):
    try:
        resposta = requests.get(url + '/robots.txt')
        if (resposta.status_code == 200):
            return resposta.text
        else:
            var = "[ Robots.txt ] - Não encontrado"
            return var
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))

#OK
#TODO
# Parar de usar a API do hackertarget
def green_whois(name_host):
    url_api = "http://api.hackertarget.com/whois/?q="
    requisicao = requests.get(url_api + name_host)
    return requisicao.text

#OK
#TODO - Filtrar saida
def green_archive(url):
    resposta_archive = json.loads(archive_search(url))
    return resposta_archive['results']
def archive_search(url):
    archive = "http://archive.org/wayback/available"
    try:
        r = requests.post(archive, data={'url': url})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text


#-----------------
# Shodan
# ------
# Precisamos de uma URL para resolver o nome
def green_gethostname(url):
    name_host = socket.gethostbyname(url)
    return name_host
def green_shodansearch(name_host,shodan_key):
    # ADD Key config
    api = Shodan(shodan_key)
    host = api.host(name_host)
    # print(ipinfo)
    # Print general info
    print("""
IP: {}
Organization: {}
Operating System: {}
                    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
    # Print all banners
    for item in host['data']:
        print("""
Port: {}
        """.format(item['port']))







def green_urlparse(url):
    data = urlparse(url)
    # Abre o dicionario
    dicionario_url = {}

    # Recebe HTTP ou HTTPS
    dicionario_url[0] = data.scheme

    # Recebe a URL
    dicionario_url[1] = data.netloc

    # Recebe o Path da aplicação
    dicionario_url[2] = data.path
    '''
    print("TIPO:" + dicionario_url[0])
    print("URL:" + dicionario_url[1])
    print("PATH:" + dicionario_url[2])
    '''
    return dicionario_url



def green_traceroute(host_ip):
    # TODO traceroute abaixo não usa uma base publica
    #retorno_traceroute = traceroute(host_ip,maxttl=50)
    url_api = "http://api.hackertarget.com/mtr/?q="
    requisicao = requests.get(url_api + host_ip)
    return requisicao.text










def green_googlesearch(url):
    #termo_digitado = "site:" + url
    #for inicia_resultados_em in [0, 10, 20, 30, 50]:
    #    parametros_de_busca = {'q': termo_digitado, 'start': inicia_resultados_em}
    #
    #    pagina_de_busca = requests.get('https://www.google.com.br/search',
    #                                   params=parametros_de_busca)
    #
    #    soup = BeautifulSoup(pagina_de_busca.text, "html.parser")
    #
    #    for item in soup.find_all('h3', attrs={'class': 'r'}):
    #        if item.a:
    #            link_sujo_do_google = item.a.attrs['href']
    #            # /url?website.com%3Fid%3D100%26x%3Dy&ui=10....
    #
    #            link_sem_url_inicial = link_sujo_do_google[7:]
    #            # website.com%3Fid%3D100%26x%3Dy&ui=10....
    #
    #            link_os_parametros_do_google = link_sem_url_inicial.split('&')[0]
    #            # website.com%3Fid%3D100%26x%3Dy
    #
    #            link_final_decodificado = unquote(link_os_parametros_do_google)
                # website.com?id=100&x=y

                #TODO google hacking não funciona no momento
                #print(link_final_decodificado)
    #
    #    dorme_por = randint(0, 2)
    #    time.sleep(dorme_por)
    print("Google Hacking não funciona no momento!")




#
# HUNTER.io
#
def hunterio_search(url,key):
    hunterio = "https://api.hunter.io/v2/domain-search"
    try:
        r = requests.get(hunterio, data={'domain': url,'api_key': key})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text

def green_hunterio(url):
    resposta_hunterio = json.loads(hunterio_search(url))
    return resposta_hunterio['results']

#
# PwnedOrNot
#
def pwnedornot_search(email):
    pwnedornot = "https://haveibeenpwned.com/api/v3/breachedaccount"
    try:
        r = requests.get(pwnedornot, data={'domain': email})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text

def green_pwnedornot(url):
    resposta_pwnedornot = json.loads(pwnedornot_search(url))
    return resposta_pwnedornot
