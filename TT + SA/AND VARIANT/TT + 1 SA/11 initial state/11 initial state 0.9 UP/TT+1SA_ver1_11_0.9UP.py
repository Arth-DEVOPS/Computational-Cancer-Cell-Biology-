from __future__ import print_function
from cProfile import label
import csv
import random
from statistics import mean, stdev
import matplotlib.pyplot as plt
import statistics


def update(A, B, C):
    randomizer = random.random()

    if randomizer <= 0.33:
        A = (not B) and (not C) and (A)
        return A,B,C

    elif 0.33 < randomizer <= 0.66:
        B = (not A) and (not C)
        return A,B,C

    else:
        C = (not A) and (not B)
        return A,B,C


def simulation(p, A, B, C):

    if random.random() <= p:
        return True

def perturbation(A, B, C):
    randomizer = random.random()

    if randomizer <= 0.33:
        A = not A
        return A,B,C

    elif 0.33 < randomizer <= 0.66:
        B = not B
        return A,B,C

    else:
        C = not C
        return A,B,C

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

def mean_exp(arr0,arr1, arr2,arr3,arr4,arr5,arr6,arr7):

    output0=['000']
    output1=['001']
    output2=['010']
    output3=['011']
    output4=['100']
    output5=['101']
    output6=['110']
    output7=['111']


    MRT_0 = statistics.mean(arr0)
    output0.append(MRT_0)
    dev_0 = statistics.pstdev(arr0)
    output0.append(dev_0)

    MRT_1 = statistics.mean(arr1)
    output1.append(MRT_1)
    dev_1 = statistics.pstdev(arr1)
    output1.append(dev_1)

    MRT_2 = statistics.mean(arr2)
    output2.append(MRT_2)
    dev_2 = statistics.pstdev(arr2)
    output2.append(dev_2)

    MRT_3 = statistics.mean(arr3)
    output3.append(MRT_3)
    dev_3 = statistics.pstdev(arr3)
    output3.append(dev_3)

    MRT_4 = statistics.mean(arr4)
    output4.append(MRT_4)
    dev_4 = statistics.pstdev(arr4)
    output4.append(dev_4)

    MRT_5 = statistics.mean(arr5)
    output5.append(MRT_5)
    dev_5 = statistics.pstdev(arr5)
    output5.append(dev_5)

    MRT_6 = statistics.mean(arr6)
    output6.append(MRT_6)
    dev_6 = statistics.pstdev(arr6)
    output6.append(dev_6)

    MRT_7 = statistics.mean(arr7)
    output7.append(MRT_7)
    dev_7 = statistics.pstdev(arr7)
    output7.append(dev_7)

    return output0, output1, output2, output3, output4, output5, output6, output7


