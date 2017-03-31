from PIL import Image
import sys
import json
import requests

key = "**API KEY**"

def getFaces(image):
	endpoint = "https://api.haystack.ai/api/image/analyze?output=json&apikey={}&model=gender".format(key)
	responseString = requests.post(endpoint, data=image)
	response = json.loads(responseString.text)
	faces = []

	for face in response["people"]:
		location = face["location"]
		x = location["x"]
		y = location["y"]
		w = location["width"]
		h = location["height"]
		face = (x, y, x + w, y + h)

		faces.append(face)

	return faces

imagePath = sys.argv[1]
imageData = open(imagePath, "rb")
image = Image.open(imagePath)
faces = getFaces(imageData)
i = 0

for face in faces:
	image.crop(face).save("face_{}.jpg".format(i))
	i += 1