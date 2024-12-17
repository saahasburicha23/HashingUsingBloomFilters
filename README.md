# HashingUsingBloomFilters
 I created a Bloom Filter for this project, using two hashing strategies, I contrasted the theoretical and experimental false positive rates of the filter while varying the constants c and k. I used Python and the extension of matplotlib to program my Bloom Filter and plot my results. 

				Bloom Filter Report 
				By: Saahas Buricha
				Perm Number: 3017456

Description:
 I created a Bloom Filter for this project, using two hashing strategies, I contrasted the theoretical and experimental false positive rates of the filter while varying the constants c and k. I used Python, VS Code, and the extension of matplot to program my Bloom Filter and plot my results. 

I first created two hash functions, the first one(hashFunction1) consists of using the formula: ((a * x + b) % p) % m. Where p is prime and >=n and a & b are just two random numbers in the range of p. By creating a function which finds the next greatest prime number(p) given a number n, we are able to generate values for p which can be used to calculate our result to this hash function. The second hash function (hashFunction2) is implemented by using seeds(initialized globally) which are randomly generated in the range of k. By using a random number generator we are able to generate a random number based on the seed value and this helps us produce our output, the hash index. In order to compare the randomness of the hash functions to each other I created a side by side plot of the two hash functions. I did this generating a random number of inputs(within the universe) and plotting the frequency of the hash value for each respective hash function. 

Here we can see the hash functions are both fairly random with a few minor differences but nothing major. HashFunction1 seems to have a couple elements with a slightly higher frequency but there are no major outliers.

I then created my BloomFilter class where I created all of the instance variables(fields) which were applicable to the bloom filter. The fields I created for this class were self.N(the size of the universe), self.n (the subset of the universe which is the number of items we insert), self.c (the load factor for our hash table, self.k (the number of hash functions), self.bitarray (which is essentially our hash table), and self.hashchoice (which is either 1 or 2). The reason we have self.hashchoice is because there are two hash functions which work differently that have been created for our bloom filter. In order for us to know which one is being used to calculate the hash index, we need to have this parameter. By using these two hash functions, I was able to create the add(x) and contains(x) functions which respectively add an element x to the bloom filter or check if an element x is already present in the bloom filter.

The next step of my project was to analyze the false positive rate for different values of k for each of the two hash functions. I did this by making a separate function which was designed to calculate the false positive rates of random elements in the universe(N). I set the number of trials to 10 as I thought this was a fair amount of trials to help gauge a valid median value for the false positive rate. I then set values for all of the instance variables in order to get the false positive rate values for each hash function. To analyze the false positive rate (FPR), we need to evaluate it across various settings for c and k. Therefore, I have selected c values of 5, 10, and 15, and for k, the values will range from 1 to 10. Essentially, for every c value we want to test all possible k values to see which value of k has the lowest false positive rate and thus see what the optimal number of hash functions we should have for the given load factor. However, before we run our experiment and calculate our experimental FPR values, we need to calculate our true theoretical FPR values. I created a function with parameters c and k that calculates the theoretical FPR values, it uses this formula: (1 - math.exp(-k / c)) ** k. 





Conclusions/Takeaways: My results differ slightly from the theoretical false positive rates but not by much. As we can see in all 3 figures, the curves are fairly similar for both hash functions and the theoretical FPR. The main difference that I found was with the projected optimal k based off the formula k = c * log(2). The projected optimal value of k for the graphs where the load factor(c) was 5 was predicted to be k =3, however according to both hash functions it said the lowest FPR was when k = 4. Similarly, for when the load factor(c) was 10 the optimal k was projected to be 7, whereas my hash functions both indicated that k =8 had the lowest FPR. Although this difference is very small, it is one that I noticed. Both of my hash functions seemed to have a good balance of randomness and thus they did not differ significantly from each other. 
