import random, string


print("******Welcome to the Dog Name Generator******\nBy Ezequiel A. Burgo - ezequielburgo@gmail.com\n")

vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
anyLetter=string.ascii_lowercase

print("A nice dog name has 4 characters :)")
firstLetter = input("I want the 1st letter to be a vowel (enter '1'), a consonant (enter'2'), random letter (enter'3'):")
secondLetter = input("I want the 2nd letter to be a vowel (enter '1'), a consonant (enter'2'), random letter (enter'3'):")
thirdLetter = input("I want the 3rd letter to be a vowel (enter '1'), a consonant (enter'2'), random letter (enter'3'):")
fourthLetter = input("I want the 4th letter to be a vowel (enter '1'), a consonant (enter'2'), random letter (enter'3'):")

def nameGenerator():
    error=False

    if firstLetter=="1":
        letter1=random.choice(vowels)
    elif firstLetter=="2":
        letter1=random.choice(consonants)
    elif firstLetter=="3":
        letter1=random.choice(anyLetter)
    else:
        error=True


    if secondLetter=="1":
       letter2=random.choice(vowels)
    elif secondLetter=="2":
        letter2=random.choice(consonants)
    elif secondLetter=="3":
        letter2=random.choice(anyLetter)
    else:
        error=True


    if thirdLetter=="1":
       letter3=random.choice(vowels)
    elif thirdLetter=="2":
        letter3=random.choice(consonants)
    elif thirdLetter=="3":
        letter3=random.choice(anyLetter)
    else:
        error=True


    if fourthLetter=="1":
       letter4=random.choice(vowels)
    elif fourthLetter=="2":
        letter4=random.choice(consonants)
    elif fourthLetter=="3":
        letter4=random.choice(anyLetter)
    else:
        error=True

    if error==False:
        name=letter1+letter2+letter3+letter4
        return (name)
    else:
        return ("Error")

names = nameGenerator()
if names=="Error":
    print("\nError, check your input and try again.")
else:
    print("\nWe suggest you these 10 names of four letters for your dog:")
    for names in range(10):
        print((nameGenerator()))