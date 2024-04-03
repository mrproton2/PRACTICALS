if __name__=='__main__':
    P=23
    G=9
    print('the value of P is :%d'%(P))
    print('the value of G is :%d' % (G))
    a=4
    print('the Private Key a for alice :%d' % (a))
    x=int(pow(G,a,P))
    b=3
    print('the Private Key a for Bob :%d' % (b))
    y=int(pow(G,b,P))
    ka= int(pow(y, a, P))
    kb= int(pow(x, b, P))
    print('Secret Key for the alice is :%d' % (ka))
    print('Secret Key for the bob is :%d' % (kb))



