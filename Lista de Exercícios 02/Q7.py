def prime_generator():
    p = 1

    while True:
        div = 0
        for i in range(1,p+1):
            if p%i == 0:
                div += 1

        if div == 2:
            yield p

        p+=1
