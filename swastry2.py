#here we will be printing football with football stuck on left whereas ball will baounce back

def main():
    for i in range(5):
        print_football(0,i)
    for i in range(5,-1,-1):
        print_football(0,i)

def print_football(x,y):
    print_space(x)
    print_no_new_line("foot")
    print_space(y)
    print_no_new_line("ball")

def print_no_new_line(object):
    print(object,end=" ")

def print_space(n):
    for i in range(n):
        print_no_new_line(" ")

if __name__ == '__main__':
    main()