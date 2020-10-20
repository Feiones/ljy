import pymysql

# 获得单词的注释
# def exexp(l):
#     i = 0
#     while True:
#         if l[i] == '':
#             i += 1
#         else:
#           return ' '.join(l[i:])
#
# # 连接数据库并将内容写入数据库
# db = pymysql.connect(host = 'localhost',
#                      port = 3306,
#                      user = 'root',
#                      password = '123456',
#                      database = 'word',
#                      charset = 'utf8')
# cur = db.cursor()
f = open('dict.txt')
for line in f:
    word = line.split(' ')[0]
    exp = line.split(' ')[1:]
    print(word)
    print(' '.join(exp).strip())
    print("============================")
    # exp = exexp(exp)
#     sql = "insert into dict (wdlist,explaina) values(%s,%s);"
#     cur.execute(sql,[word,exp])
#     db.commit()
# cur.close()
# db.close()

# 查询单词含义
# def search(word):
#     db = pymysql.connect(host='localhost',
#                          port=3306,
#                          user='root',
#                          password='123456',
#                          database='word',
#                          charset='utf8')
#     cur = db.cursor()
#     sql = "select explaina from dict where wdlist = %s;"
#     cur.execute(sql,[word])
#     db.commit()
#     exp = str(cur.fetchone()[0])
#     cur.close()
#     db.close()
#     return exp
#
# word = input("请输入要查寻的单词：")
# print(search(word))
# import re
# f = open('dict.txt')
# data = f.readline()
# print(data.split(' ')[0])
# print(' '.join(data.split(' ')[1:]).strip())

# print(data)
# tup = re.findall(r"(\S+)\s*(.*)",data)
# print(tup)



