import sys
from Fortune_Cookie import User_Manager

class Menu:
 
 
 def __init__(self):
 
 
      
      self.user_manager = User_Manager() 
 
      
      self.choices = {
 
           "1" : self.user_manager.create_user,
 
           "2" : self.user_manager.update_user,
 
           "3" : self.user_manager.api_call,

           "4" : self.user_manager.delete_user,

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