global money
global m
global q
global a

money=0
q=-1
m=0
a=0



menu={
	1:["a",10, 100],
	2:["b",10, 200],
	3:["c",10, 300],
	4:["d",10, 400],
	5:["e",10, 500],
	6:["f", 10, 600],
	7:["g",10, 700],
	8:["h",10, 800],
	9:["i",10, 900]
}

def print_menu():
	print "==================================================="
	for k, v in menu.items():
		print "button:%d : name-%s  amount-%d  won-%d " % (k,v[0], v[1], v[2])
	print "==================================================="
	

def input_money():
	global q
	global money
	global m

	
	while  True:
		m=input('Insert coin: ')
		money+=m
		if m==-1:
			money+=1
			break
	print_menu()
	print "You have %d won"% money
	

input_money()



while  True:
	select=input('select the good:') 
	if select==1:
		if money-100<0:
			print "lack of money"
			input_money()
		if money-100>=0 and menu[1][1]>0:
			menu[1][1]-=1
			money-=100
			print_menu()
		if menu[1][1]<=0:
			print "lack of this good"
		
	elif select==2:
		if money-200>=0:
			menu[1][1]-=1
			money-=200
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money-200<0:
			
			print "lack of money"
			input_money()
	elif select==3:
		if money>0:
			menu[1][1]-=1
		money-=300
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=300
			print "lack of money"
			input_money()
	elif select==4:
		if money>0:
			menu[1][1]-=1
		money-=400
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=400
			print "lack of money"
			input_money()
	elif select==5:
		if money>0:
			menu[1][1]-=1
		money-=500
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=500
			print "lack of money"
			input_money()
	elif select==6:
		if money>0:
			menu[1][1]-=1
		money-=600
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=600
			print "lack of money"
			input_money()
	elif select==7:
		if money>0:
			menu[1][1]-=1
		money-=700
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=700
			print "lack of money"
			input_money()
	elif select==8:
		if money>0:
			menu[1][1]-=1
		money-=800
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=800
			print "lack of money"
			input_money()
	elif select==9:
		if money>0:
			menu[1][1]-=1
		money-=900
		print_menu()
		
		if menu[1][1]<=0:
			print "lack of this good"
		if money<0:
			money+=900
			print "lack of money"
			input_money()