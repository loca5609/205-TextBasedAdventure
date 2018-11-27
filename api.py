# This will be the API to give images and information to the site
import requests
import json

# i will put this in a file at some point
api_key = "6565317-9e81b7ea7894f9ca685d68558"


# hell yeah
def catCall():
    catResponse = requests.get("https://cat-fact.herokuapp.com/facts")
    catDict = json.loads(catResponse.text)
    factList = []
    for i in range(len(catDict['all'])):
        if (len(catDict['all'][i]['text']) < 5):
            continue
        factList.append(catDict['all'][i]['text'])
    return factList


# @param room: the name of the room you are in, this will be the search term
# for the API to call.
def imageApiCall(room, api_key):
    url = f"https://pixabay.com/api/?key={api_key}&q="
    response = requests.get(f"{url}{room}&image_type=photo")
    responseDict = json.loads(response.text)
    return responseDict
