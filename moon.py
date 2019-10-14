items = [
"A: 3 litres of water",
"B: Shampoo",
"C: An extra Spacesuit",
"D: A shovel",
"E: Signal flares",
"F: Solar panels",
"G: The seeds for your mission",
"H: The soil for your mission",
"I: A 3 day food supply",
"J: Two 45-caliber pistols",
"K: Parachute silk",
"L: Rope",
"M: Stellar maps of the moon's constellation",
"N: Self-inflated raft",
"O: A 10 day Oxygen supply cylinder",
"P: First aid kit",
"Q: Solar powered FM walkie talkie",
"R: Magnetic Compass",
"S: Box of Matches",
"T: Portable heating unit ",
"U: A bag full of toffees ",
]

print("It is the year 2049. You are on a solo mission to restock the base on the moon with soil and seeds to grow more plants.")
print("You have just landed but you are in trouble. You have landed 300 kilometers from the moon base!")
print("You can get to the base in 3 days on your lunar rover")
print("The lunar rover can only fit you in your spacesuit and 4 other items")
print("Out of the items below, which do you bring? \n")

for name in items:
	print(name)
print("\n")

print("Type the letter of the 4 items you would like to bring seperated by commas. Do not add spaces. And enter your answer in capital letters. \n Ex: A,B,C,D")
user_choice = input()
user_list=list(user_choice.split(','))
if "A" in user_list and "O" in user_list and "F" in user_list and "I" in user_list:
	print("Congratulations!!! You will be able to make to the moonbase safely. You are ready for 2049 ;P")
else:
	print("Oops! You didn't pick the right items. Sorry, You won't be able to make it to the moonbase safely :(")

if "A" not in user_list:
	print("Without a litre of water a day, you will definitely dehydrate.")
if "O" not in user_list:
	print("Without oxygen, you won't have anything to breathe in.")
if "F" not in user_list:
	print("Without solar panels, your lunar rover will not have enough power to make it to the base .")
if "I" not in user_list:
	print("Without sufficient food, you won't be able to make it to the base. How you will get energy to drive the rover?")
if "B" in user_list:
	print("What on moon would you do with shampoo on moon?! Must be having a flare for washing your hair on moon ...")
if "C" in user_list:
	print("Another spacesuit is good but in comparision to other things , its not that important")
if "D" in user_list:
	print("Shovel : Wanna dig up a tunnel to moonbase ?")
if "G" in user_list:
	print("Seeds : Are you planing to set up a garden on moon?")
if "H" in user_list:
	print("Soil : It has no use over there.")
if "J" in user_list:
	print("Remarkably, pistols do work in a vacuum because of the oxidizer in the gun powder. But what are you going to use them for? Shoot at some random rocks for fun? I'd leave them behind too.")
if "K" in user_list:
	print("Parachute silk: Have you seen moon gloves? How are you going to do anything with something that fine? Leave it behind.")
if "L" in user_list:
	print("Rope: Hard to think of a situation where 50 feet of rope could come in handy while driving across the moon")
if "M" in user_list:
	print("Stellar maps: The moon's constel-what??? This is not even  a thing! The moon doesn't have a constellation, whatever that means. I guess I'd bring it for a good laugh when I start getting depressed about dying. Otherwise, it stays.")
if "N" in user_list:
	print("Self-Inflated Raft: Too heavy and useless. Not worth bringing it")
if "E" in user_list:
	print("Signal Flares: Useless and dangerous. Not worth bringing it. Seriously, who's going to see the flare? Observers on earth?")
if "P" in user_list:
	print("First-aid Kit: Already present in spacesuit. Not so important to take it .")
if "Q" in user_list:
	print("Intriguing. FM has pretty good range. Probably really good range on the moon. But who has the other walkie talkie? I guess I could leave on behind to talk to the folks I left, but the bigger problem is, how would you use it? If you hold it up to your head to use like regular walkie talkies, they won't hear anything. Oh, so close! Not needed.")
if "R" in user_list:
	print("Compass: Useless since there is no magnetic field. Not worthy bringing it.")
if "S" in user_list:
	print("Box of matches : Useless as there is nothing to burn.")
if "T" in user_list:
	print("Portable heating unit : Not needed unless you are on the dark side.")
if "U" in user_list:
	print("A bag full of toffees : Not needed unless you aim to share them with aliens :P.")




