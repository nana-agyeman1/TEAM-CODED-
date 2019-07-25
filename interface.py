state = 0
no_of_pos = 0
pos = {}

def my_callback(candidate, label, countVote, button, led):
    led.on()
    button.when_released = led.off
    countVote.set(1 + countVote.get())
    label['text'] = candidate +" final results = " + str(countVote.get())
    label['font'] = '60'
    print ("\t"+ candidate +" final results = ", countVote.get())


def position_callback_maker(l_candidates, l_labels, l_counts, l_buttons, l_leds):
    out = []
    for i in range(0, len(l_candidates)):
        label = l_labels[i];
        candidate = l_candidates[i]
        countVote = l_counts[i]
        button = l_buttons[i]
        led = l_leds[i]

        lam = lambda i=candidate, j=label, k=countVote, l=button, m=led: my_callback(i,j,k,l,m)
        out.append(lam)
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
    return can_list
