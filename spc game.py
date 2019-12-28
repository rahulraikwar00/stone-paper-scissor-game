#this is a simple game using python
import random
d = {1:"stone", 2:"papper", 3:"scissor"}
i = 1
your_score = 0
my_score = 0
draw = 0
print("\t\t\tMOST WELCOME TO THE LUCK GAME \n")
while i<9:
	print(" \tpls select your charm number")
	randomvalue = random.choice(list(d.values()))
	print("    \t  ready  1 2 3 start \n ")
	print("\t1 stone\n\t2 papper\n\t3 scissor")
	op =input("\t")
	try:
		opi = int(op)
		user_input = d[opi]
		if randomvalue == d[1]:
			if user_input == d[1]:
				print("\t____draw____")
				draw +=1
			elif user_input == d[2]:
				print("\t____i win____")
				my_score +=1
			else:
				print("\t____you win____")
				your_score +=1
		elif randomvalue == d[2]:
			if user_input == d[2]:
				print("\t____draw____")
				draw +=1
			elif user_input == d[3]:
				print("\t____i win____")
				my_score +=1
			else:
				print("\t____you win____")
				your_score +=1
		elif randomvalue == d[3] :
			if user_input == d[1]:
				print("\t____you win____")
				your_score +=1
			elif user_input == d[2]:
				print("\t____i win____")
				my_score +=1
			else:
				print("\t____draw____")
				draw +=1
		print(F" \t ME :___{randomvalue} and YOU :___{user_input}\n")
		v = 9 - i
		i +=1
		print(f"\tyou left {v} chancs\n\n")
	except :
		print("\twrong input\n \tWANT TO CONTINUE...? (y/n)_")
		error = input("\t")
		if error == 'n':
			break
		elif error == 'y':
			pass
		else :
			continue	
print("\t_______GAME FINISH_______\n")			
if your_score >my_score:
	print("\t..............congratulation  you win.................\n")
else:
	print(" \t...............you lose ............!\n\n")	
print(f"\tmy score : {my_score}\n\tyour score: {your_score}\n\tdraw: {draw}")						