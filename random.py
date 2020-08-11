import json
import requests
import pickle
from user import User


response = requests.get("http://yerkee.com/api/fortune/wisdom")
print(response)

class Random:
  def __init__(self):
    self.user = {}
    self.latest_ID = 1


  def api_call(self):
    pass

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
      
  def save(self):
    with open("tasks.txt", "wb") as fp:   #Pickling
      pickle.dump(self.task_list, fp)
      print("\nTasks saved! \n\n")
      
  def load(self):
    with open("tasks.txt", "rb") as fp:   #Unpickling
      self.task_list = pickle.load(fp)
      self.latest_ID = len(self.task_list)
      print("Tasks loaded!")
