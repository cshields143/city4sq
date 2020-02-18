import json, requests

url = 'https://api.foursquare.com/v2/venues/explore'
params = dict(
    client_id='BMZJXGUYB5IZX3NEZX3OBDDKGFEVBHRRFZF03ZTDN32UNU11',
    client_secret='D223GRK5PHRZ5A3BQUB0YIIONAOJRZHOZILUQ5RD3YKOHNHR',
    v='20180323',
    ll='40.7243,-74.0018',
    query='coffee',
    limit=1
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
with open('eg.json', 'w') as fp:
    json.dump(data, fp)