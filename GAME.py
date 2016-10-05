import msvcrt
import time

finish=5
finish1=8
count1=0
count=0

print "PRESS ENTER TO START THE GAME"

raw_input()
s_time=time.time()

print "PRESS D 5 TIMES FOR MOVING RIGHT "
print "ENTER S 8 TIMES FOR MOVING DOWN"
print "PRESS D 5 TIMES FOR MOVING RIGHT "
print '\n'
print "WARNING!!!  IF U PRESS ANY WRONG BUTTON U ARE OUT"
print '\n'

a=5

while(a>0):
	key=msvcrt.getch()
	if key=='d':

		count=count+1
		print ("_____"),
		
		a=a-1

		if count==finish:
			print '\n',
			continue
			print '\n',
	else:
		print '\n',
		print "SORRY!!! YOU ARE OUT",
		pass
		

			

b=8

while(b>0):
	
	key=msvcrt.getch()
	if key=='s':

		count=count+1
		print ("                             |"),
		print '\n',

		b=b-1

		if count1==finish1:
			print '\n',
			continue
			print '\n',

	else:
		print '\n',
		print "SORRY!!! YOU ARE OUT",
		pass
		

c=5
print ("                             ____"),
while(c>0):
	
	key=msvcrt.getch()
	if key=='d':

		count=count+1
		print ("_____"),
		c=c-1

		if count==finish:
			print '\n',
			continue
			print '\n',

	else:
		print '\n',
		print "SORRY!!! YOU ARE OUT",
		pass
		print '\n'
		

time_elapsed=time.time()-s_time


print '\n'
print '\n'
print "CONGRATULATIONS YOU HAVE WON THE GAME "
print '\n'
input=raw_input()

'''
1. The no. of moves in a particular direction shouldn't be told in the program.
2. The program should exit after the game is lost
3. "Turn right" or "turn down" should be printed once end of a particular direction is reached.
4. Time for completing the game should be printed
'''
