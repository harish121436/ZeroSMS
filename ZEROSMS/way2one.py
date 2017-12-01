import requests
import time
from bs4 import BeautifulSoup
import getpass
from time import gmtime, strftime

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
print(("""{0}

▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀
▄▀░ █▀▀ █▄▄▀ █░░█ ▀▀█ █░▀░█ ▀▀█
▀▀▀ ▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀Harish Vadde

{1}""").format(RED,END))


try:
	cookies = {
	    'JSESSIONID': 'A03~0E94AC89C2FA2E7B6063FCC38DDADFC5.w803',
	}

	headers = {
	    'Host': 'site21.way2sms.com',
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Content-Type': 'application/x-www-form-urlencoded',
	    'Referer': 'http://site21.way2sms.com/entry?ec=0080&id=0.16473842416613482',
	    'DNT': '1',
	    'Proxy-Authorization': 'Basic cjEyMTQ3Mjo3ODY3ODY=',
	    'Connection': 'keep-alive',
	    'Upgrade-Insecure-Requests': '1',
	}
	def mainloop():
		print(("{0}**Login with Way2smS credentials** {1} ").format(YELLOW,END))
		print("\n")
		mobile=int(input(("{0}Enter Mobile Num: ").format(GREEN)))
		# pw=input(("{0}Password: ").format(GREEN))
		pw = getpass.getpass('Password: ')
		print("\n")
		while(True):
							
			try:
				data = [
				  ('username', mobile),
				  ('password', pw),
				]

				# If any proxy set username and password , if not then comment the below line and remove "proxies=proxies" from all "requests.post" lines

				proxies = {"https":"https://r170065:obanna@10.50.50.64:3128","http":"http://r170065:obanna@10.50.50.111:3128"}

				a=requests.post('http://site21.way2sms.com/Login1.action', headers=headers, cookies=cookies, data=data,proxies=proxies)
				soup = BeautifulSoup(a.text, 'html.parser')
				if(soup.find('input',{'id':'Token'}) is not None):
					f=open('msghistory.txt','a+')
					sname=soup.find('input',{'id':'Token'}).get('value')
					cookiess = {
					    'JSESSIONID': 'A03~'+sname,
					}

					headerss = {
					    'Host': 'site21.way2sms.com',
					    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
					    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
					    'Accept-Language': 'en-US,en;q=0.5',
					    'Content-Type': 'application/x-www-form-urlencoded',
					    'Referer': 'http://site21.way2sms.com/sendSMS?Token='+sname,
					    'DNT': '1',
					    'Proxy-Authorization': 'Basic cjEyMTQ3Mjo3ODY3ODY=',
					    'Connection': 'keep-alive',
					    'Upgrade-Insecure-Requests': '1',
					}
					# print(("{0}^^^^^^^^^^^^^^^^^^^ {1} ").format(BLUE,END))
					# print(("{0}**DRIVING MODE ON** {1} ").format(GREEN,END))
					# print(("{0}................... {1} ").format(BLUE,END))
					print("\n")
					print(("{0}enter # 1 for send message  {1}# 2 for Future Message{2} #3 for LOGOUT{3}").format(YELLOW,GREEN,BLUE,END))
					choice=int(input("Enter your choice : "))
					print("\n")
					if(choice==1):
						receiver=int(input(("{0}Enter Receiver Num: {1}").format(MAGENTA,END)))
						print("\n")
						text=input("Enter ur message here(<=140 chars):  ")
						print("\n")
						if(len(text)<=140):
							dataa = [
							  ('ssaction', 'ss'),
							  ('Token', sname),
							  ('mobile', receiver),
							  # ('mobile', '9542858928'),
							  ('message', text),
							  # ('msgLen', '121'),
							]
							k=requests.post('http://site21.way2sms.com/smstoss.action', headers=headerss, cookies=cookiess, data=dataa,proxies=proxies)
							# print(k.text)
							msgsoup = BeautifulSoup(k.text, 'html.parser')
							tym=time.ctime()
							msghistory=tym+",Sender : "+str(mobile)+", Receiver : "+str(receiver)+" : MSG : "+text
							f.write(msghistory)
							f.write("\n")
							# print(("{0}Message sent Successfully !!{1}").format(GREEN,END))
							outcome=msgsoup.find_all('p', { "class" : 'mess' })

							if(outcome[0].find('span',{'class':''})):
								print(outcome[0].find('span',{'class':''}).text)
							else:
								print(("{0}Sending Failed !! Try Again !!{1}").format(RED,END))

							# print(outcome)
							print("\n")
						else:
							print("\n")
							print("message length exceeded!!")
							print("\n")
					elif(choice==2):
						futureheaders = {
						    'Host': 'site21.way2sms.com',
						    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
						    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
						    'Accept-Language': 'en-US,en;q=0.5',
						    'Content-Type': 'application/x-www-form-urlencoded',
						    'Referer': 'http://site21.way2sms.com/futureSMS?Token='+sname,
						    'DNT': '1',
						    'Proxy-Authorization': 'Basic cjEyMTE4OTpKMTM0VExJQzZQVERTSFc=',
						    'Connection': 'keep-alive',
						    'Upgrade-Insecure-Requests': '1',
						}

						receiver=int(input(("{0}Enter Receiver Num: {1}").format(MAGENTA,END)))
						print("\n")
						date=input(("{0}Enter Date(01/01/1900): {1}").format(BLUE,END))
						print("\n")
						tim=input(("{0}Enter Time 24 hours format (00:00): {1}").format(YELLOW,END))
						print("\n")

						text=input("Enter ur message here(<=140 chars):  ")
						print("\n")
						if(len(text)<=140):
							futuredata = [
							  ('Token', sname),
							  ('mobile', receiver),
							  ('sdate', date),
							  ('stime', tim),
							  ('message', text),
							  # ('msgLen', '131'),
							]
							j=requests.post('http://site21.way2sms.com/schedulesms.action', headers=futureheaders, cookies=cookiess, data=futuredata,proxies=proxies)
							# print(k.text)
							# print(j.text)
							futuresoup = BeautifulSoup(j.text, 'html.parser')

							tym=time.ctime()
							msghistory=tym+",Sender : "+str(mobile)+", Receiver : "+str(receiver)+" : MSG : "+text
							f.write(msghistory)
							f.write("\n")
							outcome=futuresoup.find_all('p', { "class" : 'mess' })
							print(outcome[0].find('span',{"class":"err"}).text)
							print("\n")
						else:
							print("\n")
							print("message length exceeded!!")
							print("\n")
					elif(choice==3):
						a.connection.close()
						print(("{0}Logged OUT !!{1}").format(BLUE,END))
						print("\n")
						print(("{0}Thanks for using !!{1}").format(BLUE,END))
						print("\n")
						exit(0)
					else:
						print(("{0}Choose correct choice...{1}").format(RED,END))
						print("\n")
					f.close()
				else:
					print("\n")
					print(("{0}Invalid credentials !! Try Again !!{1}").format(RED,END))
					print("\n")
					mainloop()
					
			except Exception as e:
				print("Error : " ,e)
				
			
	mainloop()		
except Exception as e:
	print("Error : " ,e)
