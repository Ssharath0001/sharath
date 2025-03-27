class ToDolist:
    def __init__(self) :
         self.tasks=[]

    def add_task(self,task):
         self.tasks.append({"task":task,"done":False})
         print(f"the {task} are added sucessfully")


    # def remove_task(self,task):
    #     if task in self.tasks:
    #         self.tasks.remove(task)
    #         print(f"task{task} are removed successfully")
    #     else:
    #         print(f"task{task}- is not here")

    def remove_task(self,task):
        for t in self.tasks:
            if t["task"]==task: 
                self.tasks.remove(t)
                print("task are removed successfully")
            else:
                print("task- is not here")


    def display_tasks(self):
        if self.tasks:
            print("your todo list:")
            for index,task in enumerate(self.tasks,start=1):
                status="done" if task["done"] else "not done"
                print(f"{index} . {task["task"]} - {status}")
        else:
            print("your to do list is empty")


    def mark_complete(self,task):
        task_index=int(input("enter the task number to mark as done:"))
        if 0 <= task_index <len(self.tasks):
            self.tasks[task_index]["done"]=True
            print("task marked as done!")
        else:
            print("invalid task number")



def main():
    todo_list=ToDolist()

    while True: 
        print("\n\nenter the choice")
        print("1.add the task")
        print("2.remove the task")
        print("3.display the tasks")
        print("4.mark the task done")
        print("5.exist")

        option=(input("enter the choice:"))

        if option=="1":
            task=input("enter the task add:")
            todo_list.add_task(task)

        elif option=="2":
            task=input("remove the task:")
            todo_list.remove_task(task)

        elif option=="3":
            todo_list.display_tasks()

        elif option=="4":
            todo_list.mark_complete(task)

        elif option=="5":
            print("exist the app")

        else:
            print("enter the corrrect option")
main()
