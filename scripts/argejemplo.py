# Adolfo Jeritson
# 2015
# Example of how to use arguments from command line and user input
#

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi", user_name, ", I'm the", script)
print("I'd like to ask you a few questions.")
print("Do you like me", user_name,"?")
likes = input(prompt)

print("Where do you live", user_name,"?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)


print("Alright, so you said", likes, "about liking me.")
print("You live in", lives,".  Not sure where that is.")
print("And you have a", computer, "computer.  Nice.")
