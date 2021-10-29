#prgram to print swastik back ans forth


def main():
    for i in range(2):
        for j in range(5):
            print_spaces(j)
            print("swastik")
        for j in range(5,-1,-1):
            print_spaces(j)
            print("swastik")


#here we are defining a function to print spaces
def print_spaces(n):
    for j in range(n):
        print_no_new_line(" ")


#here we are defiining how to print nothing in a straight line
#well these can also be used to print anything in a straight line

def print_no_new_line(to_print):
    print(to_print, end =" ")

if __name__ =='__main__' :
    main()



