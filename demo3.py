import pandas as pd
import numpy as np

Top=[]
def Top_N(n):
    for item in recommend:
        recomm=[]
        for it in item:
            recomm.append(it)
        recomm.sort(key=lambda x:x[1], reverse=True)
        print(recomm[0:n])
        Top.append(recomm[0:n])
    Top_N_data=pd.DataFrame(Top)
    outfile="F:\\协同过滤推荐算法\\基于用户\\Top_N.csv"
    Top_N_data.to_csv(outfile,index=False,header=False)

file="F:\\协同过滤推荐算法\\基于用户\\Recommend.csv"
data=pd.read_csv(file, header=None)
print(data.shape)
print(data)
data1=np.array(data)
recommend=data1.tolist()
#print(type(recommend))

Top_N(10)#Top-N推荐，N取10