import sys

global money
global q
global button

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

def select():
	global button
	global money

	print "==================================================="
	for k, v in menu.items():
		print "button:%d : name-%s  amount-%d  won-%d " % (k,v[0], v[1], v[2])
	print "==================================================="
	print ""
	button=input( 'selct the button:')
	if money-menu[button][2]>=0 and menu[button][1]>0:
		print "%s come out" %menu[button][0]
		menu[button][1]-=1
		money-=menu[button][2]
		print "You have %dwon" % money
		select()
		
	if money-menu[button][2]<0:
		print " Lack of money to buy this tiem" 
		print "You have %dwon" % money
		wait()

	if menu[button][1]==0:
		print "Empty of item"
		select()
		


def wait():
	global button
	global money
	
	global q
	
	q=-1
	a=input('Insert your money:')
	money+=a
	print "You have %dwon" % money
	if a==-1:
		sys.out()
	if money>=0:
		select()


money=0
q=-1

wait()



