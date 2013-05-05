import pymysql 
import sys
import random

number_of_db=1

rounds=int(input('Enter number of rounds:'))
print('Number of rounds:',rounds)

if(rounds<=-2):
	print("Invalid number of rounds...exiting")
	exit()
if(rounds>20):
	print("More than 20 rounds?!...exiting")
	exit()


#set up connection to DB
con=pymysql.connect(host='localhost',user='root',passwd='BLAH',db='German')
conn=con.cursor()

#get results from query result tuple
def english(r):
	return r[1]

def german(r):
	return r[0]


score=0
#compares provided correct answer with guess
def check_correct(correct,translations):
	#read line also includes newline-> prolly a nicer way
	if(str(correct.lower()+'\n') == str(translation).lower()):
		print("correct")
		global score
		score+=1
	else:
		print("wrong")
		print("we are given the following")
		print("translation", translation,"result",correct)

def get_list():
	conn.execute("select * from Verb order by rand() limit %s",rounds)
	results=conn.fetchall()
	#print(results)
	conn.execute("select * from Noun order by rand() limit %s",rounds)
	results+=conn.fetchall()
	#print(results)
	conn.execute("select * from Adjective order by rand() limit %s",rounds)
	results+=conn.fetchall()
	t=randomize_tuple(results)
	return t

def randomize_tuple(t):
	l=list(t)
	i=range(len(t))
	#print(l)
	random.shuffle(l)
	#print(l)
	t=tuple(l)
#	print(t)
	return t

quiz_t=get_list()

print("this is the quiz list: ",quiz_t)
r=1; #counter for rounds

for i in quiz_t:
	if(r>rounds):
		break
	direction=bool(random.getrandbits(1))
	print("Round: ",r)
	print("---------------------")
	if(direction): #direction is true so ger->eng
		print (german(i))
		translation=sys.stdin.readline()
		correct=english(i)
		check_correct(correct,translation)
	else: #direction is false so eng->ger
		print(english(i))	
		translation=sys.stdin.readline()
		correct=german(i)
		check_correct(correct,translation)
	r=r+1
	print("\n")


conn.close()
con.close()
print("score: ",score)
