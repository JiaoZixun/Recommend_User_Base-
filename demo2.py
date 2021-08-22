import pandas as pd
import numpy as np

#计算用户u对电影i的感兴趣程度
def Count_User_Interest(Sim_W,K,item_user):
    Recommend=[]
    for userid in range(1,944):
        P=[]
        for i in range(1,1683):
            cur_user_sim = Sim_W[userid]
            cur_sort=[]
            #print(cur_user_sim)
            for j in range(1,944):#取用户u的K个最近邻和看过电影i的用户之间的交集
                if item_user[i][j]!=0:#若用户j看过第i部电影则将用户j和u对j的相似度加入
                    cur_sort.append([j,cur_user_sim[j]])
            #print(cur_sort)
            cur_sort.sort(key=(lambda x: x[1]), reverse=True)#逆序
            #print(cur_sort[0:K])
            sum=0
            for user_v in cur_sort[0:K]:
                v=user_v[0]
                sum+=user_v[1]*item_user[i][v]
            P.append([i,sum])
        P.sort(key=(lambda x:x[1]), reverse=True)
        Recommend.append(P)
    print(P)
    R=pd.DataFrame(Recommend)
    outfile="F:\\协同过滤推荐算法\\基于用户\\Recommend.csv"
    R.to_csv(outfile, index=False, header=False)

file="F:\\协同过滤推荐算法\\基于用户\\user_sim.csv"
data=pd.read_csv(file, header=None)#header取消列名
user_sim=np.array(data)
#print(user_sim)

file1="F:\\协同过滤推荐算法\\基于用户\\user_rating.csv"
data1=pd.read_csv(file1,header=None)
user_rating=np.array(data1)
#print(user_rating)

file2="F:\\协同过滤推荐算法\\基于用户\\item_user.csv"
data2=pd.read_csv(file2,header=None)
item_user=np.array(data2)
#print(item_user)

Count_User_Interest(user_sim,30,item_user)#选择30个最近邻进行推荐，生成推荐列表
