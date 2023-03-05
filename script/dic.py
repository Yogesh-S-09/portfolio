from PyDictionary import PyDictionary

dictionary=PyDictionary()
def mean(word):
    x = dictionary.meaning(word)
    if(x==None): return "No Internet"
    for i in x:
        for j in range(len(x[i])):
            x[i][j]=x[i][j].translate( { ord('('):None , ord('`'):ord('"') ,ord("'"):ord('"') } )
    #x={'Noun': ['trying something to find out about it', 'any standardized procedure for measuring sensitivity or memory or intelligence or aptitude or personality etc', 'a set of questions or exercises evaluating skill or knowledge', 'the act of undergoing testing', 'the act of testing something', 'a hard outer covering as of some amoebas and sea urchins'], 'Verb': ['put to the test, as for its quality, or give experimental use to', 'test or examine for the presence of disease or infection', "examine someone's knowledge of something", 'show a certain characteristic when tested', 'achieve a certain score or rating on a test', 'determine the presence or properties of (a substance', 'undergo a test']}
    return x

print(mean('good'))