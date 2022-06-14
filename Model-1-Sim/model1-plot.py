"""
Plots results for the paper

"""

from pylab import *
from boolean2 import util

def smooth(data, w=0):
    "Smooths data by a moving window of width 'w'"
    fw = float(w)
    def average( index ):
        return sum( data[index: index+w] )/fw
    indices = range( len(data) - w )        
    out = list(map( average, indices ))
    return out

def make_plot():
    
    # contains averaged node information based on 1000 runs
    data = util.bload( 'model1-run.bin' )

    # each of these is a dictionary keyed by nodes
    run1, run2, run3, run4 = data 

    # applies smoothing to all values
    # for run in (run1, run2, run3, run4):
    #     for key, values in list(run.items()):
    #         run[key] = smooth( values, w=10 )
    
    #
    # Plotting Apoptosis
    #
    subplot(121)
    apop1, apop2, apop3, apop4, apop5, apop6, apop7, apop8, apop9 = run1['GF'], run1['RAS'], run1['RTK'], run1['PI3K'], run1['BRAF'], run1['PIP3'], run1['MEK'], run1['AKT'], run1['TF']

    ps = [ plot( apop1, 'bo-',label='GF' ), plot( apop2, 'r^-',label='RAS' ),plot(apop3,'m<-',label='RTK'),plot(apop4,'bD-',label='PI3K'),plot(apop5,'gv-',label='BRAF'),plot(apop6,'rD-',label='PIP3'),plot(apop7,'c>-',label='MEK/ERK'),plot(apop8,'y^-',label='AKT'),plot(apop9,'ko-',label='TF') ]
    legend( ps, ['GF','RAS','RTK','PI3K','BRAF','PIP3','MEK/ERK','AKT','TF'], loc='lower right' )
    title( ' Model 1 Results' )
    xlabel( 'Time Steps' )
    ylabel( 'Node Activity' )
    ylim( (-0.1, 1.1) ) 
    xlim( (0, 6) )
    #
    # Plotting FasL and Ras
    #
    # subplot(122)
    # fasL1, fasL2 = run1['FasL'], run4['FasL']
    # ras1, ras2 = run1['Ras'], run4['Ras']

    # ps = [ plot( fasL1, 'bo-' ), plot( fasL2, 'ro-' ), plot( ras1, 'b^-' ), plot( ras2, 'r^-' ) ]
    # legend( ps, 'Normal-FasL LGL-like-FasL Normal-Ras LGL-like-Ras'.split() , loc='lower left' )
    # title( ' Changes in FasL and Ras' )
    # xlabel( 'Time Steps' )

if __name__ == '__main__':
    
    # resize this to change figure size
    figure(num = None, figsize=(14, 7), dpi=80, facecolor='w', edgecolor='k')
    make_plot( )
    savefig('Figure2.png')
    show()