import random
allowConsonantClusters = 3
canEndInVowel = False
subjectObjectOrWhere = "SOV"
possibleConsonants = ['q','w','e','r','t','y','p','ts','d','f','v','g','h','j','kh','l','r','s','z','b','n','m']
possibleVowels = ['a','e','i','o','u']
# possibleVowels = possibleConsonants
def decide(i,wordBD):
    willStartWith = random.randrange(0,2)
    if len(wordBD)>1:
        if wordBD[0] == "c":
            willStartWith = 1
        else:
            willStartWith = random.randrange(0,2)
    if willStartWith == 0:
        return [possibleConsonants[random.randrange(1,len(possibleConsonants))],'c']
    if willStartWith == 1:
        return [possibleVowels[random.randrange(1,len(possibleVowels))],'v']
def generateWord():
    word = []
    wordBD = []
    for i in range(random.randrange(3, 10)):
        final = decide(i,wordBD)
        word.append(final[0])
        wordBD.append(final[1])
    print("".join(word))
    print("".join(wordBD))
generateWord()
