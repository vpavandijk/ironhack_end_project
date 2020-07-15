# import libraries
import numpy as np

# defining the states:
location_to_state = {'Depot':0, 'A.a':1, 'A.b':2, 'A.10.1':3, 'A.11.1':4, 'A.10.2':5, 'A.11.2':6, 'A.10.3':7, 'A.11.3':8, 'A.10.4':9, 'A.11.4':10, 'A.c':11, 'A.d':12, 'A.12.1':13, 'A.13.1':14, 'A.12.2':15, 'A.13.2':16, 'A.12.3':17, 'A.13.3':18, 'A.12.4':19, 'A.13.4':20, 'A.e':21, 'A.f':22, 'B.a':23, 'B.b':24, 'B.10.1':25, 'B.11.1':26, 'B.10.2':27, 'B.11.2':28, 'B.10.3':29, 'B.11.3':30, 'B.10.4':31, 'B.11.4':32, 'B.c':33, 'B.d':34, 'B.12.1':35, 'B.13.1':36, 'B.12.2':37, 'B.13.2':38, 'B.12.3':39, 'B.13.3':40, 'B.12.4':41, 'B.13.4':42, 'B.e':43, 'B.f':44, 'C.a':45, 'C.b':46, 'C.10.1':47, 'C.11.1':48, 'C.10.2':49, 'C.11.2':50, 'C.10.3':51, 'C.11.3':52, 'C.10.4':53, 'C.11.4':54, 'C.c':55, 'C.d':56, 'C.12.1':57, 'C.13.1':58, 'C.12.2':59, 'C.13.2':60, 'C.12.3':61, 'C.13.3':62, 'C.12.4':63, 'C.13.4':64, 'C.e':65, 'C.f':66}

# making the dictionary to transform states back to locations:
state_to_location = {state: location for location, state in location_to_state.items()}

# defining the actions (in this case the same as states as we can go to any location from any location:
actions = [i for i in range(len(location_to_state))]

# Create a 2D numpy array to hold the rewards for each state.
# The array contains 67 rows and 67 columns (to match the shape of the environment), and each value is initialized to 0.
# Option would be to make it a 3D array. 12 times 6 for all locations and 72 for all actions. (Would need to make the DEPOT six locations....)
R = np.zeros((len(location_to_state), len(actions)))

#define possible moves from every state. If move is possible (so in that state I can take that action) a 1 will be filled in the Rewards table.
aisles = {}
aisles[0] = [1, 2, 23, 24, 45, 46]
aisles[1] = [0, 2, 3, 24]
aisles[2] = [0, 1, 4]
aisles[3] = [1, 4, 5]
aisles[4] = [2, 3, 6]
aisles[5] = [3, 6, 7]
aisles[6] = [4, 5, 8]
aisles[7] = [5, 8, 9]
aisles[8] = [6, 7, 10]
aisles[9] = [7, 10, 11]
aisles[10] = [8, 9, 12]
aisles[11] = [9, 12, 13, 34]
aisles[12] = [10, 11, 14]
aisles[13] = [11, 14, 15]
aisles[14] = [12, 13, 16]
aisles[15] = [13, 16, 17]
aisles[16] = [14, 15, 18]
aisles[17] = [15, 18, 19]
aisles[18] = [16, 17, 20]
aisles[19] = [17, 20, 21]
aisles[20] = [18, 19, 22]
aisles[21] = [19, 22, 44]
aisles[22] = [20, 21]
aisles[23] = [0, 24, 25, 46]
aisles[24] = [0, 1, 23, 26]
aisles[25] = [23, 26, 27]
aisles[26] = [24, 25, 28]
aisles[27] = [25, 28, 29]
aisles[28] = [26, 27, 30]
aisles[29] = [27, 30, 31]
aisles[30] = [28, 29, 32]
aisles[31] = [29, 32, 33]
aisles[32] = [30, 31, 34]
aisles[33] = [31, 34, 35, 56]
aisles[34] = [11, 32, 33, 36]
aisles[35] = [33, 36, 37]
aisles[36] = [34, 35, 38]
aisles[37] = [35, 38, 39]
aisles[38] = [36, 37, 40]
aisles[39] = [37, 40, 41]
aisles[40] = [38, 39, 42]
aisles[41] = [39, 42, 43]
aisles[42] = [40, 41, 44]
aisles[43] = [41, 44, 66]
aisles[44] = [21, 42, 43]
aisles[45] = [0, 46, 47]
aisles[46] = [0, 23, 45, 48]
aisles[47] = [45, 48, 49]
aisles[48] = [46, 47, 50]
aisles[49] = [47, 50, 51]
aisles[50] = [48, 49, 52]
aisles[51] = [49, 52, 53]
aisles[52] = [50, 51, 54]
aisles[53] = [51, 54, 55]
aisles[54] = [52, 53, 56]
aisles[55] = [53, 56, 57]
aisles[56] = [33, 54, 55, 58]
aisles[57] = [55, 58, 59]
aisles[58] = [56, 57, 60]
aisles[59] = [57, 60, 61]
aisles[60] = [58, 59, 62]
aisles[61] = [59, 62, 63]
aisles[62] = [60, 61, 64]
aisles[63] = [61, 64, 65]
aisles[64] = [62, 63, 66]
aisles[65] = [63, 66]
aisles[66] = [43, 64, 65]

