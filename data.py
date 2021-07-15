'''基于SQL Server Management Studio'''
'''用户信息管理系统'''

import pymssql


def get_create_db():
    """打开SQL数据库文件Educational administration，并返回数据库连接con
    如果不存在SQL数据库文件UserInfo表以及其他表，则创建数据库和UserInfo表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    sql_create_UserInfo = '''CREATE TABLE UserInfo (
                            USERID NVARCHAR(20) PRIMARY KEY,
                            USERNAME NVARCHAR(20) NOT NULL,
                            GENDER NVARCHAR(2),
                            BIRTHDAY NVARCHAR(11),
                            DEPARTMENT NVARCHAR(50),
                            PHONE NVARCHAR(20),
                            USERTYPE NVARCHAR(4),
                            PASSWORD NVARCHAR(20) NOT NULL)'''
    cursor.execute(sql_create_UserInfo)
    db.commit()
    sql_insert_UserInfo = '''INSERT INTO UserInfo VALUES 
                              ('J001','张教务','女','1988/5/2','物理系','13912345678','教务','123456');'''
    cursor.execute(sql_insert_UserInfo)
    db.commit()

    # 在该数据库下创建课程信息表
    sql_create_COURSE = '''CREATE TABLE Course (
                            COURSEID    NVARCHAR (20)  PRIMARY KEY,
                            COURSENAME  NVARCHAR (20)  NOT NULL,
                            CREDIT      FLOAT,
                            DESCRIPTION NVARCHAR (100));'''
    cursor.execute(sql_create_COURSE)
    db.commit()

    #在该数据库下创建教学班号表
    sql_create_JXB = ''' CREATE TABLE JXB(
                        JXBID  NVARCHAR(20)  PRIMARY  KEY,
                        COURSEID  NVARCHAR(20)  NOT  NULL,
                        USERID   NVARCHAR(20)  NOT  NULL,
                        DESCRIPTION NVARCHAR(100));'''
    cursor.execute(sql_create_JXB)
    db.commit()

    # 在该数据库下创建学生成绩表
    sql_create_Grades = ''' CREATE TABLE Grades (
                        JXBID  NVARCHAR (20),
                        USERID NVARCHAR (20),
                        SCORE  INT,
                        PRIMARY KEY (
                                JXBID,
                                USERID));'''
    cursor.execute(sql_create_Grades)
    db.commit()
    return cursor  # 返回数据库连接



def check_login(userid, password, usertype):
    '''检查登陆信息是否正确'''
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT USERNAME FROM UserInfo WHERE USERID=%s
                        AND PASSWORD=%s AND USERTYPE=%s'''
        cursor.execute(sql,(userid,password,usertype))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return False
    finally:
        db.close()


def change_password(userid, password):
    """修改用户密码"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''UPDATE UserInfo SET PASSWORD=%s
                                 WHERE USERID=%s'''
        cursor.execute(sql,(password,userid))
        db.commit()
    finally:
        db.close()


############---用户管理---#############################################################
def check_user_id(userid):
    """检查UserInfo中是否存在userid"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT USERID, USERNAME FROM UserInfo WHERE USERID = %s'''
        cursor.execute(sql,(userid))
        row = cursor.fetchone()
        if row:
            return row[1] #返回用户名
        else:
            return False
    finally:
        db.close()


def get_user_list(user_type):
    """查找数据库UserInfo表，获取类型为user_type的用户信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT USERID, USERNAME, GENDER, DEPARTMENT, PHONE, BIRTHDAY
                    FROM UserInfo 
                    WHERE USERTYPE=%s'''
        cursor.execute(sql,(user_type))
        users = cursor.fetchall()
        user_list = []      #返回一个列表
        for user in users:
            user_list.append(user)
        return user_list
    finally:
        db.close()

        
def insert_user(usertype, userid, username, gender, birthday, department, phone):
    """插入一条记录到UserInfo表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''INSERT INTO UserInfo(USERID, USERNAME, GENDER, BIRTHDAY, DEPARTMENT, PHONE,USERTYPE, PASSWORD)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(sql,(userid, username, gender, birthday, department, phone, usertype, '123456'))
        db.commit()
    finally:
        db.close()


