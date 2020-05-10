# # # # # # #kivy

# # # # # # from kivy.app import App
# # # # # # from kivy.uix.label import Label
# # # # # # from kivy.uix.gridlayout import GridLayout
# # # # # # from kivy.uix.textinput import TextInput
# # # # # # from kivy.uix.button import Button
# # # # # # from kivy.uix.widget import Widget
# # # # # # from kivy.properties import ObjectProperty



# # # # # # ## INHERITING GRID LAYOUT - ie. USING PYTHON COMMANDS FOR PUTTING IN ELEMENTS

# # # # # # # class MyGrid(GridLayout):
# # # # # # #     def __init__(self,**kwargs):
# # # # # # #         super(MyGrid,self).__init__(**kwargs)
# # # # # # #         self.cols=1
# # # # # # #         self.inside = GridLayout()
# # # # # # #         self.inside.cols =2

# # # # # # #         self.inside.add_widget(Label(text="First Name: "))
# # # # # # #         self.fname = TextInput(multiline=False)
# # # # # # #         self.inside.add_widget(self.fname)

# # # # # # #         self.inside.add_widget(Label(text="Last Name: "))
# # # # # # #         self.lname = TextInput(multiline=False)
# # # # # # #         self.inside.add_widget(self.lname)

# # # # # # #         self.inside.add_widget(Label(text="Email: "))
# # # # # # #         self.email = TextInput(multiline=False)
# # # # # # #         self.inside.add_widget(self.email)
# # # # # # #         self.add_widget(self.inside)
# # # # # # #         self.submit = Button(text = "Submit", font_size=24)
# # # # # # #         self.submit.bind(on_press=self.pressed)
# # # # # # #         self.add_widget(self.submit)
    
# # # # # # #     def pressed(self,instance):
# # # # # # #         print("Name:",self.fname.text,self.lname.text)
# # # # # # #         self.fname.text = ""
# # # # # # #         self.lname.text = ""
        



# # # # # # # class MyApp(App):
# # # # # # #     def build(self):
# # # # # # #         return MyGrid()

# # # # # # # if __name__ =="__main__":
# # # # # # #     MyApp().run()



# # # # # # # INHERITING WIDGET ie. USING KV FILE

# # # # # # class MyGrid(Widget):
# # # # # #     name = ObjectProperty(None)
# # # # # #     email = ObjectProperty(None)
    
# # # # # #     def btn(self):
# # # # # #         print(self.name.text, self.email.text)
# # # # # #         self.name.text =""
# # # # # #         self.email.text=""


# # # # # # class TryApp(App):
# # # # # #     def build(self):
# # # # # #         return MyGrid()


# # # # # # if __name__ == "__main__":
# # # # # #     TryApp().run()






# # # # # # #------------------------------------------------xxxxxxxxxxxxxxxx---------------------------------------------

# # # # # # # from nltk.corpus import wordnet
# # # # # # # # from nltk.stem import WordNetLemmatizer 
# # # # # # # word = "technologically"
# # # # # # # syns = wordnet.synsets(word) 
# # # # # # # # # An example of a synset: 
# # # # # # # # lemmatizer = WordNetLemmatizer() 
  
# # # # # # # # print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))


# # # # # # # # Just the word: 
# # # # # # # for l in syns:
# # # # # # #     print("Your word : "+ word)
# # # # # # #     print("Meaning : "+l.definition())
# # # # # # #     print("Example : ",end='')
# # # # # # #     for e in l.examples() :
# # # # # # #         print(e,end="\n          ")
# # # # # # # # print(syns[0].lemmas()[0].name()) 

# # # # # # # # # Definition of that first synset: 
# # # # # # # # print(syns[0].definition()) 

# # # # # # # # # Examples of the word in use in sentences: 
# # # # # # # # print(syns[0].examples())

# # # # # # #------------------------------------------------xxxxxxxxxxxxxxxx---------------------------------------------