#set the rewards for all possible actions to 1
for row_index in range(len(location_to_state)):
    for column_index in aisles[row_index]:
        R[row_index, column_index] = 1.

# The Q-learning

episodes = 5000
discount_factor = 0.75 # also called gamma
learning_rate = 0.8 # also called alpha

# This function contains the actual Reinforcement Q learning model.
def route(starting_location, ending_location): # input is a start location and a end location.
    R_new = np.copy(R) # copy made of the Rewards table
    ending_state = location_to_state[ending_location] #transform the ending_location to a state number
    R_new[ending_state, ending_state] = 100 # seting the ending state Reward to 100 (this makes sure the route will go there for sure)
    Q = np.zeros((len(location_to_state), len(actions))) # initializing a Q table filled with zeros
    for i in range(episodes): # go throught the Q learning process (updating the table) This starts 5000 times as the settings say now!
        current_state = np.random.randint(len(location_to_state)) # Start at a random state
        playable_actions = []
        for j in range(len(actions)): # go throug all actions for that state
            if R_new[current_state, j] > 0: # if Q-value for that state/action combination is higher than 0, this makes sure we only update Q values that are with actions that are allowed (so not through wall etc.)
                playable_actions.append(j) # list of possible actions for that state
        next_state = np.random.choice(playable_actions) # after building the list of possible actions a random one is chose. So this also decides what the next state will be!
        TD = R_new[current_state, next_state] + discount_factor * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state] # calculating the temporal difference
        Q[current_state, next_state] = Q[current_state, next_state] + learning_rate * TD # updating the Q table
    route_total = [starting_location] # initializing the route output, always starts with starting_location
    next_location = starting_location # initializing next_location variable
    while (next_location != ending_location): # as long as next_location variable is NOT ending location
        starting_state = location_to_state[starting_location] # change starting_location variable to state number
        next_state = np.argmax(Q[starting_state,]) #look in Q table for highest Q value for that state, so action is defined, so next state is defined
        next_location = state_to_location[next_state] # transform next state to location
        route_total.append(next_location) #append next location to list route
        starting_location = next_location # next location become start for while loop
    return route_total # output total route

# defining the start and end point for all routes:
start_location = 'Depot'
end_location = 'Depot'

# function for route with 1 pick location:
def best_route_1(starting_location, intermediary_location, ending_location):
    return route(starting_location, intermediary_location) + route(intermediary_location, ending_location)[1:]

# function for route with 2 pick locations:
def best_route_2(starting_location, intermediary_location_1, intermediary_location_2, ending_location):
    route_1 = route(starting_location, intermediary_location_1) + route(intermediary_location_1, intermediary_location_2)[1:] +route(intermediary_location_2, ending_location)[1:]
    route_2 = route(starting_location, intermediary_location_2) + route(intermediary_location_2, intermediary_location_1)[1:] +route(intermediary_location_1, ending_location)[1:]
    if len(route_1) < len(route_2):
        route_best = route_1
    else:
        route_best = route_2
    return route_best

# function for route with 3 pick locations:
def best_route_3(start_loc, int_loc_1, int_loc_2, int_loc_3, end_loc):
    route_1 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    route_best = route_1
    route_2 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_2) < len(route_best):
        route_best = route_2
    route_3 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_3) < len(route_best):
        route_best = route_3
    route_4 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_4) < len(route_best):
        route_best = route_4
    route_5 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_5) < len(route_best):
        route_best = route_5
    route_6 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_6) < len(route_best):
        route_best = route_6
    return route_best

