import requests,pprint

r = requests.get('')
pprint.pprint(r.text)