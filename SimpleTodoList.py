class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

todo = TodoList()
todo.add_task("Do laundry")
todo.add_task("Buy groceries")
todo.view_tasks()