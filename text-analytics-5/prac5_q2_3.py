from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances


# doc1 = 'The plan for these days is really just to introduce the course.'
# doc1 = 'The plan for these days is really just to introduce the course. The plan'
# doc1 = 'The plan for these days is really just to introduce the course. The plan for these'
# doc1 = 'The plan for these days is really just to introduce the course. The plan for these days is'
doc1 = 'The plan for these days is really just to introduce the course. The plan for these days is really just'
# doc1 = 'The plan for these days is really just to introduce the course. \
#          The plan for these days is really just to introduce the course.'
doc2 = 'Look at some of the software we will use and to get this software installed; \
        get us all on the same page with respect to a basic level environment to use.'
doc3 = 'Note that the first value of the array is 1.0 because it is the Cosine Similarity\
        between the first document with itself.'
docs = [doc1, doc2, doc3] #Documents

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(docs)
print(tfidf_matrix.shape)

# calculate the cosine similarity between the first doc with each of other documents.
cos_sim_result = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)     # tfidf_matrix[0:1] scipy operation to get the first row
print(cos_sim_result)

euc_dis = euclidean_distances(tfidf_matrix[0:1], tfidf_matrix)
print(euc_dis)
