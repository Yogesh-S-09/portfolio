from PyDictionary import PyDictionary

dictionary=PyDictionary()
def mean(word):
    return dictionary.meaning(word)

x=mean(input("Enter a world:"))
for i in x:
    print(i+'=',x[i])

print(x)
