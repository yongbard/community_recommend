import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

from src.data.data_generator import DataGenerator
from src.data.data_preprocessor import DataPreprocessor
from src.data.data_validator import DataValidator
from src.models.recommender import GuildRecommender
from src.models.similarity_calculator import SimilarityCalculator
from src.utils.logger import CustomLogger  # 추가된 import
from src.utils.metrics import RecommendationMetrics  # 추가된 import

class GameRecommendationSystem:
    def __init__(self):
        # 로그 디렉토리 생성
        os.makedirs('logs', exist_ok=True)
        log_file = f'logs/recommender_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
        self.logger = CustomLogger("GameRecommender", log_file)
        self.metrics = RecommendationMetrics()
        
    def generate_sample_data(self):
        """샘플 데이터 생성"""
        print("Generating sample data...")
        generator = DataGenerator()
        
        self.user_data = generator.generate_user_data(n_users=1000)
        self.guild_data = generator.generate_guild_data(n_guilds=50)
        
        print(f"Generated {len(self.user_data)} user records and {len(self.guild_data)} guild records")
        
    def validate_data(self):
        """데이터 유효성 검증"""
        print("Validating data...")
        validator = DataValidator()
        
        user_valid, user_validations = validator.validate_user_data(self.user_data)
        guild_valid, guild_validations = validator.validate_guild_data(self.guild_data)
        
        if not user_valid:
            print("User data validation failed:", user_validations)
            raise ValueError("User data validation failed")
            
        if not guild_valid:
            print("Guild data validation failed:", guild_validations)
            raise ValueError("Guild data validation failed")
            
        print("Data validation completed successfully")
        
    def preprocess_data(self):
        """데이터 전처리"""
        print("Preprocessing data...")
        preprocessor = DataPreprocessor()
        
        self.processed_user_data = preprocessor.preprocess_user_data(self.user_data)
        self.processed_guild_data = preprocessor.preprocess_guild_data(self.guild_data)
        
        print("Data preprocessing completed")
        
    def generate_recommendations(self, user_id, top_n=5):
        """추천 생성"""
        print(f"Generating recommendations for user {user_id}")
        
        recommender = GuildRecommender(self.processed_user_data, self.processed_guild_data)
        recommendations = recommender.recommend_guilds(user_id, top_n)
        
        print(f"Generated {len(recommendations)} recommendations")
        return recommendations
        
    def generate_report(self, user_id, recommendations):
        """분석 리포트 생성"""
        print("Generating analysis report...")
        
        user_info = self.user_data.loc[user_id]
        
        report = f"""
        게임 커뮤니티 추천 분석 리포트
        =============================
        생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        
        유저 프로필
        -----------
        유저 ID: {user_id}
        레벨: {user_info['level']}
        플레이타임: {user_info['play_time']:.1f} 시간
        PvP 성향: {user_info['pvp_ratio']:.1%}
        소셜 활동성: {user_info['social_activity']:.1%}
        접속 빈도: {user_info['login_frequency']:.1%}
        
        추천된 길드
        -----------
        """
        
        for i, (guild_id, score) in enumerate(recommendations, 1):
            guild_info = self.guild_data.iloc[guild_id]
            report += f"""
        {i}. 길드 {guild_id}
           매칭 점수: {score:.2f}
           평균 레벨: {guild_info['avg_level']:.1f}
           길드원 수: {guild_info['size']}
           PvP 중심도: {guild_info['pvp_focus']:.1%}
           활동성: {guild_info['activity_rate']:.1%}
           최소 레벨 요구사항: {guild_info['min_level_req']}
           """
        
        return report

def main():
    # 시스템 초기화
    system = GameRecommendationSystem()
    
    try:
        # 데이터 준비
        system.generate_sample_data()
        system.validate_data()
        system.preprocess_data()
        
        # 테스트 유저에 대한 추천 생성
        test_user_id = 42
        recommendations = system.generate_recommendations(test_user_id)
        
        # 리포트 생성 및 출력
        report = system.generate_report(test_user_id, recommendations)
        print("\n생성된 리포트:")
        print(report)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise
    
    print("Recommendation process completed successfully")

if __name__ == "__main__":
    main()