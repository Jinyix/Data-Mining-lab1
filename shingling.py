
class Shingling:

    def __init__(self, text, k):
        #create no dupliactes shingles
        self.hashedShingles = set()
        text = text.lower()
        #get shingles and then hash
        for i in range(0, len(text) - k + 1):
            shingle = text[i:i + k]
            hashedshingle = hash(shingle)
            self.hashedShingles.add(hashedshingle)










