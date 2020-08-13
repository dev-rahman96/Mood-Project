import json
import requests




#response = requests.get("http://yerkee.com/api/fortune/wisdom")
#print(response)

class User:
    def __init__(self, name, task_id):
        # self.random()
        #self.latest_ID = 1
        self.name = name
        self.id = task_id
        
        
    
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
    self.user = {}
    self.latest_ID = 1


  def create_user(self):
    user_name = input("What do you want your username to be? ")
    user_id = self.latest_ID
    user = User(user_name, user_id)
    self.user[user_name] = user
    print("Username stored! ")


  def update_user(self):
    old_username = input("Enter current username:")
    updated_username = input("Enter new username:")
    self.user.pop(old_username) 
    self.user.append(updated_username)

  def delete_user(self):
    name = input("Please enter the username you want to delete: ")
    if name in self.user.keys():
      self.user.pop(name)
      
    else:
      print("The username does not exist ")
      
  # def save(self):
  #   with open('data.json' , 'w') as fp:
  #     json.dump(user, fp , sort_keys=True, indent=4)
      
  # def load(self):
  #   with open('data.json' , 'r') as fp:
  #     user = json.load(fp)
      
  def save(self):
      with open(test.json, 'wb') as outfile:
        json.dump(user, outfile)
      with open(test.json) as infile:
        user = json.load(infile)
      

      
  
  def api_call():
    pass
  


# #Use the new datastore datastructure
#     # print datastore["office"]["parking"]["style"]
  