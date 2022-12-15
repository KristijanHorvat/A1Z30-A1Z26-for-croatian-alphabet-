with open("words/rijeci_apo_krace.txt", "r", encoding='utf-8') as f:
    lines = f.read().split("','")
g = open("words/rijeci_brojevi.txt", "w")
abc = ['y', 'a', 'b', 'c', 'č', 'ć', 'd', 'dž', 'đ', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj', 'o', 'p', 'r', 's', 'š', 't', 'u', 'v', 'z', 'ž']

number_word=""

for word in lines:
    print(word)
    for letter in word:
        #print(letter, end=" ")
        for i in range(len(abc)):
            if(letter)==abc[i]:
                if(i<10):
                    number_word+='5'+str(i)
                    print('5'+str(i))
                else:
                    number_word+=str(i)
                    print(i)

    g.write(number_word+"', '")
    print(number_word)
    
    number_word=""