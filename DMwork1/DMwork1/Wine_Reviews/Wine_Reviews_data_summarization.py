import numpy as np
import pandas as pd
from pandas import DataFrame


#读取数据
def loader():
    filepath ="C:/Users/lenovo/Desktop/Wine_Reviews/winemag-data-130k-v2.csv" #使用的数据集文件地址
    data = pd.read_csv(filepath, header=0)
    return data

#输出标称数据频数
def count(str1,data1):
    print(data1[str1].value_counts())

#输出数值数据缺失值的个数
def NullNumber(str2,data2):
    nums = data2[str2]
    nullnum = nums.isnull().sum()
    print("null:%d"%(nullnum))

#输出数值数据的5数概括Minimum（最小值）、Q1、Median（中位数）、Q3、Maximum（最大值）
def FiveNumber(str3,data3):
    nums = data3[str3]
    nums = nums.dropna(axis = 0) #删除NaN值
    Minimum = min(nums)
    Maximum = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)
    print("Minimum:%d; Q1:%d; Median:%d; Q3:%d; Maximum:%d;"%(Minimum , Q1 , Median , Q3 , Maximum)) #都为整数







if __name__ == "__main__":
    data = loader()

    #输出标称数据的每个可能的频数
    print("country频数：")
    count("country",data)
    print("designation频数：")
    count("designation",data)
    print("province频数：")
    count("province",data)
    print("region_1频数：")
    count("region_1",data)
    print("region_2频数：")
    count("region_2",data)
    print("variety频数：")
    count("variety",data)
    print("winery频数：")
    count("winery",data)

    #输出数值数据缺失值的个数
    print("points缺失值的个数:")
    NullNumber("points", data)
    print("price缺失值的个数:")
    NullNumber("price", data)

    #输出数值数据的5数概括
    print("points的5数概括:")
    FiveNumber("points",data)
    print("price的5数概括:")
    FiveNumber("price",data)
