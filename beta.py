import random

# USER COSTOMIZE SETTINGS
clusters = True
endCons = True
diphs = True
# Set letter glyphs
con = ['d', 'h', 'j', 'k', 'l', 'm', 'n', 'ng', 'p', 'r', 's', 't','v']
vow = ['a', 'o', 'u', 'e', 'i','ä', 'ö','y']
clus = ['','']
diph = ['ei','äi','yi','öi','ui','oi','ai','öy','äy']
wordLen = random.randrange(3,6)
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
    if clusters == False or diphs == False:
        for i in range(wordLen):
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
    if cvc[len(cvc)-1] == "C" and endCons == False:
        word.append(genLetter(1)[0])
    print("### Weston's Conlanger ###")
    print("Word:"+("".join(word)).capitalize())
    # print("Structure:"+"".join(cvc))
genWord()

