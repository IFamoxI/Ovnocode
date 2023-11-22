vivod = ""
quan = int(input())
crib = {}
for i in range(quan):
    words = input().split()
    word = words[0]
    desc = words[1:len(words) + 1]
    crib[word] = desc
for i in range(int(input())):
    word = input()
    if word not in crib:
        vivod += "Нет в словаре"
    else:
        vivod += word
print(vivod, sep = "\n")
