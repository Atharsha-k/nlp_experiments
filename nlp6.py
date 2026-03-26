# Install required library
!pip install scikit-learn

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Sample dataset
texts = [
    "I love this movie",
    "This film was amazing",
    "What a fantastic performance",
    "I enjoyed the story",
    "Absolutely wonderful experience",
    "I hate this movie",
    "This film was terrible",
    "What a boring performance",
    "I disliked the story",
    "Awful and disappointing experience"
]

labels = [
    "positive", "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative", "negative"
]

# TEXT VECTORIZATION
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# NAIVE BAYES MODEL
nb_model = MultinomialNB()
nb_model.fit(X, labels)

nb_predictions = nb_model.predict(X)
nb_accuracy = accuracy_score(labels, nb_predictions)

# SVM MODEL
svm_model = SVC(kernel='linear')
svm_model.fit(X, labels)

svm_predictions = svm_model.predict(X)
svm_accuracy = accuracy_score(labels, svm_predictions)

# OUTPUT
print("=== TEXT CLASSIFICATION RESULTS ===")
print(f"Naive Bayes Accuracy: {nb_accuracy:.2f}")
print(f"SVM Accuracy: {svm_accuracy:.2f}")