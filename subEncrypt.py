# substitution cypher encryption by flipping the alphabet

alphabet1=[]
alpha1 = 'a'
for i in range(0, 26): 
    alphabet1.append(alpha1) 
    alpha1 = chr(ord(alpha1) + 1)  

alphabet2=[]
alpha2 = 'A'
for i in range(0, 26): 
    alphabet2.append(alpha2) 
    alpha2 = chr(ord(alpha2) + 1)  

def reverseLetter(letter):
    if (letter.islower()):
        return alphabet1[25 - alphabet1.index(letter)]
    elif(letter.isupper()):
        return alphabet2[25 - alphabet2.index(letter)]
    elif(letter==" "):
        return " "
    elif(letter.isdigit()):
        return ""+ str(abs(int(letter)-9))
    else:
        return letter

# sentence = input("Type a sentence: ")

def encrypted(message):
    letters=[]
    out = ""
    for l in message:
        letters.append(reverseLetter(l))
    for z in letters:
        out = out+z
    return out

# print(encrypted(sentence))

