import requests
import uuid

base_url = 'https://todo.pixegami.io/'

def create_task(user_id, content):
    task_data = {"user_id": user_id, "content": content, "is_done": False}
    response = requests.post(f"{base_url}/tasks", json=task_data)
    return response

def get_task(task_id):
    response = requests.get(f"{base_url}/tasks/{task_id}")
    return response

def test_create_task():
    user_id = str(uuid.uuid4()) 
    content = "Complete integration testing"
    response = create_task(user_id, content)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    
    if response.status_code == 200:
        task_id = response.json().get('id')
        if task_id:
            response = get_task(task_id)
            assert response.status_code == 200, "Failed to retrieve task after creation"
            assert response.json().get('content') == content, "Task content mismatch"
            assert response.json().get('user_id') == user_id, "Task user_id mismatch"
            assert response.json().get('is_done') is False, "Task is_done should be False"
            print("Create task test passed.")
        else:
            print("No task ID found in the response.")
    else:
        print("Failed to create task, cannot proceed with further actions.")

def update_task(task_id, new_content, new_status):
    task_data = {"content": new_content, "is_done": new_status}
    response = requests.patch(f"{base_url}/tasks/{task_id}", json=task_data)
    return response

def test_update_task():
    user_id = str(uuid.uuid4())
    content = "Initial task content"
    create_response = create_task(user_id, content)

    print("Create Task - Status Code:", create_response.status_code)
    print("Create Task - Response Body:", create_response.text)

    if create_response.status_code == 200:
        task_id = create_response.json().get('id')
        if task_id:
            new_content = "Updated content"
            new_status = True
            update_response = update_task(task_id, new_content, new_status)
            
            print("Update Task - Status Code:", update_response.status_code)
            print("Update Task - Response Body:", update_response.text)

            if update_response.status_code == 200:
                get_response = get_task(task_id)
                assert get_response.json().get('content') == new_content, "Content did not update"
                assert get_response.json().get('is_done') == new_status, "Status did not update"
                print("Update task test passed.")
            else:
                print("Failed to update task, cannot verify updates.")
        else:
            print("Task ID was not returned in creation response, cannot proceed with update test.")
    else:
        print("Failed to create task, cannot proceed with update test.")


def list_tasks(user_id):
    response = requests.get(f"{base_url}/tasks?user_id={user_id}")
    return response

def test_list_tasks():
    user_id = str(uuid.uuid4()) 
    for i in range(3):
        create_task(user_id, f"Task {i+1}")

    response = list_tasks(user_id)
    print("List Tasks - Status Code:", response.status_code)
    print("List Tasks - Response Body:", response.text)
    
    assert response.status_code == 200, "Failed to list tasks"
    tasks = response.json()
    assert len(tasks) == 3, "Number of tasks mismatch"

    print("List tasks test passed.")

def delete_task(task_id):
    response = requests.delete(f"{base_url}/tasks/{task_id}")
    return response

def test_delete_task():
    user_id = str(uuid.uuid4())
    content = "Task to be deleted"
    create_response = create_task(user_id, content)
    task_id = create_response.json()['id']

    delete_response = delete_task(task_id)
    assert delete_response.status_code == 200, "Failed to delete task"

    get_response = get_task(task_id)
    assert get_response.status_code == 404, "Task should not be found after deletion"

    print("Delete task test passed.")

if __name__ == "__main__":
    test_create_task()
    test_update_task()
    test_list_tasks()
    test_delete_task()
