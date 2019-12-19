#kivy



# from nltk.corpus import wordnet
# # from nltk.stem import WordNetLemmatizer 
# word = "technologically"
# syns = wordnet.synsets(word) 
# # # An example of a synset: 
# # lemmatizer = WordNetLemmatizer() 
  
# # print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))


# # Just the word: 
# for l in syns:
#     print("Your word : "+ word)
#     print("Meaning : "+l.definition())
#     print("Example : ",end='')
#     for e in l.examples() :
#         print(e,end="\n          ")
# # print(syns[0].lemmas()[0].name()) 

# # # Definition of that first synset: 
# # print(syns[0].definition()) 

# # # Examples of the word in use in sentences: 
# # print(syns[0].examples())

###################speech_recognition####################

# import speech_recognition as sr 
# r = sr.Recognizer()
# with sr.Microphone() as source:
# 	r.adjust_for_ambient_noise(source)
#     print("Speak into the microphone")
#     audio = r.listen(source)
# 	print("Thanks.")
# try :
#     print("Transcription: " +r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Audio unintelligible")
# except sr.RequestError as e:
#     print("Cannot obtain results;{0}".format(e))

###############################text to speech###########################
# import pyttsx3 
  
# # initialisation 
# engine = pyttsx3.init() 
  
# # testing  
# a ="Adam"
# print("Welcome to the Finding Zone, where you can find words !!!")
# engine.say("Welcome"+a)
# engine.runAndWait()
# print("Choose your option:")

# engine.say("Choose your Option ")
# engine.runAndWait()
# print("1.Find a word with similar meaning")
# engine.say("Press 1 to Find a word with a similar meaning")
# engine.runAndWait()
# print("2.Find a word with opposite meaning")
# engine.say("Press 2 to Find a word with opposite meaning")
# engine.runAndWait()
# print("3.Find a word rhyming with your word")
# engine.say("Press 3 to Find a word rhyming with your word")
# engine.runAndWait()
# print("4.Find a word for your crossword puzzle")
# engine.say("press 4 to Find a word for your crossword puzzle")
# engine.runAndWait()

# import pyttsx3
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

