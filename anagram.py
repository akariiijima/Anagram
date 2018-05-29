#辞書を読み込み
f = open("dictionary.txt")
data = f.read()
f.close()
dictionary_data = data.split("\n")


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
            return sys.stdin.read(1)#入力したデータを受け取って表示
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)#fdモードをoldから取得

#main
input_char = ""
match = ""
long_char = ""
while True:
    print(match)
    print("BEST : " + long_char)
    
    key = ord(getch())
    input_char += chr(key)
    print("\n>>> " + input_char + "\n")
    if key == 3:#C-x-c
        break
    else:
        match = ""
        for dictionary in dictionary_data:
            each_dictionary = list(dictionary)
            char = input_char
            count = 0
            for match_char in each_dictionary:
                if char.find(match_char) != -1:
                    char = char[:(char.find(match_char))]+char[(char.find(match_char))+1:]
                else:
                    count = 1
                    break
            if count != 1:
                match += dictionary + " "
                if len(long_char) < len(dictionary):
                    long_char = dictionary
            
            

        
                     
