from __future__ import print_function
import random
from statistics import mean, stdev
import matplotlib.pyplot as plt


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


def main():
    p = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    mean_array = []
    stdev_array = []

    sim_param = 10000

    p_trav = 0

    conv_time_array = []

    while p_trav < 10:

        ctr = 0
        conv_time_array = []
        mean_val = 0
        std_dev_val = 0

        while ctr < sim_param:

            A = True
            B = True
            conv_time = 1

            while True:

                if (simulation(p[p_trav], A, B)):
                    A, B = update(A, B)

                if (A == B):
                    conv_time = conv_time + 1
                    continue

                else:
                    conv_time_array.append(conv_time)
                    break

            ctr = ctr + 1

        mean_val = mean(conv_time_array)
        std_dev_val = stdev(conv_time_array)

        mean_array.append(mean_val)
        stdev_array.append(std_dev_val)

        p_trav = p_trav + 1

    plt.title("Mean Convergence Time vs Update Probability Plot ", loc = 'center')
    plt.xlabel("Update Probability")
    plt.ylabel("Mean Convergence Time")
    plt.plot(p,mean_array, '_:k', ms = 18, mec = 'g', mfc = 'g')
    plt.errorbar(p,mean_array,xerr=None,yerr = stdev_array, fmt='_:k', ecolor='r',barsabove=True)
    plt.show()

main()