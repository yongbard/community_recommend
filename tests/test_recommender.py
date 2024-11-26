import pytest
import pandas as pd
import numpy as np
from src.models.recommender import GuildRecommender

class TestGuildRecommender:
    @pytest.fixture
    def sample_data(self):
        """테스트용 샘플 데이터 생성"""
        user_data = pd.DataFrame({
            'user_id': range(3),
            'level': [10, 20, 30],
            'pvp_ratio': [0.2, 0.5, 0.8],
            'social_activity': [0.3, 0.6, 0.9]
        })
        
        guild_data = pd.DataFrame({
            'guild_id': range(2),
            'avg_level': [15, 25],
            'pvp_focus': [0.3, 0.7],
            'activity_rate': [0.4, 0.8]
        })
        
        return user_data, guild_data
    
    def test_recommendation_output(self, sample_data):
        """추천 시스템 출력 테스트"""
        user_data, guild_data = sample_data
        recommender = GuildRecommender(user_data, guild_data)
        
        recommendations = recommender.recommend_guilds(user_id=0, top_n=2)
        
        assert len(recommendations) == 2
        assert all(isinstance(r[0], int) for r in recommendations)
        assert all(isinstance(r[1], float) for r in recommendations)
        
    def test_similarity_calculation(self, sample_data):
        """유사도 계산 테스트"""
        user_data, guild_data = sample_data
        recommender = GuildRecommender(user_data, guild_data)
        
        similarity = recommender.calculate_similarity(
            user_data[['level', 'pvp_ratio', 'social_activity']],
            guild_data[['avg_level', 'pvp_focus', 'activity_rate']]
        )
        
        assert similarity.shape == (3, 2)
        assert np.all(similarity >= -1) and np.all(similarity <= 1)