tasks = [] 

def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False}) 
    print(f"Đã thêm công việc: '{task_name}'.")

def list_tasks():
    
    if not tasks:
        print("\n--- Danh sách công việc trống ---")
        return

    print("\n--- Danh sách công việc ---")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['name']}") 

if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà") 
    list_tasks()
