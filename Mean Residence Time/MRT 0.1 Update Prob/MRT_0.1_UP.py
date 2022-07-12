from __future__ import print_function
from cProfile import label
import csv
import random
from statistics import mean, stdev
import matplotlib.pyplot as plt
import statistics


def update(A, B):
    if random.random() >= 0.5:
        A = not B
        return A, B
    else:
        B = not A
        return A, B


def simulation(p, A, B):

    if random.random() <= p:
        return True

def perturbation(A, B):
    if random.random() >= 0.5:
        A = not A
        return A, B
    else:
        B = not B
        return A, B

def mean_exp(arr0,arr1, arr2,arr3):

    output0=['00']
    output1=['01']
    output2=['10']
    output3=['11']

    MRT_00 = statistics.mean(arr0)
    output0.append(MRT_00)
    dev_00 = statistics.pstdev(arr0)
    output0.append(dev_00)

    MRT_01 = statistics.mean(arr1)
    output1.append(MRT_01)
    dev_01 = statistics.pstdev(arr1)
    output1.append(dev_01)

    MRT_10 = statistics.mean(arr2)
    output2.append(MRT_10)
    dev_02 = statistics.pstdev(arr2)
    output2.append(dev_02)

    MRT_11 = statistics.mean(arr3)
    output3.append(MRT_11)
    dev_11 = statistics.pstdev(arr3)
    output3.append(dev_11)

    return output0, output1, output2, output3


def generator(p_perturb, p_update):

    run_loop = 0
    arr_RT_00 = []
    arr_RT_01 = []
    arr_RT_10 = []
    arr_RT_11 = []

    while run_loop < 100:

        RT_00 = 0
        RT_01 = 0
        RT_10 = 0
        RT_11 = 0

        A = True
        B = True
        RT_11 = RT_11 + 1
        sim_time = 1 

        while sim_time <= 1000:

            if simulation(p_perturb, A, B):
                A,B = perturbation(A,B)
            if simulation(p_update, A, B):
                A,B = update(A,B)

            if A == False and B == False:
                RT_00 = RT_00 + 1
            if A == False and B == True:
                RT_01 = RT_01 + 1
            if A == True and B == False:
                RT_10 = RT_10 + 1
            if A == True and B == True:
                RT_11 = RT_11 + 1

            sim_time = sim_time + 1
        
        arr_RT_00.append(RT_00)
        arr_RT_01.append(RT_01)
        arr_RT_10.append(RT_10)
        arr_RT_11.append(RT_11)
        
        
        run_loop = run_loop + 1

    return arr_RT_00, arr_RT_01, arr_RT_10, arr_RT_11



def main():

    p_update = 0.1

    p_perturb = 0.1
    line1,line2,line3,line4 = generator(p_perturb, p_update)
    line1,line2,line3,line4 = mean_exp(line1,line2,line3,line4)

    p_perturb = 0.3
    line5,line6,line7,line8 = generator(p_perturb, p_update)
    line5,line6,line7,line8 = mean_exp(line5,line6,line7,line8)

    p_perturb = 0.5
    line9,line10,line11,line12 = generator(p_perturb, p_update)
    line9,line10,line11,line12 = mean_exp(line9,line10,line11,line12)

    p_perturb = 0.7
    line13,line14,line15,line16 = generator(p_perturb, p_update)
    line13,line14,line15,line16 = mean_exp(line13,line14,line15,line16)

    p_perturb = 0.9
    line17,line18,line19,line20 = generator(p_perturb, p_update)
    line17,line18,line19,line20 = mean_exp(line17,line18,line19,line20)



    with open("MRT " + "p=0.1 UP perturbation " + " output.tsv", "w") as csvfile:
        writer = csv.writer(csvfile, dialect="excel-tab")
        writer.writerow(['STATE','MRT','STD. DEV'])
        writer.writerow([])
        writer.writerow(['P_update=0.1','P_perturb = 0.1'])
        writer.writerow(line1)
        writer.writerow(line2)
        writer.writerow(line3)
        writer.writerow(line4)
        writer.writerow([])
        writer.writerow(['P_update=0.1','P_perturb = 0.3'])
        writer.writerow(line5)
        writer.writerow(line6)
        writer.writerow(line7)
        writer.writerow(line8)
        writer.writerow([])
        writer.writerow(['P_update=0.1','P_perturb = 0.5'])
        writer.writerow(line9)
        writer.writerow(line10)
        writer.writerow(line11)
        writer.writerow(line12)
        writer.writerow([])
        writer.writerow(['P_update=0.1','P_perturb = 0.7'])
        writer.writerow(line13)
        writer.writerow(line14)
        writer.writerow(line15)
        writer.writerow(line16)
        writer.writerow([])
        writer.writerow(['P_update=0.1','P_perturb = 0.9'])
        writer.writerow(line17)
        writer.writerow(line18)
        writer.writerow(line19)
        writer.writerow(line20)



main()