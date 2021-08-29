# 基于用户的协同过滤算法

## 1. 数据

使用movielens-100k数据集中的u1.base文件作为实验集

## 2.实验

在demo1中建立用户-评分矩阵和项目-用户矩阵，根据项亮的《推荐系统实践》中建立倒排表，然后计算用户相似度。

用户评分矩阵

![1](https://github.com/JiaoZixun/Recommend_User_Base-/blob/master/img/1.jpg)

项目用户矩阵（用户评分矩阵转置）

用户相似度

![2](https://github.com/JiaoZixun/Recommend_User_Base-/blob/master/img/2.jpg)

在demo2中利用用户间的相似度，计算用户v对电影i的感兴趣值。

推荐，[电影id，感兴趣值]

![3](https://github.com/JiaoZixun/Recommend_User_Base-/blob/master/img/3.png)

在demo3中将用户对不同电影的感兴趣值进行排序，进行Top-N推荐，选取前N个作为推荐列表。

Top-N推荐，[电影id，感兴趣值]

![4](https://github.com/JiaoZixun/Recommend_User_Base-/blob/master/img/4.jpg)
