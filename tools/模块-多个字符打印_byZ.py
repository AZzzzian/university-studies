import string
def gradual1_print(text):
    lowercase_alphabet = list(string.ascii_lowercase)
    Punctation_mark = list(string.punctuation)
    Full_Characters = lowercase_alphabet + Punctation_mark
    i = x = 0
    Words = list(text)  # 你需要print的words
    length = len(Words)
    num=[]
    while i<length:
        num.append(" ")
        i=i+1
    sWords = [s.lower() for s in Words]
    n1=0
    n2=1
    n3=2
    n4=3
    a=b=c=d=0
    x=3
    while num!=Words:
        while x<length:
            num[n1]=Full_Characters[a]
            num[n2]=Full_Characters[b]
            num[n3]=Full_Characters[c]
            num[n4]=Full_Characters[d]
            a=a+1
            b=b+1
            c=c+1
            d=d+1
            if sWords[n1]==" ":
                num[n1] = Words[n1]
                x = x + 1
                n1 = x
            if num[n1]==sWords[n1]:
                num[n1]=Words[n1]
                x=x+1
                n1=x
                a=0
            if sWords[n2]==" ":
                num[n2] = Words[n2]
                x = x + 1
                n2 = x
            if num[n2] == sWords[n2]:
                num[n2]=Words[n2]
                x=x+1
                n2=x
                b=0
            if sWords[n3] == " ":
                num[n3] = Words[n3]
                x = x + 1
                n3 = x
            if num[n3]==sWords[n3]:
                num[n3]=Words[n3]
                x=x+1
                n3=x
                c=0
            if sWords[n4] == " ":
                num[n4] = Words[n4]
                x = x + 1
                n4 = x
            if num[n4] == sWords[n4]:
                num[n4]=Words[n4]
                x=x+1
                n4=x
                d=0
            print_string = ''.join(num)
            print(print_string, flush=True)
        if n1!=length or n2!=length or n3!=length or n4!=length:
            num=Words
    print_string = ''.join(num)
    print(print_string, flush=True)




gradual1_print("Welcome to Python Programming")