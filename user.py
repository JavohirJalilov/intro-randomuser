import requests
import json


def get_user(user_data: dict) -> dict:
    '''get user from data
    
    Args:
        user_data (dict): user data from https://randomuser.me/api/
        
    Returns:
        dict: {
            'firstname': user firstname,
            'lastname': user lastname,
            'age': user age,
            'country': user country
        }
    '''
    results = user_data['results'][0]
    name = results['name']
    data = {
        'firstname': name['first'],
        'lastname': name['last'],
        'age': results['dob']['age'],
        'country': results['location']['country']
    }
    return data


def get_users(url: str, n: int) -> list:
    '''get n users from url
    
    Args:
        url (str): api url
        n (int): number of users
        
    Returns:
        list: list of users. user from get_user()
    '''
    users_data = []
    for i in range(n):
        r = requests.get(url)
        data = r.json()
        user = get_user(data)
        users_data.append(user)

    return users_data

def write_users_to_file(file_path: str, data:list):
    '''write n users to file

    Args:
        url (str): api url
        data (list): number of users
    '''
    with open(file_path, 'w') as f:
        data = json.dumps(data)
        f.write(data)
    
url = 'https://randomuser.me/api/'
data = get_users(url, 10)

write_users_to_file('result.json', data)