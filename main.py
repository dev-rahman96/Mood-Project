import sys
from giphy import Giphy


class Menu:
  def __init__(self):
    self.app = Giphy()
    self.options = {

      "1": self.app.create_giphy,

      "2": self.app.update_giphy,

      "3": self.app.show_giphy,

      "4": self.app.delete_giphy,

      "Q": self.quit

    }
    
    def menu_options(self):
      print("""
      **********Welcome to Giphy mood generator*************
        
        Please choose one of the following options:
         1. Create a Giphy

         2. Update a Giphy

         3. Show Giphy's

         4. Delete Giphy

        'Q' Quit app

      *******************************************************
        
         """)

def run(self):
    while True:
      self.menu_options()
      option = input("Enter an option: ")
      action = self.options.get(option)

      if action:
        action()
      else:
        print("{0} is not a valid option, Please try again".format(option))


def quit(self):

      choice = input("Do you want to save your session? y/n \n\n")
      if("y" in choice.lower()):
        self.task_manager.save() # saving our session to a file 
 
      ''' quit or terminate the program '''
 
      print("Thank you for visiting the warehouse today! \n")
 
      sys.exit(0)
    




    
