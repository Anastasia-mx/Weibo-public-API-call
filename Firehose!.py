
# coding: utf-8

# In[1]:

import urllib.request
import json
import pandas as pd

#TOKEN must be replaced by your developer token for SinaWeibo
token = 'TOKEN'
page = urllib.request.Request('https://api.weibo.com/2/statuses/public_timeline.json?access_token=' + token)
response = urllib.request.urlopen(page)
str_response = response.read().decode('utf-8')
data = json.loads(str_response)
df = pd.io.json.json_normalize(data['statuses'])

df.head()

dfingest = []

dfingest = df.text[0:4]


# In[ ]:

#script that got the json but didn't put it anywhere
#url = 'https://api.weibo.com/2/statuses/public_timeline.json'
#params = {'source': '157679999', 'access_token': '2.00wPOUWGp79GsD434bad3a5b03nvE4', 'count': 50}

# request public timeline
#response = requests.get(url, params=params)
#jres = response.json()
#print(jres)


#other things i tried that didn't work
#rawreply = connection.response().read()
#data = json.loads(rawreply.decode())

#elevations = response.read()
#data = json.loads(elevations)


# In[ ]:



