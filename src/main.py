import requests


parameters = "q=catch22"
contents = requests.get(f"https://openlibrary.org/search.json?{parameters}")
print(contents.content)
