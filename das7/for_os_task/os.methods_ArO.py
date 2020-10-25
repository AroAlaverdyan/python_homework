import os

print("we are here:", os.getcwd())

os.chdir("/Users/Artak/Desktop/for_os_task")
standart_place = os.getcwd()
print("Now here", os.getcwd())

os.makedirs("Dir1/Dir2")
os.makedirs(f"{os.getcwd()}/Dir1/Dir3/Dir4")

print("\nIn 'for_os_task' folder 'Dir1, Dir2, Dir3 and Dir4' folders have been created!!!")

def Dir4():
    directories_4 = "Dir4"
    location_4 = f"{standart_place}/Dir1/Dir3"
    path_4 = os.path.join(location_4, directories_4)
    os.rmdir(path_4)

def Dir3():
    directories_3 = "Dir3"
    location_3 = f"{standart_place}/Dir1"
    path_3 = os.path.join(location_3, directories_3)
    os.rmdir(path_3)

def Dir2():
    directories_2 = "Dir2"
    location_2 = f"{standart_place}/Dir1"
    path_2 = os.path.join(location_2, directories_2)
    os.rmdir(path_2)


yes_or_no = "\nUser, do you want to delete some directories or files?? yes/no\n"
question = "\nOkay, now choose which one do you want: Dir1, Dir2, Dir3, Dir4 or file1\n"
check = True
while check:
    try:
        my_input1 = input(yes_or_no)
        if my_input1 != "yes" and my_input1 != "no":
            raise ValueError("Please, give me CORRECT value for this question")
        check = False
    except ValueError as v:
        print(v)

if my_input1 == "no":
    print("Okay, I'll not delete anything")

    
while my_input1 == "yes":
    check = True
    while check:
        try:
            my_input2 = input(question)

            os.chdir("/Users/Artak/Desktop/for_os_task")
                
            if my_input2 == "Dir1":
                if os.path.exists(f"/Users/Artak/Desktop/for_os_task/{my_input2}") == False:
                    raise NameError(f"{my_input2} does not exist")      

            if my_input2 == "Dir2" or my_input2 == "Dir3":
                if os.path.exists(f"/Users/Artak/Desktop/for_os_task/Dir1/{my_input2}") == False:
                    raise NameError(f"{my_input2} does not exist")

            if my_input2 == "Dir4":
                if os.path.exists(f"/Users/Artak/Desktop/for_os_task/Dir1/Dir3/{my_input2}") == False:
                    raise NameError(f"{my_input2} does not exist")

            if my_input2 == "file1":
                if os.path.exists(f"/Users/Artak/Desktop/for_os_task/file1.txt") == False:
                    raise NameError(f"{my_input2} does not exist")

            check = False
            
        except NameError as n:
            print(n)
        
        
    if my_input2 == "Dir1":
        if os.path.exists("/Users/Artak/Desktop/for_os_task/Dir1/Dir3") == True:
            if os.path.exists("/Users/Artak/Desktop/for_os_task/Dir1/Dir3/Dir4") == True:
                Dir4()      
            Dir3()
        if os.path.exists("/Users/Artak/Desktop/for_os_task/Dir1/Dir2"):
            Dir2()
        
        os.chdir("/Users/Artak/Desktop/for_os_task")
        os.rmdir("Dir1")
        print("Dir1 has been deleted.")
        if os.path.exists("/Users/Artak/Desktop/for_os_task/file1.txt") == True:
            print("In 'for_os_task' folder is exist only 'file1'")

        

    elif my_input2 == "Dir2":
        
        Dir2()
        print("Dir2 has been deleted.")
        
    elif my_input2 == "Dir3":
        if os.path.exists("/Users/Artak/Desktop/for_os_task/Dir1/Dir3/Dir4") == True:
            Dir4()        
        
        Dir3()
        print("Dir3 has been deleted.")

    elif my_input2 == "Dir4":
        
        Dir4()
        print("Dir4 has been deleted.")

    elif my_input2 == "file1":
        file = "file1.txt"
        location = "/Users/Artak/Desktop/for_os_task"
        path = os.path.join(location, file)
        os.remove(path)
        print(f"{my_input2} has been deleted!!!")

    elif my_input2 != "file1" and "Dir4" and "Dir3" and "Dir2" and "Dir1":
        print(f"Sorry, but there's no {my_input2} file or folder in 'for_os_task'")
    
    if os.listdir("/Users/Artak/Desktop/for_os_task") == []:
        print("'for_os_task' folder is empty")
        break
    
        
    my_input1 = input(yes_or_no)