import json
import requests




#response = requests.get("http://yerkee.com/api/fortune/wisdom")
#print(response)

class User:
    def __init__(self, user_name, user_id):
        # self.random()
        self.user_id = 1
        self.user_name = user_name
        
        
        
    
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
  def __init__(self):
    self.URL = "http://yerkee.com/api/fortune/wisdom"
    self.init()
      
  def init(self):
    try:
      req = requests.get(self.URL)
      res = req.json()
    except:
        print("Network error")


class User_Manager:
  def __init__(self):
    self.first_ID = 1
    self.user = []
    self.latest_ID = 1

  def create_user(self):
    user_name = input(f"What is the name of the user?\n")
    latest_id = self.first_ID
    new_user = User(user_name, latest_id)
    self.user.append(new_user)
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
    for person in self.user:
      print(person)

    print("""

    **************************
    """)
    return self.user



  def update_user(self):
    pass

      
    

  def delete_user(self):
    name = input("Please enter the username you want to delete: ")
    if name in self.user.keys():
      self.user.pop(name)
    else:
      print("The username does not exist ")
      
  def save(self):
    with open('data.json' , 'w') as fp:
      json.dump(user, fp , sort_keys=True, indent=4)
      
  def load(self):
    with open('data.json' , 'r') as fp:
      user = json.load(fp)
      

  
  def api_call():
    pass
  


# #Use the new datastore datastructure
#     # print datastore["office"]["parking"]["style"]
  