



def small_digit_finder(my_list):
    smallest = my_list[0]
    for i in range (len(my_list)):
        if my_list[i] <= int(smallest):
            smallest = my_list[i]
    print(str(smallest))





list = [999,333,444,555,666,777,888,999]
small_digit_finder(list)