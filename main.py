from compareSets import CompareSets
from shingling import Shingling
from MinHashing import MinHashing
from CompareSignatures import CompareSignatures

from test_docs.test_doc import doc1, doc2, doc3, doc4, doc5, doc6

tests = [{"d1": doc1, "d2": doc2}, {"d1": doc3, "d2": doc4}, {"d1": doc5, "d2": doc6}]

for round in range(0, len(tests)):
  print('========================Test {}========================'.format(round+1))
  # Shingling docs
  s1 = Shingling(text=tests[round]["d1"], k=10).getShingles()
  s2 = Shingling(text=tests[round]["d2"], k=10).getShingles()

  # Jaccard Similarity
  jaccard_similarity = CompareSets(s1, s2).getSimilarity()
  print('[Jaccard] Similarity:', jaccard_similarity)

  # MinHashing Similarity
  m = MinHashing(N=10)
  sig1, sig2 = m.getSignatures(s1, s2)
  minhashing_sim = CompareSignatures(sig1, sig2).getSimilarity()
  print('[MinHashing] Estimated similarity:', minhashing_sim)

