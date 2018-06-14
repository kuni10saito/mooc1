import populartimes
gid="AIzaSyBQv0IZlVassvx8X6_n9ZCUY-nrxWK2w1E" #Google Maps API key 
pid="ChIJw9u_XSsrAmARMIwpeAshKu4" #•Fªé‚ÌƒvƒŒƒCƒX ID

data=populartimes.get_id(gid, pid)
d1=data['populartimes']

import pandas as pd
df = pd.DataFrame()
col_list=[]
for i in range(len(d1)):
   m = d1[i]
   df[i]=m['data']
   col_list.append(m['name'])

df.columns=col_list
df.to_csv('week.csv')
