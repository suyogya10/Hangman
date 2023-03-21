# Coding Challenge 3, hangman.py
# Name: Suyogya Gautam
# Student No: 2059802

import random
import string
import os

WORDLIST_FILENAME = "words.txt"

responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):

    let=True
    while let:
        random.choice(all_words)
        if random.choice(all_words) in random_letters:
            pass
        else:
            let=False
            return random.choice(all_words)

def load_words():

    file_text=open(WORDLIST_FILENAME,"r")
    all_words=file_text.read().split()
    file_text.close()
    
    return all_words
    

def is_word_guessed(word, letters_guessed):

    
    if letters_guessed in word:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return True
    else:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return False


def get_guessed_word(word, letters_guessed):

    
    if len(text)==0:
        for char in word:
            if letters_guessed==char:
                text.append(letters_guessed)
            else:
                text.append("_")

    else:
        i=0
        for e in word:
            if letters_guessed==e:
                text[i]=e
            i+=1
            
    return text


def get_remaining_letters(letters_guessed):

    from string import ascii_lowercase
    string=ascii_lowercase
    for elem in letters_guessed:
        string=string.replace(elem,"")
    return string

def get_score():
    
    ranking={}

    if not os.path.isfile("scores.txt"):
        message="No Score exists"
        return message
        
    else:
        scr=open("scores.txt","r")
        for lines in scr:
            ln=lines.strip("\n").split(" ")
            score=ln[0]
            name=ln[1]
            ranking.update({name:score})
        return ranking
    


def save_score(name, score):
    lst=[]
    while True:
        if os.path.isfile("scores.txt")==True:
            if not os.stat("scores.txt").st_size == 0:
                file=open("scores.txt","r")
                lines=file.readlines()
                for line in lines:
                    stripped=line.strip("\n")
                    file_index=stripped.split(" ")
                    if name==file_index[1]:
                        if score>=int(file_index[0]):
                            rev=str(score)+" "+name
                            lst.append(rev)
                        
                            
                        else:
                            lst.append(stripped)
  
                            
                            
                    else:
                        striped=line.strip("\n")
                        lst.append(striped)
                        rev=str(score)+" "+name  
                        if rev not in lst:
                            rev=str(score)+" "+name    
                            lst.append(rev)
            else:
                file=open("scores.txt","w")
                rev=str(score)+" "+name
                file.write(rev)
                file.write("\n")
                lst.append(rev)
                
                
            break
        else:
            file=open("scores.txt","w")
            rev=str(score)+" "+name
            file.write(rev)
            file.write("\n")
            lst.append(rev)
            
    file=open("scores.txt","w")
    for elem in lst:
        file.write(elem)
        file.write("\n")
        
    file.close()

        
wordlist = load_words()
print("Loading words..")
print(len(wordlist))
print("Welcome to Hangman Ultimate Edition")


