#辞書を読み込み
dictionary_data = []
with open("dictionary.txt", "r") as f:
    for line in f:
        dictionary_data.append(line.split())


#1文字enter無し入力getch()
#(参照)https://torina.top/detail/428/
try:
    from msvcrt import getch
except ImportError:
    def getch():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()#標準入力のファイルディスクプリタを取得
        old = termios.tcgetattr(fd)#fdの端末属性をゲットする
        try:
            tty.setraw(fd)#fdのモードをrawモードに切替
            return sys.stdin.read(16)#入力したデータを受け取って表示
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)#fdモードをoldから取得

            
#main
input_char = ""#(後にsortされる)入力された文字
input_char_origin = ""#入力された文字をそのまま連ねたもの
match = ""#入力された文字に含まれる単語全て
long_char = ""#BESTな単語
char_point = 0#dictionaryの得点
long_char_point = 0#BESTな単語の得点

while True:
    print(match)
    print("BEST : " + long_char)
    
    key = ord(getch())
    input_char += chr(key)
    input_char_origin += chr(key)
    print("\n>>> " + input_char_origin + "\n")

    #input_charをsortして戻す
    sort_char = ""
    for c in sorted(input_char, key = str):
        sort_char += c
    input_char = sort_char
        
    if key == 3:#C-x-cで終了
        break
    else:
        match = ""
        for dictionary in dictionary_data:
            each_dictionary = list(dictionary[1])
            char = input_char
            count = 0
            for match_char in each_dictionary:
                if char.find(match_char) != -1:
                    char = char[:(char.find(match_char))]+char[(char.find(match_char))+1:]
                else:#含まれる文字が無かったら
                    count = 1
                    break
            if count != 1:#matchした文字があったら
                match += dictionary[0] + " "
                char_point = len(dictionary[1])
                
                for d in dictionary[1]:#点数の高い文字の検索
                    if d == "c" or d == "f" or d == "h" or d == "l" or d == "m" or d == "p" or d == "v" or d == "w" or d == "y" or d == "q":
                        char_point += 1
                    elif d == "j" or d == "k" or d == "x" or d == "z":
                        char_point += 2
                if long_char_point < char_point:
                    long_char = dictionary[0]
                    long_char_point = char_point
                     

        
                     
