# 2021-06-17

> 오늘 한 내용 정리이기에 조회하는 코드들과 중복 되는 의미의 코드는 생략하고 갑니다

---



## SQL

### INSERT 

```sql
insert into 테이블(추가할 칼럼들), vlues(추가할 밸류값);
```

### DELETE 

``` sql
# where 뒤에 삭제할 조건을 쓴다
delete from 테이블 where 칼럼 = '조건';
```



## Data Understanding

### 타겟지정 : tip

```python
import pymysql.cursors
import pandas as pd

# 불러오기
conn = pymysql.connect(host='localhost', user='zeros', 
                       password='160525', db='tip', charset='utf8',
                       autocommit=True, cursorclass=pymysql.cursors.DictCursor)
try:
    with conn.cursor() as curs:
        sql = "select * from tips;"
        curs.execute(sql)
        rs = curs.fetchall()
        df = pd.DataFrame(rs)
finally:
    conn.close()
```



### 데이터 Encoding

```python
df["sex"] = df["sex"].replace({"Female" : 0, "Male" : 1})
df["smoker"] = df["smoker"].replace({"No" : 0, "Yes" : 1})
df["day"] = df["day"].replace({"Thur" : 0, "Fri" : 1, "Sat" : 2, "Sun" : 3})
df["time"] = df["time"].replace({"Lunch" : 0, "Dinner" : 1})
# tip_rate 파생변수 추가 
df['tip_rate']= df['tip']/df['total_bill']

# 파생변수를 추가 한 후 null값 처리를 하기위해 조회
df.isnull().sum()
```



### Null 값 처리

```python
from numpy import isnan
from sklearn.impute import SimpleImputer


y = df['tip'] # y=타겟
X = df.drop('tip',axis=1) #학습할 x에서 tip을 드랍

data = X.values
y = y.values

#NULL값 확인
sum(isnan(data).flatten()), sum(isnan(y).flatten())

#IMPUTED DATA SET, Null 값 처리
imputer = SimpleImputer(strategy='median')
imputer.fit(data)
data_trans = imputer.transform(data) 
```



### RFE : 중요도 낮은 칼럼 숙청

```python
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

rfe = RFE(estimator=SVR(kernel="linear"), n_features_to_select=4)
rfe.fit(df1, y)
#랭킹 보기(중요도)
for i in range(df1.shape[1]):
  print('Column: %d, Selected=%s, Rank: %d' % (i, rfe.support_[i], rfe.ranking_[i]))

# 랭킹에 따라서 랭킹1위를 제외한 나머지는 숙청
df1.drop(['sex','smoker','size'], axis=1)
```





### pca

``` python
from sklearn.decomposition import PCA
# pca변형을 정의
trans = PCA(n_components=7)

# 데이터변환
X_dim = trans.fit_transform(data_trans)

# 설명력이 높은 순의 데이터 출력
trans.explained_variance_ratio_.
# 다시 데이터프레임으로 보기
data_pca = pd.DataFrame(X_dim)
data_pca.describe().round(2)



```



### Regression Feature Selection
```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

fs = SelectKBest(score_func=f_regression, k=4)
# apply feature selection
X_selected = fs.fit_transform(df1, y)

print(X_selected.shape)

df3 = pd.DataFrame(X_selected)
df3
```



수업 중 내용(순서없음 그냥 들리는 대로 적음)  

- flatten() :1줄로 컬럼을 이어놓고 어레이 갯수를 새어줌

- pca 는 독립변수들끼리의 상관관계만으로만 차원을 축소시키고 rfe는 독립변수들과 목표변수와의 관계를 통해 차원을 축소시킨다.
- Data Understanding => 목표변수를 정의 하는 게 중요

