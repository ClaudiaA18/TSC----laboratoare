import requests

def get_marks():
    r = requests.get('http://localhost/api/note')
    if r.status_code == 200:
        return r.json()
    return None