#v3_stable
# вход
print("login")
log = input ("login: ")
if log == "Bodia":
	print ("login is ok! ")
print("password: ")
pas = input ("password: ")
if pas == "ConyCony":
	print("password is correct")
	print("please whait!")
	sys = True


#если пароль неверный 
else:
	print("pass or login is not correct!")
	sys = False
	#если правильно
if sys == True:
	print("pass is ConyCony")
	import time
	import webbrowser
	webbrowser.open('klubok.bazar.kr.ua')
	print("Do you want to watch youtube?")
	v = input ("y n ")
	if v == "y ":
		webbrowser.open("youtube.com")

	print("you will go to assistant!")
	time.sleep(4)
	print("Hi, " + log )
	print("Do you want to lock system?")
	lock1 = input ("y or n")
	if lock1 == "y":
		print ("system was lock!")
		sys = False
		pas = input ("password: ")
		if pas == "ConyCony":
			print("password is correct")
			print("please whait!")
			sys = True
	print("you will go to assistant!")
	print("Hi, " + log )
	print("your quation ")
	print("when you want to lock system you may tipe 'lock' ")
	qua = input ("your quation")
	if qua == "lock":
		print ("system was lock!")
		sys = False
		pas = input ("password: ")
		if pas == "ConyCony":
			print("password is correct")
			print("please whait!")
			sys = True
	#framework
	print("Do you want to open framework?")
	fr1 = input ("yes or no")
	if fr1 == "yes":
		pass1 = input ("password")
		if pass1 == "ConyCony":
		frame = True
		if frame == True:
			print("{[framework is loading...]}")
			time.sleep(2)
			print("welcome!")
			print("hello " + log)
			print("If you want exit print 'exit' ")
			quf = input(quation )
			if quf == "exit":
				exit()
			elif quf == "hello":
				print("hello " + log )
			elif quf == "How are you?":
				print("Im fine, and you?")
				ge = input
				if ge == good:
					print("Its good!")
					elif ge == "bad"
					print("its bad!")
				if quf == "quit":
					frame = False
					print("its all for now,  this is 3v so.... ") 
					exit() 
				
					
			else:
				print("what? ") 
			



