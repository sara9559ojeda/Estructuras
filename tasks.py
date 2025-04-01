class Task:
    def __init__(self, title, description, date, status, reminder):
        self.title = title
        self.description = description
        self.date = date
        self.status = status
        self.reminder = reminder
        self.next = None  

class TaskList:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def add_task(self, task):
        if self.first_node is None:
            self.first_node = task
            self.last_node = task
        else:
            self.last_node.next = task
            self.last_node = task

    def show_tasks(self):
        current_node = self.first_node  # Se recorre desde el primer nodo
        while current_node is not None:
            print("Title:", current_node.title)
            print("Description:", current_node.description)
            print("Date:", current_node.date)
            print("Status:", current_node.status)
            print("Reminder:", current_node.reminder)
            print("----------------------------")
            current_node = current_node.next  


tasks_list = TaskList()

while True:

    tittle = input("ingrese el titulo ")
    description = input("ingrese la descripcion ")
    date = input("ingrese la fecha de entrega ")
    status = input("ingrese el estado de su tarea ")
    reminder = input("recordatorio ")
    task1 = Task(tittle, description, date, status, reminder)


    tasks_list.add_task(task1)

    if input("Agregar otra tarea? s/n ") != "s":
        break

tasks_list.show_tasks()
