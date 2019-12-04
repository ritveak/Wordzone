from nltk.corpus import wordnet
def fun(word,leng):
    if leng>1:
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
        fin = []
        for l in fn:
            if len(l) == leng:
                print(l)
            
        #print(fin)

fun("Literature",3)
