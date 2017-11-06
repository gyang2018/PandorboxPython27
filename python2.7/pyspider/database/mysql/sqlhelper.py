#encoding=utf-8
import pymysql



class SqlHelper(object):
    def __init__(self,host,user,pwd,db,dbtype='mysql'):
        self.host = "192.168.1.143"
        self.user = "root"
        self.pwd = "P@ssw0rd"
        self.db = "test"
        self.dbtype = dbtype
        # 51792
        # self.conn = pymssql.connect(host=r"127.0.0.1\SQLEXPRESS", user="sa", password=r"pwd", database="dbname",charset="utf8")
        # File "pymssql.pyx", line 641, in pymssql.connect (pymssql.c:10824) pymssql.OperationalError:
        # (20009, 'DB-Lib error message 20009, severity 9:\nUnable to connect: Adaptive Server is unavailable or does not exist (127.0.0.1\\SQLEXPRESS)\n')

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        # self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        if self.dbtype=='mssql':
            self.conn = pyodbc.connect('Driver={SQL Server};Server=self.host;Database=self.db;uid=self.user;pwd=self.pwd')
            #self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db,charset="utf8")
        if self.dbtype=='mysql':
            self.conn=pymysql.connect(host=self.host,user=self.user,password=self.pwd,db=self.db,charset='utf8mb4')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    #dbinfo = conf.GetSectionConfig("mssqldb")
    #ms = SqlHelper(host=dbinfo["mssqlserver"], user=dbinfo["mssqluser"], pwd=dbinfo["mssqlpwd"], db=dbinfo["testdb"],dbtype='mssql')
    #resList = ms.ExecQuery("SELECT * FROM test")

    ms = SqlHelper()
    resList = ms.ExecQuery("SELECT * FROM testtb")
    print resList
