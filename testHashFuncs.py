import matplotlib.pyplot as plt
import numpy as np


def plot_hash_distributions(N, n, c, k):
   
    bf1 = BloomFilter(N, n, c, k, hash_choice=1)
    bf2 = BloomFilter(N, n, c, k, hash_choice=2)

  
    inputs = np.random.randint(1, N, size=n)

   
    hashVals1st = []
    hashVals2nd = []

    for x in inputs:
        for i in range(k):
            hashVals1st.append(bf1.hashFunction1(x, i))
            hashVals2nd.append(bf2.hashFunction2(x, i))


    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    fig.suptitle('Hash Function Freq Distributions (shows randomness)')

    axes[0].hist(hashVals1st, bins=bf1.m, color='blue', alpha=0.7)
    axes[0].set_title('Hash Function 1 Distribution')
    # axes[0].set_title('Hash Distribution for 1 & 2')




    axes[0].set_xlabel('Hash Value')
    axes[0].set_ylabel('Frequency')

    axes[1].hist(hashVals2nd, bins=bf2.m, color='green', alpha=0.7)
    axes[1].set_title('Hash Function 2 Distribution')
    axes[1].set_xlabel('Hash Value')
    axes[1].set_ylabel('Frequency')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


plot_hash_distributions(N=10000, n=1000, c=5, k=3) #N is universe n is subset c is loadfac
