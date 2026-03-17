import string
import time
def gradual1_print(text,speed = 0.05):
    lowercase_alphabet = list(string.ascii_lowercase)
    punctation_mark = list(string.punctuation)
    full_Characters = lowercase_alphabet + punctation_mark
    i = x = 0
    Words = list(text)  # 你需要print的words
    length = len(Words)
    while x < length:

        while i < 57:
            printing_number = full_Characters[i]  # 快速通过的字母+符号
            b = Words[:x]  # 需要的字母前x-1位
            c = Words[x]  # 需要的字母第x位
            d = [s.lower() for s in c]  # 全部小写再根据原本大写
            e = ','.join(map(str, d))
            if ' ' in c:
                break
            else:
                if printing_number == e:
                    time.sleep(speed)  # 覆盖一次小写
                    string_correct= ''.join(b)
                    print(string_correct+c,flush=True)
                    break
                else:
                    string_correct= ''.join(b)
                    time.sleep(speed)
                    print(string_correct + printing_number,flush=True)
            i = i + 1
        i = 0
        x = x + 1
gradual1_print("Welcome to use, original by Z")
