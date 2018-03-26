import sys
import random

def free_time_intervals(interval_lst, T):

    interval_lst_sorted = sorted(interval_lst) # sorts in Theta(n*log(n)) time

    t = 0
    return_lst = []

    while (interval_lst_sorted):

        (a, b) = interval_lst_sorted.pop(0)

        if (a > T): # break loop if 'a' is greater than T
            break

        if (t < a): # check conditon for free time interval
            return_lst.append((t, a))

        if (t < b): # keep the farther logout time
            t = b

    if (t < T):
        return_lst.append((t, T))

    return return_lst



def max_logged_in(interval_lst, T):

    timeline = [] # array containing elements with time value and login(+1) / logout(-1) data

    for i in interval_lst:
        timeline.append((i[0], +1))
        timeline.append((i[1], -1))

    timeline.sort() # sorts in Theta(n*log(n)) time

    users = 0 # current number of users
    max_n = 0 # max_logged_in_num
    max_t = 0 # max_logged_in_time

    for i in timeline:

        if (i[0] > T): # exit look if current time is greater than T
            break

        users = users + i[1]

        if (users > max_n):
            max_n = users
            max_t = i[0]

    return (max_n, max_t)



if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
