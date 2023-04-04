def each_year(P, r, n, t):

    for period in range(t):
        amount = P*(pow((1+r/n), n*(period+1)))
        print('Period:', period+1, amount)

    return amount

# https://www.statology.org/compound-interest-in-python/