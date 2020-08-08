import sys

class Menu:
 
 
 def __init__(self):
 
 
      
      self.random = Random() 
 
      
      self.choices = {
 
           "1" : self.random.create_user,
 
           "2" : self.random.update_user,
 
           "3" : self.random.api_call,

           "4" : self.random.delete_user,

           "Q" : self.quit
 
 
 
        }
 
 
 
 def display_menu(self):
 
       print(""" 
            **************************
             Welcome to our mood program!
             How can we help you?  
 
 
             1. Create User
 
             2. Update User
 
             3. Fortune

             4. Delete User

             Q. Quit program
 
             """)
 
 
 def run(self):
 
     ''' Display menu and respond to user choices '''
 
     while True:
 
           self.display_menu()
 
           choice = input("Enter an option: " )
 
           action = self.choices.get(choice)
 
           if action:
 
                action()
 
           else:
 
              print("{0} is not a valid choice".format(choice))

 def quit(self):

      choice = input("Do you want to save your session? y/n \n\n")
      if("y" in choice.lower()):
 
        ''' quit or terminate the program '''
 
      print("Thank you for visiting the warehouse today! \n")
 
      sys.exit(0) 