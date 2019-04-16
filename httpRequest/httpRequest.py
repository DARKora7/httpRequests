import requests
from requests.exceptions import HTTPError
import used_functions as uf

try:
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    response.raise_for_status
except HTTPError as http_er:
    print(f'Http Error has occured: {http_er}')
except Exception as er:
    print(f'An Error has occured: {er}')
finally:
    print("connected")
    if uf.validateData(response.json()):
        SortedCustList = uf.ExtractList(response.json())
        uf.MakeTextFile(SortedCustList)
    else:
        quit()
