import random 
import matplotlib.pyplot as plt

def update(A, B ,C):

    randomizer = random.random()

    if randomizer <= 0.33:
        A = not B or not C
        return A,B,C

    elif 0.33 < randomizer <= 0.66:
        B = not A or not C
        return A,B,C

    else:
        C = not A or not B
        return A,B,C

def CountFrequency(my_list):
 
    freq = {}

    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% s : % d"%(key, value))

    return freq


def main():
    
    ctr = 0 
    
    l1 = []
    s1 = []
    
    while ctr < 10000:
        
        A = random.choice([True, False])
        B = random.choice([True, False])
        C = random.choice([True, False])

        A_prev = A
        B_prev = B
        C_prev = C

        s1 = []

        while True:

            A,B,C = update(A,B,C)

            if (A == A_prev) and (B == B_prev) and (C == C_prev):
                s1 = [A, B, C]
                l1.append(s1)
                break

            else:
                A_prev = A
                B_prev = B
                C_prev = C
                continue

        ctr = ctr + 1

    l3=[]
    count = 0
    for item in l1:
        if item not in l3:
            count += 1
            l3.append(item)
    print ("No of unique items are:"), count
    print
    print("They are:"), l3
    print

    l2=[]
    for item in l1:
        l2.append(str(item))


    d1 = CountFrequency(l2)
    plt.bar(range(len(d1)), list(d1.values()), align='center')
    plt.xticks(range(len(d1)), list(d1.keys()))
    plt.title("Frequency of each stable state for second variant of toggle traid for 10000 trials")
    plt.xlabel("Stable States of A B C")
    plt.ylabel("Frequncy")
    plt.show()

                
main()