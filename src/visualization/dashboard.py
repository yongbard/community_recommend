import matplotlib.pyplot as plt
import seaborn as sns

class RecommendationDashboard:
    """추천 시스템 대시보드"""
    
    def __init__(self, user_data, guild_data, recommendations):
        self.user_data = user_data
        self.guild_data = guild_data
        self.recommendations = recommendations
        
    def create_dashboard(self, user_id):
        """종합 대시보드 생성"""
        plt.figure(figsize=(20, 10))
        
        # 유저 프로필
        plt.subplot(231)
        self._plot_user_profile(user_id)
        
        # 추천된 길드 특성
        plt.subplot(232)
        self._plot_guild_characteristics()
        
        # 유사도 히트맵
        plt.subplot(233)
        self._plot_similarity_heatmap()
        
        # 길드 크기 분포
        plt.subplot(234)
        self._plot_guild_size_distribution()
        
        # 레벨 매칭 분석
        plt.subplot(235)
        self._plot_level_matching(user_id)
        
        # 활동성 비교
        plt.subplot(236)
        self._plot_activity_comparison()
        
        plt.tight_layout()
        
    def _plot_user_profile(self, user_id):
        """유저 프로필 시각화"""
        user = self.user_data.iloc[user_id]
        features = ['level', 'play_time', 'pvp_ratio', 'social_activity', 'login_frequency']
        
        sns.barplot(x=features, y=[user[f] for f in features])
        plt.title('User Profile')
        plt.xticks(rotation=45)
        
    def _plot_guild_characteristics(self):
        """길드 특성 방사형 차트"""
        recommended_guilds = self.recommendations
        categories = ['Level', 'PvP', 'Activity', 'Size', 'Requirements']
        
        for guild_id, score in recommended_guilds:
            values = self.guild_data.iloc[guild_id][
                ['avg_level', 'pvp_focus', 'activity_rate', 'size', 'min_level_req']
            ]
            plt.plot(categories, values, label=f'Guild {guild_id}')
            
        plt.title('Guild Characteristics')
        plt.legend()