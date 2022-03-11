import time
import requests
import sys as n
import random
import threading

#=======
rhaby2 = int(5)
#========
rhaby = int(1)
ruksI='IdMN1w9spls'
rg = 'D'
#@Python824
ruks_ = '\033[1;36m'
ruks__ = '\033[1;36m'
jruks = '\033[1;37m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'

N =0
R =('━'*60)
print("✥.....•✥")
print(".......")
rukS = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ENTER YOUR TOKEN : '+BGreen)
Ruks = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ENTER YOUR ID :'+BGreen)
print(R)
def ruks():
	global N
	global rukS
	global Ruks
	tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
	t ='poiuytrewqasdfghjklmnbvcxz1234567890'
	ruKs = requests.session()
	try:	
		while True:
		    N +=1
		    rhaby1 = str("".join(random.choice(t)for i in range(2)))
		    email =  str("".join(random.choice(tuks1)for i in range(1)))
		    for password in range(rhaby):
		        password = ''
		        for item in range(rhaby2):
		             rhaby3 = ''
		        for item in range(rhaby2):
		            rhaby3 += random.choice(rhaby1)	        
		        user = (rhaby3+email)
		        url = f"https://t.me/{user}"
		        req = ruKs.get(url)
		        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:	
		        	print(jruks+'['+BGreen+f'{N}'+jruks+'] Available'+BGreen+f' [{user}]') 
		        	RUKS3= f'https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=✥-  𝙃𝙀𝙇𝙇𝙊 𝙉𝙀𝙒 𝙐𝙎𝙀𝙍 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 .•\n━━━━━━━━━━━━\n✥. 𖣨.user : @{user} \n━━━━━━━━━━━━\n : 𝐶𝐻𝐴𝑁𝑁𝐸𝐿: @BESTxHACKER  '
		        	req = ruKs.post(RUKS3)
		        	
		        else:
		        	print(jruks+'['+BRed+f'{N}'+jruks+'] Unavailable'+BRed+f'-[{user}]')
	except:
		print('  :@B_1_2_4  ')       	
thread = []
for i in range(100):
	thread1 =threading.Thread(target=ruks)
	thread1.start()
	thread.append(thread1)
for thread2 in thread:
	thread2.join
	
	
	
	
	
