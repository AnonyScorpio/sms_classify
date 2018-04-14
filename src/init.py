# -*- coding: utf-8 -*-
"""
	初始化 主要用于生成词汇表  init/summary.line，
	后面用于生成one-hot 词向量，
	顺便把分词结果保存下来用于后面训练一和评估 
"""
import segment
seg = segment.segment()
smsList = {}
# name:分类名,  trian_num:训练样本数,   test_num:评估样本数 }
# trian_num最好大于80000，越多越好，
# trian_num/test_num 推荐为3/2以上 ，
# trian_num+test_num 不能超过对应文件总数量
smsList['vcode'] = {'name':'验证码类','trian_num':80000,"test_num":20000}
smsList['sale'] = {'name':'营销类','trian_num':80000,"test_num":20000}
smsList['info'] = {'name':'通知类','trian_num':80000,"test_num":20000}
dict = {}
for smsType in smsList:
	with open('data/'+smsList[smsType]['name']+'/parse.line','r',encoding='utf-8',errors='ignore') as f:
		with open('init/train_'+smsType+'.line','w+') as train:
			line = f.readline();
			for i in range(smsList[smsType]['trian_num']):#前N行作训练样本数据
				line = f.readline();
				wordSet = seg.cutToDict(line)
				print(str(wordSet),file=train)
				for key in wordSet:
					if key in dict:
						dict[key] += 1
					else:
						dict[key] = 1
		with open('init/test_'+smsType+'.line','w+') as test:
			for i in range(smsList[smsType]['test_num']):#再后面的N行做评估样本数据
				line = f.readline();
				wordSet = seg.cutToDict(line)
				print(str(wordSet),file=test)

with open('init/summary.line','w+') as s:
	for key in dict:
		print("%s \t %d" % (key,dict[key]),file = s)

print('词汇表总数量：',len(dict))