# function for route with 4 pick locations:
def best_route_4(start_loc, int_loc_1, int_loc_2, int_loc_3, int_loc_4, end_loc):
    route_1 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    route_best = route_1
    route_2 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_2) < len(route_best):
        route_best = route_2
    route_3 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_3) < len(route_best):
        route_best = route_3
    route_4 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_4) < len(route_best):
        route_best = route_4
    route_5 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_5) < len(route_best):
        route_best = route_5
    route_6 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_6) < len(route_best):
        route_best = route_6
    route_7 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_7) < len(route_best):
        route_best = route_7
    route_8 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_8) < len(route_best):
        route_best = route_8
    route_9 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_9) < len(route_best):
        route_best = route_9
    route_10 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_10) < len(route_best):
        route_best = route_10
    route_11 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_11) < len(route_best):
        route_best = route_11
    route_12 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_12) < len(route_best):
        route_best = route_12
    route_13 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_13) < len(route_best):
        route_best = route_13
    route_14 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_14) < len(route_best):
        route_best = route_14
    route_15 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_15) < len(route_best):
        route_best = route_15
    route_16 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_16) < len(route_best):
        route_best = route_16
    route_17 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_17) < len(route_best):
        route_best = route_17
    route_18 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_18) < len(route_best):
        route_best = route_18
    route_19 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_19) < len(route_best):
        route_best = route_19
    route_20 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_20) < len(route_best):
        route_best = route_20
    route_21 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_21) < len(route_best):
        route_best = route_21
    route_22 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_22) < len(route_best):
        route_best = route_22
    route_23 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_23) < len(route_best):
        route_best = route_23
    route_24 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_24) < len(route_best):
        route_best = route_24
    return route_best

