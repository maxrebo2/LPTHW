doYouWantToSeeTommorow = input("Do You Want to See Tommorow? " + "Is Jordan, Bubba?")
numberOfGuesses = 1

while doYouWantToSeeTommorow == "no":
    numberOfGuesses = numberOfGuesses + 1
    doYouWantToSeeTommorow = input("Yes you do. ")


print("No you don't.")
print("It took you " + str(numberOfGuesses) + " guesses.")