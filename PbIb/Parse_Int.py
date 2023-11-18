from bs4 import BeautifulSoup
import requests

name = 'ZBLAN fluoride glass    '
url = 'https://refractiveindex.info/?shelf=glass&book=ZBLAN&page=Gan'
RibnoeFile = 'material.txt'

request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")
vse_gadi = str(bs.find_all("script"))

a = vse_gadi.split("data_n_wl")[1]
first = a.split("data_k_wl")[0]
second = a.split("data_n")[1]
second = second.split("data_k")[0]
first = first.split("[")[1]
first = first.split("]")[0]
second = second.split("[")[1]
second = second.split("]")[0]

f = open(RibnoeFile, 'a')
f.write("\n" + name + "\n" + first + "\n" + second + "\n")
