import json
import requests
import os
import pickle
from user import User

class Giphy:
  def __init__(self):
    self.moodlist = {}
    self.latest_ID = 1

  def create_giphy(self):
    class_mood = user()
    m = class_mood.get_mood()

    if m in self.giphy.keys():
      print(f"{m} already exited, the giphy is:{self.giphy[m]}"'\n')
    else: 
      #advise = self.call_giphy_api()
      print(f"\n The giphy is: {giphy}"'\n')
      self.giphy[m] = giphy
  
  
  def show_giphy(self):
    if not self.giphy:
      print("There is no giphy")
      return
    
    print("We have these giphy: \n")
    self.giphy = dict(sort(self.giphy.items()))
    for(mood,giphy) in self.giphy.items():
        print(mood,": ", giphy, '\n')
        
  def update_giphy(self):
    mood_name = input('You want to change your giphy mood? Here is the list of moods you can choose from:', self.moodlist,'. Please pick your new current mood.')
    return print(f"Your mood has been changed:",mood_name)
    self.show_giphy()
  
  def delete_giphy(self):
    delete_giphy = input(f"Which giphy mood would you like to delete? \n")
    if delete_giphy in self.list.keys():
      self.list.pop(delete_giphy)
      print("The {delete_giphy} has been deleted.")
    else:
      print("The giphy mood does not exist.") 

  def exception(self):
    while userinput in self.moodlist:
      print (self.moodlist)
    else:
     print ("User must pick a valid choice! ") 
  
  # def call_giphy_api(self):
  #   giphy = requests.get
  #   ('https://developers.giphy.com/')
  #   giphy = giphy.json()
  #   giphy = giphy ["slip"]["giphy"]
  #   return giphy
  

    

  #def save(self):
  #   with open('tasks.json', 'w') as w:

  #     #moodlist = {}
      
  #     for keys, mood in self.moodlist.items():
  #       self.moodlist[keys] = mood

  #     json.dump(self.moodlist, w)

  #def load(self):
  #  with open("tasks.json", "rb") as fp:   #Unpickling
  #    self.moodlist = pickle.load(fp)
  #    self.latest_ID = len(self.moodlist)
  #    print("Your dwarf mood loaded!")
      
        
 


#Moods = Doc:https://giphy.com/gifs/disney-snow-white-doc-and-the-seven-dwarfs-OtM3z3qfDBfGM, Happy:https://giphy.com/gifs/disney-snow-white-doc-and-the-seven-dwarfs-12IFzyI7bQr88E, Sneezy:https://giphy.com/gifs/disney-snow-white-doc-and-the-seven-dwarfs-gNqPZGiwsZs9a, Sleepy:https://giphy.com/gifs/disney-snow-white-doc-and-the-seven-dwarfs-v2XKEg53xUFtC, Bashful:https://giphy.com/gifs/dwarf-snow-white-and-the-seven-dwarves-aww-shucks-26vUxJ9rqfwuIEkTu, Grumpy:https://giphy.com/gifs/disney-snow-white-doc-and-the-seven-dwarfs-IScTu2L6wFJYc, Dopey:https://giphy.com/gifs/cute-disney-dancing-nOqDm37B67gcg
  