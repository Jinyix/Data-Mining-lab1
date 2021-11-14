import random

class MinHashing:

  def __init__(self, N=32) -> None:
    '''
    @param N: number of permutations / length of produced signature
    '''

    self.N = N
  
  def _createPermutations(self, numOfShingles) -> list:
    '''
    @param numOfShingles: number of Shingles
    @return: an two-dimensinal array that is used to simulate N times of permutations
    '''

    permutations = []

    for _ in range(self.N):
      permutation = []
      for _ in range(numOfShingles):
        rowNum = random.randint(0, numOfShingles-1)
        while rowNum in permutation:
          rowNum = random.randint(0, numOfShingles-1)
        permutation.append(rowNum)
      
      permutations.append(permutation)
    
    return permutations
      
  
  def getSignatures(self, s1, s2) -> tuple:
    '''
    @param s1: a set of integers (hashed shingles)
    @param s2: a set of integers (hashed shingles)
    @return: a tuple that consists of two lists of signatures for s1 and s2
    '''

    # get permutations
    superset = s1 | s2
    permutations = self._createPermutations(len(superset))

    sig1 = []
    sig2 = []
    superset = list(superset)

    # perform N times of permutations
    for permutation in permutations:
      # find the first rowNum where the element appears in s1
      for rowNum in permutation:
        if superset[rowNum] in s1:
          sig1.append(rowNum)
          break

      # find the first rowNum where the element appears in s2
      for rowNum in permutation:
        if superset[rowNum] in s2:
          sig2.append(rowNum)
          break

    return (sig1, sig2)
