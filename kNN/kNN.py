#coding=utf-8
from numpy import *
import operator
from os import listdir

def createDataSet():
  group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
  labels =['A','A','B','B']
  return group,labels

#inX用于分类的输入向量，dataSet训练样本集标签向量labels，k为用于选择最近邻居的数目，其中标签向量的元素数目和dataset的行数相同

def classifyKnn0(inX,dataSet,labels,k):
  dataSetSize=dataSet.shape[0]
#15-22行利用欧式距离计算xA和xB的距离
  diffMat=tile(inX,(dataSetSize,1))-dataSet
  #**2矩阵乘法，即diffmat*diffMat
  sqlDiffMat=diffMat**2
  #计算每一行（二维数组中类似于矩阵的行）的和
  #axis=0为每一列
  sqlDistances = sqlDiffMat.sum(axis=1)
  distances=sqlDistances**0.5
  sortedDisIndicies=distances.argsort()
  classCount={}
#26-28选择距离最小的k个点
  for i in range (k):
      voteIlabel=labels[sortedDisIndicies[i]]
      classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
#排序
  sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
  return sortedClassCount[0][0]
# 测试分类结果
def datingClassTest():
    hoRate = 0.10 #选择10%作为测试集合
    datingDataMat, datingLabels=file2matrix('datingTestSet2.txt')
    norMat, ranges, minValues=autoNorm(datingDataMat)
    m=norMat.shape[0] #m行
    numTestVecs=int(m*hoRate) #选择前10%作为测试集合，后90%作为训练集合
    errorCount=0.0
    for i in range(numTestVecs):
        #训练集合是从numTestVecs（前10%到最后m行）
        classifierResult=classifyKnn0(norMat[i:], norMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print "the classifer came back with %d,the answer is %d " % (classifierResult, datingLabels[i])
        if(classifierResult!=datingLabels[i]): errorCount+=1.0
    print "the total error rate is:%f" % (errorCount/float(numTestVecs))
    
#读取文件内容到矩阵
def file2matrix(filename):
    fr=open(filename)
    arrayLines=fr.readlines()
    numLines=len(arrayLines)
    returnMat=zeros((numLines, 3))#创建以零填充的特征矩阵
    classLabelVector=[]
    index=0
    for line in arrayLines:
        line=line.strip()
        listFromLine=line.split('\t')
        #依次存储每一行到 特征矩阵中
        returnMat[index, :]=listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat, classLabelVector
    
def autoNorm(dataSet):
    #寻找数据集合最小行
    minValues = dataSet.min(0)
     #寻找数据集合最大行
    maxValues = dataSet.max(0)
    ranges = maxValues-minValues
    normDataSet=zeros(shape(dataSet))
    m=dataSet.shape[0]
    #重复某个数组。比如tile(A,n)，功能是将数组A重复n次，构成一个新的数组
    normDataSet=dataSet-tile(minValues, (m, 1))
    normDataSet=normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minValues

