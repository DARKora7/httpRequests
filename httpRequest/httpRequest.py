import requests
from requests.exceptions import HTTPError
from used_functions import *



def run():
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
        if validateData(response.json()):
            SortedCustList = ExtractList(response.json())
            MakeTextFile(SortedCustList)
        else:
            quit()
