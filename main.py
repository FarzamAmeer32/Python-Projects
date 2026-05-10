from calculator import make_calculation
from to_do_app import ToDoList

print("1. Calculator")
print("2. To-Do App")

choice = input("Choose option: ")

if choice == "1":
    make_calculation()
elif choice == "2":
    obj = ToDoList()
    obj.Dashboard()