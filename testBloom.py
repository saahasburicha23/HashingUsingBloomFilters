import matplotlib.pyplot as plt
import math
from bloom import BloomFilter
import random
import numpy as np
def get_fprRate(N, n, c, k, hash_choice, trials=10):

    fprtracker = []
    for _ in range(trials):
        bloom_filter = BloomFilter(N, n, c, k, hash_choice)

        
        present = set(random.randint(0, N - 1) for _ in range(n)) #in rnge of universe
        
        for item in present:
            bloom_filter.add(item)
        
        tries = 10000  
        falsePos = 0
        for _ in range(tries):
            x = random.randint(0, N - 1)
            if x not in present and bloom_filter.contains(x):
                falsePos += 1
        fprRate = falsePos / tries
        fprtracker.append(fprRate)

    return np.median(fprtracker)

def theoreticalValFunc(k, c):
    ans = (1 - math.exp(-k / c)) ** k
    return ans


N = 10**8     
n = 10000      


cVals = [5, 10, 15]  
kVals = range(1, 11) #graph will sjow from 1 to 10

for c in cVals:
    
    k_star = int(round(c * math.log(2)))
    print(f"\nFor c = {c}, Optimal k* = {k_star}")

    
    func1FPR = []
    func2FPR = []
    tfpr = []

   
    for k in kVals:
        print(f"Computing for k = {k} ...")
       
        fpr_h1 = get_fprRate(N,n,c,k, hash_choice =1)
        func1FPR.append(fpr_h1)
       
        fpr_h2 = get_fprRate(N, n, c, k, hash_choice=2)
        func2FPR.append(fpr_h2)

        
        tp = theoreticalValFunc(k, c)
        tfpr.append(tp)
      
        print(f"  FPR Hash 1 value is : {fpr_h1:.6f}, FPR Hash 2 value is: {fpr_h2:.6f}, Theoretical FPR value is: {tp:.6f}")


    plt.figure(figsize=(5, 3))


    plt.plot(kVals, func1FPR, label='Experimental FPR (Hash Function 1)', marker='o', color='red')
    plt.plot(kVals, func2FPR, label='Experimental FPR (Hash Function 2)', marker='s', color='blue')
    plt.plot(kVals, tfpr, label='Theoretical FPR', linestyle='--', color='black')
    plt.axvline(x=k_star, color='green', linestyle=':', label=f'Optimal k = {k_star}')
    plt.xlabel('Number of Hash Functions (k)')
    plt.ylabel('False Positive Rate')
    plt.title(f'False Positive Rate vs. Number of Hash Functions (c = {c})')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
