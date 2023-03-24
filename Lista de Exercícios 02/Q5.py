def mult_matrix(m1, m2):
    l1 = len(m1); l2 = len(m2)
    c1 = len(m1[0]); c2 = len(m2[0]) 
    assert(c1 == l2)

    mult = [] 
    lm = l1; cm = c2

    for i in range(0,lm):
        line = []
        for j in range(0, cm):
            sum = 0

            #line i times column j
            for k in range(0,c1):
                sum += m1[i][k] * m2[k][j]

            line.append(sum)
        mult.append(line)

    return mult
            