def generator(p_perturb, p_update):

    state_A = [None] * 100
    state_B = [None] * 100
    state_C = [None] * 100
    run_loop = 0
    arr_RT_000 = []
    arr_RT_001 = []
    arr_RT_010 = []
    arr_RT_011 = []
    arr_RT_100 = []
    arr_RT_101 = []
    arr_RT_110 = []
    arr_RT_111 = []

    while run_loop < 100:

        state_A[run_loop]=[]
        state_B[run_loop]=[]
        state_C[run_loop]=[]
        RT_000 = 0
        RT_001 = 0
        RT_010 = 0
        RT_011 = 0
        RT_100 = 0
        RT_101 = 0
        RT_110 = 0
        RT_111 = 0

        A = True
        B = True
        C = True
        RT_111 = RT_111 + 1
        state_A[run_loop].append(int(A))
        state_B[run_loop].append(int(B))
        state_C[run_loop].append(int(C))
        sim_time = 1 

        while sim_time <= 1000:

            if simulation(p_perturb, A, B,C):
                A,B,C = perturbation(A,B,C)
            if simulation(p_update, A, B,C):
                A,B,C = update(A,B,C)

            state_A[run_loop].append(int(A))
            state_B[run_loop].append(int(B))
            state_C[run_loop].append(int(C))

            if A == False and B == False and C == False:
                RT_000 = RT_000 + 1
            if A == False and B == False and C == True:
                RT_001 = RT_001 + 1
            if A == False and B == True and C == False:
                RT_010 = RT_010 + 1
            if A == False and B == True and C == True:
                RT_011 = RT_011 + 1
            if A == True and B == False and C == False:
                RT_100 = RT_100 + 1
            if A == True and B == False and C == True:
                RT_101 = RT_101 + 1
            if A == True and B == True and C == False:
                RT_110 = RT_110 + 1
            if A == True and B == True and C == True:
                RT_111 = RT_111 + 1

            sim_time = sim_time + 1
        
        arr_RT_000.append(RT_000)
        arr_RT_001.append(RT_001)
        arr_RT_010.append(RT_010)
        arr_RT_011.append(RT_011)
        arr_RT_100.append(RT_100)
        arr_RT_101.append(RT_101)
        arr_RT_110.append(RT_110)
        arr_RT_111.append(RT_111)
        
        
        run_loop = run_loop + 1

    state_A = mean_arr(state_A)
    state_B = mean_arr(state_B)
    state_C = mean_arr(state_C)
    return arr_RT_000, arr_RT_001, arr_RT_010, arr_RT_011,arr_RT_100, arr_RT_101, arr_RT_110, arr_RT_111, state_A, state_B, state_C

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

    p_update = 0.9

    p_perturb = 0.1
    line1,line2,line3,line4,line5,line6,line7,line8,state_A_1,state_B_1,state_C_1 = generator(p_perturb, p_update)
    line1,line2,line3,line4,line5,line6,line7,line8 = mean_exp(line1,line2,line3,line4,line5,line6,line7,line8)

    p_perturb = 0.3
    line9,line10,line11,line12,line13,line14,line15,line16,state_A_3,state_B_3,state_C_3 = generator(p_perturb, p_update)
    line9,line10,line11,line12,line13,line14,line15,line16 = mean_exp(line9,line10,line11,line12,line13,line14,line15,line16)

    p_perturb = 0.5
    line17,line18,line19,line20,line21,line22,line23,line24,state_A_5,state_B_5,state_C_5 = generator(p_perturb, p_update)
    line17,line18,line19,line20,line21,line22,line23,line24 = mean_exp(line17,line18,line19,line20,line21,line22,line23,line24)

    p_perturb = 0.7
    line25,line26,line27,line28,line29,line30,line31,line32,state_A_7,state_B_7,state_C_7 = generator(p_perturb, p_update)
    line25,line26,line27,line28,line29,line30,line31,line32 = mean_exp(line25,line26,line27,line28,line29,line30,line31,line32)

    p_perturb = 0.9
    line33,line34,line35,line36,line37,line38,line39,line40,state_A_9,state_B_9,state_C_9 = generator(p_perturb, p_update)
    line33,line34,line35,line36,line37,line38,line39,line40 = mean_exp(line33,line34,line35,line36,line37,line38,line39,line40)



    with open("TT+1SA ver1 MRT " + "p=0.9 UP perturbation " + " output.tsv", "w") as csvfile:
        writer = csv.writer(csvfile, dialect="excel-tab")
        writer.writerow(['STATE','MRT','STD. DEV'])
        writer.writerow([])
        writer.writerow(['P_update=0.9','P_perturb = 0.1'])
        writer.writerow(line1)
        writer.writerow(line2)
        writer.writerow(line3)
        writer.writerow(line4)
        writer.writerow(line5)
        writer.writerow(line6)
        writer.writerow(line7)
        writer.writerow(line8)
        writer.writerow([])
        writer.writerow(['P_update=0.9','P_perturb = 0.3'])
        writer.writerow(line9)
        writer.writerow(line10)
        writer.writerow(line11)
        writer.writerow(line12)
        writer.writerow(line13)
        writer.writerow(line14)
        writer.writerow(line15)
        writer.writerow(line16)
        writer.writerow([])
        writer.writerow(['P_update=0.9','P_perturb = 0.5'])
        writer.writerow(line17)
        writer.writerow(line18)
        writer.writerow(line19)
        writer.writerow(line20)
        writer.writerow(line21)
        writer.writerow(line22)
        writer.writerow(line23)
        writer.writerow(line24)
        writer.writerow([])
        writer.writerow(['P_update=0.9','P_perturb = 0.7'])
        writer.writerow(line25)
        writer.writerow(line26)
        writer.writerow(line27)
        writer.writerow(line28)
        writer.writerow(line29)
        writer.writerow(line30)
        writer.writerow(line31)
        writer.writerow(line32)
        writer.writerow([])
        writer.writerow(['P_update=0.9','P_perturb = 0.9'])
        writer.writerow(line33)
        writer.writerow(line34)
        writer.writerow(line35)
        writer.writerow(line36)
        writer.writerow(line37)
        writer.writerow(line38)
        writer.writerow(line39)
        writer.writerow(line40)
        

    dev_A=[deviation(state_A_1), deviation(state_A_3), deviation(state_A_5), deviation(state_A_7), deviation(state_A_9)]

    dev_B=[deviation(state_B_1), deviation(state_B_3), deviation(state_B_5), deviation(state_B_7), deviation(state_B_9)]

    dev_C=[deviation(state_C_1), deviation(state_C_3), deviation(state_C_5), deviation(state_C_7), deviation(state_C_9)]

    i = 0 
    sim_time=[]
    while i <=1000:
        sim_time.append(i)
        i = i + 1


    with open("TT+1SA ver1 Trajectory" + "p=0.9 UP perturbation " + " output.tsv", "w") as csvfile:
        writer = csv.writer(csvfile, dialect="excel-tab")
        writer.writerow(['The Std.Dev','for A for','0.1,0.3,0.5,0.7,0.9','respectively'])
        writer.writerow(dev_A)
        writer.writerow([])
        writer.writerow(['The Std.Dev','for B for','0.1,0.3,0.5,0.7,0.9','respectively'])
        writer.writerow(dev_B)
        writer.writerow([])
        writer.writerow(['The Std.Dev','for C for','0.1,0.3,0.5,0.7,0.9','respectively'])
        writer.writerow(dev_C)
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
        writer.writerow([])
        writer.writerow(['Trajectory','for','Node C'])
        writer.writerow([])
        writer.writerow(state_C_1)
        writer.writerow([])
        writer.writerow(state_C_3)
        writer.writerow([])
        writer.writerow(state_C_5)
        writer.writerow([])
        writer.writerow(state_C_7)
        writer.writerow([])
        writer.writerow(state_C_9)

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

    state_C_1 = zoom(state_C_1)
    state_C_3 = zoom(state_C_3)
    state_C_5 = zoom(state_C_5)
    state_C_7 = zoom(state_C_7)
    state_C_9 = zoom(state_C_9)



    plt.subplot(3,1,1)
    plt.title("Mean Expression Level Trajectory Of Node A,B,C respectively between 400-420", loc = 'center')
    plt.plot(sim_time,state_A_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.1')
    plt.plot(sim_time,state_A_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.3')
    plt.plot(sim_time,state_A_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.5')
    plt.plot(sim_time,state_A_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.7')
    plt.plot(sim_time,state_A_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.9')
    plt.legend(bbox_to_anchor=(1.1, 1.05))

    plt.subplot(3,1,2)
    plt.plot(sim_time,state_B_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.1')
    plt.plot(sim_time,state_B_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.3')
    plt.plot(sim_time,state_B_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.5')
    plt.plot(sim_time,state_B_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.7')
    plt.plot(sim_time,state_B_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.9')
    plt.ylabel("Mean expression level percentage")

    plt.subplot(3,1,3)
    plt.plot(sim_time,state_C_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.1')
    plt.plot(sim_time,state_C_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.3')
    plt.plot(sim_time,state_C_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.5')
    plt.plot(sim_time,state_C_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.7')
    plt.plot(sim_time,state_C_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='P_p 0.9')
    plt.xlabel("Time")
    
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
    plt.subplots_adjust(hspace=0.15,wspace=0.20,left=0.1,bottom=0.06,top=0.94,right=0.9)
    plt.savefig('Mean Node Trajectory Output.png',bbox_inches="tight")



main()