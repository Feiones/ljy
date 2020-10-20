import pymysql
db = pymysql.connect(host = 'localhost',
                     port = 3306,
                     user = 'root',
                     password = '123456',
                     database = 'stu',
                     charset = 'utf8')
cur = db.cursor()

def register():
    n = input('输入姓名：')
    passwd = input('输入密码：')
    sql = "select * from user where name = '%s';"%n
    cur.execute(sql)
    res = cur.fetchone()
    if res:
        # print("用户已存在")
        return False

    try:
        sql = "insert into user (name,password) values (%s,%s);"
        cur.execute(sql,[n,passwd])
        db.commit()
        return True
    except:
        db.rollback()
        return False

while True:
    print("""
            ====================
            1.注册　　　　　2.登录 
             """)
    cmm = input("请输入命令：")
    # 注册
    if cmm == '1':

        if register():
            print("注册成功")
        else:
            print("注册失败")

    # 登录
    if cmm == '2':
        pass
        # login()


cur.close()
db.close()