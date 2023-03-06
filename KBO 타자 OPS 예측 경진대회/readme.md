# KBO 타자 OPS 예측 경진대회
---
- https://dacon.io/competitions/official/62540/overview/description


### 목적
---
- 2019년 타자들의 상반기 OPS를 예측하는 모델 개발

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
프로젝트 구조
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
