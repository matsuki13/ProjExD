from datetime import datetime
import random

NUM_OF_TRILS = 5 #試行回数
NUM_OF_ALL_CHARS = 10 #最大文字数
NUM_OF_ABS_CHARS = 2 #欠損文字数

def main():
    st = datetime.datetime.now()
    for _ in range(NUM_OF_TRILS):
        seikai = shutsudai()
        f = kaitou(seikai)
        if f == 1:
            break
    ed = datetime.datetime.now() # 時間計測終了
    print(f"所要時間：{(ed-st).seconds}秒かかりました")

def shutsudai():
    #全アルファベットの文字リスト
    alphabets = [chr(c+65) for c in range(26)]
    #全アルファベットからNUM_OF_ALL_CHARS個の文字をランダムに選ぶ：対象文字
    all_char_lst = random.sample(alphabets,NUM_OF_ALL_CHARS)
    print(f"対象文字：{all_char_lst}")

    abs_char_lst = random.sample(XXXX,YYYY)
    print(f"欠損文字:{abs_char_lst}")

    pre_char_lst = [c for c in all_char_lst if c not in abs_char_lst]
    print(f"表示文字:{pre_char_lst}")

    return abs_char_lst

def kaitou(seikai):
    num = int(input("欠損文字はいくつあるでしょうか？"))
    if num != NUM_OF_ABS_CHARS:
        print("不正解です")
        return 0
    else:
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        for i in range(NUM_OF_ABS_CHARS)
        c = input(f"{i+1}つ目の文字を入力してください：")
        if c not in seikai:
            print("不正解！またチャレンジしてね")
            print("-"*50)
            return 0
        seikai.remove(c)
    print("正解です。ゲームを終了します")
    return 1


if __name__ == "__main__": 
    main()