def update_user(usertype, userid, username, gender, birthday, department, phone):
    """更新一条记录到UserInfo表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''UPDATE UserInfo
                    SET USERTYPE = %s
                        ,USERNAME = %s
                        ,GENDER = %s
                        ,BIRTHDAY = %s
                        ,DEPARTMENT = %s
                        ,PHONE = %s                        
                    WHERE USERID = %s'''
        cursor.execute(sql,(usertype, username,gender,birthday,department,phone,userid))
        db.commit()
    finally:
        db.close()


def delete_user(userid):
    """从UserInfo表中删除一条记录"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''DELETE FROM UserInfo
                    WHERE USERID = %s'''
        cursor.execute(sql, (userid))
        db.commit()
    finally:
        db.close()


############---课程管理---#########################################################################
def check_course_id(courseid):
    """检查Course表中是否存在courseid"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT COURSEID, COURSENAME FROM COURSE WHERE COURSEID=%s'''
        cursor.execute(sql,(courseid))
        row = cursor.fetchone()
        if row:
            return row[1] #返回课程名称
        else:
            return False
    finally:
        db.close()


def get_course_list():
    """查找数据库Course表，获取课程信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT * FROM Course'''
        cursor.execute(sql)
        courses = cursor.fetchall()
        course_list = []
        for course in courses:
            course_list.append(course)
        return course_list
    finally:
        db.close()



def insert_course(courseid, coursename, credit, description):
    """插入一条记录到Course表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''INSERT INTO COURSE(COURSEID, COURSENAME, CREDIT, DESCRIPTION) 
                                        VALUES (%s,%s,%s,%s)'''
        cursor.execute(sql, (courseid, coursename, credit, description))
        db.commit()
    finally:
        db.close()


def update_course(courseid, coursename, credit, description):
    """更新一条记录到COURSE表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''UPDATE COURSE
                    SET COURSENAME = %s
                        ,CREDIT = %s
                        ,DESCRIPTION = %s
                    WHERE COURSEID = %s'''
        cursor.execute(sql, (coursename, credit, description, courseid))
        db.commit()
    finally:
        db.close()


def delete_course(courseid):
    """从COURSE表中删除一条记录"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''DELETE FROM COURSE
                    WHERE COURSEID = %s'''
        cursor.execute(sql, (courseid, ))
        db.commit()
    finally:
        db.close()

###########---开课计划JXB---#########################################################################
def check_jxb_id(jxbid):
    """检查JXB中是否存在jxbid"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT j.COURSEID, c.COURSENAME, j.USERID, u.USERNAME, j.DESCRIPTION
                   FROM JXB  AS j, Course AS c, UserInfo AS u
                  WHERE j.COURSEID = c.COURSEID
                    AND j.USERID = u.USERID
                    AND j.JXBID = %s;'''
        cursor.execute(sql, (jxbid))
        row = cursor.fetchone()
        if row:
            return row
        else:
            return False
    finally:
        db.close()


def get_course_name(courseid):
    """查找数据库Course表，获取课程名字信息"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT COURSENAME FROM Course WHERE COURSEID=%s '''
        cursor.execute(sql,(courseid))
        coursename = cursor.fetchone()
        course_name = coursename[0]
        return course_name
    finally:
        db.close()


def get_teacher_name(teacherid):
    """查找数据库UserInfo表，获取老师名字信息"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT USERNAME FROM UserInfo WHERE USERID=%s '''
        cursor.execute(sql,(teacherid))
        teachername = cursor.fetchone()
        teacher_name = teachername[0]
        return teacher_name
    finally:
        db.close()



def get_jxb_list():
    """查找数据库JXB，获取课程安排教学班号信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT j.JXBID, j.COURSEID, c.COURSENAME, j.USERID, u.USERNAME, j.DESCRIPTION
                   FROM JXB AS j, Course AS c, UserInfo AS u
                  WHERE j.COURSEID = c.COURSEID
                    AND j.USERID = u.USERID;'''
        cursor.execute(sql)
        jxbs = cursor.fetchall()
        jxb_list = []
        for jxb in jxbs:
            jxb_list.append(jxb)
        return jxb_list     
    finally:
        db.close()


def insert_jxb(jxbid, courseid, userid, description):
    """插入一条记录到JXB表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''INSERT INTO JXB(JXBID, COURSEID, USERID,DESCRIPTION)
                                      VALUES (%s,%s,%s,%s)'''
        cursor.execute(sql, (jxbid, courseid, userid, description))
        db.commit()
    finally:
        db.close()