# # # # # # # import speech_recognition as sr 
# # # # # # # r = sr.Recognizer()
# # # # # # # with sr.Microphone() as source:
# # # # # # # 	r.adjust_for_ambient_noise(source)
# # # # # # #     print("Speak into the microphone")
# # # # # # #     audio = r.listen(source)
# # # # # # # 	print("Thanks.")
# # # # # # # try :
# # # # # # #     print("Transcription: " +r.recognize_google(audio))
# # # # # # # except sr.UnknownValueError:
# # # # # # #     print("Audio unintelligible")
# # # # # # # except sr.RequestError as e:
# # # # # # #     print("Cannot obtain results;{0}".format(e))

# # # # # # ###############################text to speech###########################
# # # # # # # import pyttsx3 
  
# # # # # # # # initialisation 
# # # # # # # engine = pyttsx3.init() 
  
# # # # # # # # testing  
# # # # # # # a ="Adam"
# # # # # # # print("Welcome to the Finding Zone, where you can find words !!!")
# # # # # # # engine.say("Welcome"+a)
# # # # # # # engine.runAndWait()
# # # # # # # print("Choose your option:")

# # # # # # # engine.say("Choose your Option ")
# # # # # # # engine.runAndWait()
# # # # # # # print("1.Find a word with similar meaning")
# # # # # # # engine.say("Press 1 to Find a word with a similar meaning")
# # # # # # # engine.runAndWait()
# # # # # # # print("2.Find a word with opposite meaning")
# # # # # # # engine.say("Press 2 to Find a word with opposite meaning")
# # # # # # # engine.runAndWait()
# # # # # # # print("3.Find a word rhyming with your word")
# # # # # # # engine.say("Press 3 to Find a word rhyming with your word")
# # # # # # # engine.runAndWait()
# # # # # # # print("4.Find a word for your crossword puzzle")
# # # # # # # engine.say("press 4 to Find a word for your crossword puzzle")
# # # # # # # engine.runAndWait()

# # # # # # # import pyttsx3
# # # # # # # def onStart(name):
# # # # # # #    print ('starting', name)
# # # # # # # def onWord(name, location, length):
# # # # # # #    print ('word', name, location, length)
# # # # # # # def onEnd(name, completed):
# # # # # # #    print ('finishing', name, completed)
# # # # # # # engine = pyttsx3.init()
# # # # # # # engine.connect('started-utterance', onStart)
# # # # # # # engine.connect('started-word', onWord)
# # # # # # # engine.connect('finished-utterance', onEnd)
# # # # # # # engine.say('The quick brown fox jumped over the lazy dog.')
# # # # # # # engine.runAndWait()








# # # # # # # #All the important imports
# # # # # # # from kivy.app import App
# # # # # # # from kivy.uix.button import Button
# # # # # # # from kivy.lang import Builder
# # # # # # # from kivy.uix.screenmanager import ScreenManager, Screen

# # # # # # # #To get a purplish background in all the screens
# # # # # # # from kivy.core.window import Window
# # # # # # # Window.clearcolor = (0.259, 0.251, 0.447,0.9)

# # # # # # # #Main Window Screen declaration
# # # # # # # class MainWindow(Screen):
# # # # # # #     pass

# # # # # # # #Find Zone
# # # # # # # class FindWindow(Screen):
# # # # # # #     pass

# # # # # # # #Understand Zone
# # # # # # # class UnderstandWindow(Screen):
# # # # # # #     pass

# # # # # # # #Knowledge Zone
# # # # # # # class KnowWindow(Screen):
# # # # # # #     pass

# # # # # # # #Window Manager
# # # # # # # class WindowManager(ScreenManager):
# # # # # # #     pass

# # # # # # # #To load our kv file:
# # # # # # # kv = Builder.load_file("try.kv")

# # # # # # # #Our main App
# # # # # # # class tryApp(App):
# # # # # # #     def build(self):
# # # # # # #         return kv#MyGrid()

# # # # # # # #App initialising through main
# # # # # # # if __name__ == "__main__":
# # # # # # #     tryApp().run()





# # # # import re
# # # # def load_words():
# # # #     with open('words_alpha.txt') as word_file:
# # # #         # valid_words = set(word_file.read().split())
# # # #         valid_words = word_file.read().split()

# # # #     return valid_words


# # # # if __name__ == '__main__':
# # # #     english_words = load_words()

