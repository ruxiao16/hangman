from random import randint
def hangman(word):
	wrong = 0
	stages = ["",
			"_________            ",
			"|                    ",
			"|          |         ",
			"|          O         ",
			"|         /|\        ",
			"|         / \        ",
			"|                    ",
			]
	rletters = list(word)
	board = ["__"]*len(word)
	win = False
	print("welcome to Hangman") 

	while wrong < len(stages) - 1:
		print("\n")
		msg = "Guess a letter: "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print((" ".join(board)))
		e = wrong + 1;
		print("\n".join(stages[0:e]))
		if "__" not in board:
			print("you win!")
			print(" ".join(board))
			win  = True
			break

	if not win:
		print("\n".join(stages[0:wrong]))
		print("you lose it was {}.".format(word))


word_bank = ["brailles","reveries","titilation","agonistic","piggy","back",
			"oblong","discretion","paradigm"]
index = randint(0,len(word_bank)-1)
hangman(word_bank[index])