def update_jxb(jxbid, courseid, userid, description):
    """更新一条信息到JXB表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''UPDATE JXB
                    SET COURSEID = %s
                        ,USERID = %s
                        ,DESCRIPTION = %s
                    WHERE JXBID = %s'''
        cursor.execute(sql, (courseid, userid, description, jxbid))
        db.commit()
    finally:
        db.close()


def delete_jxb(jxbid):
    """从JXB表删除一条记录"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''DELETE FROM JXB
                    WHERE JXBID = %s'''
        cursor.execute(sql, (jxbid))
        db.commit()
    finally:
        db.close()



############学生选课Grade#########################################################################
def check_grade_id(jxbid, userid):
    """检查Grade表中是否存在jxbid、userid， 即userid是否已经选jxbid"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT jxbid FROM Grades 
                          WHERE JXBID = %s 
                            AND USERID = %s '''
        cursor.execute(sql, (jxbid, userid))
        row = cursor.fetchone()
        if row:
            return True
        else:
            return False
    finally:
        db.close()


def get_grades_list_by_student(userid):
    """查找数据库Grades表，获取学生userid选课信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:        
        sql = '''SELECT g.JXBID, j.COURSEID, c.COURSENAME, j.USERID, u.USERNAME, j.DESCRIPTION, g.SCORE
                   FROM Grades AS g, JXB AS j, Course AS c, UserInfo AS u
                  WHERE g.JXBID = j.JXBID
                    AND j.COURSEID = c.COURSEID
                    AND j.USERID = u.USERID
                    AND g.USERID = %s'''           
        cursor.execute(sql, (userid))
        grades = cursor.fetchall()
        grade_list = []
        for grade in grades:
            grade_list.append(grade)
        return grade_list
    finally:
        db.close()


def get_all_grades_list_by_student():
    """查找数据库Grades表，获取所有选课信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:        
        sql = '''SELECT g.JXBID, j.COURSEID, c.COURSENAME, j.USERID, u.USERNAME, j.DESCRIPTION
                   FROM Grades AS g, JXB AS j, Course AS c, UserInfo AS u
                  WHERE g.JXBID = j.JXBID
                    AND j.COURSEID = c.COURSEID
                    AND j.USERID = u.USERID
                    GROUP BY g.JXBID,j.COURSEID, c.COURSENAME, j.USERID, u.USERNAME, j.DESCRIPTION'''           
        cursor.execute(sql)
        grades = cursor.fetchall()
        grade_list = []
        for grade in grades:
            grade_list.append(grade)
        return grade_list
    finally:
        db.close()


def insert_grade(jxbid, userid):
    """插入一条信息到Grades表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''INSERT INTO Grades(JXBID, USERID)
                                      VALUES (%s,%s)'''
        cursor.execute(sql, (jxbid, userid))
        db.commit()
    finally:
        db.close()


def delete_grade(jxbid, userid):
    """从Grades表删除一条记录"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''DELETE FROM Grades
                    WHERE JXBID = %s
                       AND USERID = %s'''
        cursor.execute(sql, (jxbid, userid))
        db.commit()
    finally:
        db.close()


############教师成绩登录Grades#########################################################################
def get_jxbid_list_by_user(userid):
    """查找数据库JXB表，获取指定教师userid授课课程信息JXBID列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT j.JXBID
                   FROM JXB AS j
                  WHERE j.USERID = %s ;'''
        cursor.execute(sql, (userid))
        jxbs = cursor.fetchall()
        jxbId_list = []
        for jxb in jxbs:
            jxbId_list.append(jxb[0])
        return jxbId_list
    finally:
        db.close()



def get_grade_list_by_jxbid(jxbid):
    """查找数据库Grades表，获取指定课程的学生选课信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT g.USERID, u.USERNAME, u.GENDER, u.DEPARTMENT, g.SCORE
                   FROM Grades AS g, UserInfo AS u
                  WHERE g.USERID = u.USERID
                    AND g.JXBID = %s;'''
        cursor.execute(sql, (jxbid))
        grades = cursor.fetchall()
        grade_list = []
        for grade in grades:
            grade_list.append(grade)
        return grade_list
    finally:
        db.close()



def get_course_by_jxbid(jxbid):
    """查找数据库Grades表，获取指定课程的课程信息列表"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''SELECT COURSENAME
                    FROM COURSE,JXB
                    WHERE COURSE.COURSEID = JXB.COURSEID
		                AND JXB.JXBID = %s'''
        cursor.execute(sql, (jxbid))
        course = cursor.fetchone()
        course = course[0]
        return course
    finally:
        db.close()



def update_grade_score(score, jxbid, userid):
    """更新学生成绩信息列表到数据库Grade"""
    db = pymssql.connect('.','sa','sa','Educational administration')
    cursor = db.cursor()
    try:
        sql = '''UPDATE Grades
                   SET SCORE = %s
                  WHERE JXBID = %s
                    AND USERID = %s;'''
        cursor.execute(sql,(score, jxbid, userid))
        db.commit()
    finally:
        db.close()



###############---插入函数---###################################################
