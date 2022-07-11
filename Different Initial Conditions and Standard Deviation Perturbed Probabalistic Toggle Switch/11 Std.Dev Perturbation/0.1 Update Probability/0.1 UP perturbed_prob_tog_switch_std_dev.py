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

def mean_exp(arr):
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



def generator(p_perturb, p_update):

    state_A = [None] * 100
    run_loop = 0

    while run_loop < 100:

        state_A[run_loop]=[]
        A = True
        B = True
        state_A[run_loop].append(int(A))
        sim_time = 1 

        while sim_time <= 1000:

            if simulation(p_perturb, A, B):
                A,B = perturbation(A,B)
            if simulation(p_update, A, B):
                A,B = update(A,B)

            state_A[run_loop].append(int(A))

            sim_time = sim_time + 1
        
        run_loop = run_loop + 1

    state_A = mean_exp(state_A)
    return state_A

def deviation(arr):
    l = []
    i = 200

    while i <= 1000:
        l.append(arr[i])
        i = i + 1
    
    res = statistics.pstdev(l)
    return res



def main():

    p_update = 0.1

    p_perturb = 0.1
    state_A_1 = generator(p_perturb, p_update)

    p_perturb = 0.3
    state_A_3 = generator(p_perturb, p_update)

    p_perturb = 0.5
    state_A_5 = generator(p_perturb, p_update)

    p_perturb = 0.7
    state_A_7 = generator(p_perturb, p_update)

    p_perturb = 0.9
    state_A_9 = generator(p_perturb, p_update)

    dev=[deviation(state_A_1), deviation(state_A_3), deviation(state_A_5), deviation(state_A_7), deviation(state_A_9)]
    dev_entry = [str(dev)]

    i = 0 
    sim_time=[]
    while i <=1000:
        sim_time.append(i)
        i = i + 1

        with open("11 std dev " + "p=0.1 UP perturbation " + " output.tsv", "w") as csvfile:
            writer = csv.writer(csvfile, dialect="excel-tab")
            writer.writerow(['The standard deviation for mean convergence level between t=200 and t=1000 for perturbation probability 0.1, 0.3, 0.5, 0.7 and 0.9 was found to be the following respectively'])
            writer.writerow(dev_entry)
            writer.writerow([])
            writer.writerow(sim_time) 
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


    # plt.title("Mean Expression Level Trajectory Of Node A For Update Probability = 0.1", loc = 'center')
    # plt.xlabel("Time")
    # plt.ylabel("Mean expression level percentage")
    # plt.plot(sim_time,state_A_1, '.-k', ms = 1, mec = 'r', mfc = 'r', label='Perturbation Probability = 0.1')
    # plt.plot(sim_time,state_A_3, '.-g', ms = 1, mec = 'r', mfc = 'r', label='Perturbation Probability = 0.3')
    # plt.plot(sim_time,state_A_5, '.-b', ms = 1, mec = 'r', mfc = 'r', label='Perturbation Probability = 0.5')
    # plt.plot(sim_time,state_A_7, '.-m', ms = 1, mec = 'r', mfc = 'r', label='Perturbation Probability = 0.7')
    # plt.plot(sim_time,state_A_9, '.-c', ms = 1, mec = 'r', mfc = 'r', label='Perturbation Probability = 0.9')
    # plt.legend()
    # plt.show() 


    
   

main()