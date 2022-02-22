import requests
import pandas as pd


# api_endpoint
url = "https://api.reliefweb.int/v1/disasters?appname=l3sdoc"
params = {"limit": 10, "profile": "list", "preset": "analysis"}


# sending get request and saving the response as response object
r = requests.get(url=url, params=params)

if r.status_code == 200:
    json_data = r.json()
    print(json_data["data"])
    df = pd.DataFrame.from_records(json_data["data"]["fields"])
