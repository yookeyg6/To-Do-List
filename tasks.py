def load_task():
    try:
        with open("tasks.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def load_done():
    try:
        with open("done_tasks.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
    
def show_task(tasks):
    if len(tasks) > 0:
        print("Список задач: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) {task.strip()}")
    else:
        print("Список задач пуст.")
        
def add_task(tasks):
    task = input("Добавьте новую задачу: ")
    tasks.append(task)
    print("Задача добавлена.")
    return tasks
    
def delete_task(tasks):
    show_task(tasks)
    if len(tasks) == 0:
        return tasks
    else: 
        num = int(input("Выберите задачу для удаления: "))
        tasks.pop(num - 1)
        save_task(tasks)
        print("Задача удалена.")
        return tasks

def save_task(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task.strip() + "\n")

def show_done(done_tasks):
    if len(done_tasks) > 0:
        print("Выполненные задачи:")
        for i, task in enumerate(done_tasks, 1):
            print(f"{i}) {task.strip()}")
    else:
        print("Выполненных задач нет.")

def done_task(tasks, done_tasks):
    show_task(tasks)
    if len(tasks) == 0:
        return tasks, done_tasks
    num = int(input("Выберите выполненную задачу: "))
    done = tasks.pop(num - 1)
    done_tasks.append(done)

    print("Задача отмечена как выполненная.")
    return tasks, done_tasks
        
def save_done(done_tasks):
    with open("done_tasks.txt", "w") as file:
        for task in done_tasks:
            file.write(task.strip() + "\n")

def main():
    tasks = load_task()
    done_tasks = load_done()
    while True: 
        print("\n\t To-Do List \t")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Удалить задачу")
        print("4. Выполненные задачи")
        print("5. Сохранить и выйти")
        
        choice = input("Выберите действие: ")
        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
            save_task(tasks)
        elif choice == "3":
            tasks = delete_task(tasks)
            save_task(tasks)
        elif choice == "4":
            show_done(done_tasks)
            print("\nОтметить задачу как выполненную?")
            print("1 - Да \t 2 - Нет")
            answer = input()            
            if answer == "1":
                tasks, done_tasks = done_task(tasks, done_tasks)
                save_task(tasks)
                save_done(done_tasks)
        elif choice == "5":
            save_task(tasks)
            save_done(done_tasks)
            print("Выход.")
            break

main()