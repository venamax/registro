sc = SparkContext(conf=conf)
registro = sc.textFile('hdfs:///user/root/hdfsdirectory/nacional.csv')
print registro.first()