import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class GuildRecommender:
    def __init__(self, user_data, guild_data):
        self.user_data = user_data
        self.guild_data = guild_data
    
    def calculate_similarity(self, user_features, guild_features):
        return cosine_similarity(user_features, guild_features)
    
    def recommend_guilds(self, user_id, top_n=5):
        user_features = self.user_data[['level', 'pvp_ratio', 'social_activity']]
        guild_features = self.guild_data[['avg_level', 'pvp_focus', 'activity_rate']]
        
        similarity_matrix = self.calculate_similarity(user_features, guild_features)
        user_similarities = similarity_matrix[user_id]
        
        # 유저 레벨이 길드 최소 레벨 요구사항을 충족하는지 확인
        user_level = self.user_data.iloc[user_id]['level']
        valid_guilds = self.guild_data['min_level_req'] <= user_level
        
        # 최종 추천 점수 계산
        recommendations = []
        for guild_id in range(len(self.guild_data)):
            if valid_guilds.iloc[guild_id]:
                guild_score = user_similarities[guild_id]
                recommendations.append((guild_id, guild_score))
        
        # 상위 N개 길드 추천
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:top_n]