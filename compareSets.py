
class CompareSets:

    def __init__(self, set1, set2):
        intersection = set1 & set2
        union = set1 | set2
        self.similarity = len(intersection) / len(union)
