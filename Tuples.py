if __name__ == '__main__':
    n = (raw_input())
    integers = (raw_input())
    integer_list = integers.split()
    integer_list = map(int, integer_list)
    t = tuple(integer_list)
    print (hash(t))