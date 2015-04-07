#######################################################################
#####  Version 0.1.0-alpha of Michael A.'s first python program:  #####
#####     PLACEHOLDER TITLE - A Medieval Text-based Adventure     #####
#######################################################################

from sys import exit

#def act_iia(): 
	#Act II-A - The Escape
#def act_iib(): 
	#Act II-B - Peaceful Surrender
#def act_iic(): 
	#Act II-C - Forced Surrender

def dead(why):
	print why, "Game Over."
	exit(0)


def aa_tackle():
	print "You run at the man in an attempt to tackle him."
	print "The heavy weight of the torch slows you down."
	print "He has plenty of time to react and slides his sword"
	print "between your ribs. He yanks the sword back out."
	dead("You collapse in pain and die in a pool of your own blood.")


def aba_run():
	print "You run for the door as the man is staggered, quickly"
	print "grabbing his sword on the way out. You find yourself in"
	print "a hallway with another door at the end. You run toward"
	print "the door and exit swiftly...\n"
	#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iia()


def abb_2ndswing():
	print "You think since since you managed to get one good hit in, maybe"
	print "you can take this guy out. You draw back the torch and swing it"
	print "again, but he's too quick. He dodges the blow and in the same quick"
	print "motion, he draws a sharp dagger and sticks you in the neck."
	dead("Everything fades as you lie on the ground bleeding out.")


def ab_swing():
	print "You run towards the man and take a swing at him."
	print "The torch connects with a thud against his head and"
	print "he staggers backwards, dropping his sword. Knocked back,"
	print "but not out.\n"
	print "What do you do?"
	print "----------------------"
	print "A. Run for the door."
	print "B. Take another swing."
	print "----------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			aba_run()
		elif next == "B":
			abb_2ndswing()
		else:
			print "Sorry, I do not understand. Please type A or B."


def aca_surrender():
	print "You surrender the torch to him. He pulls a small length of"
	print "rope out and ties your hands behind your back. He then nudges"
	print "you out the doorwar into a hallway where another open door"
	print "awaits...\n"
	#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iib()


def acb_fight():
	print "You pretend to hand over the torch. As he reaches for it, you"
	print "swing it at his face. He expertly dodges the blow and swiftly"
	print "brings the pommel of his sword down upon the top of your head."
	print "The room spins as you drift into unconsciousness and fall to"
	print "the ground. He ties your hands up and drags you out the door"
	print "and down the hallway. Maybe trying to trick him wasn't the"
	print "best option...\n"
	#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iic()


def ac_explain():
	print '"Honestly sir, I do not know. I woke up minutes ago in this'
	print 'room and cannot remember a thing." He looks you up and down and'
	print 'then states, "This area of the castle has been locked down for'
	print 'months. I have no idea how you got in here. No matter, I must'
	print 'take you to the head guard. He will decide your fate. Please'
	print 'hand me that torch."\n'
	print "What do you do?"
	print "-------------------------------------"
	print "A. Surrender the torch."
	print "B. Give him the torch... To his face!"
	print "-------------------------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			aca_surrender()
		elif next == "B":
			acb_fight()
		else:
			print "Sorry, I do not understand. Please type A or B."

def a_torch():
	print "You pick up the torch."
	print "Suddenly the door bursts open."
	print "A man armed with a drawn longsword and suited in chainmail armor"
	print "from head to toe rushes in the room.\n"
	print '"I heard a loud explosion come from this room. Who are you?"\n'
	print "What do you do?"
	print "------------------------------"
	print "A. Attempt to tackle the man."
	print "B. Swing the torch at the man."
	print "C. Explain your situation."
	print "------------------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			aa_tackle()
		elif next == "B":
			ab_swing()
		elif next =="C":
			ac_explain()
		else:
			print "Sorry, I do not understand. Please type A, B, or C."
	exit(0)


def baa_sword():
	print "You grab his sword and not wanting to wait around, you run out"
	print "the door and find yourself in a hallway. There is another open"
	print "door at the end. You run out it to the mysteries that lie beyond.\n"
	#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iia()

