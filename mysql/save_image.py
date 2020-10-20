import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()
# 存储图片
# with open('timg.jpg','rb') as f:
#     data = f.read()
# try:
#     sql = "update class set image = %s where name = 'lb';"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)

# 提取图片
sql = "select image from class where name = 'lb';"
cur.execute(sql)
data = cur.fetchone()
print(data)
with open('t.jpg','wb') as f:
    f.write(data[0])
    f.close()

cur.close()
db.close()
