
	#使用说明

	这里使用python 3.6基于scikit-learn 的朴素贝叶斯实现的一个短文本分类器
	代码有详细注释，可以查看源代码

	依赖直接使用pip安装就好了： 
		jieba (0.39)
		numpy (1.14.1)
		openpyxl (2.5.2)
		pip (9.0.1)
		scikit-learn (0.19.1)
		scipy (1.0.0)
		sklearn (0.0)

	#使用方法：

	测试：先使用验证生成好的数据模型：
		cd sms_class; 到主目录 
		python src/production.py 会显示出下列信息
		输出:
			测试样例为： ['您好！您的京东订单46892957801退款已成功受理，99.00元将返还到您原
			支付账户，请在1-15个工作日内注意查收，如有疑问请致电京东【京东】', '[注册验证码]
			：187204【京东到家】', '年货美食满199减100，饮料冲调200减188神券！优惠多多，抓紧
			囤货 dc.jd.com/sPtKQQ 回复BK退订【京东】']
			Building prefix dict from the default dictionary ...
			Loading model from cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache
			Loading model cost 0.747 seconds.
			Prefix dict has been built succesfully.
			测试结果为： ['sale' 'vcode' 'sale']


	1.数据转化：
		执行python src/parse_data.py 会将data各分类目录下各xlsx文件合并下生成每行一短信的parse.line文件
		会输出：
			data/营销类
			data/营销类\SDK-BBX-010-19103 (2).xlsx
			data/营销类\SDK-BBX-010-19103 (3).xlsx
			data/通知类
			data/通知类\SDK-BBX-010-23277(4).xlsx
			data/验证码类
			data/验证码类\SDK-BBX-010-22943.xlsx

		可以添一些额外的数据


	2.初始化数据:
	   先在打开文件，配置一下各分类的训练样本数，校验样本数
	   执行python src/init.py  会将上步的parse.line文件直接按分类生成训练样本数据，校验样本数据，生成词汇表
	   这是只有小部分数据
	   输出：
			Building prefix dict from the default dictionary ...
			Loading model from cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache
			Loading model cost 0.893 seconds.
			Prefix dict has been built succesfully.
			词汇表总数量： 1005
		
	3.生成训练模型，并评估
		执行python src/model_nb.py  会有下面类似信息，生 

		输出：
			Building prefix dict from the default dictionary ...
			Loading model from cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache
			Loading model cost 0.759 seconds.
			Prefix dict has been built succesfully.
			['sale' 'info' 'vcode']
			Accuracy on  training set:0.9900833333333333
			total_num on vcode test set:2000
			Accuracy on vcode test set:1.0
			total_num on sale test set:2000
			Accuracy on sale test set:0.995
			total_num on info test set:2000
			Accuracy on info test set:0.949


	4.生产类型可以再将词汇表，和模型目录修改为新生成的文件 
		详见src/production.py


	#目录结构

	sms_class 
	│  README.MD 								#说明文档
	│										
	├─data             							#初始数据，这里只保留很小一部分，再多自己添加
	│  ├─营销类 								#分类
	│  │      SDK-BBX-010-19103 (2).xls         #xlsx文件
	│  │      SDK-BBX-010-19103 (3).xls
	│  │      parse.line                        #执行python src/parse_data.py 生成的line行文件，每行一短信
	│  │
	│  ├─通知类
	│  │      SDK-BBX-010-23277(4).xlsx
	│  │      parse.line                        #执行python src/parse_data.py 生成的line行文件，每行一短信
	│  │
	│  └─验证码类
	│          SDK-BBX-010-22943.xlsx
	│          parse.line                       #执行python src/parse_data.py 生成的line行文件，每行一短信
	│  
	├─default 									#已经生成的样例数据目录，用于对照
	│  ├─init 									#同init目录，默认数据
	│  │      summary.line 						#默认词汇表
	│  │      test_info.line 					#默认测试样本数据  通知类
	│  │      test_sale.line 					#默认测试样本数据  营销类
	│  │      test_vcode.line 					#默认测试样本数据  验证码类
	│  │      train_info.line 					#默认训练样本数据  通知类
	│  │      train_sale.line 					#默认训练样本数据  营销类
	│  │      train_vcode.line 					#默认训练样本数据  验证码类
	│  │
	│  └─model 									#模型目录
	│         naive_bayes_each_80000.pkl 		#scikit-learn模型文件，这个是每一类80000训练数据，生成的模型
	│
	├─init 										#生成好的词汇表，和训练样本及校验样本
	│      summary.line  						#生成好的词汇表
	│      test_info.line
	│      test_sale.line
	│      test_vcode.line
	│      train_info.line
	│      train_sale.line
	│      train_vcode.line
	│
	├─model 									#生成好的模型目录
	│      naive_bayes.pkl 						#训练好的scikit-learn模型文件
	└─src 										#python 脚本目录
	    │  init.py                              #初始化，生成训练和测试样本
	    │  model_nb.py 							#生成模型
	    │  parse_data.py 						#将xlsx转化成.line文件
	    │  production.py 						#用于生产使用，使用defalut目录下默认词汇表和模型
	    │  segment.py 							#分词器，使用jieba分词 用于分词和生成one-hot词向量
	    │
	    └─__pycache__ 							#python
	            segment.cpython-36.pyc
