from __future__ import print_function
from cProfile import label
import csv
import random
from statistics import mean, stdev
import matplotlib.pyplot as plt
import statistics
import numpy as np


def update(A, B):
    if random.random() >= 0.5:
        A = (not B) and (A)
        return A, B
    else:
        B = (not A) and (B)
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

def mean_arr(arr):
    i = 0 
    k = 0
    l = []
    while k <= 1000:
        i = 0
        sum = 0
        while i< 100:
            sum = sum + arr[i][k]
            i = i + 1
        l.append(sum)
        k = k + 1
    return l

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

    state_A = [None] * 100
    state_B = [None] * 100
    run_loop = 0
    arr_RT_00 = []
    arr_RT_01 = []
    arr_RT_10 = []
    arr_RT_11 = []

    while run_loop < 100:

        state_A[run_loop]=[]
        state_B[run_loop]=[]
        RT_00 = 0
        RT_01 = 0
        RT_10 = 0
        RT_11 = 0

        A = True
        B = True
        RT_11 = RT_11 + 1
        state_A[run_loop].append(int(A))
        state_B[run_loop].append(int(B))
        sim_time = 1 

        while sim_time <= 1000:

            if simulation(p_perturb, A, B):
                A,B = perturbation(A,B)
            p_update = np.random.normal(0.4,0.1)
            if simulation(p_update, A, B):
                A,B = update(A,B)

            state_A[run_loop].append(int(A))
            state_B[run_loop].append(int(B))

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

    state_A = mean_arr(state_A)
    state_B = mean_arr(state_B)
    return arr_RT_00, arr_RT_01, arr_RT_10, arr_RT_11, state_A, state_B

def deviation(arr):
    l = []
    i = 200

    while i <= 1000:
        l.append(arr[i])
        i = i + 1
    
    res = statistics.pstdev(l)
    return res

def zoom(arr):
    i = 400
    brr=[]
    while i <= 420:
        brr.append(arr[i])
        i = i + 1
    return brr


