#!usr/bin/python 
#Coded By P47r1ck & low1z
#Recode By Anarchy99

import sys, smtplib, socket, time
import random, string
from smtplib import SMTP 

socket.setdefaulttimeout(5)   




print(r"""
    _   _  _   _   ___  ___ _  ___   _____ ___ 
   /_\ | \| | /_\ | _ \/ __| || \ \ / / _ / _ \
  / _ \| .` |/ _ \|   | (__| __ |\ V /\_, \_, /
 /_/ \_|_|\_/_/ \_|_|_\\___|_||_| |_|  /_/ /_/ 
                 MASS SMTP CHECKER
                 john.dhoe412@gmail.com
		 https://www.facebook.com/jancoxx412
		 """)


t = string.ascii_lowercase
acak = ''.join(random.choice(t) for i in range(5))


def timer():
        now = time.localtime(time.time())
        return time.asctime(now)

def sendchk(listindex, host, user, password):   
	try:
		fail = open("die.txt","a")
		fromaddr = str(user)
		toaddr = str(email)
#toaddr = "someone@yahoo.com"
		message = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: RESULT TEST EMAIL [%s]

BERHASIL TEST EMAIL DARI %s
""" % (fromaddr,toaddr,acak,host)
		smtp = smtplib.SMTP(host, 587)
		smtp.login(user, password)
		code = smtp.ehlo()[0]
		if not (200 <= code <= 299):
			code = smtp.helo()[0]
			if not (200 <= code <= 299):
				raise SMTPHeloError(code, resp)
		smtp.sendmail(user, toaddr, message)
		print("\033[92m")
		print "\n\t[!] Berhasil ngirim dari",host
		print "\t[!] Pesan Terkirim\n"
		LSstring = host+":"+user+":"+password+"\n"
		nList.append(LSstring)		
		LFile = open("live.txt", "a")
		LFile.write(LSstring) 		
		LFile.close()
		AMSout = open("logsmtp.txt", "a")
		AMSout.write("[Server"+str(nList.index(LSstring))+"]\nName="+str(host)+"\nPort=587\nUserID=User\nBccSize=50\nUserName="+str(user)+"\nPassword="+str(password)+"\nAuthType=0\n\n")
		smtp.quit()
	except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException):
		fail.write("[-] Login Gagal : {0}:{1}:{2}\n".format(str(host),str(user),str(password)))
		print("\033[91m")
		print "[-] Login Gagal Bos : ", host, user, password
		pass


# Do not change anything below. 
email = raw_input(" [ - ] Email Destinatoon : ")
accounts = raw_input(" [ - ] SMTP LIST : ")
try: 
    list = list(open(accounts))
except: 
	print"\n[+] File list Notfound"
	print"\n[+] Please Check Again"

#listindex = 0
nList = []
for line in list:
	try:
		host = line.split(':')[0]
		user = line.split(':')[1].replace('\n', '')
		password = line.split(':')[2].replace('\n', '')
		sendchk(list.index(line), host, user, password)
	except:
		print '\n[+] Wrong List Format ...'
		print host, user
		print '\n[!] Format list IP:USER:PASS'
		print '\n[-] Aborted...\n'
		exit(1)

print "[!] Ended at: " + timer() + ""
