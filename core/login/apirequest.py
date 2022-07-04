from urllib import response
import requests
baseurl='https://rickandmortyapi.com/api/'
endpoint='character'
pageNo='/?page=' 
a=4
print("defffr")
x=str(a)
r=requests.get(baseurl+endpoint+ pageNo+x)
data=r.json()
print(r)
t= data['results'][0]['name']
print(t)
for i in data['results']:
  print(i['name'])
#p=response['info']['pages']
def getpages(response):
  return(response['info']['pages'])