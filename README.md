# ID2222 Data Mining - Homework 1: Finding Similar Items: Textually Similar Documents

This is homework 1 of course ID2222 Data Mining, created by Group 12 (Jinyi Xu, Zheyun Wu)

## Solution

### Class Shingling

The class *Shingling* constructs *k*–shingles set of a given length *k=7* from a given document *text*, and then computes a hash value for each unique shingle with function *hash().* Its function *getShingles()* returns the hased shingles for later function call when calculating similarities.

### Class CompareSets

The class *CompareSets* computes the Jaccard similarity of two sets of hashed shingles *set1* and *set2* whose values are gained from *Shingling.getShingles()*. It returns the value of Jaccard similarity within function *getSimilarity()*.

### Class MinHashing

The class *MinHashing* computes MinHash signatures of given sets of hashed shingles.

A *MinHashing* instance is initialized with a parameter N that represents the number of permutations, which is also the length of generated signatures, if N is not given, N is set to 32 by default. `mh = MinHashing(N=128)`

Then we can get signatures of two sets of hashed shingles by invoking MinHashing instance's getSignatures() method. `sig1, sig2 = mh.getSignatures(set1, set2)`

Implementation explanation: to compute the signatures, firstly a superset is created from given sets, then `_createPermutations()` is called with a parameter `numOfShingles` that denotes the length of the superset, so as to generate and return a two-dimensional array `permutations`. The length of `permutations` is equal to N, which represents how many times the permutation should be performed. Each element of permutations is an integer array whose length is equal to the length the superset, it is filled with unique integers ranging from 0 to `numOfShingles` in random order, this will be used to simulate the permutation process of MinHashing. Finally the two input sets will experience the permutation process N times, which produces signature lists of two given sets.

### Class CompareSignatures

The class *CompareSignatures* computes the estimated similarity from given MinHashing signatures.

A *CompareSignatures* instance is initialized with two parameters sig1 and sig2, which namely represents two lists of signatures. `c = CompareSignatures(sig1, sig2)`

Then simply invoke the instance's getSimilarity() method to get the similarity. `sim = c.getSimilarity()`

Implementation explanation: to compute the similarity of two given signatures, the two signature lists are traversed to compare if the values of the same index in two signatures are equal or not. The similarity is computed from `"number of same values at the same index" / "length of signature"`

### Main Program

The main program, `main.py`, does following steps:

1. asks users to input three parameters `k`, `N` and `similarity threshold` (if not given they will be set with default values),
2. computes the Jaccard similarity and MinHashing similarity of three pairs of testing documents respectively, which is located in the `/test_docs/test_doc.py`,
3. compares the computed similarities with the threshold similarity,
4. displays results on the terminal.

## To run the program in CLI

1. Make sure Python3 is installed locally
2. Git clone the source code

    ```bash
    git clone https://github.com/Jinyix/Data-Mining-lab1
    ```

3. Go to root directory of the project, run following command

    ```bash
    cd Data-Mining-lab1
    python3 main.py
    ```

4. Enter parameters according to CLI prompts:

    ```bash
    Enter shingle lengh k (default 7): 10
    Enter wanted signature length N (default 32): 128
    Enter similarity threshold (default 0.8): 0.75
    ```
