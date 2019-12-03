import pronouncing
import re
import sys
from nltk.corpus import wordnet
import nltk
import re
from nltk.stem import WordNetLemmatizer

print("Enter your Choice:\n1.Find your word --- rhyming to, meaning similar to, meaning opposite to , Ace your crossword game\n"+
"2.Understand your word --- Examples, root, meaning\n"+
"3.Know new things --- other synset props like hypernym, hyponym etc --- Their definition and implementation (use documents)")
btn1 = input()

switch(btn1){
    case 1:
        print("Choose your option:\n1.Find a word with similar meaning\n2.Find a word with opposite meaning\n3.Find a word rhyming with your word\n4.Find a word for your crossword puzzle")
        ch = input()
        find(ch)
    case 2:


}

def find(ch) :
    switch(ch){
        case 1:
            print("Enter your word:")
            wordin = input()
            syn(wordin)
        case 2:
            print("Enter your word:")
            wordin = input()
            ant(wordin)
        case 3:
            print("Do you want your rhyming word to be of some particular meaning?\nPress 0 for NO and 1 for YES")
            cho = input()
            if(cho == 0)
                rhy(wordin)
            else
                rhymerdic()
        case 4:
            print("Enter a single word that is nearest to the description")
            wordin = input()
            print("Enter the length of the word")
            leng=input()
            cha=''
            posi=-1
            cross(wordin,leng,cha,posi)
    }

def syn(word):

def ant(word):

def rhy(word):

def cross(word,leng,cha,posi):
    if(posi=-1):
        #do without position 


    else:
        


    print("Need narrower results?\nEnter 1 if you have fixed characters,else 0." )
    more = input()
    if(more==1):
        print("Enter the character and its position that is fixed\nCharacter:")
        cha = input()
        print("Enter its position(starting from 0)")
        posi = input()
        cross(word,leng,cha,posi)
        
    

def rhymerdic() :
    # a proper module separately made for finding rhyming words; also based on cmudict.
    print("Enter the word whose rhyming word you wish to find : ")
    iword = input()

    fb = pronouncing.rhymes(iword)
    #Simple synonym set
    rr=[]
    print("Enter the word whose meaning should resemble with the rhyming word \n(enter \"*\" if you wish to see all rhyming words) : ")
    mword = input()
    if(mword=="*"):
        print(fb)
        sys.exit()
    syns=wordnet.synsets(mword)
    for syn in syns:
        rr+=syn.lemma_names()

    #Since simple synonym set is not enough, lets add more related words 
    #finding all related words among which rhyming words is to be found

    hr=[]
    syns=wordnet.synsets(mword)
    for syn in syns:
        sn=syn.hypernyms()#broader category:colour is a hypernym of red.
        an=syn.hyponyms() #narrower category - red : color
        dn=syn.member_holonyms()#Body is a holonym of arm, leg and heart
        for s in sn:
            hr+=s.lemma_names()
        for a in an:
            hr+=a.lemma_names()
        for d in dn:
            hr+=s.lemma_names()
            
    #now even "loaf" gets included when "food" is given as input

    #making the list richer by adding synonyms of the words which are in hr.
    fn=[]
    for h in hr:
        ss=wordnet.synsets(h)
        for s in ss:
            fn+=s.lemma_names()

    fn = list(dict.fromkeys(fn)) # removing duplicates

        
    #now selecting only the words that are common in both

    fo = list(set(fb)&set(fn))
    for chk in fb:
        for chk1 in fn:
            my_regex = r".*" + re.escape(chk) + r"$"
            found =(re.search(my_regex ,chk1, re.M|re.I))
            if found:
                fo.append(found.group())
    fo=list(set(fo))

    print(fo)




    mean=input("If you wish to see the meaning and other details \nof the resulting words enter 1 else 0")
    if(mean=="0"):
        sys.exit()
    l = WordNetLemmatizer()
    for det in fo :
        print("The details of the word \""+ det +"\" are as follows:\n")
        ld=l.lemmatize(det)
        lw=wordnet.synsets(det)
        print("Main Word - " + ld +"\n" )
        print("Meaning - "+ lw[0].definition() +"\n")
    

    
    
