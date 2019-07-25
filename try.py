state = 0
no_of_pos = 0
pos = {}

def setupMachine():
    global state

    no_of_pos = int(input("Enter number of positions:"))
    for i in range(no_of_pos):
        name = input("Enter position name:")
        can = int(input("Enter number of candidates:"))
        can_list = {}
        for j in range(can):
            can_name = input("Enter name of candidate number " + str(j + 1) + ":")
            can_list[j] = can_name
        pos[name] = can_list    
    state = 1
    print(state)
    print("Setup successful")

setupMachine()