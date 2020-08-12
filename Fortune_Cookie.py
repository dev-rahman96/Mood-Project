import json
import requests
import user_class



#response = requests.get("http://yerkee.com/api/fortune/wisdom")
#print(response)

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


class Random:
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
  #   with open("tasks.txt", "wb") as fp:   #Pickling
  #     pickle.dump(self.task_list, fp)
  #     print("\nTasks saved! \n\n")
      
  # def load(self):
  #   with open("tasks.txt", "rb") as fp:   #Unpickling
  #     self.task_list = pickle.load(fp)
  #     self.latest_ID = len(self.task_list)
  #     print("Tasks loaded!")
      
  
  def api_call():
    pass
  
  def save(self):
    
  #prompt the user for a file to import
    filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open JSON File", filter)

#Read JSON data into the datastore variable
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)

#Use the new datastore datastructure
    # print datastore["office"]["parking"]["style"]
  