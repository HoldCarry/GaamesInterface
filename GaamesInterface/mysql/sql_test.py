import pymysql

#1.创建一个客户端链接
client =  pymysql.connect(
    host = "teststore-01.ctgmop49hwif.ap-southeast-1.rds.amazonaws.com",   #连接的数据库服务器主机名，默认为本地主机（localhost）；字符串类型（String）
    user= "awstestuser",    #用户名，默认为当前用户；字符串类型（String
    password="97303af4f0be7e0551111ec78f78a880", #密码，无默认值；字符串类 （String
    db= "cdo_account_message",      #数据库名称，无默认值；字符串类型（String）
    port=33066,     #指定数据库服务器的连接端口，默认为3306；整型（int）
    charset='utf8'  #字符集
)
#2.创建游标
cursor = client.cursor()
#3.sql命令语句
sql = "SELECT * FROM msg_task where status=6"
#4.执行sql命令语句
cursor.execute(sql)
#5.获取表头
rows = cursor.fetchall()
des = cursor.description #显示每列详细信息
print("表头:", ",".join([item[0] for item in des])) #获取表头
#6.遍历出每条数据库数据
for i in rows:
   print(i)

