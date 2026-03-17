import string
import time
def gradual2_print(text,speed=0.02):
    lowercase_alphabet = list(string.ascii_lowercase)
    punctation_mark = list(string.punctuation)
    full_Characters = lowercase_alphabet + punctation_mark
    i = x = 0
    Words = list(text)  # 你需要print的words
    length = len(Words)
    while x < length:
        if Words[x] not in full_Characters:
            print(Words[x],end="")
            time.sleep(speed*50)
        else:
            while i < 57:
                printing_number = full_Characters[i]  # 快速通过的字母+符号
                b = Words[:x]  # 需要的字母前x-1位
                c = Words[x]  # 需要的字母第x位
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
    print()                                     #print自动空行如果你需要的话
gradual2_print("26367848welcome to use this program")

