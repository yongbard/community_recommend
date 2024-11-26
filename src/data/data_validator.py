# src/data/data_validator.py
import pandas as pd
import numpy as np

class DataValidator:
    """데이터 유효성 검증 클래스"""
    
    @staticmethod
    def validate_user_data(df):
        """유저 데이터 유효성 검증"""
        validations = {
            'user_id': len(df['user_id'].unique()) == len(df),
            'level': df['level'].between(1, 100).all(),
            'play_time': (df['play_time'] >= 0).all(),
            'pvp_ratio': df['pvp_ratio'].between(0, 1).all(),
            'social_activity': df['social_activity'].between(0, 1).all(),
            'login_frequency': df['login_frequency'].between(0, 1).all()
        }
        
        validation_results = {k: bool(v) for k, v in validations.items()}
        return all(validation_results.values()), validation_results
    
    @staticmethod
    def validate_guild_data(df):
        """길드 데이터 유효성 검증"""
        validations = {
            'guild_id': len(df['guild_id'].unique()) == len(df),
            'avg_level': df['avg_level'].between(1, 100).all(),
            'size': df['size'].between(1, 100).all(),
            'pvp_focus': df['pvp_focus'].between(0, 1).all(),
            'activity_rate': df['activity_rate'].between(0, 1).all(),
            'min_level_req': df['min_level_req'].between(1, 100).all()
        }
        
        validation_results = {k: bool(v) for k, v in validations.items()}
        return all(validation_results.values()), validation_results