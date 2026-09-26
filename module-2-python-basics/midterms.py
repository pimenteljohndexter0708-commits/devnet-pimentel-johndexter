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

    pass

def add_device(name, ip):
    # ask for name, IP, status — build the string, add to the list

    name = input("Enter your name: ")
    ip = float("Enter your IP address")

    status = f"Name: {name}, IP: {ip}"

    devices.append(status)

    return
    pass

def view_devices(device_list):
    # loop through and print every device — handle empty list
    pass

def count_active_inactive(device_list):
    # loop through, count Active vs Inactive, return both
    pass

def find_device(device_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_device(device_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()

        opt = int(input("Choose an option: "))

        if opt == 1:
            add_device()
        elif opt == 2:
            view_devices()
        elif opt == 3:
            count_active_inactive()
        elif opt == 4:
            find_device()
        else:
            exit
        break
        # use if/elif to call the right function based on choice
        # set running = False when the user picks Exit

main()