def hangman(word):
    game_mech=False
    attempts=6
    
    print(word)

    #choice 
    while True:
        menu_input=str(input("Do you want to Play (p) view the leaderboard (l) or quit (q):").lower())

        if menu_input!="p" and menu_input!="l" and menu_input!="q":
            print("Invalid Input!")
        else:
            break
    #player name
    if menu_input=="p":
        print("*************************")
        print("NOTE: ENTER YOUR FULL NAME")
        while True:
            user_name=str(input("What is your name? :").lower())
            if user_name=="":
                print("Invalid Input!")
            else:
                break
        print(responses[0].format(len(word)))
        print("*************************")
        # Game main
        while not game_mech:
            print(responses[4].format(attempts))
            print(responses[5].format(get_remaining_letters(used_letters)))
            while True:
                guessed_letter=str(input("Please guess a letter:").lower())
                if len(guessed_letter)>1 or guessed_letter==" " or guessed_letter=="":
                    print("Invalid!")
                else:
                    break
                
            if guessed_letter not in used_letters:
                if is_word_guessed(word, guessed_letter)==True:
                    get_guessed_word(word, guessed_letter)
                    print(responses[6].format(" ".join(text)))
                    print("------------")
                    
                    #win
                    if "".join(text)==word:
                        print(responses[1])
                        score=len(set(word))*attempts
                        print("Your total score for this game is:{}".format(score))
                        random_letters.append(word)
                        game_mech=True
                        rounds[0]+=1
                        if rounds[0]>0:
                            empty_word.clear()
                            text.clear()
                            used_letters.clear()
        
                        loop=True
                        while loop:
                            end_input=str(input("A new personal best! Would you like to save your score(y/n):").lower())
                            if end_input !="y" and end_input !="n":
                                print("Invalid Input")
                            else:     
                                if end_input=="y":
                                    print("Ok, your score has been saved.")
                                    save_score(user_name,score)
                                    print("*************************")
                                    intp=str(input("Would you like to restart?(y/n)").lower())
                                    if intp=="y":
                                        word = choose_random_word(wordlist)
                                        hangman(word)
                                    else:
                                        print("Thanks for playing, goodbye!")
                                else:
                                    intp=str(input("Would you like to restart?(y/n)").lower())
                                    if intp=="y":
                                        word = choose_random_word(wordlist)
                                        hangman(word)
                                    else:
                                        print("Thanks for playing, goodbye!")
                                loop=False
                                
                        
                # wrong 
                else:
                    if not text:
                        print(responses[7].format(" ".join(empty_word)))
                        print("*************************")
                    else:
                        print(responses[7].format(" ".join(text)))
                        print("*************************")
                    vowel="aeiou"
                    if guessed_letter in vowel:
                        attempts-=2
                    else:
                        attempts-=1  
            # Repeat   
            else:
                print(responses[8].format(" ".join(text)))
                print("*************************")
                
            #loss
            if attempts<=0:
                random_letters.append(word)
                print(responses[3].format(word))
                game_mech=True
                rounds[0]+=1
                if rounds[0]>0:
                    empty_word.clear()
                    text.clear()
                    used_letters.clear()
                intp=str(input("Would you like to restart?(y/n)").lower())
                if intp=="y":
                    word = choose_random_word(wordlist)
                    hangman(word)
                else:
                    print("Thank you for playing HANGMAN ULTIMATE EDITION!")
                    
    elif menu_input=="l":
        
        ranks=get_score()
        if os.path.isfile("scores.txt"):
        
            if len(ranks)==0:
                print("*************************")
                print("\n")
                print("   "+"No saved progress!")
                print("\n")
                print("*************************")
                intp=str(input("Would you like to restart?(y/n)").lower())
                if intp=="y":
                    word = choose_random_word(wordlist)
                    hangman(word)
                else:
                    print("Thanks for playing, goodbye!")
                
            else:   
                ranks=get_score()
                sort= sorted(ranks.items(), key=lambda t:t[1], reverse=True)
                print("{:<15}{:<15}".format("Score","Names"))
                print("*************************")   
                for i in range(0,len(sort)):
                    print("{:<15}{:<15}".format(sort[i][1],sort[i][0]))
                print("*************************")
                intp=str(input("Would you like to restart?(y/n)").lower())
                if intp=="y":
                    word = choose_random_word(wordlist)
                    hangman(word)
                else:
                    print("Thanks for playing, goodbye!")
            
        else:
            print("*************************")
            print("\n")
            print("   "+"No saved progress!")
            print("\n")
            print("*************************")
     
empty_word=[]
text=[]
used_letters=[]
rounds=[0]
random_letters=[]
# Driver function for the program
if __name__ == "__main__":
    word = choose_random_word(wordlist)
    #word = "abc" testing ko lagi
    for i in range(0,len(word)):
        empty_word.append("_")
    hangman(word)
    #a word is already given for the teacher to check the program.
    
  
    


    
