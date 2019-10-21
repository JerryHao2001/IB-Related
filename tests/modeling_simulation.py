import pandas as pd
import numpy as np



def basic_matrix(matrix):
    for i in range(len(matrix)):
        Sum = sum(matrix[i][:])
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                matrix[i][j] = 1/Sum
    return matrix

def further_matrix(matrix):
    for i in range(len(matrix)):
        Sum = sum(matrix[i][:])
        if Sum == 0:
            for j in range(len(matrix)):
                matrix[i][j] = 1/len(matrix)
    return matrix

def selfish(web):
    for i in range(len(web)):
        web[i] = web[i]*0.85 + 0.15/len(web)
    return web

matrix=np.loadtxt('Matrix.csv',dtype=float, delimiter=',')
web = np.array([[1/len(matrix)] for i in range(len(matrix))])

print(matrix)
matrix = basic_matrix(matrix)
print(matrix)
matrix = further_matrix(matrix)
matrix = np.transpose(matrix)

def vote(web,matrix):
    origin = web
    web = np.dot(matrix,web)
    web = selfish(web)
    if abs(np.sum(web-origin)) <0.1:
        return web
    else:
        vote(web,matrix)

result = vote(web,matrix)
print(result)

data = pd.DataFrame(result)
writer = pd.ExcelWriter('Matrix.xlsx')		# 写入Excel文件
data.to_excel(writer, 'page_1', float_format='%.5f')		# ‘page_1’是写入excel的sheet名
writer.save()

writer.close()


