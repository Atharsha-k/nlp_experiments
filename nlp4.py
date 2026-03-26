import sys

# Install gensim
!{sys.executable} -m pip install gensim

from gensim.models import Word2Vec

# Sample sentences
sentences = [
    ["natural", "language", "processing"],
    ["natural", "language", "understanding"],
    ["machine", "learning", "models"],
    ["deep", "learning", "neural", "networks"],
    ["word", "embedding", "using", "word2vec"],
    ["word", "embedding", "techniques"],
    ["artificial", "intelligence", "applications"],
    ["nlp", "uses", "machine", "learning"]
]

# Train Word2Vec model
model = Word2Vec(
    sentences,
    vector_size=100,
    window=4,
    min_count=1,
    sg=1   # Skip-gram model
)

# Vocabulary
print("VOCABULARY:")
print(model.wv.index_to_key)

# Word vector
print("\nWORD VECTOR FOR 'language':")
print(model.wv["language"])

# Similar words
print("\nWORDS SIMILAR TO 'language':")
for word, score in model.wv.most_similar("language", topn=5):
    print(word, ":", round(score, 3))

# Similarity scores
print("\nSIMILARITY BETWEEN 'language' AND 'processing':")
print(round(model.wv.similarity("language", "processing"), 3))

print("\nSIMILARITY BETWEEN 'learning' AND 'models':")
print(round(model.wv.similarity("learning", "models"), 3))