# KBO 타자 OPS 예측 경진대회
---
- https://dacon.io/competitions/official/62540/overview/description


### 목적
---
- 2019년 타자들의 상반기 OPS를 예측하는 모델 개발
- 현재 2023년 이기에 2000년부터 2022년까지의 데이터를 수집하여 데이터를 최신화 하였음

### 데이터 
---
- 데이터 구조
```
${data}
├─ Pre_Season_Batter.csv
├─ Regular_Season_Batter.csv
├─ Regular_Season_Batter_Day_by_Day_b4.csv
└─ submission.csv
```

- 데이터 설명
1. Pre_Season_Batter : KBO에서 활약한 타자들의 역대 정규시즌 성적을 포함하여 몸무게, 키 ,생년월일 등의 기본정보
2. Regular_Season_Batter_Day_by_Day.csv: KBO에서 활약한 타자들의 일자 별 정규시즌 성적
3. Pre_Season_Batter.csv : KBO에서 활약한 타자들의 역대 시범경기(정규시즌 직전에 여는 연습경기) 성적
4. ubmission.csv : 참가자들이 예측해야 할 타자의 이름과 아이디 목록

### 프로젝트 구조
---
```
${PROJECT}
├── results/
├── data/
│   ├─ Pre_Season_Batter.csv
│   ├─ Regular_Season_Batter.csv
│   ├─ Regular_Season_Batter_Day_by_Day_b4.csv
│   └─ submission.csv
├── EDA.ipynb
├── preprocessing.ipynb
└── Model.ipynb
```

### 데이터 분석

- - -

- OPS(종속변수)를 제외하고 25개의 독립변수가 존재

- 야구 선수를 평가할 때 가장 많이 사용하는 WAR(대체 선수 대비 승리 기여도)지표와 BABIP(Batting Average on Balls In Play)이라는 파생변수가 중요할 것이라 판단
  - BABIP이라는 파생변수 생성
    - ![image](https://user-images.githubusercontent.com/110336043/223058799-2641ca71-0857-442e-b945-6e8bd0a68f04.png)

- 다중공선성 문제 해결
   - 야구 데이터의 특성상 다중 공선성이 발생
     - 예) 타율 = (안타+2루타+3루타+홈런) / 타수
     - 예시 처럼 많은 데이터들이 각 데이터 간의 조합을 통하여 데이터가 추가 평가지표가 된다.
     
  1. 랜덤포레스트의 feature_importance를 통한 변수 선택
      - 특성 중요도를 통하여 특성 중요도가 높은 변수들을 선택하여 다시 모델링을 진행
  2. PCA를 통한 차원축소
      - PCA기법을 통하여 데이터를 축소시켜 다중공선성 문제를 해결

- OPS와 상관성이 높은 woBA와 WRC+그리고 장타가 상관계수가 0.9이상으로 나타난다.

  - wOBA(Weighted On-Base Average, 가중 출루율)는 야구에서 쓰이는 통계 지표로서, 타자의 타석당 득점 기여도를 출루율 스케일로 표현한다
  - Weighted Runs Created의 줄임말로 조정 득점 창출력을 말한다. 뒤에 +가 붙은 건 파크팩터 등을 추가로 반영했다는 의미다.

- 이상치 존재
  - 2022년 KBO기준으로 타율이 가장 높은 타자는 82년도 백인천(0.412)선수 인데 규정 타석을 다 채우지 않은 데이터까지 존재하여 이상치 존재
  - ![image](https://user-images.githubusercontent.com/110336043/223059976-b11893d6-7405-40ca-8118-b7bded73405b.png)
  
  - 이상치 제거 후
  - ![image](https://user-images.githubusercontent.com/110336043/223060183-91c81276-cbf9-4122-a47b-5d63b9f50080.png)

- WAR 범주화
  - WAR
    > <span style="color: Grey">Decision of player’s value via WAR (fangraph)</span>
  - ![image](https://user-images.githubusercontent.com/110336043/223062090-ce868fba-b061-4376-8d2c-22d362d681c5.png)
  
  - 위의 기준을 통하여 WAR을 범주화
  - 6이상의 선수는 MVP급 활약을 한 선수, 5\~6 사이의 선수는 Superstar, 4\~5 사이의 선수는 All-star급 활약을 한 선수등 WAR을 수치 자체가아닌 위와 같이 세분화 하여 이산형 자료로 사용하는 것이 더 적절하다고 판단하였음

- 사용 모델

  - PCA(주성분 분석)
  - ARDRegression : 
  
### 피드백 및 추가 개선 사항

- 변수선택법 후진 제거법 적용 후 비교
  - 적용 전 AIC
    - ![image](https://user-images.githubusercontent.com/110336043/223401422-d5b5e188-b772-4e79-958e-19b5c06dea00.png)
  - 적용 후 AIC
    - ![image](https://user-images.githubusercontent.com/110336043/223401512-97008b5b-c7be-4520-93b5-8d9a1831752e.png)
    
    - 후진 제거법을 통하여 변수 선택을 한 결과 AIC가 감소하는 것을 확인 할 수 있다.
    - 선택된 변수 : 타점, 도실, 출루, 장타
    - OPS와 연관성이 깊은 출루와 장타라는 변수가 선택된 것을 확인할 수 있다.


- 시각화를 통하여 실제 선수들의 OPS와 얼마나 차이가 나는지 비교
  - ![image](https://user-images.githubusercontent.com/110336043/223401615-8374d2a6-c2b1-4597-9b54-4f982ebdc4f8.png)

  - ![image](https://user-images.githubusercontent.com/110336043/223401585-35f7aba0-d781-4177-9b45-4b7393c14768.png)
  
  - ![image](https://user-images.githubusercontent.com/110336043/223401740-c494d553-9709-4b5e-ad9a-7fced489c761.png)
  
  - 실제 2022년도의 OPS와 비교했을 때 거의 차이가 안나고 유사하게 그래프가 형성되는 것을 확인 할 수 있다.

