from api import imageApiCall
from PIL import Image
import requests
from io import BytesIO

api_key = "6565317-9e81b7ea7894f9ca685d68558"
imageDict = imageApiCall("throne", api_key)

imageUrls = []
for i in range(len(imageDict['hits'])):
    url = imageDict['hits'][i]['largeImageURL']
    imageUrls.append(url)

# print(imageUrls)
# Test of reading an image
response = requests.get(imageUrls[15])
img = Image.open(BytesIO(response.content))
img.show()