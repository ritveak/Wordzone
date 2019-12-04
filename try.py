from nltk.corpus import wordnet
# from nltk.stem import WordNetLemmatizer 
  



word = "technologically"
syns = wordnet.synsets(word) 
# # An example of a synset: 
# lemmatizer = WordNetLemmatizer() 
  
# print("Root word :", lemmatizer.lemmatize(syns[0].lemma_names()[0]))


# Just the word: 
for l in syns:
    print("Your word : "+ word)
    print("Meaning : "+l.definition())
    print("Example : ",end='')
    for e in l.examples() :
        print(e,end="\n          ")
# print(syns[0].lemmas()[0].name()) 

# # Definition of that first synset: 
# print(syns[0].definition()) 

# # Examples of the word in use in sentences: 
# print(syns[0].examples())