# function for route with 5 pick locations:
def best_route_5(start_loc, int_loc_1, int_loc_2, int_loc_3, int_loc_4, int_loc_5, end_loc):
    route_1 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    route_best = route_1
    route_2 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_2) < len(route_best):
        route_best = route_2
    route_3 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] +  route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_3) < len(route_best):
        route_best = route_3
    route_4 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_4) < len(route_best):
        route_best = route_4
    route_5 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_5) < len(route_best):
        route_best = route_5
    route_6 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_6) < len(route_best):
        route_best = route_6
    route_7 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_7) < len(route_best):
        route_best = route_7
    route_8 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_8) < len(route_best):
        route_best = route_8
    route_9 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_9) < len(route_best):
        route_best = route_9
    route_10 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_10) < len(route_best):
        route_best = route_10
    route_11 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_11) < len(route_best):
        route_best = route_11
    route_12 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_12) < len(route_best):
        route_best = route_12
    route_13 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_13) < len(route_best):
        route_best = route_13
    route_14 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_14) < len(route_best):
        route_best = route_14
    route_15 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_15) < len(route_best):
        route_best = route_15
    route_16 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_16) < len(route_best):
        route_best = route_16
    route_17 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_17) < len(route_best):
        route_best = route_17
    route_18 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_18) < len(route_best):
        route_best = route_18
    route_19 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_19) < len(route_best):
        route_best = route_19
    route_20 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_20) < len(route_best):
        route_best = route_20
    route_21 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_21) < len(route_best):
        route_best = route_21
    route_22 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_22) < len(route_best):
        route_best = route_22
    route_23 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_23) < len(route_best):
        route_best = route_23
    route_24 = route(start_loc, int_loc_1) + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_24) < len(route_best):
        route_best = route_24
    route_25 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_25) < len(route_best):
        route_best = route_25
    route_26 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_26) < len(route_best):
        route_best = route_26
    route_27 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] +  route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_27) < len(route_best):
        route_best = route_27
    route_28 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_28) < len(route_best):
        route_best = route_28
    route_29 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_29) < len(route_best):
        route_best = route_29
    route_30 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_30) < len(route_best):
        route_best = route_30
    route_31 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_31) < len(route_best):
        route_best = route_31
    route_32 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_32) < len(route_best):
        route_best = route_32
    route_33 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_33) < len(route_best):
        route_best = route_33
    route_34 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_34) < len(route_best):
        route_best = route_34
    route_35 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_35) < len(route_best):
        route_best = route_35
    route_36 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_36) < len(route_best):
        route_best = route_36
    route_37 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_37) < len(route_best):
        route_best = route_37
    route_38 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_38) < len(route_best):
        route_best = route_38
    route_39 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_39) < len(route_best):
        route_best = route_39
    route_40 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_40) < len(route_best):
        route_best = route_40
    route_41 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_41) < len(route_best):
        route_best = route_41
    route_42 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_42) < len(route_best):
        route_best = route_42
    route_43 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_43) < len(route_best):
        route_best = route_43
    route_44 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_44) < len(route_best):
        route_best = route_44
    route_45 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_45) < len(route_best):
        route_best = route_45
    route_46 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_46) < len(route_best):
        route_best = route_46
    route_47 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_47) < len(route_best):
        route_best = route_47
    route_48 = route(start_loc, int_loc_2) + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_48) < len(route_best):
        route_best = route_48
    route_49 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_49) < len(route_best):
        route_best = route_49
    route_50 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_50) < len(route_best):
        route_best = route_50
    route_51 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] +  route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_51) < len(route_best):
        route_best = route_51
    route_52 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_52) < len(route_best):
        route_best = route_52
    route_53 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_53) < len(route_best):
        route_best = route_53
    route_54 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_54) < len(route_best):
        route_best = route_54
    route_55 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_55) < len(route_best):
        route_best = route_55
    route_56 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_56) < len(route_best):
        route_best = route_56
    route_57 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_57) < len(route_best):
        route_best = route_57
    route_58 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_58) < len(route_best):
        route_best = route_58
    route_59 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_59) < len(route_best):
        route_best = route_59
    route_60 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_60) < len(route_best):
        route_best = route_60
    route_61 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_61) < len(route_best):
        route_best = route_61
    route_62 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_62) < len(route_best):
        route_best = route_62
    route_63 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_63) < len(route_best):
        route_best = route_63
    route_64 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_64) < len(route_best):
        route_best = route_64
    route_65 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_65) < len(route_best):
        route_best = route_65
    route_66 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_66) < len(route_best):
        route_best = route_66
    route_67 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_67) < len(route_best):
        route_best = route_67
    route_68 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_68) < len(route_best):
        route_best = route_68
    route_69 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_69) < len(route_best):
        route_best = route_69
    route_70 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_70) < len(route_best):
        route_best = route_70
    route_71 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_71) < len(route_best):
        route_best = route_71
    route_72 = route(start_loc, int_loc_3) + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_72) < len(route_best):
        route_best = route_72
    route_73 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_73) < len(route_best):
        route_best = route_73
    route_74 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_74) < len(route_best):
        route_best = route_74
    route_75 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] +  route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_75) < len(route_best):
        route_best = route_75
    route_76 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_76) < len(route_best):
        route_best = route_76
    route_77 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_77) < len(route_best):
        route_best = route_77
    route_78 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_78) < len(route_best):
        route_best = route_78
    route_79 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_7) < len(route_best):
        route_best = route_7
    route_80 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_80) < len(route_best):
        route_best = route_80
    route_81 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_81) < len(route_best):
        route_best = route_81
    route_82 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_82) < len(route_best):
        route_best = route_82
    route_83 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_83) < len(route_best):
        route_best = route_83
    route_84 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_84) < len(route_best):
        route_best = route_84
    route_85 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_85) < len(route_best):
        route_best = route_85
    route_86 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_86) < len(route_best):
        route_best = route_86
    route_87 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_5)[1:] + route(int_loc_5, end_loc)[1:]
    if len(route_87) < len(route_best):
        route_best = route_87
    route_88 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_88) < len(route_best):
        route_best = route_88
    route_89 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_89) < len(route_best):
        route_best = route_89
    route_90 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_90) < len(route_best):
        route_best = route_90
    route_91 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_91) < len(route_best):
        route_best = route_91
    route_92 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_92) < len(route_best):
        route_best = route_92
    route_93 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_93) < len(route_best):
        route_best = route_93
    route_94 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_94) < len(route_best):
        route_best = route_94
    route_95 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_95) < len(route_best):
        route_best = route_95
    route_96 = route(start_loc, int_loc_4) + route(int_loc_4, int_loc_5)[1:] + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_96) < len(route_best):
        route_best = route_96
    route_97 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_97) < len(route_best):
        route_best = route_97
    route_98 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_98) < len(route_best):
        route_best = route_98
    route_99 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] +  route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_99) < len(route_best):
        route_best = route_99
    route_100 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_100) < len(route_best):
        route_best = route_100
    route_101 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_101) < len(route_best):
        route_best = route_101
    route_102 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_102) < len(route_best):
        route_best = route_102
    route_103 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_103) < len(route_best):
        route_best = route_103
    route_104 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_104) < len(route_best):
        route_best = route_104
    route_105 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_105) < len(route_best):
        route_best = route_105
    route_106 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_106) < len(route_best):
        route_best = route_106
    route_107 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_107) < len(route_best):
        route_best = route_107
    route_108 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_108) < len(route_best):
        route_best = route_108
    route_109 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_109) < len(route_best):
        route_best = route_109
    route_110 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_110) < len(route_best):
        route_best = route_110
    route_111 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_4)[1:] + route(int_loc_4, end_loc)[1:]
    if len(route_111) < len(route_best):
        route_best = route_111
    route_112 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_112) < len(route_best):
        route_best = route_112
    route_113 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_113) < len(route_best):
        route_best = route_113
    route_114 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_3)[1:] + route(int_loc_3, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_114) < len(route_best):
        route_best = route_114
    route_115 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_115) < len(route_best):
        route_best = route_115
    route_116 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_116) < len(route_best):
        route_best = route_116
    route_117 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, int_loc_3)[1:] + route(int_loc_3, end_loc)[1:]
    if len(route_117) < len(route_best):
        route_best = route_117
    route_118 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_2)[1:] + route(int_loc_2, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_118) < len(route_best):
        route_best = route_118
    route_119 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_1)[1:] + route(int_loc_1, int_loc_2)[1:] + route(int_loc_2, end_loc)[1:]
    if len(route_119) < len(route_best):
        route_best = route_119
    route_120 = route(start_loc, int_loc_5) + route(int_loc_5, int_loc_4)[1:] + route(int_loc_4, int_loc_3)[1:] + route(int_loc_3, int_loc_2)[1:] + route(int_loc_2, int_loc_1)[1:] + route(int_loc_1, end_loc)[1:]
    if len(route_120) < len(route_best):
        route_best = route_120                                                                                                                   
    return route_best


