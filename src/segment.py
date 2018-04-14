# -*- coding: utf-8 -*-
"""
	jieba进行词，并进行词性过滤，制作one-hot向量
"""
import jieba.posseg as psseg
class segment:
	psType = ['n','v','vn'] # jieba 分词 过滤词性列表，这是这使用 动词名词和动名词
	#path 为指定的词汇总文件
	def __init__(self,path = 'init/summary.line'):
		try:
			with open(path,'r') as s:
				total = [tmp.split(' \t ')[0] for tmp in s.readlines()]
				self.total_dict = dict(zip(total,list(range(len(total)))))
		except IOError:
			self.total_dict = {}
	#直接对Str进行分词
	def cut(self,sms):
		words = psseg.cut(sms)
		return [w for w,t in words if t in self.psType]
	#直接对Str进行分词制作成字典
	def cutToDict(self,sms):
		words = psseg.cut(sms)
		return set(self.cut(sms))
	#分词制作成one-hot词向量
	def getVector(self,sms):
		return self.dictToVector(self.cutToDict(sms))
	#词字典转成one-hot词向量
	def dictToVector(self,dict):
		tmp = [0]*len(self.total_dict)
		for w in dict:
			if w in self.total_dict:
				tmp[self.total_dict[w]]	= 1
		return tmp

