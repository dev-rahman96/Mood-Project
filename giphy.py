def create_giphy(self):
    class_mood = user()
    m = class_mood.get_mood()

    if m in self.giphy.keys():
      print(f"{m} already exited, the giphy is :
      {self.giphy[m]\n"})
    else: 
      advise = self.call_giphy_api()
      print(f"\n The giphy is: {giphy}\n")
      self.giphy[m] = giphy