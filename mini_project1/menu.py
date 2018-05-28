#! /usr/bin/env python3

import time
import webbrowser
import datetime
import whois


option = ''' 
	1 for search
	2 for image
	3 for URL name
	4 current time and date
	5 open default browser
	6 all network ip
	7 enter domain and owner name
	'''

print (option)

choice = int(input("Enter the choice:"))

if choice == 1 :
	data=input("Enter the statement:- ")
	done_data=data.strip().split()
	for i in done_data:
		webbrowser.open_new_tab("https://www.google.com/search?q="+i)
	
elif choice == 2 :
	data=input("Enter the statement:- ")
	done_data=data.strip().split()
	for i in done_data:
		webbrowser.open_new_tab("https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjMh6THoofbAhVJG5QKHVIKB1gQ_AUICigB&biw=1301&bih=670"%i)

elif choice == 3 :
	data=input("Enter the statement:-")
	done_data=data.strip().split()
	
elif choice == 4 :
	print("Time:- ",datetime.datetime.now().time())
	print("Date:- ",datetime.datetime.now().date())


elif choice == 5 :
	webbrowser.get('windows-default').open('www.google.com')
	

elif choice == 6 :
	data=input("Enter the statement:-")
	done_data=data.strip().split()

elif choice == 7 :
	data=input("Enter the domain:-")
	w = whois.whois(data)
	if w.domain_name=='null':
		print("Not registered!!")
	else:
		print("Domain-Name:- ",w.domain_name)
		print("Emails:- ",w.emails)

else :
	print("Wrong Choice!!!!!")
	time.sleep(2)
	print("Kicking you out")
	quit()
	


