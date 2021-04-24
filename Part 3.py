import pandas as pd
import json
import requests

request=requests.get("https://api.covid19api.com/summary")
print(request.status_code)
print(request.text)
