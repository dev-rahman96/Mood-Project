import json
import requests




#response = requests.get("http://yerkee.com/api/fortune/wisdom")
#print(response)

class User:
    def __init__(self, user_name, latest_id):
        # self.random()
        self.name = user_name
        self.id = latest_id
        
        
        
    
    # def get_ran(self):
    #     return self.rand
    
    # def set_ran(self):
    #     pass

    # def ran(self):
    #     current_ran = input (f"What is your current mood?")
    #     ran_id = self.latest_ID
    #     self.randomlist.append
    #     (current_ran, ran_id)

class Fortune:
  def fortune_cookie(self):
    response = requests.get("http://yerkee.com/api/fortune/wisdom")
    wisdom = json.loads(response.text)
 


class User_Manager:
  def __init__(self):
    self.first_ID = 1
    self.userlist = []

  def create_user(self):
    user_name = input(f"What is the name of the user?\n")
    latest_id = self.first_ID
    new_user = User(user_name, latest_id)
    self.userlist.append(new_user)
    print(f"New user created with ID: {latest_id}")
    self.first_ID += 1
    self.show_user()
    return(latest_id)

  #def create_user(self):
    #user_name = input("What do you want your username to be? ")
   # user_id = self.latest_ID
   # user = User(user_name, user_id)
   # self.user[user_name] = user
   # print("Username stored! ")
    
  def show_user(self):
    print("""
    **************************
    Your User Listing:
    """)
    for person in self.userlist:
      print(person)

    print("""

    **************************
    """)
    return print(f"userlist")



  def update_user(self):
    latest_id = int(input(f"Enter the ID of the user to update: \n"))
    latest_id = latest_id - 1
    user_name = input(f"What is the new name for user {latest_id}: \n")
    user_to_update = self.userlist[int(latest_id)]
    user_to_update.name = user_name
    return print(f"Your user has been updated: {user_to_update}")
    self.show_user()
   
  def delete_user(self):
    latest_id = int(input(f"Enter the ID of the user to delete: \n"))
    latest_id = latest_id - 1
    self.userlist.pop(latest_id)
    print(f"The user has been deleted!")
    self.show_user()  

  #def delete_user(self):
   # name = input("Please enter the username you want to delete: ")
    #if name in self.user.keys():
     # self.user.pop(name)
    #else:
     # print("The username does not exist ")
      
  def save(self):
    with open('user_file.json' , 'w') as write_file:
      json.dump(userlist, write_file , indent=4)
      
  def load(self):
    with open('user_file.json' , 'r') as read_file:
      userlist = json.load(read_file)
   

  
  def api_call():
    pass
  


# #Use the new datastore datastructure
#     # print datastore["office"]["parking"]["style"]
  