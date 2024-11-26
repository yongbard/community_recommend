from setuptools import setup, find_packages

setup(
    name="game_community_recommender",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pandas>=2.0.0',
        'numpy>=1.24.0',
        'scikit-learn>=1.2.0',
        'matplotlib>=3.7.0',
        'seaborn>=0.12.0',
        'pyyaml>=6.0.0',
        'pytest>=7.3.0',
    ],
)