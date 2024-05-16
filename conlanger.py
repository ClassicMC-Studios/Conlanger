import random

# USER COSTOMIZE SETTINGS
clusters = True
# Set letter glyphs
con = ['b','v','s','sh','k','kh','n','r']
vow = ['a','i','o']
clus = ['shk','sr','shr','br']
diph = ['ai','eo','uo']
wordLen = random.randrange(3,10)
# END CUSTOMIZATION

# Pure random letter generator FIXED tells it which letter group 
def genLetter(fixed):
    if fixed == 0:
        return [con[random.randrange(1,len(con))],'C']
    if fixed == 1:
        return [vow[random.randrange(1,len(vow))],'V']
    if fixed == 2:
        return [clus[random.randrange(1,len(clus))],'CC']
    if fixed == 3:
        return [diph[random.randrange(1,len(diph))],'VV']
# The word generator itself cvc is an array with 
def genWord():
    word = []
    cvc = []
    # Clusters asks if it should include for example ST or SL
    if clusters == False:
        for i in range(5):
            if i == 0:
                tempLet = genLetter(random.randrange(0,2))
                word.append(tempLet[0])
                cvc.append(tempLet[1])
            else:
                if cvc[i-1] == "C":
                    tempLet = genLetter(1)
                    word.append(tempLet[0])
                    cvc.append(tempLet[1])
                else:
                    tempLet = genLetter(0)
                    word.append(tempLet[0])
                    cvc.append(tempLet[1])
    else:
        for i in range(wordLen):
            if i == 0:
                tempLet = genLetter(random.randrange(0,3))
                word.append(tempLet[0])
                cvc.append(tempLet[1])
            else:
                if cvc[i-1] == "C" or cvc[i-1] == "CC":
                    fix = random.randrange(1,3)
                    if fix == 2:
                        fix+=1
                    tempLet = genLetter(fix)
                    word.append(tempLet[0])
                    cvc.append(tempLet[1])
                else:
                    fix = random.randrange(0,2)
                    if fix == 1:
                        fix+=1
                    tempLet = genLetter(fix)
                    word.append(tempLet[0])
                    cvc.append(tempLet[1])
    print("".join(word))
    print("".join(cvc))
genWord()
print(genLetter(3))