def bab_armor():
	print "You decide that taking your time in order to be better armed is"
	print "worth the risk. You struggle to remove his helmet, then reach to"
	print "pull off his chainmail hauberk. He suddenly jolts awake and"
	print "pushes you off, knocking you to the ground. He draws a dagger and"
	print "plunges it toward your heart. You grab his hands holding it back"
	print "in the classic cliche way, but his strength proves too much."
	dead("Everything fades as the knife slides home into your chest.")


def ba_tackle():
	print "You sprint toward the man hitting him with enough force to slam"
	print "his head against the wall. He slumps, appearing unconscious.\n"
	print "What do you do?"
	print "------------------------------"
	print "A. Grab his sword and leave."
	print "B. Loot his sword and armor."
	print "------------------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			baa_sword()
		elif next == "B":
			bab_armor()
		else:
			print "Sorry, I do not understand. Please type A or B."


def bb_stab():
	print "You run at the man. You thrust the dagger toward his heart before"
	print "he even has a chance to react. Unfortunately for you, the"
	print "dagger was in worse shape than you thought. The rusted blade snaps"
	print "as it makes contact with his armor. He laughs as he lifts his sword"
	print "and brings the sharp blade down on you."
	dead("Well, that's one way to solve your amnesia problem.")


def bca_follow():
	print "You surrender to him. He pulls out a short piece of rope and"
	print "ties your hands behind your back. He then reaches down and"
	print "confiscates the dagger. Damn, he saw you hide it. He then nudges"
	print "you out the doorway to the end of the hallway where another"
	print "open door awaits..."
	#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iib()


def bcb_stab():
	print 'You "surrender" to him. He pulls out a piece of rope. As he'
	print "reaches out to tie your hands, you pull the dagger. You take"
	print "a stab at killing your would-be captor. The dagger connects with"
	print "his armor and the blade crumbles. Damn, that thing was in even"
	print "worse shape than you thought. He punches you in the face, the"
	print "impact of his gauntlets knocking you unconscious. He ties your"
	print "hands up and drags you out the door. You're rather sure that"
	print "attempted murder isn't going to make the best first impression..."
		#Delete the next 3 lines when Act II is completed.
	print "TO BE CONTINUED IN ACT II..."
	exit(0)
	#Undo comment on this line when Act II is completed.
	#act_iic()


def bc_explain():
	print "You quickly hide the dagger in your boot and answer,"
	print '"Honestly sir, I do not know. I woke up minutes ago in this'
	print 'room and cannot remember a thing." He looks you up and down and'
	print 'then states, "This area of the castle has been locked down for'
	print 'months. I have no idea how you got in here. No matter, I must'
	print 'take you to the head guard. He will decide your fate."\n'
	print "What do you do?"
	print "----------------------------"
	print "A. Follow him peacefully."
	print "B. Stab him with the dagger."
	print "----------------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			bca_follow()
		elif next == "B":
			bcb_stab()


def b_dagger():
	print "You pick up the rusty dagger. Suddenly the door burts open."
	print "A man armed with a drawn longsword and suited from head to toe"
	print 'in chainmail armor rushes in. "I heard a loud explosion come'
	print 'from this room. Who are you?"\n'
	print "What do you do?"
	print "------------------------------"
	print "A. Attempt to tackle the man."
	print "B. Attempt to stab the man."
	print "C. Explain your situation."
	print "------------------------------"

	while True:
		next = raw_input(">> ")

		if next == "A":
			ba_tackle()
		elif next == "B":
			bb_stab()
		elif next == "C":
			bc_explain()
		else:
			print "Sorry, I do not understand. Please type A, B, or C."


def act_i():
	print "------------------"
	print "ACT I - THE ROOM"
	print "------------------"
	print "You awake in a small room."
	print "You don't remember anything."
	print "You look around the room to see what you can see."
	print "You see a door straight in front of you."
	print "You see a rusty dagger in the middle of the room."
	print "You also see a rather large metal torch on the back wall.\n"
	print "What do you do?"
	print "------------------"
	print "A. Pick up torch." 
	print "B. Pick up dagger."
	print "------------------"
	
	while True:
		next = raw_input(">> ")

		if next == "A":
			a_torch()
		elif next == "B":
			b_dagger()
		else:
			print "Sorry, I do not understand. Please type A or B."





print "*****************************************************************"
print "Welcome to PLACEHOLDER TITLE - A Medieval Text-based Adventure..."
#print "Please name your adventurer..."

#usrname = raw_input(">> ")

act_i()