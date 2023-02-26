import numpy as np

# 팀 통합
def team_change(team):

    if team == "쌍방울":
        team = "SK"

    elif team == "OB":
        team = "두산"
    
    elif team == "해태":
        team = "KIA"

    elif team == "우리":
        team = "넥센"
    
    elif team == "히어로즈":
        team = "넥센"

    else:
        team

    return team

# 몸무게로 변환
def weigth(kg):

    # 몸무게가 3자리인 선수 고려
    if len(kg) == 11:

        kg = str(kg)[6:9]

    else:
        kg = str(kg)[6:8]

    return int(kg)

# 몸무게 범주화
def weight_to_category(kg):

    if kg >= 94:
        
        x = int(3)

    elif kg >= 85:

        x = int(2)

    elif kg >= 78:

        x = int(1)

    elif kg >= 0 and kg < 78:

        x = int(0)

    else:

        x = np.NaN

    return x

# 나이 범주화
def age_to_category(age):

    if age >= 38:

        age = 3

    elif age >= 29:
        
        age = 2

    elif age >= 23:

        age = 1

    else:

        age = 0

    return age