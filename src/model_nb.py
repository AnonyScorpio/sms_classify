# -*- coding: utf-8 -*-
"""
	使用简单机器学习算法 朴素贝叶斯算法   scikit-learn 实现
	这里的学习算法可以修改一下，具体选择看是否更优

	2：高斯朴素贝叶斯（Gaussian Naive Bayes）
	3：多项式朴素贝叶斯（Multinomial Naive Bayes）
	4：伯努利朴素贝叶斯（ Bernoulli Naive Bayes）

	这里以BernoulliNB 为例

"""
import numpy as np
from sklearn.externals import joblib
from sklearn.naive_bayes import BernoulliNB #MultinomialNB ,GaussianNB
import segment
seg = segment.segment()
#读取训练样本和评价样本，生成one-hot词向量
smsList = {'vcode':'验证码类','sale':'营销类','info':'通知类'}
X = []
Y = []
t_X={}
t_Y={}
for smsType in smsList:
	t_X[smsType]=[]
	t_Y[smsType]=[]
	with open('init/train_'+smsType+'.line','r') as f:
		for s in [eval(t) for t in f.readlines()]:
			tmp = seg.dictToVector(s)
			X.append(tmp)
			Y.append(smsType)
	with open('init/test_'+smsType+'.line','r') as f:
		for s in [eval(t) for t in f.readlines()]:
			tmp = seg.dictToVector(s)
			t_X[smsType].append(tmp)
			t_Y[smsType].append(smsType)
print('训练样本总数：',len(X))

#开始训练 并保存模型
clf = BernoulliNB() #MultinomialNB,GaussianNB
clf.fit(np.array(X), np.array(Y))
joblib.dump(clf,'model/naive_bayes.pkl') 

#简单测试
demo_test = ['尊敬的客户，我们已收到您服务单257405864中的商品，我们会尽快安排处理。您可在“返修/退换货”中查询相关状态，微信关注“京东售后”，售后进度随时查看。【京东】','您好！您的京东订单46892957801退款已成功受理，99.00元将返还到您原支付账户，请在1-15个工作日内注意查收，如有疑问请致电京东【京东】','[注册验证码]：606227【京东到家】']
print(clf.predict([seg.getVector(sms) for sms in demo_test]))

#训练准准确率
print("Accuracy on  training set:%s" % (clf.score(X, Y)))
#分类的验证准确率
for  smsType in smsList:
	print("total_num on %s test set:%s" % (smsType,len(t_X[smsType])))
	print("Accuracy on %s test set:%s" % (smsType,clf.score(t_X[smsType], t_Y[smsType])))