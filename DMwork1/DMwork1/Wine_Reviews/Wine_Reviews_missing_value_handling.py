import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")
def FiveNumber(str3,data3):
    nums = data3[str3]
    nums = nums.dropna(axis = 0) #删除NaN值
    Minimum = min(nums)
    Maximum = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)
    print("Minimum:%d; Q1:%d; Median:%d; Q3:%d; Maximum:%d;"%(Minimum , Q1 , Median , Q3 , Maximum)) #都为整数

wine_reviews = pd.read_csv("C:/Users/lenovo/Desktop/Wine_Reviews/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.columns)

wine_reviews_price = wine_reviews['price']


"""
#将缺失部分剔除

wine_reviews_price = wine_reviews_price.dropna(how='any')


print("price的5数概括:")
FiveNumber("price",wine_reviews)

#画price盒图
wine_reviews_price.plot.box()
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='blue', alpha=0.75)
plt.show()
"""


"""
#用最高频率值来填补缺失值

wine_reviews.price[wine_reviews.price.isnull()] = wine_reviews.price.dropna().mode().values

wine_reviews_price = wine_reviews['price']


print("price的5数概括:")
FiveNumber("price",wine_reviews)

#画price盒图
wine_reviews_price.plot.box()
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='blue', alpha=0.75)
plt.show()

"""

"""
#通过属性的相关关系来填补缺失值
from sklearn.impute import SimpleImputer

df_relation = wine_reviews[['price']]
Simpleimp = SimpleImputer(missing_values=np.nan, strategy='mean')
Simpleimp.fit(df_relation)
df_relation = Simpleimp.transform(df_relation)
wine_reviews_price = pd.DataFrame(df_relation, columns = ['price'])

print("price的5数概括:")
FiveNumber("price",wine_reviews)

#画price盒图
wine_reviews_price.plot.box()
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='blue', alpha=0.75)
plt.show()
"""
"""
#通过数据对象之间的相似性来填补缺失值
new_wine_reviews = wine_reviews.dropna(subset=['price'])
x = new_wine_reviews['points']
y = new_wine_reviews['price']

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

X = np.array(x).reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

new_wine_reviews = wine_reviews.copy()
for index, row in new_wine_reviews[wine_reviews['price'].isna()].iterrows():
    new_wine_reviews['price'][index] = model.predict(np.array(row['points']).reshape(-1, 1))

print(new_wine_reviews.info())
wine_reviews_price = new_wine_reviews['price']
print("price的5数概括:")
FiveNumber("price",new_wine_reviews)

#画price盒图
wine_reviews_price.plot.box()
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='blue', alpha=0.75)
plt.show()
"""
