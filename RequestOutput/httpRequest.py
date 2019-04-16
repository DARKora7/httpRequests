import requests
from requests.exceptions import HTTPError

def validateData(json):
    valid =True
    Checklist = ["name","phone","email"]
    if len(json) != 10:
        valid = False
    else:
        for i in json:
            if not ((Checklist[0]) and (Checklist[1]) and (Checklist[2])) in i:
                valid = False
                break
            else:
                if (i["email"].count('@')==0) and ((i["email"][i["email"].find('@'):].count('.')==0)):
                    valid = False
                    break
    return valid


def MakeTextFile(list):
    f = open("ContactList.txt", "w")
    print(f.name)
    f.write('='*100+'\n'+'Contact List\n'+'-'*100+'\n'+'{:20} {:20} {:30} {:20}\n'.format('Last Name', 'First Name', 'Phone', 'email address','')+'-'*100+'\n')
    for i in list:
        f.writelines(i)
    f.write('{:=<100}'.format(''))
    f.close()

def ExtractList(json):
    unSortedCustList = []
    for i in json:
        name = i["name"].split()
        if i["name"].find(' ')<5:
            unSortedCustList.append('{:20} {:20} {:30} {:20}\n'.format(name[2], name[1], i["phone"], i["email"]))
        else:
            unSortedCustList.append('{:20} {:20} {:30} {:20}\n'.format(name[1], name[0], i["phone"], i["email"]))
    unSortedCustList.sort()
    return unSortedCustList


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
