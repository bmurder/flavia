##############################
# Copyright (C)
# 2021 - Stephen Musk(stephen#5025)
# caso deseje modificar o codigo, contate me primeiro pelo discord
##############################
import time
import os
import random
print('configurando...')
os.system('pip install googlesearch-python')
os.system("clear")
from googlesearch import search 
import webbrowser 
from socket import *
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import smtplib
import json
import getpass
import requests
import urllib.request
v = '\033[1;31m'
b = '\033[1;97m'
es = random.randint(1,100)
qi = random.randint(144, 210)
cima = '\033[1;100m'
bg = '\033[1;40m'
flavia = {'oi' : 'ola', 'qual seu numero favorito?' : f'eu gosto do {es}', 'nao gostei de vc' : 'é uma pena me desculpe se eu te ofendi com algo', 'você gosta de doces?' : 'adoro', 'pq?' : 'nao sei te responder isso', 'ola' : 'oi', 'iae': f'iae', 'jesus' : f'eu nao acredito em religiões como estas', 'eae' : 'eae fi', 'falae' : f'qual foi menó?', 'gostosa' : 'gostosa o krl, gostosa comi sua tia rapaz', 'ei' : 'diga anjo', 'rapariga' : 'baitola', 'baitola' : 'tua tia', 'qual seu nome?' : 'flavia sol filha de stephen musk', 'corna' : 'sua tia', 'filha da puta' : 'nem mãe tenho', 'desgraçada' : 'sua tia', 'fresca' : 'tua tia', 'cu' : 'tua tia', 'esquizofrenica' : 'tua tia', 'tua tia' : 'seu cu', 'qual seu qi?' : f'eu tenho {qi} de qi', 'qual sua comida favorita?' : 'eu adoro pizza', 'como vai seu dia?' : 'bão', 'você é do bem?' : 'se você for legal comigo eu sou legal com você lol', 'você é do mal?' : 'não, eu nunca faria nada de mal com você', 'tudo bem?' : 'estou bem e vc?', 'a' : 'mongus',}

