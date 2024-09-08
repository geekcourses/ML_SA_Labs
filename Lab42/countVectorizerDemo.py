from sklearn.feature_extraction.text import CountVectorizer

train_docs = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the ?',
]

vectorizer = CountVectorizer(
    vocabulary=['first', 'second','document'],
    binary=True
)

# print(vectorizer.vocabulary_)

X_test = vectorizer.fit_transform(train_docs)
print(X_test.toarray())