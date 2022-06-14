# dynamically generated code
# abbreviations: c=concentration, d=decay, t=threshold, n=newvalue
# [(0, 'AKT', False), (1, 'BRAF', False), (2, 'GF', (1.0, 1.0, 0.5)), (3, 'MEK', False), (4, 'PI3K', True), (5, 'PIP3', True), (6, 'RAS', True), (7, 'RTK', True), (8, 'TF', False)]
c0, d0, t0 = 0.000000, 1.000000, 0.500000 # AKT
c1, d1, t1 = 0.000000, 1.000000, 0.500000 # BRAF
c2, d2, t2 = 1.000000, 1.000000, 0.500000 # GF
c3, d3, t3 = 0.000000, 1.000000, 0.500000 # MEK
c4, d4, t4 = 1.000000, 1.000000, 0.500000 # PI3K
c5, d5, t5 = 1.000000, 1.000000, 0.500000 # PIP3
c6, d6, t6 = 1.000000, 1.000000, 0.500000 # RAS
c7, d7, t7 = 1.000000, 1.000000, 0.500000 # RTK
c8, d8, t8 = 0.000000, 1.000000, 0.500000 # TF
dt = 0.07
x0 = c0, c1, c2, c3, c4, c5, c6, c7, c8
def derivs( x, t):
    c0, c1, c2, c3, c4, c5, c6, c7, c8 = x
    n0, n1, n2, n3, n4, n5, n6, n7, n8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    
    #1: GF * = GF
    n2  = float(  ( c2 > t2 )  ) - d2 * c2
    
    #1: RTK * = GF
    n7  = float(  ( c2 > t2 )  ) - d7 * c7
    
    #1: RAS * = RTK
    n6  = float(  ( c7 > t7 )  ) - d6 * c6
    
    #1: PI3K * = RTK or RAS
    n4  = float(  ( c7 > t7 )  or  ( c6 > t6 )  ) - d4 * c4
    
    #1: BRAF * = RAS
    n1  = float(  ( c6 > t6 )  ) - d1 * c1
    
    #1: PIP3 * = PI3K
    n5  = float(  ( c4 > t4 )  ) - d5 * c5
    
    #1: MEK * = BRAF
    n3  = float(  ( c1 > t1 )  ) - d3 * c3
    
    #1: AKT * = PIP3
    n0  = float(  ( c5 > t5 )  ) - d0 * c0
    
    #1: TF * = AKT and MEK
    n8  = float(  ( c0 > t0 )  and  ( c3 > t3 )  ) - d8 * c8

    return ( n0, n1, n2, n3, n4, n5, n6, n7, n8 ) 
