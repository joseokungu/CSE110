"""
Author: Jose Okitandende

Purpupose: Write a program with variables and strings to accomplish a meaningful task

"""
print("please enter the following information: ")
print("")

#These words of clever story:
#The word are inserted into the story.
noun = input("Noun: ")
pronoun = input("Pronoun: ")
adverb = input("Adverb: ")
adjectif = input("Adjectif: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamaction = input("Exclamaction: ")
verb = input("Verb: ")
verb = input("Verb: ")
noun = input("Noun: ")

print ("")
#This clever story.
#the exclamaction word and every word that starts a sentence are capitalize.


print("Your story is: ")
print ("")
madlibs =f'{"The".capitalize()} other {noun}, {pronoun} was {adverb} in trouble. {"It".capitalize()} all started when I saw a very \n {adjectif} {animal} {verb} down the hallway. "{exclamaction.capitalize()}!" I yelled. {"But".capitalize()} all \n I could think to do was to {verb} over and over. {"Miraculously".capitalize()}, \n that caused it to stop, but not before it tried to {verb} \n right in front of my {noun}. '
print(madlibs)
