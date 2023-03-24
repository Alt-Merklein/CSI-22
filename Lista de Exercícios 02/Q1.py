def remove_empty(list):
    cont = 0
    for i in range(0,len(list)):
        if (len(list[cont]) == 0):
            del list[cont]
            cont -= 1
        cont += 1
