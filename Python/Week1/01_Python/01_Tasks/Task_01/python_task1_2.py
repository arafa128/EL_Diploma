def isVowel(char):
    VOWEL=['a','e','i','o','u','A','E','I','U','O']

    if char in VOWEL:
        print("The character '{char}' is a vowel!")
    else:
        print(f"The character '{char}' is not vowel!") 

#userinput= input("Enter Character :")
isVowel(input("Enter Character :"))