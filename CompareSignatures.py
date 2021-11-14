class CompareSignatures:
  def __init__(self, sig1, sig2) -> None:
    '''
    @param sig1: signature
    @param sig2: signature
    '''
    if len(sig1) != len(sig2):
      raise Exception("Length of two signatures are not equal")

    self.sig1 = sig1
    self.sig2 = sig2
    self.similarity = None

  def getSimilarity(self) -> float:
    # compute similarity if it has not been computed
    if self.similarity is None:
      same = 0
      for i in range(len(self.sig1)):
        if self.sig1[i] == self.sig2[i]:
          same += 1
      self.similarity = same / len(self.sig1)

    return self.similarity