import random 
import csv
import matplotlib.pyplot as plt

def update1(A, B ,C):

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

def update2(A, B ,C):

    randomizer = random.random()

    if randomizer <= 0.33:
        A = not B and not C
        return A,B,C

    elif 0.33 < randomizer <= 0.66:
        B = not A and not C
        return A,B,C

    else:
        C = not A and not B
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
     
    p_trav = 0
    p = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    while p_trav < 11:

        l1 = []
        s1 = []
        ctr = 0

        while ctr < 10000:
            
            A = random.choice([True, False])
            B = random.choice([True, False])
            C = random.choice([True, False])
            
            A_prev = A
            B_prev = B
            C_prev = C

            s1 = []
            
            while True:

                if random.random() > p[p_trav]:
                    A,B,C = update1(A,B,C)
                else:
                    A,B,C = update2(A,B,C)
                
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

        
        l_entry = ["State","Frequency"]
        with open("p=" + str(p[p_trav]) + " output.tsv", "w") as csvfile:
            writer = csv.writer(csvfile, dialect="excel-tab")
            writer.writerow(l_entry) 
            writer.writerow([])
            writer.writerow(["For Probability p =",p[p_trav]])
            writer.writerow([])
            for key, value in d1.items():
                writer.writerow((key, value))
        
            

        # plt.bar(range(len(d1)), list(d1.values()), align='center')
        # plt.xticks(range(len(d1)), list(d1.keys()))
        # plt.title("Frequency of each stable state for probabalistic toggle traid for 10000 trials")
        # plt.xlabel("Stable States of A B C")
        # plt.ylabel("Frequncy")
        # plt.show()

        p_trav = p_trav + 1
                
main()