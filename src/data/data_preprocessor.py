# src/data/data_preprocessor.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    """데이터 전처리를 위한 클래스"""
    
    def __init__(self):
        self.scaler = StandardScaler()
        
    def preprocess_user_data(self, user_data):
        """유저 데이터 전처리"""
        features = ['level', 'play_time', 'pvp_ratio', 'social_activity', 'login_frequency']
        scaled_data = pd.DataFrame(
            self.scaler.fit_transform(user_data[features]),
            columns=features,
            index=user_data.index
        )
        return scaled_data
    
    def preprocess_guild_data(self, guild_data):
        """길드 데이터 전처리"""
        features = ['avg_level', 'size', 'pvp_focus', 'activity_rate', 'min_level_req']
        scaled_data = pd.DataFrame(
            self.scaler.fit_transform(guild_data[features]),
            columns=features,
            index=guild_data.index
        )
        return scaled_data