def main():

    p_update = 0.4

    p_perturb = 0.1
    line1,line2,line3,line4,state_A_1,state_B_1 = generator(p_perturb, p_update)
    line1,line2,line3,line4 = mean_exp(line1,line2,line3,line4)

    p_perturb = 0.3
    line5,line6,line7,line8,state_A_3,state_B_3 = generator(p_perturb, p_update)
    line5,line6,line7,line8 = mean_exp(line5,line6,line7,line8)

    p_perturb = 0.5
    line9,line10,line11,line12,state_A_5,state_B_5 = generator(p_perturb, p_update)
    line9,line10,line11,line12 = mean_exp(line9,line10,line11,line12)

    p_perturb = 0.7
    line13,line14,line15,line16,state_A_7,state_B_7 = generator(p_perturb, p_update)
    line13,line14,line15,line16 = mean_exp(line13,line14,line15,line16)

    p_perturb = 0.9
    line17,line18,line19,line20,state_A_9,state_B_9 = generator(p_perturb, p_update)
    line17,line18,line19,line20 = mean_exp(line17,line18,line19,line20)



    with open("MRT "+" output.tsv", "w") as csvfile:
        writer = csv.writer(csvfile, dialect="excel-tab")
        writer.writerow(['STATE','MRT','STD. DEV'])
        writer.writerow([])
        writer.writerow(['P_up=N(0.4,0.1)','P_perturb = 0.1'])
        writer.writerow(line1)
        writer.writerow(line2)
        writer.writerow(line3)
        writer.writerow(line4)
        writer.writerow([])
        writer.writerow(['P_up=N(0.4,0.1)','P_perturb = 0.3'])
        writer.writerow(line5)
        writer.writerow(line6)
        writer.writerow(line7)
        writer.writerow(line8)
        writer.writerow([])
        writer.writerow(['P_up=N(0.4,0.1)','P_perturb = 0.5'])
        writer.writerow(line9)
        writer.writerow(line10)
        writer.writerow(line11)
        writer.writerow(line12)
        writer.writerow([])
        writer.writerow(['P_up=N(0.4,0.1)','P_perturb = 0.7'])
        writer.writerow(line13)
        writer.writerow(line14)
        writer.writerow(line15)
        writer.writerow(line16)
        writer.writerow([])
        writer.writerow(['P_up=N(0.4,0.1)','P_perturb = 0.9'])
        writer.writerow(line17)
        writer.writerow(line18)
        writer.writerow(line19)
        writer.writerow(line20)

    dev_A=[deviation(state_A_1), deviation(state_A_3), deviation(state_A_5), deviation(state_A_7), deviation(state_A_9)]

    dev_B=[deviation(state_B_1), deviation(state_B_3), deviation(state_B_5), deviation(state_B_7), deviation(state_B_9)]

    i = 0 
    sim_time=[]
    while i <=1000:
        sim_time.append(i)
        i = i + 1


    with open("Trajectory"+" output.tsv", "w") as csvfile:
        writer = csv.writer(csvfile, dialect="excel-tab")
        writer.writerow(['The Std.Dev','for A for','0.1,0.3,0.5,0.7,0.9','respectively'])
        writer.writerow(dev_A)
        writer.writerow([])
        writer.writerow(['The Std.Dev','for B for','0.1,0.3,0.5,0.7,0.9','respectively'])
        writer.writerow(dev_B)
        writer.writerow([])
        writer.writerow(sim_time) 
        writer.writerow([])
        writer.writerow(['Trajectory','for','Node A'])
        writer.writerow([])
        writer.writerow(state_A_1)
        writer.writerow([])
        writer.writerow(state_A_3)
        writer.writerow([])
        writer.writerow(state_A_5)
        writer.writerow([])
        writer.writerow(state_A_7)
        writer.writerow([])
        writer.writerow(state_A_9)
        writer.writerow([])
        writer.writerow(['Trajectory','for','Node B'])
        writer.writerow([])
        writer.writerow(state_B_1)
        writer.writerow([])
        writer.writerow(state_B_3)
        writer.writerow([])
        writer.writerow(state_B_5)
        writer.writerow([])
        writer.writerow(state_B_7)
        writer.writerow([])
        writer.writerow(state_B_9)

        i = 400 
    sim_time=[]
    while i <=420:
        sim_time.append(i)
        i = i + 1
    

    state_A_1 = zoom(state_A_1)
    state_A_3 = zoom(state_A_3)
    state_A_5 = zoom(state_A_5)
    state_A_7 = zoom(state_A_7)
    state_A_9 = zoom(state_A_9)

    state_B_1 = zoom(state_B_1)
    state_B_3 = zoom(state_B_3)
    state_B_5 = zoom(state_B_5)
    state_B_7 = zoom(state_B_7)
    state_B_9 = zoom(state_B_9)

    plt.subplot(2,1,1)
    plt.title("Mean Expression Level Trajectory Of Node A,B,C respectively between 400-420 for Network 5", loc = 'center')
    plt.plot(sim_time,state_A_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.1')
    plt.plot(sim_time,state_A_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.3')
    plt.plot(sim_time,state_A_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.5')
    plt.plot(sim_time,state_A_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.7')
    plt.plot(sim_time,state_A_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.9')
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.subplot(2,1,2)
    plt.plot(sim_time,state_B_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.1')
    plt.plot(sim_time,state_B_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.3')
    plt.plot(sim_time,state_B_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.5')
    plt.plot(sim_time,state_B_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.7')
    plt.plot(sim_time,state_B_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.9')
    plt.ylabel("Mean expression level percentage")
    plt.xlabel("Time Step")
    
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.subplots_adjust(hspace=0.15,wspace=0.20,left=0.1,bottom=0.06,top=0.94,right=0.9)
    plt.savefig('Mean Node Trajectory Output.png',bbox_inches="tight")

    



main()