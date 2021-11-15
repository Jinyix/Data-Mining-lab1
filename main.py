from compareSets import CompareSets
from shingling import Shingling
from MinHashing import MinHashing
from CompareSignatures import CompareSignatures

from test_docs.test_doc import doc1, doc2, doc3, doc4, doc5, doc6

tests = [{"d1": doc1, "d2": doc2}, {"d1": doc3, "d2": doc4}, {"d1": doc5, "d2": doc6}]

k = int(input("Enter shingle lengh k (default 7): ") or 7) 
N = int(input("Enter wanted signature length N (default 32): ") or 32)
t = float(input("Enter similarity threshold (default 0.8): ") or 0.8)
if t <= 0 or t > 1:
  raise Exception("[ERROR] The threshold should be between 0 to 1!")

for round in range(0, len(tests)):

  print('========================Test {}========================'.format(round+1))
  print('Document 1 (only showing 60 characters): "{}"'.format(tests[round]["d1"][0:60]))
  print('Document 2 (only showing 60 characters): "{}"'.format(tests[round]["d2"][0:60]))

  # Shingling docs
  s1 = Shingling(text=tests[round]["d1"], k=k).getShingles()
  s2 = Shingling(text=tests[round]["d2"], k=k).getShingles()


  # Jaccard Similarity
  jaccard_similarity = CompareSets(s1, s2).getSimilarity()
  result_1 = ('>=', 'Similar') if jaccard_similarity >= t else ('<', 'Not similar')
  print('[Jaccard] Similarity: {} {} threshold {}, result is {}'.format(jaccard_similarity, result_1[0], t, result_1[1]))

  # MinHashing Similarity
  m = MinHashing(N=N)
  sig1, sig2 = m.getSignatures(s1, s2)
  minhashing_sim = CompareSignatures(sig1, sig2).getSimilarity()
  result_2 = ('>=', 'Similar') if jaccard_similarity >= t else ('<', 'Not similar')
  print('[MinHash] Similarity: {} {} threshold {}, result is {}'.format(jaccard_similarity, result_2[0], t, result_2[1]))

  print('\n')

