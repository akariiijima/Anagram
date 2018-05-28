#辞書を読み込み
dictionary = []
with open("dictionary.txt", "r") as f:
    for line in f:
        dictionary.append(line.split())


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
while True:
    key = ord(getch())
    if key == 3:#C-x-c
        break
    else:
        input_char += chr(key)
        print('>>> ' + input_char)

        #入力された文字をsortする
        for i in range(len(input_char)):
            sort_char = ""
            for c in sorted(input_char, key = str):
                sort_char += c
        
        #2分木探索
        low = 0
        high = len(dictionary) - 1
        
        while (low <= high):
            middle = (low + high) // 2
            #print(low)
            #print(high)
            #print("\n")
            if sort_char == dictionary[middle][1]:
                print("match : " + dictionary[middle][0])
                break
            elif sort_char < dictionary[middle][1]:
                #print("row")
                high = middle -1
            elif sort_char > dictionary[middle][1]:
                #print("high")
                low = middle + 1

                     
