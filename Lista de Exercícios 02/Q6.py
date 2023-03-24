def read_backwards(list):
    list.reverse()
    for elem in list:
        yield elem

