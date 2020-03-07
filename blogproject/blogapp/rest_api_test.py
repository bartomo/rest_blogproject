import json
import requests
import pprint

url = "http://localhost:8000/api/entry/"
payload = {
    'title': 'post_test',
    'content': 'post_test content',
    'category': 'post json',
    'user_name': 'rest_api',
}
headers = {'content-type': 'application/json'}

test_url = 'http://127.0.0.1:5000/'

def get_by_rest(target_url, item_data):
    try:
        response = requests.post(target_url, headers=headers, json=item_data)
        # response = requests.get(target_url)
        result = response.json()
        pprint.pprint(result)
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    get_by_rest(url, payload)

