import math
import random
import numpy as np
import matplotlib.pyplot as plt

class BloomFilter:
    def __init__(self, N, n, c, k, hash_choice=1):
        self.N = N               
        self.n = n               
        self.c = c               
        self.k = k               
        self.m = int(self.c * self.n)  
        self.bit_array = [0] * self.m
        self.hash_choice = hash_choice

        if self.hash_choice == 1:
           
            
            self.p = self.findP(N)
            
            self.hashParameters = [
                (random.randint(1, self.p - 1), random.randint(0, self.p - 1))
                for _ in range(self.k)
            ]
        else:
            
            self.hashSeedsforF2 = [random.randint(0, 1 << 32) for _ in range(self.k)]

    def findP(self, N):
        
        def is_prime(num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            # while (i * i) <= num:
            #     if num % i == 0 and num % (i + 2) == 0:
            #         return False
            #     i += 6
            return True

        prime = N
        while not is_prime(prime):
            prime += 1
        return prime

    # Part 2 add/cotnains (x)
    def add(self, x):
        for i in range(self.k):
            if self.hash_choice == 1:
                hash_index = self.hashFunction1(x, i)
            else:
                hash_index = self.hashFunction2(x, i)
            self.bit_array[hash_index] = 1

    def contains(self, x):
        for i in range(self.k):
            if self.hash_choice == 1:
                hash_index = self.hashFunction1(x, i)
            else:
                hash_index = self.hashFunction2(x, i)
            if not self.bit_array[hash_index]:
                return False
        return True

    def hashFunction1(self, x, index):
        
        a, b = self.hashParameters[index]
        p = self.p
        m = self.m
        return ((a * x + b) % p) % m

    def hashFunction2(self, x, index):
       
        r = random.Random(self.hashSeedsforF2[index] + x)
        return r.randint(0, self.m - 1)