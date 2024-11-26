import matplotlib.pyplot as plt
import seaborn as sns

class RecommendationVisualizer:
    """추천 결과 시각화 클래스"""
    
    def __init__(self, user_data, guild_data):
        self.user_data = user_data
        self.guild_data = guild_data
    
    def plot_user_profile(self, user_id):
        """유저 프로필 시각화"""
        plt.figure(figsize=(8, 5))
        sns.barplot(
            x=['Level', 'Play Time', 'PvP Ratio', 'Social Activity', 'Login Freq'],
            y=self.user_data.iloc[user_id][['level', 'play_time', 'pvp_ratio', 'social_activity', 'login_frequency']]
        )
        plt.title(f'User {user_id} Profile')
        plt.xticks(rotation=45)
    
    def plot_guild_recommendations(self, recommended_guilds):
        """추천된 길드 특성 시각화"""
        categories = ['Level Match', 'PvP Focus', 'Social Activity', 'Size', 'Activity Rate']
        plt.figure(figsize=(10, 6))
        for guild_id, score in recommended_guilds:
            guild_data = self.guild_data.iloc[guild_id]
            self._plot_guild_characteristics(categories, guild_data, score)
        plt.title('Recommended Guilds Characteristics')
        plt.legend(bbox_to_anchor=(1.05, 1))