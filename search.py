import json, requests

url = 'https://api.foursquare.com/v2/venues/search'
params = dict(
    client_id='BMZJXGUYB5IZX3NEZX3OBDDKGFEVBHRRFZF03ZTDN32UNU11',
    client_secret='D223GRK5PHRZ5A3BQUB0YIIONAOJRZHOZILUQ5RD3YKOHNHR',
    near='Spokane, WA',
    v='20200218'
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
with open('spokane.json', 'w') as fp:
    json.dump(data, fp)