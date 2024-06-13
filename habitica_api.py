import requests

class HabiticaAPI:
    def __init__(self, user_id, api_token):
        self.base_url = 'https://habitica.com/api/v3'
        self.headers = {
            'x-client': 'your-client-id',  
            'x-api-user': user_id,
            'x-api-key': api_token
        }

    def get_user(self):
        response = requests.get(f'{self.base_url}/user', headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_tasks(self):
        response = requests.get(f'{self.base_url}/tasks/user', headers=self.headers)
        response.raise_for_status()
        return response.json()['data']

    def create_task(self, task):
        response = requests.post(f'{self.base_url}/tasks/user', json=task, headers=self.headers)
        response.raise_for_status()
        return response.json()['data']
