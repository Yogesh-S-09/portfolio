from PyDictionary import PyDictionary

dictionary=PyDictionary()
def mean(word):
    x = dictionary.meaning(word)
    for i in x:
        for j in range(len(x[i])):
            x[i][j]=x[i][j].translate( { ord('('):None , ord('`'):ord('"') ,ord("'"):ord('"') } )
    return x

print(mean('good'))