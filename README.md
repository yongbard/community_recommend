# 길드 추천 시스템 문서

## 개요
본 시스템은 게임 플랫폼에서 플레이어들에게 적합한 길드를 추천하는 시스템입니다. 플레이어의 특성, 길드의 특성, 행동 패턴 등 다양한 요소를 고려하여 최적의 매칭을 제공합니다.

## 시스템 구조

### 1. 데이터 생성 (DataGenerator)

#### 플레이어 데이터 구조
```python
{
    'user_id': 42,
    'level': 75,          # 게임 레벨 (1-100)
    'play_time': 450,     # 플레이 시간 (시간)
    'pvp_ratio': 0.8,     # PvP 선호도 (0-1)
    'social_activity': 0.7,# 소셜 활동성 (0-1)
    'login_frequency': 0.9 # 접속 빈도 (0-1)
}
```

#### 길드 데이터 구조
```python
{
    'guild_id': 1,
    'avg_level': 70,      # 길드 평균 레벨
    'size': 45,           # 길드원 수
    'pvp_focus': 0.75,    # PvP 중심도 (0-1)
    'activity_rate': 0.85,# 길드 활동성 (0-1)
    'min_level_req': 30   # 최소 레벨 요구사항
}
```

### 2. 데이터 검증 (DataValidator)

다음과 같은 검증 절차를 수행합니다:

- **범위 검증**
  - 레벨: 1-100 사이
  - 비율 값: 0-1 사이
  - 길드 크기: 양수
- **중복 검사**
  - 사용자 ID 중복 확인
  - 길드 ID 중복 확인

### 3. 데이터 전처리 (DataPreprocessor)

모든 특성을 동일한 스케일로 정규화합니다:
```python
# 정규화 예시
# 정규화 전
level = 75, pvp_ratio = 0.8

# 정규화 후
level = 0.75, pvp_ratio = 0.8  # 0-1 사이 값으로 통일
```

### 4. 추천 시스템 (GuildRecommender)

#### 매칭 알고리즘
1. **코사인 유사도 계산**
   ```python
   # 특성 벡터 예시
   유저_특성 = [0.7, 0.8, 0.9]  # [레벨, PvP, 소셜]
   길드_특성 = [0.75, 0.85, 0.8]
   유사도_점수 = 코사인유사도(유저_특성, 길드_특성)  # 0.95
   ```

2. **필터링 로직**
   ```python
   if 유저_레벨 >= 길드_최소레벨:
       # 추천 후보로 고려
   else:
       # 추천 제외
   ```

3. **최종 점수 계산**
   ```python
   최종_점수 = (코사인유사도 * 0.6 +  # 성향 매칭
              레벨_적합도 * 0.2 +    # 레벨 차이
              활동성_매칭 * 0.2)    # 활동 시간대
   ```

## 시스템 출력 예시

```
추천된 길드 목록:

1. 길드 "드래곤 워리어스"
   * 매칭 점수: 0.92
   * 추천 이유: PvP 성향이 비슷하고 레벨대가 적절함

2. 길드 "소셜 게이머스"
   * 매칭 점수: 0.85
   * 추천 이유: 높은 소셜 활동성과 비슷한 접속 패턴
```

## 시스템 장점
- 다차원 데이터를 활용한 정교한 매칭
- 객관적이고 수치화된 추천 기준
- 확장 가능한 모듈식 구조
- 성능 측정 및 개선이 용이

## 적용 시나리오

### 신규 유저 추천 예시
```python
신규유저 = {
    'level': 15,
    'play_time': 20,
    'pvp_ratio': 0.3,
    'social_activity': 0.9
}

# 추천 결과
추천길드 = "소셜 초보자 길드"
추천이유 = "초보자 친화적이며 사교적인 분위기의 길드"
```

## 기대 효과
- 유저 만족도 증가
- 길드 활성화 촉진
- 게임 참여도 향상
- 장기 유저 확보

## 향후 발전 방향
1. 실시간 데이터 분석 및 반영
2. 머신러닝 모델 도입
3. 유저 피드백 시스템 구축
4. 시즌별 특성 반영

## 결론
본 추천 시스템은 게임의 소셜 요소를 강화하고 유저 경험을 개선하는데 핵심적인 역할을 합니다. 특히 대형 게임사의 경우, 이를 통해 건강한 게임 커뮤니티 형성과 장기적인 게임 생태계 구축이 가능합니다.