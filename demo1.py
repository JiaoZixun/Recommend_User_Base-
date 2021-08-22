import pandas as pd
import numpy as np
import math


#建立用户-评分矩阵
user_rating = np.zeros((944, 1683))#数据集共943个用户，1682部电影
#print(user_rating)
def Create_User_rating_Table(data):
    for it in data:
        user_rating[it[0]][it[1]]=it[2]
    print(user_rating)
    outfile = "F:\\协同过滤推荐算法\\基于用户\\user_rating.csv"
    data1=pd.DataFrame(user_rating)
    #print(data1.shape)
    data1.to_csv(outfile, index=False, header=False)

#建立倒排表
def Create_Item_user_Table(data):
    #对用户-评分矩阵进行转置
    item_user = np.transpose(data)
    #print(item_user)
    outfile = "F:\\协同过滤推荐算法\\基于用户\\item_user.csv"
    data1 = pd.DataFrame(item_user)
    data1.to_csv(outfile, index=False, header=False)
    return item_user

#建立相似度矩阵
def Create_Sim_Matrix(item_users):
    N = np.zeros(944)  # 943位用户的评分数量
    C = np.zeros((944,944))#分子
    for i in range(1,1683):
        for j in range(1,944):#从每一部电影中取出每个用户的评分，若为0则表示该用户没有观看该部电影
            if item_users[i][j] != 0:
                N[j]+=1
                for k in range(1,944):
                    if item_users[i][k] != 0:
                        if j==k:
                            continue
                        C[j][k]+=1
    #计算相似度
    W = np.zeros((944,944))
    for u in range(1,944):
        for v in range(1,944):
            if u == v:
                continue
            W[u][v]=C[u][v]/math.sqrt(N[u]*N[v])
    #print(W)
    outfile = "F:\\协同过滤推荐算法\\基于用户\\user_sim.csv"
    data1 = pd.DataFrame(W)
    data1.to_csv(outfile, index=False, header=False)

file="F:\\协同过滤推荐算法\\ml-100k\\u1.base"
lieming=["用户id", "电影id", "评分", "时间"]
data = pd.read_table(file, names=lieming)
#print(data)
list_data = np.array(data)#转换数组
#print(list_data)
data=list_data.tolist()#转换list
#print(type(data))

Create_User_rating_Table(data)
item_users=Create_Item_user_Table(user_rating)
Create_Sim_Matrix(item_users)#得到相似度矩阵
