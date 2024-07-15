def display_options():
        print("To-Do List Menu")
        print("1. Add a Task")
        print("2. View a Task")
        print("3. Delete Task")
        print("4. Exit")
        
def view_tasks(list):
    if list:
        print("To-do List")
        for i, task in enumerate(list,start=1):
            print(f"{i}. {task}")
    else:
        print("No items in ur list lol")


def add_task(list):
    task = input("Enter the task: ")
    if task:
        list.append(task)
        print(f"{task} has been added")
    else:
        print("Enter a valid task")

def delete_task(list):
    view_tasks(list)  # Display current tasks with indices
    if list:
        try:
            index = int(input("Enter the index of the task to delete: "))
            if 1 <= index <= len(list):
                deleted_task = list.pop(index - 1)
                print(f"Task '{deleted_task}' has been deleted")
            else:
                print("Invalid index. No task deleted.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No items in your list")
               
def main():
    list =[]
    while True:
        display_options()
        option = input("Choose an Option: ")
        if option == "1":
            add_task(list)
        elif option == "2":
            view_tasks(list)
        elif option == "3":
            delete_task(list)
        elif option =="4":
            print("Exiting the program")
        else: 
             print("invalid option, choose again")
                
if __name__ == "__main__":
    main()