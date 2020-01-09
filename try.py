# #kivy

# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty



# ## INHERITING GRID LAYOUT - ie. USING PYTHON COMMANDS FOR PUTTING IN ELEMENTS

# # class MyGrid(GridLayout):
# #     def __init__(self,**kwargs):
# #         super(MyGrid,self).__init__(**kwargs)
# #         self.cols=1
# #         self.inside = GridLayout()
# #         self.inside.cols =2

# #         self.inside.add_widget(Label(text="First Name: "))
# #         self.fname = TextInput(multiline=False)
# #         self.inside.add_widget(self.fname)

# #         self.inside.add_widget(Label(text="Last Name: "))
# #         self.lname = TextInput(multiline=False)
# #         self.inside.add_widget(self.lname)

# #         self.inside.add_widget(Label(text="Email: "))
# #         self.email = TextInput(multiline=False)
# #         self.inside.add_widget(self.email)
# #         self.add_widget(self.inside)
# #         self.submit = Button(text = "Submit", font_size=24)
# #         self.submit.bind(on_press=self.pressed)
# #         self.add_widget(self.submit)
    
# #     def pressed(self,instance):
# #         print("Name:",self.fname.text,self.lname.text)
# #         self.fname.text = ""
# #         self.lname.text = ""
        



# # class MyApp(App):
# #     def build(self):
# #         return MyGrid()

# # if __name__ =="__main__":
# #     MyApp().run()



# # INHERITING WIDGET ie. USING KV FILE

# class MyGrid(Widget):
#     name = ObjectProperty(None)
#     email = ObjectProperty(None)
    
#     def btn(self):
#         print(self.name.text, self.email.text)
#         self.name.text =""
#         self.email.text=""


# class TryApp(App):
#     def build(self):
#         return MyGrid()


# if __name__ == "__main__":
#     TryApp().run()






# #------------------------------------------------xxxxxxxxxxxxxxxx---------------------------------------------

# # from nltk.corpus import wordnet
# # # from nltk.stem import WordNetLemmatizer 
# # word = "technologically"
# # syns = wordnet.synsets(word) 
# # # # An example of a synset: 
# # # lemmatizer = WordNetLemmatizer() 
  
# # # print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))


# # # Just the word: 
# # for l in syns:
# #     print("Your word : "+ word)
# #     print("Meaning : "+l.definition())
# #     print("Example : ",end='')
# #     for e in l.examples() :
# #         print(e,end="\n          ")
# # # print(syns[0].lemmas()[0].name()) 

# # # # Definition of that first synset: 
# # # print(syns[0].definition()) 

# # # # Examples of the word in use in sentences: 
# # # print(syns[0].examples())

# #------------------------------------------------xxxxxxxxxxxxxxxx---------------------------------------------


# # import speech_recognition as sr 
# # r = sr.Recognizer()
# # with sr.Microphone() as source:
# # 	r.adjust_for_ambient_noise(source)
# #     print("Speak into the microphone")
# #     audio = r.listen(source)
# # 	print("Thanks.")
# # try :
# #     print("Transcription: " +r.recognize_google(audio))
# # except sr.UnknownValueError:
# #     print("Audio unintelligible")
# # except sr.RequestError as e:
# #     print("Cannot obtain results;{0}".format(e))

# ###############################text to speech###########################
# # import pyttsx3 
  
# # # initialisation 
# # engine = pyttsx3.init() 
  
# # # testing  
# # a ="Adam"
# # print("Welcome to the Finding Zone, where you can find words !!!")
# # engine.say("Welcome"+a)
# # engine.runAndWait()
# # print("Choose your option:")

# # engine.say("Choose your Option ")
# # engine.runAndWait()
# # print("1.Find a word with similar meaning")
# # engine.say("Press 1 to Find a word with a similar meaning")
# # engine.runAndWait()
# # print("2.Find a word with opposite meaning")
# # engine.say("Press 2 to Find a word with opposite meaning")
# # engine.runAndWait()
# # print("3.Find a word rhyming with your word")
# # engine.say("Press 3 to Find a word rhyming with your word")
# # engine.runAndWait()
# # print("4.Find a word for your crossword puzzle")
# # engine.say("press 4 to Find a word for your crossword puzzle")
# # engine.runAndWait()

# # import pyttsx3
# # def onStart(name):
# #    print ('starting', name)
# # def onWord(name, location, length):
# #    print ('word', name, location, length)
# # def onEnd(name, completed):
# #    print ('finishing', name, completed)
# # engine = pyttsx3.init()
# # engine.connect('started-utterance', onStart)
# # engine.connect('started-word', onWord)
# # engine.connect('finished-utterance', onEnd)
# # engine.say('The quick brown fox jumped over the lazy dog.')
# # engine.runAndWait()








# # #All the important imports
# # from kivy.app import App
# # from kivy.uix.button import Button
# # from kivy.lang import Builder
# # from kivy.uix.screenmanager import ScreenManager, Screen

# # #To get a purplish background in all the screens
# # from kivy.core.window import Window
# # Window.clearcolor = (0.259, 0.251, 0.447,0.9)

# # #Main Window Screen declaration
# # class MainWindow(Screen):
# #     pass

# # #Find Zone
# # class FindWindow(Screen):
# #     pass

# # #Understand Zone
# # class UnderstandWindow(Screen):
# #     pass

# # #Knowledge Zone
# # class KnowWindow(Screen):
# #     pass

# # #Window Manager
# # class WindowManager(ScreenManager):
# #     pass

# # #To load our kv file:
# # kv = Builder.load_file("try.kv")

# # #Our main App
# # class tryApp(App):
# #     def build(self):
# #         return kv#MyGrid()

# # #App initialising through main
# # if __name__ == "__main__":
# #     tryApp().run()


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.lang import Builder

long_text = 'yay moo cow foo bar moo baa\n ' * 200

Builder.load_string('''
<ScrollableLabel>:
    Label:
        size_hint_y: None
        height: self.texture_size[1]
        text_size: self.width, None
        text: root.text
''')

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class ScrollApp(App):
    def build(self):
        return ScrollableLabel(text=long_text)

if __name__ == "__main__":
    ScrollApp().run()