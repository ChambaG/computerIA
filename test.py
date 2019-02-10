from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

resource = urlopen("https://cs.copart.com/v1/AUTH_svc.pdoc00001/PIX133/6c257fb3-e3b4-41b6-82af-da92725e8752.JPG", context= context)
output = open("Data/file02.jpg", "w+")
output.write(resource.read())
output.close()