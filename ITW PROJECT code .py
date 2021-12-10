import random


def tobuychances(score,chances):
	chances=0
	score=score-25
	chances=chances+1
	print("\033[1;33;40m    your score=",score,end=" ")
	print("    your chances=",chances)
	print("\033[1;30;40m ")
	print("\033[1;36;40mInterested in playing")
	print("\033[1;30;40m ")
	k=int(input("\033[1;31;40menter 1 to play game again"))
	if(k==1):
		game(score,chances)
	else:
		print("\033[1;30;40m ")
		print("\033[1;34;40mYour purchase will be of no use")
		
	
def rollthedice():
	x=random.randint(1,6)
	y=random.randint(1,6)
	z=random.randint(1,6)
	print("\033[1;32;40m    dice1",end=" ")
	print("    dice2",end=" ")
	print("    dice3",end=" ")
	print("    sum",end="\n     ")
	print("\033[1;31;40m",x,end="         ")
	print(y,end="         ")
	print(z,end="        ")
	r=x+y+z
	print(r)
	return(r)
	

def game(score,chances):
	list11=["scartch card worth Rs.5000-/-","50% discount in flipkart shopping","95% discount in BBQ Nation","flight ticket to Dubai","Lunch with Mahendra Singh Dhoni","100% discount at Malabar & Joyallukas"]
	while(chances>0):
		if(score!=1000):
			chances=chances-1
			guessnumber=int(input("\033[1;32;40mtry your luck|| enter your guess number"))
			print("\033[0;30;40m ")
			print("\033[1;36;40m      you guessed number=",guessnumber)
			print("\033[0;30;40m ")
			s=int(input("\033[1;37;40menter 1 to roll the dice"))
			if(s==1):
				y=rollthedice()
				if(y==guessnumber):
					print("\033[0;30;40m ")
					list1=["That's like the champion!","Hip Hip Hurray!","Cheers","Bravo!!!","Greetings","Keep up with the josh"," On cloud Nine","Be full of the joys of spring"]
					print("\033[1;32;40m",random.choice(list1))
					print("you won in this chance!!,go, continue with the game ")
					score=score+100
					chances=chances+3
					print("\033[0;30;40m ")
					print("\033[1;33;40m    your score=",score,end=" ")
					print("    your chances=",chances)
					print("\033[0;30;40m ")
				else:
					print("\033[0;30;40m ")
					list2=["OOPS!!","It does not go your way......","Winners never stop trying","Failure is a step to success","The sky's the limit","winners never quit,quitters never win.....","It's an experience,Not finish","Rise up like a CHAMPION....."]
					print("\033[1;36;40m",random.choice(list2))
					print("you lost in this chance!!,it's not over,go,continue with game")
					score=score-50
					chances=chances-1
					print("\033[0;30;40m ")
					print("\033[1;33;40m    your score=",score,end=" ")
					print("    your chances=",chances)
					print("\033[0;30;40m ")
			else:
				print("\033[0;30;40m ")
				print("\033[1;31;40mdice not rolled")
		else:
			print("\033[0;30;40m ")
			print("\033[1;32;40m..^*'*^..you are $rewarded$ ..^*'*^..")
			print("\033[1;33;40m",random.choice(list11))
	if(score>0):
		print("\033[0;30;40m ")
		print("\033[1;33;40m    your score=",score,end=" ")
		print("      your chances=",chances)
		print("\033[0;30;40m ")
		print("\033[1;35;40m     you are still alive in game,,..As per game rules,you can buy chances with 25 score points")
		print("\033[0;30;40m ")
		g=int(input("\033[1;37;40menter 1., to buy chances"))
		if(g==1):
			tobuychances(score,chances)
		else:
			print("\033[1;31;40mNot interested to buy chances OK..you are up... in the game!!! restart the game")
	else:
		print("\033[1;34;40m   luck does not favoured")
		print("your score and chances are zero or negative")
		print("\033[0;30;40m ")
		print("\033[1;33;40mRESTART THE GAME")
		print("\033[0;30;40m ")
		print("\033[1;32;40mTHANK YOU FOR CHOOSING US")


def main():
	print(end="                       ")
	print("\033[1;37;40m!!!WELCOME!!!")
	print("\033[1;30;40m ")
	print(end="           ")
	print("\033[1;32;40m->>>>Wheel... of.... Fortune:THE GAME<<<<-     ")
	print("\033[0;30;40m",end="           ")
	print("\033[1;31;40m            ----Bang!;; oN yoUR lu€k!....!...! ")
	print("\n")
	print("\033[1;33;40m¥ Rules of the GaMe ¥                                   ")
	print("\033[1;35;40mIn the Game,Three dice are rolled,The sum of the numbers occured is taken as output.So a player has total 18 choices.")
	print("For every chance player is asked to guess a number of his/her choice between 1 to 18.And asked to roll the dice")
	print("--->If the guessed number and sum of numbers of dice is same, the player's score is increased by 100 points and chances are increased by 3")
	print("--->if they are not same, the player's score is reduced by 50 points and chances are reduced by 1")
	print("--->At the end,, if player's score reaches 1000 points.The player is rewarded")
	print("___Initially to procced with the game, player is given 400 points as score and 12 chances")
	print("-->if player's score is not zero but his chances are zero, then player can buy chances with 1 chance =25 score points........ ")
	print("!Note!:If player quits game in middle,he has to start again as a new player")
	print("\n")
	playername=input("\033[1;36;40menter your name please.")
	print("\033[0;30;40m ")
	print("\033[1;32;40m                   ||| Welcome!!"+' '+playername.upper()+"|||")
	print("\033[0;30;40m ")
	print("\033[1;31;40mRead the rules! if ok with rules")
	a=int(input("enter 1., to enter the game"))
	print("\033[0;30;40m ")
	if(a==1):
		global score
		score=400
		global chances
		chances=12
		print("\033[1;33;40m    your score=",score,end=" ")
		print("    your chances=",chances)
		print("\033[0;30;40m ")
		game(score,chances)
		
	else:
		print("\033[1;34;40m   NOT INTERESTED")
		print("Mark My Words,,your are going to miss the most fun time")


if __name__=="__main__":
		main()
		
		
	

