class RecommendationMetrics:
    """추천 시스템 성능 측정 메트릭스"""
    
    @staticmethod
    def calculate_precision_at_k(recommended_items, relevant_items, k):
        """Top-K Precision 계산"""
        if len(recommended_items) > k:
            recommended_items = recommended_items[:k]
        
        hits = len(set(recommended_items) & set(relevant_items))
        return hits / k if k > 0 else 0
    
    @staticmethod
    def calculate_recall_at_k(recommended_items, relevant_items, k):
        """Top-K Recall 계산"""
        if len(recommended_items) > k:
            recommended_items = recommended_items[:k]
            
        hits = len(set(recommended_items) & set(relevant_items))
        return hits / len(relevant_items) if len(relevant_items) > 0 else 0