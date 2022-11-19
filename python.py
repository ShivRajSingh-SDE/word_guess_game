#Step 1 

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(f"Your chossen word is {chosen_word}")



display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
  
  display += "_"


guess = input("Guess a letter: ").lower()


for posstion in range(word_lenght):
  letter = chosen_word[posstion]

  if letter == guess:
    display[posstion]= letter
    
print(display)
  
ss

