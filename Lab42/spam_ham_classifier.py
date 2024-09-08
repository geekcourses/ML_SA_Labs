from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import numpy as np

# Define the dataset (emails and their corresponding class: Spam or Ham)
emails = [
    'free offer',       # spam
    'free meeting',     # spam
    'free',             # spam
    'offer',            # ham
    'meeting',          # ham
]

# Corresponding labels: 1 for spam, 0 for ham
labels = [1, 1, 1, 0, 0]

# Vectorize the data to create a bag-of-words model (binary: presence/absence of words)
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(emails)

# Initialize the Bernoulli Naive Bayes classifier
bnb = BernoulliNB(alpha=1)

# Train the classifier
bnb.fit(X, labels)

# Test it on a new email containing 'free' and 'offer', but not 'meeting'
new_email = ['free offer']
X_test = vectorizer.transform(new_email)

# Predict the class for the new email
predicted_class = bnb.predict(X_test)

# Print predicted class and probabilities for each class
print(f'predicted class: {predicted_class}')
print(f'probabilities for each class: ${bnb.predict_proba(X_test)}')
print('~'*80)

# Print the likelihood probabilities for each class (Spam, Ham)
log_likelihoods = bnb.feature_log_prob_
likelihoods = np.exp(log_likelihoods) # Convert log probabilities to actual probabilities
print(f'Likelihoods (Spam first, then Ham):\n{likelihoods}')
print('~'*80)

# Print feature counts for each class (Spam and Ham)
feature_counts = bnb.feature_count_
print(f'Feature counts (Spam first, then Ham):\n{feature_counts}')
print('~'*80)

# Print CountVectorizer details:
print(f'Vocabulary: {vectorizer.vocabulary_}')
print(f'Vectorised emails:\n{X.toarray()}')