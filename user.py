class User:
  def __init__(self):
    self.mood()

  
  def mood(self):
    current_mood = input(f"What is your current mood? ")
    mood_id = self.latest_ID
    self.moodlist.append(current_mood, mood_id)
    



    # while True:
    #   try:







  # def get_mood(self):
  #   print (f"The available moods are ", {self.moodlist})
  #   return self.m 
  
  # def set_mood(self):
  #   current_mood = input(f"Please pick a mood from the available list. ", {self.moodlist})