# function to decide which ROUTE function needs to be used:
def best_route(l):
    if len(l) == 1:
        return best_route_1(start_location, l[0], end_location)
    elif len(l) == 2:
        return best_route_2(start_location, l[0], l[1], end_location)
    elif len(l) == 3:
        return best_route_3(start_location, l[0], l[1], l[2], end_location)
    elif len(l) == 4:
        return best_route_4(start_location, l[0], l[1], l[2], l[3], end_location)
    elif len(l) == 5:
        return best_route_5(start_location, l[0], l[1], l[2], l[3], l[4], end_location)

# start function. Gives the option to input to five different pick locations:
def start():
    print('Welcome, here you can select picklocations.')
    location = input('Select a picklocation: ')
    location = str(location.upper())
    location_list = []
    location_list.append(location)
    test = input('Do you want to select another picklocation? (y/n): ')
    test = test.upper()
    if test == 'Y':
        location_2 = input('Select a second picklocation: ')
        location_2 = str(location_2.upper())
        location_list.append(location_2)
        test_2 = input('Do you want to select another picklocation? (y/n): ')
        test_2 = test_2.upper()
        if test_2 == 'Y':
            location_3 = input('Select third picklocation: ')
            location_3 = str(location_3.upper())
            location_list.append(location_3)
            test_3 = input('Do you want to select another picklocation? (y/n): ')
            test_3 = test_3.upper()
            if test_3 == 'Y':
                location_4 = input('Select fourth picklocation: ')
                location_4 = str(location_4.upper())
                location_list.append(location_4)
                test_4 = input('Do you want to select another picklocation? (y/n): ')
                test_4 = test_4.upper()
                if test_4 == 'Y':
                    location_5 = input('Select fifth (and last) picklocation: ')
                    location_5 = str(location_5.upper())
                    location_list.append(location_5)
                    print(f'Thanks for selecting! These are the five locations included in this pickround {location_list}')
                    print(f'We will now calculate the shortest route!')
                    print('\n')
                    output_route = best_route(location_list)
                    print(f'The shortest route is: {output_route}.')
                    print('\n')
                    print(f'The length of this route is: {len(output_route)}.')
                else:
                    print(f'Thanks, these are the four locations included in this pickround {location_list}')
                    print(f'We will now calculate the shortest route!')
                    print('\n')
                    output_route = best_route(location_list)
                    print(f'The shortest route is: {output_route}.')
                    print('\n')
                    print(f'The length of this route is: {len(output_route)}.')
            else:
                print(f'Thanks, these are the three locations included in this pickround {location_list}')
                print(f'We will now calculate the shortest route!')
                print('\n')
                output_route = best_route(location_list)
                print(f'The shortest route is: {output_route}.')
                print('\n')
                print(f'The length of this route is: {len(output_route)}.')
        else:
            print(f'Thanks, these are the two locations included in this pickround {location_list}')
            print(f'We will now calculate the shortest route!')
            print('\n')
            output_route = best_route(location_list)
            print(f'The shortest route is: {output_route}.')
            print('\n')
            print(f'The length of this route is: {len(output_route)}.')
    else:
        print(f'Thanks, this is the location included in this pickround {location_list}')
        print(f'We will now calculate the shortest route!')
        print('\n')
        output_route = best_route(location_list)
        print(f'The shortest route is: {output_route}.')
        print('\n')
        print(f'The length of this route is: {len(output_route)}.')

start() # to start the route making:
