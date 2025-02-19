import requests
import json


parameters = "q=catch22"
response = requests.get(f"https://openlibrary.org/search.json?{parameters}")
response_dict = json.loads(response.content)
print(response_dict['docs'][0]['ia'])

# url = "https://api.archivelab.org/v1/books"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.text)
