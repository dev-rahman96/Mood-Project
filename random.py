import json
import requests


response = requests.get("http://yerkee.com/api/fortune/wisdom")
print(response)

class Random:
  def __init__(self):
    self.user = {}
    self.latest_ID = 1


  def api_call(self):
    pass

  def create_user(self):
    pass


  def update_user(self):
    pass

  def read(self):
    pass

  def delete_user(self):
    pass
