import requests

data = {'os_username':'wzy','os_password':'5639421275'}
s = requests.Session()
r = s.post('http://jira.rsvptech.ca:8080/jira/rest/dashboards/1.0/10000/gadget/0/prefs',params=data)
print(r.text)