import requests, threading

try:
	url = input('Enter URL: ')
	if url[0:8] == r"https://" or url[0:7] == r"http://":
		pass
	else:
		url="https://"+url
except:
	print('Incorrect url')
try:
	wordlist = input('Enter name of wordlist (example admin.txt): ')
except:
	print('Incorrect wordlist')

def dir():
	print(" - - - Starting - - - ")
	try:
		with open(wordlist) as wl:
			for i in (wl):
				try:
					if i[0]=='/':
						r = requests.get(url+'/'+i[:-1])
						headers = r.headers
						status_code = r.status_code
						print("[*] ", url+i[:-1], 'Code:', status_code)
						if status_code == 200:
							print(" Conteng-length:", headers["Content-length"])
					else:
						r = requests.get(url+'/'+i[:-1])
						headers = r.headers
						status_code = r.status_code
						print("[*] ", url+'/'+i[:-1], 'Code:', r.status_code)
						if status_code == 200:
							print(" Conteng-length:", headers["Content-length"])
				except Exception as e:
					print(f"[-] Error: {e}")
	except Exception as er:
		print(f"[-] Error: {er}")
	print('- - - Stopping program - - - ')

dir_thread = threading.Thread(target=dir)
dir_thread.start()
dir_thread.join()
dir()
