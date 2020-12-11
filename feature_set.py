def find_features(docs):
    words = set(docs)
    features = {}
    for w in all_words:   # all words is the list of all words/token made after the preprocessing
        features[w] = (w in words)
    return features
