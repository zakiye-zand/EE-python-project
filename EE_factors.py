def F_to_P(i, n, f):
    factor = 1/(1+i)**n
    return f*factor

def P_to_F(i, n , p):
    factor = (1+i)**n
    return p*factor

def A_to_P (i, j, n, Ai=1):
    if i!=j:
        factor= (1-((1+j)**n)*((1+i)**-n))/(i-j)
    else:
        factor = n/(i+1)
    return Ai*factor

def p_to_a(i, n, PV):
    factor2= (i * (1 + i)**n) / ((1 + i)**n - 1) * PV
    return PV*factor2

