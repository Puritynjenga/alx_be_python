task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
# if priority == "low":
#     print("none")
# else:
#     print("okay") 
time = input("Is it time-bound? (yes/no): ").lower()



match priority:

    case "high":
            priority == "high"
    case "medium":
            priority == "medium"
    case "low" :  
            priority =="low"   
    case _:
            print("there is no such choice")

if time == "yes":
    print(f"Reminder:{task} is a high priority task that requires immediate  attention today!")   
else:
    print(f"Note:'{task}' is a low priority task. Consider completing it when you have free time. ")       

        





