"""
Midterm Practical Exam — Network Device Inventory Tool
Student:Pimentel, John Dexter A.
"""

devices = []  # starts empty — the user adds devices as the program runs

def display_menu():
    # print the menu, return the user's choice

    # inventory = ["Add a device", "View all devices", "Count active vs inactive devices", "Find a device by name", "Exit"]
    # for laman in inventory:
    #     print(laman)
    #     break

    print("1. Add a device")
    print("2. View all devices")
    print("3. Count active vs Inactive devices")
    print("4. Find a device by name")
    print("5. Exit")


def add_device(device_list):
    # ask for name, IP, status — build the string, add to the list

    name = input("Enter your name: ")
    ip = float(input("Enter your IP address: "))

    status = f"Name: {name}, IP: {ip}"

    devices.append(status)

def view_devices(device_list):
    # loop through and print every device — handle empty list

    for device in devices:
        for i in range(1):
            print(i, ":",  device)

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"

    name = input("Enter the name you want to find: ")

    isthere = name in devices

    if name in devices:
        print("Found")
    else:
        print("Not found")


# BONUS (optional)
def remove_device(device_list):

    rem = input("What do you want to remove? ")

    if rem  in devices:
        devices.remove(rem)
    else:
        print("Not found")


def main():
    running = True
    while running:
        choice = display_menu()

        opt = int(input("Choose an option: "))

        if opt == 1:
            devices.append(add_device(devices))
        
            main()
    
        elif opt == 2:
            view_devices(devices)
            main()
        elif opt == 3:
            count_active_inactive()
        elif opt == 4:
            find_device(devices)
        elif opt == 5:
            remove_device(devices)
        else:
            exit
        break
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit
main()
