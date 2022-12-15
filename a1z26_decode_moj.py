with open("words/rijeci_brojevi_sortirani.txt", "r", encoding='utf-8') as f:
    lines = f.read().split("', '")
abc = ['y', 'a', 'b', 'c', 'č', 'ć', 'd', 'dž', 'đ', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']
word=""
for i in lines:
    for j in range(0, len(i)-1, 2):
        if(i[j]=='5'):
            word+=abc[int(i[j+1])]
        else:
            word+=abc[int(i[j]+i[j+1])]
    print(word)
    word=""