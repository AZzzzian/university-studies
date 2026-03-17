import string
import time
import random
def gradual_typing(text, speed=0.01):
    lowercase_alphabet = list(string.ascii_lowercase)
    punctation_mark = list(string.punctuation)
    full_characters = lowercase_alphabet + punctation_mark
    i = x = 0
    words = list(text)  # 你需要print的words
    length = len(words)
    while x < length:
        while i < 57:
            printing_number = full_characters[i]  # 快速通过的字母+符号
            c = words[x]  # 需要的字母第x位
            d = [s.lower() for s in c]  # 全部小写再根据原本大写
            e = ','.join(map(str, d))   # 将列表转换回字符
            if ' ' in c:
                time.sleep(speed)
                print(" ",end="",flush=True)
                break
            else:
                if printing_number == e:
                    print(c,end="",flush=True)
                    time.sleep(speed)
                    break
                else:
                    print(printing_number,end="")
                    time.sleep(speed)
                    print("\b",end="",flush=True)
            i = i + 1
        i = 0
        x = x + 1
    print()
def get_word():
    with open("words_need", "r", encoding="utf-8") as file:
        lines = file.readlines()
        return random.choice(lines).strip()
def check_word(w):
    if len(w)== 6:
       if w.isalpha():
           return w
       else:
           print("typing wrong, please try again:")
           w = input()
           return check_word(w)
    else:
        print("typing wrong, please try again:",end="")
        w = input()
        return check_word(w)
def print_colored(text, color):
    colors = {"green": "\033[32m", "red": "\033[31m", "yellow": "\033[33m","reset": "\033[0m"}
    print(colors[color] + text + colors["reset"],end=" ")
def guessing_hard_mode(w,turns=0):
    running=True
    while running:
        guess = []
        if 9-turns > 0:
            print("remaining attempts:", 9 - turns)
        else:
            print("attempts used:", turns)
        guess_word = str.lower((input("Your guess:")))
        guess.extend(check_word(guess_word))
        print("++---++---++---++---++---++---++") #print the form
        for i in range(6):
            print("||",end=" ")
            if guess[i]==w[i]:
                print_colored(guess[i], "green")
                time.sleep(0.5)
            else:
                print_colored(guess[i], "red")
                time.sleep(0.5)
            print(end="")
        print("||",end="\n")
        print("++---++---++---++---++---++---++")
        if guess == word:
            print("\nCongratulations!You guessed the word!", "using", turns+1, "turns!")
            running=False
        if turns == 9:
            print("No more attempts!\n1.Continue to try more\n2.Check the answer\nEnter your choice:", end="")
            choice = input()
            if choice == "1":
                guessing_hard_mode(word,turns)
            if choice == "2":
                print("answer is:", ''.join(word))
        turns += 1
    print(end="\n")
def guessing_ez_mode(w,turns=0):
    running=True
    if dumb_mode == True:
            turns = 7
    while running:
        guess = []
        if 9 - turns > 0:
            print("remaining attempts:", 9 - turns)
        else:
            print("attempts used:", turns)
        guess_word = str.lower((input("Your guess:")))
        guess.extend(check_word(guess_word))
        print("++---++---++---++---++---++---++") #print the form
        for i in range(len(guess)):
            if guess[i]==w[i]:
                print("||",end=" ")
                print_colored(guess[i], "green")
                time.sleep(0.5)
            elif guess[i] in w:
                print("||",end=" ")
                print_colored(guess[i], "yellow")
                time.sleep(0.5)
            else:
                print("||",end=" ")
                print_colored(guess[i], "red")
                time.sleep(0.5)
        print("||", end="\n")
        print("++---++---++---++---++---++---++")
        if guess == word:
            if dumb_mode == True:
                gradual_typing("Congratulation! You just get the word I told you. SOOOOO SMART! ")
                running=False
            else:
                print("Congratulations!You guessed the word!", "using", turns+1, "turns!")
                running=False
        if turns == 8:
            if dumb_mode == True:
                gradual_typing("No doubt you are a dumb")
                gradual_typing("or? you find the special surprise!")
                gradual_typing("congrats! you are a dumb!")
                with open('message.txt', 'w', encoding='utf-8') as file:
                    file.write("you are a dumb")
                print("go check your message.txt")
                exit(0)
            else:
                print("No more attempts!\n1.Continue to try more\n2.Check the answer\nEnter your choice:", end="")
                choice = input()
                if choice == "1":
                    guessing_ez_mode(word,turns)
                if choice == "2":
                    print("答案为：", ''.join(word))
        turns += 1
def test_choice():
    guess_time=0
    while guess_time<=3:
        global dumb_mode
        try:
            choice = int(input())
            if 1<= choice <= 4:
                guess_time = 3
                return choice
            else:
                if guess_time >= 2:
                    gradual_typing("No way, you write wrong again", 0.002)
                    gradual_typing("so, u dont like that number", 0.002)
                    gradual_typing("don't worry, I can start it for you", 0.002)
                    gradual_typing("--playing dumb mode--")
                    dumb_mode = True
                    return 1
                else:
                    gradual_typing("Please enter a valid choice.")
                    guess_time = guess_time + 1
        except:
            if guess_time >= 2:
                gradual_typing("No way, you write wrong again", 0.002)
                gradual_typing("so, u dont like that number", 0.002)
                gradual_typing("don't worry, I can start it for you", 0.002)
                gradual_typing("--playing dumb mode--")
                dumb_mode = True
                return 1
            else:
                gradual_typing("it seems like you didn't enter a number")
                gradual_typing("please try again:D")
                guess_time=guess_time+1
def print_manu():
    print("+---------------------------------------------+")
    gradual_typing("|Welcome to Wordle 6 - Computing Words Edition!|", 0.003)
    gradual_typing("|one. Start Game(ez one)                      |", 0.003)
    gradual_typing("|two. Start Game(hard mode)                   |", 0.003)
    gradual_typing("|three. Instructions                          |", 0.003)
    gradual_typing("|four. Quit                                   |", 0.003)
    print("+-----------------------------------------------+")
def print_instructions():
    gradual_typing("nice to see you here, sir")
    gradual_typing("wondering if u see this familiar,well that is me, Zirui Zhao, I shew this code before, now what you seeing is the iterated version")
    gradual_typing("which also improved by myself")
    gradual_typing("I wrote these all by myself, also learning something through Internet ofcourse")
    gradual_typing("so, hope u having fun:D")
    print("\n")
dumb_mode = False
# THIS the LITTLE SURPRISE FOR U, MY RESPECTED TEACHER :D

#I know you didn't want to see this, but you can try to be stupid actually, believe in me

# I used the typing code I wrote before but considering the typing need to be fast, so it maybe not that apparent

# I prepared a surprise for u! sir! you have to be a dumb and type wrong for 2 more times!
finished= True
while finished:                            # manu
    print_manu()
    gradual_typing("Enter your choice:")
    choice=test_choice()
    if choice == 1:                 #esay mode
        print("game starts!(ez)")
        word = []
        word.extend(get_word())
        text="".join(word)
        if dumb_mode == True:
            gradual_typing("hey dumy, maybe the answer is:"f"{text}")
        guessing_ez_mode(word)
        finished = False

    if choice == 2:                 #hard mode
        print("game starts!(hard)")
        word = []
        word.extend(get_word())
        guessing_hard_mode(word)
        finished = False

    if choice == 3:
        print_instructions()

    if choice == 4:                  #quit
        print("Make sure if you want to quit \n1.Quit\n2.return the manu")
        choice = input()
        if choice == "1":
            finished = False