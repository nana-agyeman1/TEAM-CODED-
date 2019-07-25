ostate = 0
no_of_pos = 0
pos = {}


def position_callback_maker(l_candidates, l_labels, l_counts):
    out = []
    for i in xrange(0, len(l_candidates)):
        label = l_labels[i];
        candidate = l_candidates[i]
        countVote = l_counts[i]
        
        def my_callback():
            label['text'] = candidate +" final results = " + str(countVote.get())
            label['font'] = '60'
            print ("\t"+ candidate +" final results = ", countVote.get())
            
        out.push(my_callback)
    return out

def setupMachine():
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