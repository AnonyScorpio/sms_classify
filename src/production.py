# -*- coding: utf-8 -*-
"""
	直接使用生成好的模型，用于生产环境下 
	使用方法与模型评估相同 主要是predict方法

	这里使用已经生成好的默认词汇表和模型
"""
from sklearn.externals import joblib
import segment
seg = segment.segment('default/init/summary.line') #使用默认词汇表，注意路径
clf = joblib.load('default/model/naive_bayes_each_80000.pkl') #加载默认模型，注意路径
demo_test = ['尊敬的京东会员您好，您在京东预约的商品【编号:2289329】，将于1月19日10点0分准时抢购，货源有限先到先得。详情猛戳链接：item.m.jd.com/ware/view.action?wareId=2289329','您好！您的京东订单46892957801退款已成功受理，99.00元将返还到您原支付账户，请在1-15个工作日内注意查收，如有疑问请致电京东【京东】','[注册验证码]：606227【京东到家】']
print("测试样例为：",demo_test);
print("测试结果为：",clf.predict([seg.getVector(sms) for sms in demo_test]))
