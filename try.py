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

import speech_recognition as sr 
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
    print("Speak into the microphone")
    audio = r.listen(source)

try :
    print("Transcription: " +r.recognize_google(audio))
except sr.UnknownValueError:
    print("Audio unintelligible")
except sr.RequestError as e:
    print("Cannot obtain results;{0}".format(e))

##########################test case generation###################
# Python3 code to demonstrate 
# to compute all possible permutations 
# using list comprehension 

# initializing lists 
# list1 = ["Transaction - Sell on cash & collect payment now"
# ,"Transaction - Sell on credit & collect payment later"
# ,"Transaction - Buy on cash & pay right away"
# ,"Transaction - Buy on credit & pay later"
# ,"Transaction - Receive payment from customer"
# ,"Transaction - Receive advance from customer"
# ,"Transaction - Pay vendor/supplier"
# ,"Transaction - Pay advance to vendor or supplier"
# ,"Transaction - Buy on Petty Cash Account"
# ,"Transaction - Transfer main cash to petty cash"
# ,"Transaction - Withdraw Cash From Bank"
# ,"Transaction - Deposit Cash In Bank"
# ,"Transaction - Transfer Funds From One Bank To Another"
# ,"Transaction - Transfer Inventory Item From One Branch To Another"
# ,"Transaction - Credit Note for customer"
# ,"Transaction - Debit Note for customer"
# ,"Transaction - Credit Note for vendor"
# ,"Transaction - Debit Note for vendor"
# ,"Transaction - Refund Advance Received"
# ,"Transaction - Refund Amount Received Against Invoice"
# ,"Transaction - Reversal of ITC"
# ,"Transaction - Cancellation/Voiding Invoice"
# ,"Transaction - Create Sales Order/Bill Of Material"
# ,"Transaction - Create Purchase Requisition"
# ,"Transaction - Create Purchase Order"
# ,"Transaction - Material Issue Note"
# ,"Transaction - Make Provision/Journal Entry"] 
# list2 = ["Item - Cash"
# ,"Item - Petty Cash"
# ,"Item - Bank"
# ,"Item - Debtors"
# ,"Item - Advance to Vendors"
# ,"Item - TDS Receivables"
# ,"Item - Input SGST"
# ,"Item - Input CGST"
# ,"Item - Input IGST"
# ,"Item - Input CESS"
# ,"Item - Input SGST-RCM"
# ,"Item - Input CGST-RCM"
# ,"Item - Input IGST-RCM"
# ,"Item - Input CESS-RCM"
# ,"Item - Inter branch accounts"
# ,"Item - Fixed assets"] 
# list3 = [
#     "Status - Require Approval"
# ,"Status - Require Clarification"
# ,"Status - Clarified"
# ,"Status - Approved"
# ,"Status - Require Additional Approval"
# ,"Status - Rejected"
# ,"Status - Accounted"
# ] 

# list4 = ["Branch - Fast Polo - HO"
# ,"Branch - Testing Part 1"
# ,"Branch - Testing Part 2"
# ,"Branch - Mumbai"
# ,"Branch - HYDERABAD"
# ,"Branch - Kerala"
# ,"Branch - Aizawl"
# ,"Branch - ABC"]

# # printing lists 
# # print ("The original lists are : " + str(list1) +
# # 							" " + str(list2) +
# # 							" " + str(list3)) 

# # using list comprehension 
# # to compute all possible permutations 
# res = [[i, j, k,l] for i in list1 
# 				for j in list2 
# 				for k in list3
#                 for l in list4] 

# # printing result 
# # for l in res:
# #     print (str(l))
# import random
# random.shuffle(res)
# for i in range(21,30):
#     print (res[i])
# # for i in range(0,50):
# #     print(res[random.random()*100])
