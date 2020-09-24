

######################################################
# this functions only purpose is to ask for and
# recieve user input
#####################################################
def user_input():
    words = input("please enter a word or sentence :")
    return words

######################################################
# this functions splits the sentences into manageble
# words
#####################################################
def word_editor(words):
    word_list = words.rsplit(" ")
    sentence = " "
    for n in word_list:
       temp = pig_latinor(n)
       sentence = sentence + temp
    return sentence

######################################################
# this functions takes a word and converts it to pig
# latin
#####################################################
def pig_latinor(word):
    vowels_list = ["a","e","i","o","u","y"] # this list contains all the vowels
    if word.isdigit():                      # making sure the word isnt a number 
        word = word + " "
    elif len(word) >1:
        if (vowels_list.count(word[0]) == 0 and 
            vowels_list.count(word[1]) == 0):     
            # this is to make sure that words that start with th or sr retain proper pronunciation
            temp_letter = word[:2]               
            word = word[2:]       
        else:
            temp_letter = word[0]
            word = word[1:]

        word = word + " " + temp_letter + "ay "
    else:                             # this deals with the single letter words
        word = word + "ay "
    
    return word

###############################################################
# this functions cleans up the displays the newly made sentence
###############################################################
def display(sentence):
    sentence.strip()
    print(sentence)

########################################################
# this is where it is all controlled
########################################################
users_sentence = user_input()
piglatin_sentence = word_editor(users_sentence)
display(piglatin_sentence)