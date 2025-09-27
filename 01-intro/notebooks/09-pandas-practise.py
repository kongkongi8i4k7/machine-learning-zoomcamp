import pandas as pd
import numpy as np

#DataFrames
#NA用None
data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=columns)
print(df)

data2 = [
    {
        "Make": "Nissan",
        "Model": "Stanza",
        "Year": 1991,
        "Engine HP": 138.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "sedan",
        "MSRP": 2000
    },
    {
        "Make": "Hyundai",
        "Model": "Sonata",
        "Year": 2017,
        "Engine HP": None,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "Sedan",
        "MSRP": 27150
    },
    {
        "Make": "Lotus",
        "Model": "Elise",
        "Year": 2010,
        "Engine HP": 218.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "convertible",
        "MSRP": 54990
    },
    {
        "Make": "GMC",
        "Model": "Acadia",
        "Year": 2017,
        "Engine HP": 194.0,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "4dr SUV",
        "MSRP": 34450
    },
    {
        "Make": "Nissan",
        "Model": "Frontier",
        "Year": 2017,
        "Engine HP": 261.0,
        "Engine Cylinders": 6,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "Pickup",
        "MSRP": 32340
    }
]
print('----------------')
df= pd.DataFrame(data2)
print(df)
print('----------------')
df_haed= df.head(2)#df_haed= df.head(n = 2)
print(df_haed)
#访问col
print(df.Make)#print(df['Make'])，当有空格或者-，只能用后者

#df['Make']                 # 传进去的是字符串 str取单列 → 返回 Series
#df[['Make','Model','MSRP']]  # 传进去的是列表 list 取多列 → 返回 DataFrame
#df['Make','Model','MSRP']    # 实际上传进去的是元组 tuple，逗号 优先于中括号 [] 的索引运算。只有在 df.columns 是 MultiIndex 的时候才可能合法，否则报错

df['id']=[1,2,3,4,5]
print(df)
print(df['id'])
del df['id']
print(df.index)#RangeIndex(start=0, stop=5, step=1),index:df.index 是 DataFrame 的一个属性（attribute），
#不是方法。Row labels），类型通常是 pd.Index
print(df.Make.index)#RangeIndex(start=0, stop=5, step=1)

#row+index
print(df.loc[1])#label-based location逻辑索引，可以行名/列名/等
print(df.iloc[1])#integer location位置索引，只能整数/整数列表/切片
print(df.loc[[1,2]])#单个标签 → 返回 Series，标签列表 / slice / 布尔数组 → 返回 DataFrame，返回的是表格形式，不是 Series
df.index=['a','b','c','d','e']#df.index 序列容器，row labels,需要一个 可迭代对象，tuple 是可迭代的，
#用列表，pandas 会自动把它转换成一个 Index 对象，#DataFrame的属性， 状态信息， 类型是pd.Index,
                                #df.index = pd.Index(['a','b','c'])
                
print(df.loc['a'])
print(df.loc[['a','b','c']])

print(df.iloc[[1,3]])
df.reset_index()#0,1...
df.reset_index(drop = True)#不要旧索引
print('--------')
#元素操作
print(df[['Engine HP','MSRP']]/100)
#Filterings
print(df['Year'] >= 2000)#返回的不是Dataframe,而是TRUE,FALSE
print(df[df['Year'] >= 2000])#返回的是Dataframe

print(df[
    (df['Model'] == 'Elise') & (df['Year'] >= 2000)
    ]) 
#字符串  #这个NP没有，NP主要处理数字，这个可以处理字符串？
df['Vehicle_Style'] = df['Vehicle_Style'].str.lower().str.replace(' ' , '_')
#.str.replace()：pandas 的字符串方法访问器 (Series.str)对 每个字符串元素内部的子串 做替换
#所以能处理 "Sport Car" → "sport_car"
#.replace()：Series/DataFrame 的通用替换方法。整个元素值 进行匹配替换，不会在字符串内部做子串替换
print(df)
s = pd.Series(["Sport Car", "SUV"])
print(s.replace(" ", "_"))# 没有任何变化，因为 Series 里没有元素恰好等于 " "。

#统计学
print("统计学")
print(df.MSRP.max())
print(df.MSRP.mean())
print(df.MSRP.describe())
print("df.describe()")
print(df.describe().round(2))#四舍五入，round:凑整，四舍五入
print(df.Make.nunique())#4,df.nunique()，摘要
#查看是否缺失值
print(df.isnull())#True/False
print('-----')
print(df.isnull().sum())#对列求和，每列缺失值
#Grouping
#根据Transmission Type分组成MANUAL，AUTOMATIC，计算每组MSRP平均值
print(df.groupby('Transmission Type').MSRP.mean())

#getting the Numpy arrays
print(df.MSRP)#Series
print(df.MSRP.values)#值array[ 2000 27150 54990 34450 32340]
print(df.to_dict(orient='records'))