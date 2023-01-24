import requests
import json
from PIL import Image


def catimage_request():

    APIresponse = requests.get('https://api.thecatapi.com/v1/images/search')

    data = json.loads(APIresponse.content)

    catimage_link = data[0].get('url')
    catimage_file = requests.get(catimage_link, stream=True)
    catimage = Image.open(catimage_file.raw)
    catimage.show()

    return catimage


if __name__ == '__main__':
    catimage_request()
