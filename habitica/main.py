from habitica_api import HabiticaAPI

def main():
    user_id = '2827f1e4-ac3c-4438-ba78-b85a371ce140'
    api_token = '77f50e16-b072-42e8-b923-8fe3d5f61e69'

    habitica = HabiticaAPI(user_id, api_token)

    #grabbing user information
    user = habitica.get_user()
    print("User Info:", user)

    #grabbing tasks
    tasks = habitica.get_tasks()
    print("Tasks:", tasks)

    #creating a new task
    new_task = {
        "text": "New Habitica Task",
        "type": "todo",
        "notes": "This is a test task."
    }
    created_task = habitica.create_task(new_task)
    print("Created Task:", created_task)

if __name__ == '__main__':
        main()