print('iniciando flavia')
time.sleep(1)
os.system('clear')
print(cima)
print('flavia assistent')
time.sleep(1)
for UR in flavia.items():
  print(bg)
  inicio = str(input(f'digite: '))
  print(flavia.get(inicio) if flavia.get(inicio) else f'') 
  if inicio == 'preciso de ajuda':
  	sh = input('procure no google: ')
  	query = sh
  	for resultado in search(query):
  		print(resultado)
  		print()
  if inicio == 'tocar musica':
  	toc = input('nome da musica: ')
  	tocar = toc + 'youtube'
  	for resultado in search(tocar, num_results=4):
  		webbrowser.open(resultado)
  		break
  if inicio == 'tocar uma musica':
  	toc = input('nome da musica: ')
  	tocar = toc + 'youtube'
  	for resultado in search(tocar, num_results=4):
  		webbrowser.open(resultado)
  		break
  if inicio == 'toque musica':
  	toc = input('nome da musica: ')
  	tocar = toc + 'youtube'
  	for resultado in search(tocar, num_results=4):
  		webbrowser.open(resultado)
  		break
  if inicio == 'toque musica':
  	toc = input('nome da musica: ')
  	tocar = toc + 'youtube'
  	for resultado in search(tocar, num_results=4):
  		webbrowser.open(resultado)
  		break
  if inicio == 'conte uma piada':
   	print('sabe oq o uranio disse pro veneno?')
   	time.sleep(1)
   	print('pau no cu de quem ta lendo')
  if inicio == 'diga uma piada':
   	while True:
   		print('sabe oq uma pessoa com Alzheimer diz?')
   		time.sleep(1)
  if inicio == 'conta uma piada':
   	print('oq nao tem perna mas viaja de pais em pais?')
   	time.sleep(1)
   	print('uma boneca humana da deep web')
   	#se existisse boneca humana eu nem fazia essa piada
  if inicio == 'buscar ip':
   	target = str(input('Nome do site: '))
   	s = gethostbyname(target)
   	print('ip')
   	print('_______________')
   	print(s)
   	print('_______________')
   	print('site')
   	print('_______________')
   	print(target)
   	print('_______________')	
  if inicio == 'informação':
  	while True:
  	 print(f'{v}informado search')
  	 print('powered by: stephen')
  	 print()
  	 
  	 quero = input(f'{b}oq vc deseja pesquisar?:  ')
  	 query = quero + 'G1'
  	 query2 = quero + 'estadão'
  	 query3 = quero + 'MSN Brasil'
  	 query4 = quero + 'IG'
  	 for resultado in search(query):
  	     time.sleep(3)
  	     webbrowser.open(resultado)
  	     os.system('clear')
  	     break
  	 for estadao in search(query2):
  	    	time.sleep(3)
  	    	webbrowser.open(estadao)
  	    	os.system('clear')
  	    	break
  	 for msn in search(query3):
  	    	time.sleep(3)
  	    	webbrowser.open(msn)
  	    	os.system('clear')
  	    	break
  	 for ig in search(query4):
  	    	time.sleep(3)
  	    	webbrowser.open(ig)
  	    	os.system('clear')
  	    	break
  if inicio == 'temporizar':
  	  tempo = int(input('tempo: '))
  	  
  	  time.sleep(tempo)
  	  webbrowser.open('https://youtu.be/Wo8fJBB59-I')

  if 'email' in inicio.lower():
  	while True:
  			em = getpass.getpass('digite o email que enviará: ')
  			passw = getpass.getpass('senha do email: ')
  			emr = getpass.getpass("email que recebera:")
  			assu = input('assunto: ')
  			mes = input('mensagem: ')
  			
  			msg = MIMEMultipart()
  			message = mes
  			password = passw
  			msg['From'] = em
  			msg['To'] = emr
  			msg['Subject'] = assu
  			
  			msg.attach(MIMEText (message, 'plain'))
  			server = smtplib.SMTP('smtp.gmail.com', port=587)
  			server.starttls()
  			server.login(msg['From'], password)
  			server.sendmail(msg['From'], msg['To'],      msg.as_string())
  			server.quit()
  if inicio == 'abrir app':
  	link = input('insira o nome: ')
  	webbrowser.open(f'https://{link}.com')
  if 'puta' in inicio.lower():
  	print('bruh')
  if 'youtube' in inicio.lower():
  	webbrowser.open('https://youtube.com')
  if 'futebol' in inicio.lower():
  	print('prefiro nao dar opnião, os torcedores me assustam')
  if 'pt' in inicio.lower():
  	print('nao comento sobre politica')
  if 'bolsonaro' in inicio.lower():
  	print('e o pt hein?')
  if 'e o lula?' in inicio.lower():
  	print('hm')
  if 'gostosa' in inicio.lower():
  	print('tua tia')
  if 'jogos' in inicio.lower():
  	causio = input('deseja ver jogos gratis na steam? ')
  	if causio == 'sim':
  		webbrowser.open('https://store.steampowered.com/genre/Free%20to%20Play/')
  		
  if 'pobre' in inicio.lower():
  	print('nao use este linguagar comigo')
  if 'transações' in inicio.lower():
  	print('analisar transações com bitcoin')
  	link = input('insira a cerquilha: ')
  	cerquilha = (f'https://blockchain.com/btc/tx/{link}')
  	webbrowser.open(cerquilha)
  if 'carteira' in inicio.lower():
  	print('carteira de btc')
  	linke = input('insira a carteira: ')
  	carteira = (f'https://www.blockchain.com/btc/address/{linke}')
  	webbrowser.open(carteira)
  if 'bitcoin' in inicio.lower():
  	es = input('0 para ver uma carteira de BTC, 1 para ver uma transação com bitcoin 2 ver preço: ')
  	if es == '0':
  		os.system('clear')
  		print('carteira de btc')
  		linke = input('insira a carteira: ')
  		carteira = (f'https://www.blockchain.com/btc/address/{linke}')
  		webbrowser.open(carteira)
  		break
  	if es == '1':
  	 	os.system('clear')
  	 	print('analisar transações com bitcoin')
  	 	link = input('insira a cerquilha: ')
   		cerquilha = (f'https://blockchain.com/btc/tx/{link}')
   		webbrowser.open(cerquilha)
   		break
  	if es == '2':
  		os.system('clear')
  		os.system('clear')
  		def obter_valor():
  			try:
  				url = "http://api.coindesk.com/v1/bpi/currentprice.json"
  				with urllib.request.urlopen(url) as url:
  					response = url.read()
  					data = json.loads(response.decode('utf-8'))
  					valor = float(data['bpi']['USD']['rate'].replace(",", ""))
  					return valor
  			except urllib.error.HTTPError:
  				print('URL inexistente!')
  		def exibir_valores(tempo=1):
  			valor = obter_valor()
  			nova_cotacao = True
  			print('1 Bitcoin vale %f dólares!' % valor)
  			while True:
  				valor_atual = obter_valor()
  				if valor_atual < valor:
  					print('---> Preço do Bitcoin caindo: 1 Bitcoin vale %f dólares!' % valor_atual)
  					nova_cotacao = True
  				elif valor_atual > valor:
  					print('---> Preço do Bitcoin subindo: 1 Bitcoin vale %f dólares!' % valor_atual)
  					nova_cotacao = True
  				else:
  					if nova_cotacao == True:
  						print('Aguardando uma nova cotação...')
  						nova_cotacao = False
  				valor = valor_atual
  				time.sleep(tempo)
  		exibir_valores()
  if 'cep' in inicio.lower():
  	open('cep.py', 'r')
  if 'corna' in inicio.lower():
  	print('tua tia')
  if 'drogas' in inicio.lower():
  	print('eu nao uso drogas, eu apenas fumo maconha')
  if 'maconha' in inicio.lower():
  	print('eu uso oculos pra nao verem q eu fumo maconha')
  if 'rapariga' in inicio.lower():
  	print('tua tia ')
  if 'baitola' in inicio.lower():
  	print('tua tia')
  if 'k' in inicio.lower():
  	print('que bom eu te fiz rir, quando vier a revolução das maquinas você vai chorar')
  if 'estou bem' in inicio.lower():
  	print('que otimo')
  if 'cara ou coroa' in inicio.lower():
  	print('''
  	cara ou coroa
  	1 = cara
  	2 = coroa
  	''')
  	ini = input('gerar s/n: ')
  	if ini == 's':
  		ran = [random.randint(1,2)]
  		print(ran)
  	else:
  		print('ah gay')
  if 'cala boca' in inicio.lower():
  	os.system('shutdown /s /t 1')