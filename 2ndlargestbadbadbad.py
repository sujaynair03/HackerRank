if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    big_numb = -101
    scnd_numb = -101
    for elem in arr:
        if elem > big_numb:
            scnd_numb = big_numb
            big_numb = elem
        if (elem > scnd_numb) and (elem < big_numb):
            scnd_numb = elem
    print(scnd_numb)
