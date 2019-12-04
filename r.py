import pronouncing
import re
import sys
from nltk.corpus import wordnet
import nltk
import re
from nltk.stem import WordNetLemmatizer



def syn(word):
    print("Synonyms for " + word+" are :\n")
    synonyms = [] 
     
  
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name())     
    print(set(synonyms)) 
   



def ant(word):
    print("Antonyms for " + word+" are :\n")
    antonyms = []
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas():  
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name())
    print(set(antonyms)) 

def rhy():
    print("Enter your word")
    word = input()
    fb = pronouncing.rhymes(word)
    print(fb)
    



def cross(word,leng,cha,posi):
    #do without position
    rr=[]
    syns=wordnet.synsets(word)
    for syn in syns:
        rr+=syn.lemma_names()

    #Since simple synonym set is not enough, lets add more related words 
    #finding all related words among which rhyming words is to be found

    hr=[]
    syns=wordnet.synsets(word)
    for syn in syns:
        sn=syn.hypernyms()#broader category:colour is a hypernym of red.
        an=syn.hyponyms() #narrower category - red : color
        dn=syn.member_holonyms()#Body is a holonym of arm, leg and heart
        for s in sn:
            hr+=s.lemma_names()
        for a in an:
            hr+=a.lemma_names()
        for d in dn:
            hr+=d.lemma_names()
            
    #now even "loaf" gets included when "food" is given as input

    #making the list richer by adding synonyms of the words which are in hr.
    fn=[]
    for h in hr:
        ss=wordnet.synsets(h)
        for s in ss:
            fn+=s.lemma_names()

    fn = list(dict.fromkeys(fn)) # removing duplicates

    if(posi==-1):
        for l in fn:
            if len(l) == leng:
                print(l)
        print("Need narrower results?\nEnter 1 if you have fixed characters,else 0." )
        more = int(input())
        if(more==1):
            print("Enter the character and its position that is fixed\nCharacter:")
            cha = input()
            print("Enter its position(starting from 0)")
            posi = int(input())
            cross(word,leng,cha,posi)



    else:
        print("Narrower results:")
        for l in fn:
            if len(l) == leng and l[posi]==cha:
                print(l)



    
        
    

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
            hr+=d.lemma_names()
            
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




    mean=int(input("If you wish to see the meaning and other details \nof the resulting words enter 1 else 0"))
    if(mean=="0"):
        sys.exit()
    l = WordNetLemmatizer()
    for det in fo :
        print("The details of the word \""+ det +"\" are as follows:\n")
        ld=l.lemmatize(det)
        lw=wordnet.synsets(det)
        print("Main Word - " + ld +"\n" )
        print("Meaning - "+ lw[0].definition() +"\n")
    
def find(ch) :

    if ch==1:
        print("Welcome to Synzone ")
        print("Enter your word:")
        wordin = input()
        syn(wordin)
    elif ch==2:
        print("Welcome to Antizone")
        print("Enter your word:")
        wordin = input()
        ant(wordin)
    elif ch==3:
        print("Welcome to Rhymzone")
        print("Do you want your rhyming word to be of some particular meaning?\nPress 0 for NO and 1 for YES")
        cho = int(input())
        if cho==0:
            rhy()
        else:
            rhymerdic()
    elif ch==4:
        print("Welcome to CrosswordZone")
        print("Enter a single word that is nearest to the description")
        wordin = input()
        print("Enter the length of the word")
        leng=int(input())
        cha=''
        posi=-1
        cross(wordin,leng,cha,posi)

def mean(word):
    syns = wordnet.synsets(word) 
    # # An example of a synset: 
    # lemmatizer = WordNetLemmatizer() 
    
    # print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))
    # Just the word: 
    print("Your word : "+ word)
    for l in syns:
        print("Meaning : "+l.definition())
        print("Example : ",end='')
        for e in l.examples() :
            print(e,end="\n          ")
        print("")

#------------------------------------------------------Start of main program-----------------------------------------------------

print("Enter your Choice:\n1.Find your word --- rhyming to, meaning similar to, meaning opposite to , Ace your crossword game\n"+
"2.Understand your word --- Examples, root, meaning\n"+
"3.Know new things --- other synset props like hypernym, hyponym etc --- Their definition and implementation (use documents)")
btn1 = int(input())
if btn1==1:
    print("Welcome to the Findhub where you can find words !!!")
    print("Choose your option:\n1.Find a word with similar meaning\n2.Find a word with opposite meaning\n3.Find a word rhyming with your word\n4.Find a word for your crossword puzzle")
    co = int(input())
    find(co)
elif btn1==2:
    print("Welcome to the Knowledge Hub, where you can understand your word !!!")
    print("Enter your word:")
    word=input()
    #print("Choose what you wish to know:\n1.Meaning\n2.Root\n3.Examples")
    # co = int(input())
    mean(word)



    