# # # #     w=input("Enter the word fragment :")
# # # #     p=input("Enter its position : /n(^ for starting and $ for end, blank for anywhere) ")
# # # #     l=input("Enter the length you desire :(blank if no specification)")
# # # #     st=w
# # # #     if(p=="^"):
# # # #         st="^"+w
# # # #         if(l.isdigit()):
# # # #             le=int(l)-len(w)
# # # #             if(le>0):
# # # #                 st = st+".{"+str(le)+"}"
# # # #             else:
# # # #                 print("Word Length can't be lesser that the fragment length.")
# # # #     elif (p=="$"):
# # # #         st=w+"$"
# # # #         if(l.isdigit()):
# # # #             le=int(l)-len(w)
# # # #             if(le>0):
# # # #                 st = ".{"+str(le)+"}"+st
# # # #             else:
# # # #                 print("Word Length can't be lesser that the fragment length.")
# # # #     elif(p==""):
# # # #         if(l.isdigit()):
# # # #             le=int(l)-len(w)
# # # #             if(le>0):
# # # #                 st = ".*"+w+".*"
# # # #             else:
# # # #                 print("Word Length can't be lesser that the fragment length.")

# # # #     elif(p.isdigit()):
# # # #         st = ".{"+p+"}"+w
# # # #         if(l.isdigit()):
# # # #             le=int(l)-len(w) - int(p)
# # # #             if(le>0):
# # # #                 st = st+".{"+str(le)+"}"
# # # #             else:
# # # #                 print("Word Length can't be lesser that the fragment length.")
# # # #     else:
# # # #         print("Invalid position")


# # # #     print(st)
    
# # # #     reg = re.compile(st)
# # # #     # regex=re.compile(reg)

# # # #     match=list(filter(reg.match,english_words))
# # # #     for word in match:
# # # #         if(l.isdigit()):
# # # #             if(len(word)==int(l)):
# # # #                 print(word)
# # # #         else:
# # # #             print(word)
# # # #     # print("zikkurats" in english_words)
# # # #     # print(reg.findall("adumbrate"))


# # # from kivy.app import App
# # # from kivy.uix.label import Label
# # # from kivy.uix.scrollview import ScrollView
# # # from kivy.properties import StringProperty
# # # from kivy.lang import Builder

# # # long_text = 'yay moo cow foo bar moo baa\n ' * 200

# # # Builder.load_string('''
# # # <ScrollableLabel>:
# # #     Label:
# # #         size_hint_y: None
# # #         height: self.texture_size[1]
# # #         text_size: self.width, None
# # #         text: root.text
# # # ''')

# # # class ScrollableLabel(ScrollView):
# # #     text = StringProperty('')
# # #     pass

# # # class ScrollApp(App):
# # #     def build(self):
# # #         return ScrollableLabel(text=long_text)

# # # # if __name__ == "__main__":
# # #     ScrollApp().run()

# # from spellchecker import SpellChecker

# # spell = SpellChecker()
# # str = input()

# # print(spell.correction(str))
# # for s in spell.correction(str):
# #     str+=" "+s
# # print(str)
# # print(len(spell.candidates(str)))

# import pronouncing
# fb = pronouncing.rhymes("light")
# for a in fb:
#     print(a+" ")
# import re
# import sys
# from nltk.corpus import wordnet
# import nltk
# import re
# from nltk.stem import WordNetLemmatizer

# word = input()
# synonyms = [] 

# for syn in wordnet.synsets(word):
    
#     for l in syn.lemmas():
#         print() 
#         print(l.name()+" - "+syn.pos())
# # if(len(synonyms)>0):     
# #     #print("Synonyms for " + word+" are :\n")
# #     #print(set(synonyms))
# #     ss=set(synonyms)
# #     new = "" 
# #     for x in ss: 
# #         new += x+"\n"
# #         #add more details like pos and all  
# #     return new
# # else:
# #     #print("No synonyms were found, try entering a different word.")
# #     str="No synonyms were found for the given input\n\n"           
# #     return str

#API for calling datamuse

# import requests
# word = "light"
# mean = "literature"
# response =  requests.get("https://api.datamuse.com/words?ml="+mean+"&rel_rhy="+word)
# for a in response.json():
#     print(a["word"])

