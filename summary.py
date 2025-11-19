class Summary:
    def __init__(self, summary: str, header: str = "File Summary"):
        self.summary = summary
        self.header = header

    # Select the 10 most common words from the summary not including articles, prepositions, or conjunctions
    def key_words(self):
        wordsToIgnore = ["", " ", "the", "is", "in", "and", "to", "a", "of", "it", "that", "on", "for", "with", "as", "by", "at", "an", "be", "this", "from", "or"]

        wordCount = {}
        words = self.summary.split()
        for word in words:
            word = word.lower().strip(".,!?;:\"'()[]{}")
            if word in wordsToIgnore:
                continue
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1

        topWords = sorted(wordCount, key=wordCount.get, reverse=True)[:10]
        return topWords
