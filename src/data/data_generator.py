# src/data/data_generator.py
import numpy as np
import pandas as pd

class DataGenerator:
    """게임 데이터 생성을 위한 클래스"""
    
    def __init__(self, seed=42):
        self.seed = seed
        np.random.seed(seed)
        
    def generate_user_data(self, n_users=1000):
        """유저 데이터 생성"""
        return pd.DataFrame({
            'user_id': range(n_users),
            'level': np.random.randint(1, 100, n_users),
            'play_time': np.random.normal(500, 100, n_users).clip(0),  # 음수 방지
            'pvp_ratio': np.random.random(n_users),
            'social_activity': np.random.random(n_users),
            'login_frequency': np.random.normal(0.7, 0.1, n_users).clip(0, 1)  # 0-1 사이로 제한
        })
    
    def generate_guild_data(self, n_guilds=50):
        """길드 데이터 생성"""
        return pd.DataFrame({
            'guild_id': range(n_guilds),
            'avg_level': np.random.normal(50, 10, n_guilds).clip(1, 100),  # 1-100 사이로 제한
            'size': np.random.randint(10, 100, n_guilds),
            'pvp_focus': np.random.random(n_guilds),
            'activity_rate': np.random.random(n_guilds),
            'min_level_req': np.random.randint(1, 50, n_guilds)
        })