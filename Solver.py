from datetime import datetime
from itertools import permutations
from collections import OrderedDict 

def removeAlphaDup(wordlist): #Remove alphabet duplicates from words in wordlist e.g. hello become helo
    newwordlist = []
    for word in wordlist:
        newwordlist.append(''.join(OrderedDict.fromkeys(word))) #After removing duplicate using OrderDict, append to newwordlist
    return newwordlist
    #print("test")

def switchKey(word): #Add keyword to front of alpha, without duplicates
    #alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #alpha='abcdefghijklmnopqrstuvwxyz'
    key='abcdefghijklmnopqrstuvwxyz'
    newkey=word+key
    newkey=''.join(OrderedDict.fromkeys(newkey))
    return newkey
    
    #print((permutations(key))

def wordFinder(wordlist,phrase): #Find words from the wordlist in the phrase
    #list = ['this','is','a','test','not']
    sublist = []
    
    for word in wordlist:
        if(phrase.find(word)>0): #Check if there's a word from the wordlist, if found returns word from list. 
            sublist.append(word)
            #print(word)
    return sublist
    #print(sublist)
    #a = phrase.find('thee')
    #print phrase

def decrypt(phrase):    
    wordlist = open('English3000.txt','r').read().split('\n') #Read from the word list
    outputname = "Output" + str(datetime.now().strftime('-%Y%m%d-%H%M')) + ".txt" #Name format of output file
    f = open(outputname,'a') #Write to file in append mode
    newwordlist = removeAlphaDup(wordlist)
    alpha='abcdefghijklmnopqrstuvwxyz'
    for word in newwordlist: #Iterate through newwordlist 
        sublist = []
        newphrase = ''
        newkey = switchKey(word)
        for char in phrase:
            pos = alpha.find(char)
            newphrase=newphrase+newkey[pos]
        sublist = wordFinder(wordlist,newphrase)
        if sublist: #If sublist is not empty, write to file
            f.write(str(sublist)+'\n')
    f.close()
        #print(newphrase)
        #print newkey
    #print(newwordlist)
    #wordFinder(wordlist,phrase)
    #switchKey(phrase)
    
#print(len(list(permutations(['a','b','c','d','e','f','g','h','i','j','k','l']))))
#phrase = 'reluezntuotheepdesnygudotistl?lk'
phrase = 'reluezntuotheepdesnygudotistllk' #This is the string you want to decipher
decrypt(phrase)


