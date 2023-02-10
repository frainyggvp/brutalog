import requests

try:
	url = input('Enter URL: ')
except:
	print('Incorrect url')
try:
	wordlist = input('Enter name of wordlist (example admin.txt): ')
except:
	print('Incorrect wordlist')

with open(wordlist) as wl:
	for i in (wl):
		if i[0]=='/':
			print((url+i[:-1]), 'Code:', requests.get(url+'/'+i[:-1]).status_code)
		else:
			print((url+'/'+i[:-1]), 'Code:', requests.get(url+'/'+i[:-1]).status_code)

print('Stopping program')
