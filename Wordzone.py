from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
import pronouncing
import re
import sys
from nltk.corpus import wordnet
import nltk
import re
from nltk.stem import WordNetLemmatizer
import pyttsx3 
  
# initialisation 
engine = pyttsx3.init()


class MyGrid(FloatLayout):

    def syn(self,word):

        
        synonyms = [] 
        
    
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas(): 
                synonyms.append(l.name())
        if(len(synonyms)>0):     
            print("Synonyms for " + word+" are :\n")
            print(set(synonyms))
        else:
            print("No synonyms were found, try entering a different word.");
    



    def ant(self,word):
        
        antonyms = []
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas():  
                if l.antonyms(): 
                    antonyms.append(l.antonyms()[0].name())
        if(len(antonyms)>0):     
            print("antonyms for " + word+" are :\n")
            print(set(antonyms))
        else:
            print("No antonyms were found, try entering a different word."); 

    def rhy(self):
        print("Enter your word")
        word = input()
        fb = pronouncing.rhymes(word)
        if(len(fb)>0):
            print(fb)
        else:
            print("No rhyming words were found, try entering a different word."); 
        



    def cross(self,word,leng,cha,posi):
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
        crosscount = 0
        if(posi==-1):
            for l in fn:
                if len(l) == leng:
                    print(l)
                    crosscount+=1
            if(crosscount>0):
                print("Need narrower results?\nEnter 1 if you have fixed characters,else 0." )
                more = int(input())
                if(more==1):
                    print("Enter the character and its position that is fixed\nCharacter:")
                    cha = input()
                    print("Enter its position(starting from 0)")
                    posi = int(input())
                    self.cross(word,leng,cha,posi)
            else:
                print("No words were found, try entering a different word."); 



        else:
            narrowcount=0;
            
            for l in fn:
                if len(l) == leng and l[posi]==cha:
                    if(narrowcount==0):
                        print("Narrower results:")
                    narrowcount+=1
                    print(l)
                if(narrowcount==0):
                    print("No words were found, try entering a different word."); 



        
            
        

    def rhymerdic(self) :
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
        
    def find(self,ch) :

        if ch==1:
            print("Welcome to Synzone ")
            print("Enter your word:")
            wordin = input()
            self.syn(wordin)
        elif ch==2:
            print("Welcome to Antizone")
            print("Enter your word:")
            wordin = input()
            self.ant(wordin)
        elif ch==3:
            print("Welcome to Rhymzone")
            print("Do you want your rhyming word to be of some particular meaning?\nPress 0 for NO and 1 for YES")
            cho = int(input())
            if cho==0:
                self.rhy()
            else:
                self.rhymerdic()
        elif ch==4:
            print("Welcome to CrosswordZone")
            print("Enter a single word that is nearest to the description")
            wordin = input()
            print("Enter the length of the word")
            leng=int(input())
            cha=''
            posi=-1
            self.cross(wordin,leng,cha,posi)

    def mean(self,word):
        syns = wordnet.synsets(word) 
        # # An example of a synset: 
        # lemmatizer = WordNetLemmatizer() 
        
        # print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))
        # Just the word: 
        # print("Your word : "+ word)

        for l in syns:
            print("Meaning : "+l.definition())
            print("Example : ",end='')
            for e in l.examples() :
                print(e,end="\n          ")
            print("")
        if(len(syns)==0):
            print("No words were found, try entering a different word.")



    def findZone(self):
        print("Welcome to the Finding Zone, where you can find words !!!")
        # engine.say("Welcome to the Finding Zone, where you can find words")
        # engine.runAndWait()
        print("Choose your option:")
        # engine.say("Choose your Option ")
        # engine.runAndWait()
        print("1.Find a word with similar meaning")
        # engine.say("Press 1 to Find a word with a similar meaning")
        # engine.runAndWait()
        print("2.Find a word with opposite meaning")
        # engine.say("Press 2 to Find a word with opposite meaning")
        # engine.runAndWait()
        print("3.Find a word rhyming with your word")
        # engine.say("Press 3 to Find a word rhyming with your word")
        # engine.runAndWait()
        print("4.Find a word for your crossword puzzle")
        # engine.say("and, press 4 to Find a word for your crossword puzzle")
        # engine.runAndWait()
        co = int(input())
        self.find(co)

    def understandZone(self):
        print("Welcome to the Understanding Zone, where you can understand your word !!!")
        # engine.say("Welcome to the Understanding Zone,a place where you can understand your word !!!")
        # engine.runAndWait()
        print("Enter your word:")
        # engine.say("Enter your word")
        # engine.runAndWait()
        word=input()
        #print("Choose what you wish to know:\n1.Meaning\n2.Root\n3.Examples")
        # co = int(input())
        self.mean(word)

    def knowledgeZone(self):
        print("Welcome to the Knowledge Zone, here you can learn new words related to your word.")
        # engine.say("Welcome to the Knowledge Zone, here you can learn new words related to your word.")
        # engine.runAndWait()
        print("Enter your word:")
        # engine.say("Enter your word")
        # engine.runAndWait()

        word = input()
        sn=""
        an=""
        dn=""
        syns=wordnet.synsets(word)
        for syn in syns:
            
            s=syn.hypernyms()#broader category:colour is a hypernym of red.
            for q in s:
                sn+=q.lemma_names()[0]+"\n"
            a=syn.hyponyms() #narrower category - red : color'
            for q in a:
                an+=q.lemma_names()[0]+"\n"
            d=syn.member_holonyms()#Body is a holonym of arm, leg and heart
            for q in d:
                dn+=q.lemma_names()[0]+"\n"
        if(sn!=""):
            print("Hypernym (Words with broader meaning for eg, colour is a hypernym of red) :\n")
            print(sn+"\n")
        # engine.say("On your screen are the hypernyms of "+word+", Hypernyms are the Words with broader meaning for example, colour is a hypernym of red")
        # engine.runAndWait()
        if(an!=""):
            print("Hyponym (Words with narrower meaning for eg red is hyponym of colour):\n")
            print(an+"\n")
        # engine.say("On your screen are the hypornyms of "+word+", Hypernyms are the Words with narrower meaning for example, red is a hyponym of color")
        # engine.runAndWait()
        if(dn!=""):
            print("Holonym (thing that comprises of other things for eg body is holonym of arm ):\n")
            print(dn+"\n")
        if(an=="" and sn=="" and dn=="" ):
            print("No related word was found");
        # engine.say("On your screen are the holonyms of "+word+", Holonym is a thing that comprises of other things for eg body is holonym of arm")
        # engine.runAndWait()
            # for s in sn:
            #     hr+=s.lemma_names()
            # for a in an:
            #     hr+=a.lemma_names()
            # for d in dn:
            #     hr+=d.lemma_names()





#------------------------------------------------------Start of main program-----------------------------------------------------

# #rate = engine.getProperty('rate')
# #engine.setProperty('rate', rate+10)
# print("Enter your Choice:\n1.Find your word which is rhyming to, meaning similar to, meaning opposite to or to Ace your crossword game")
# # engine.say("Enter your Choice:")
# # engine.say("press 1, to Find your word which is rhyming to, meaning similar to, meaning opposite to or to Ace your crossword game")
# # engine.runAndWait()
# print("2.Understand your word, that is to get Examples, root and meaning of your word")
# # engine.say("press 2, to Understand your word, that is to get Examples, root and meaning of your word")
# # engine.runAndWait()
# print("3.Know new words related to your word, like hypernym, hyponym etc")
# # engine.say("press 3, to Know new words related to your word, like hypernym, hyponym etc")
# # engine.runAndWait() 

    



    


    # name = ObjectProperty(None)
    # email = ObjectProperty(None)

    # def btn(self):
    #     print(self.name.text, self.email.text)
    #     self.name.text =""
    #     self.name.text=""


class WordApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    WordApp().run()