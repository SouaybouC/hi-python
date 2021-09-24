import random

word_list = ["abaft", "abandoned", "abashed", "aberrant", "abhorrent", "abiding", "abject", "ablaze",
                 "able", "abnormal", "aboard", "aboriginal", "abortive", "abounding", "abrasive", "abrupt", "absent",
                 "absorbed", "absorbing", "abstracted", "absurd", "abundant", "abusive", "accept", "acceptable",
                 "accessible", "accidental", "account", "accurate", "achiever", "acid", "acidic", "acoustic",
                 "acoustics", "acrid", "act", "action", "activity", "actor", "actually", "ad hoc", "adamant",
                 "adaptable", "add", "addicted", "addition", "adhesive", "adjoining", "adjustment", "admire", "admit"]
nb_guess = 1
good_guess = 0
word = [letter for letter in random.choice(word_list)]
word_copy = word.copy()
user_word = [""] * len(word)
print(user_word)
while(nb_guess <(len(word)+3) or user_letter == word or nb_guess == 1):  
    print("Choose your letter: ")
    user_letter = input()
    if user_letter in word_copy : 
        
        letter_index = word_copy.index(user_letter)
        user_word.insert((letter_index + len(word)-len(word_copy)),user_letter)
        word_copy.remove(user_letter) 
        good_guess+=1
        user_word.remove("")
        print("You have "+str(nb_guess)+"life(ves)")
    else : print("WRONG")
    print(user_word)
    nb_guess+=1
