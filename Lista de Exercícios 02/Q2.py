def tuple_average(tuples):
    averages = ()

    for tup in tuples:
        sum = 0
        n = len(tup)
        for item in tup:
            sum += item
        averages = averages + (sum/n,)
    
    return averages