# word = "indite"
# response= requests.get("https://od-api.oxforddictionaries.com/api/v2/entries/en-gb/"+word+"?strictMatch=false",headers={"Accept": "application/json","app_id": "c1498ba3","app_key": "ec959282e97d787344cbe7cfeb13c965"})
# try:
#     for a in response.json()["results"]:
#         for b in a["lexicalEntries"][0]["entries"][0]["senses"]:
#             print("Definition: "+b["definitions"][0])
    
#             print("Example: "+b["examples"][0]["text"])
   
# except KeyError:
#     print(response.json()["error"])

# across=input("Across - ")
# apos = int(input("Across common position - "))
# alen = int(input("Across length - "))
# down = input("Down - ")
# dpos = int(input("Down common position - "))
# dlen = int(input("Down length - "))
# words=word.split()
# w=""
# for a in words:
#     if(w==""):
#         w+=a
#     else:
#         w+="+"+a
# print(w)

# ares= requests.get("https://api.datamuse.com/words?ml="+across)
# dres = requests.get("https://api.datamuse.com/words?ml="+down)
# fn=""
# for a in ares.json():
#     if(len(a["word"])==alen):
#         for d in dres.json():
#             if(len(d["word"])==dlen):
#                 if(a["word"][apos]==d["word"][dpos]):
#                     fn+="Across - "+a["word"] +"\nDown - "+ d["word"]+"\nor\n"

# print(fn)
    


##WORD FREQUENCY FOR RATING SEARCHES.
# from wordfreq import word_frequency
# from wordfreq import zipf_frequency
# from wordfreq import top_n_list
# from wordfreq import iter_wordlist
# from wordfreq import get_frequency_dict
# print(word_frequency('the', 'en'))
# print(word_frequency('cafe', 'en')>word_frequency('indite', 'en'))
# print(zipf_frequency('fart', 'en'))
# print(zipf_frequency('pant', 'en'))
# print(zipf_frequency('crazy', 'en'))
# print(zipf_frequency('mozambique', 'en'))
# print(zipf_frequency('cumbersome', 'en'))

# print(top_n_list('en', 10))

# count=0
# for a in get_frequency_dict('en'):
#     count+=1
#     if(count<10):
#         print(a)
#     else:
#         break



# import os
# import pickle

# # inp=[6.05, 5.79, 5.17, 4.22, 4.77, 6.12, 4.32, 4.67, 6.32,5.18,4.07, 4.95, 4.07, 5.42, 4.72, 4.72, 6.12, 4.57, 5.12,6.07, 4.49, 4.07, 5.62, 6.52,4.12, 5.12, 6.37, 4.41,6.05, 4.79, 5.17, 4.22, 4.77, 5.12, 5.32, 6.67, 4.32,5.18,6.07, 4.95,4.07, 4.42, 5.72, 4.75, 4.12, 4.57, 5.12,5.07, 5.49, 5.07, 5.62, 5.52, 5.12, 5.12, 5.37, 5.41]
# # inp=[3.05, 2.79, 2.17, 2.22, 2.77, 3.12, 3.32, 2.67, 2.32,3.18,3.07, 2.95, 3.07, 2.42, 2.72, 2.72, 3.12, 2.57, 3.12,3.07, 2.49, 3.07, 2.62, 2.52, 3.12, 2.12, 3.37, 2.41,3.05, 2.79, 3.17, 3.22, 2.77, 2.12, 2.32, 2.67, 3.32,3.18,3.07, 2.05, 3.07, 2.42, 2.22, 2.72,2.12, 2.57, 3.12,2.07, 2.49, 3.07, 2.62, 2.52, 3.12, 3.12, 3.37, 3.41]

# if os.path.exists('./data/high.pkl'):
#     with open ('./data/high.pkl', 'rb') as f:
#         dataset_mid_level = pickle.load(f) 
#         # for a in inp:
#         #     dataset_mid_level.append(a)

# with open ('./data/chk1.pkl', 'wb') as f:
#             pickle.dump(dataset_mid_level, f)
# print(dataset_mid_level)

# from collections import defaultdict
# import pickle
# with open ('corpus_data/frequenc_words.pkl', 'rb') as f:
#          dataset = pickle.load(f)

# print(dataset.get(4.8))