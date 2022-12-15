with open("words/rijeci_brojevi.txt", "r", encoding='utf-8') as f:
    lines = f.read().split("', '")
g = open("words/rijeci_brojevi_sortirani.txt", "w")
numbers=[]
word=""
for i in lines:
    print(int(i))
    numbers.append(int(i))

print("not sorted "+str(numbers))
numbers.sort()
print("sorted "+str(numbers))
#to file txt
for k in range(len(numbers)):
    g.write(str(numbers[k])+"', '")