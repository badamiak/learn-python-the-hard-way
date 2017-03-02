from sys import argv

script, user_name = argv
prompt = "%s@host: " %user_name

print("Hi %s, I'm the %s script" %(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s ?" %user_name)
likes = input(prompt)

print("Where do you live %s?" %user_name)
lives = input(prompt)

print("What kindof computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" %(likes, lives, computer))