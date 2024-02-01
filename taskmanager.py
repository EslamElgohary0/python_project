"""(task manager)
1: make user to add tasks
2:make user to sign at the complete task
3-show the task isn't complete
4-exit the program"""
print("&& wlecome to the tasks manager &&")
# make func to add
def add_tasks():
    global list_task
    list_task=input("please add your tasks:").strip().lower().split(",")
    print(f"your task list is {list_task}")
#sign com task func
def sign_com_tasks():
    print(f"your task list is {list_task}")
    number_taskscom=int(input("please enter how many task is completed: "))
    print("nice! keep going")
    x=0
    while x<number_taskscom:
        task_com=input("please enter a task completed: ").lower().strip()
        try:
         list_task.remove(task_com)
        except:
            print("you enter a item that is't here\nplease try again")
            break
        x +=1
    print(f"remender tasks is {list_task}") 

#show task func
def show_tasks():
    try:
     print(f"you task list is{list_task}")
    except:
        print("there are't list")
# the func that code start in here
while True:
    print("""  
          1-add a tasks
          2-sign at the complete task
          3-show the task isn't complete
          4-exit the program""")
    the_choice=input("please enter your choice:").strip()
    if the_choice=="1":
        add_tasks()
    elif the_choice=="2":
        sign_com_tasks()
    elif the_choice=="3":
        show_tasks()
    elif the_choice=="4":
        print("the program end.")
        break
    else:
        print("you choice a incorrect number please enter number fron 1 to 4")
