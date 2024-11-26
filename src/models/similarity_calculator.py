import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class SimilarityCalculator:
    @staticmethod
    def calculate_cosine_similarity(matrix1, matrix2):
        return cosine_similarity(matrix1, matrix2)
    
    @staticmethod
    def calculate_euclidean_similarity(matrix1, matrix2):
        return 1 / (1 + np.linalg.norm(matrix1[:, np.newaxis] - matrix2, axis=2))