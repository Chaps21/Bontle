#Creating a Quizz Game

print("Welcome to my Quizz Game")
playing = input ("Do you want to play a game? ")
if playing != "yes": 
    quit() 
    print("Lets play Game: ")
    
   #Let's play and choose the correct letter 
    
print ("Where is Capaciti Located? ")
mylist=('a.Eastern Cape' +'\n'  "b. Gauteng"+'\n' "c.Western Cape" +'\n' "d. Limpopo")
print(mylist)


answer = input("Pick a correct letter  ")
if answer == "c":
    print("Correct!") 
       
else: 
    print("That is incorrect. Try Again. ")
print("The correct answer is C !")
# print ("Your current score is {0}".format(score))


 
   
