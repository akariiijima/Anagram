#辞書リスト番号
#0:辞書の文字、1:ソートした文字、2,3,…:その文字に含まれる文字

#辞書を読み込み
dictionary = []
with open("dictionary.txt", "r") as f:
    for line in f:
        dictionary.append(line.split())

#1:sortした文字をsort
if len(dictionary[0]) == 1:
    for i in range(len(dictionary)):
        char = ""
        for c in sorted(dictionary[i][0], key = str):
            char += c
        dictionary[i].append(char)
sort_dictionary = sorted(dictionary, key=lambda x: x[1])


#辞書を書き込み
f = open('dictionary.txt', 'w')
for i in range(len(sort_dictionary)):
    for j in range(len(sort_dictionary[i])):
        if j == len(sort_dictionary[i])-1:
            f.write(str(sort_dictionary[i][j]))
        else:
            f.write(str(sort_dictionary[i][j]) + " ")
    if i != len(sort_dictionary)-1:
        f.write("\n")    
f.close()
