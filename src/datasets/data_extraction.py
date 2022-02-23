import requests
import pandas as pd


# api_endpoint
url = "https://api.reliefweb.int/v1/disasters?appname=l3sdoc"
# https://api.reliefweb.int/v1/disasters?appname=rwint-user-0&profile=list&preset=latest&slim=1
params = {"limit": 2, "profile": "full", "preset": "analysis"}


# sending get request and saving the response as response object
# r = requests.get(url=url, params=params)
r = requests.get(url="https://api.reliefweb.int/v1/countries/111")

# checking status code
if r.status_code == 200:
    json_data = r.json()
    print(json_data)
    # print(json_data["data"])
    # df = pd.DataFrame.from_records(json_data["data"]["fields"])
