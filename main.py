print("Welcome to this chatbot")
name = input("what is your name?: ")
age = input("Hello " + name + "How old are you?: ")

print("welcome "+ name + "How can i help you today?")
print("please chose a number 1-4")



def display_menu():
    print ("option 1")
    print ("option 2")
    print ("option 3")
    print ("Exit")

def user_selection():
   in_use = False
   
   user_choice = int(input("Enter a Number 1-4:"))
   if user_choice == 1:
     print (1)
   elif user_choice == 2:
    print (2)
   elif user_choice == 3:
    print (3)
   elif user_choice == 4:
    print ("Program ends,Goodbye")
    in_use = False
   else:
    print ("/nSorry, not a valid choice")





display_menu()
user_selection()
