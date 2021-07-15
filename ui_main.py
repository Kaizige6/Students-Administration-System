import tkinter as tk
import tkinter.messagebox
import ui_change_password
import ui_user
import ui_course
import ui_jxb
import ui_student
import ui_teacher


class MainWindow():
    def __init__(self, userid, username, usertype):
        #self.CreateStatusBar()  # 创建状态栏
        self.window = tk.Tk()
        self.window.title('学生信息管理系统界面')
        self.userid = userid
        self.username = username
        self.usertype = usertype
        self.window.geometry('800x600')

        

        #创建菜单，添加菜单项
        menu_system = tk.Menu(self.window)
        menu_student = tk.Menu(self.window)
        menu_teacher = tk.Menu(self.window)
        menu_jw = tk.Menu(self.window)
        menu_help = tk.Menu(self.window)
        
        #根据不同角色显示菜单栏以及介绍文本
        menubar = tk.Menu(self.window)  #主菜单栏
        menubar.add_cascade(label = '系统', menu = menu_system)
        if self.usertype == '教务':
            menubar.add_cascade(label = '教务', menu = menu_jw)
            lb_welcome = tk.Label(self.window, text = self.Welcome(jxb()))
            lb_welcome.grid(row=0, column=0)
            #lb_welcome1 = tk.Label(self.window, text = '欢迎使用教务系统！',font=("Verdana", 20), bg='pink')
            #lb_welcome1.grid(row=0, column=0)
        elif self.usertype == '教师':
            menubar.add_cascade(label = '教师', menu = menu_teacher)
            lb_welcome = tk.Label(self.window, text = self.Welcome(teacher()))
            lb_welcome.grid(row=0, column=0)
            #lb_welcome1 = tk.Label(self.window, text = '欢迎使用教师系统！',font=("Verdana", 20),bg='pink')
            #lb_welcome1.grid(row=0, column=0)
        elif self.usertype == '学生':
            menubar.add_cascade(label = '学生', menu = menu_student)
            lb_welcome = tk.Label(self.window, text = self.Welcome(student()))
            lb_welcome.grid(row=0, column=0)
            #lb_welcome1 = tk.Label(self.window, text = '欢迎使用学生系统！',font=("Verdana", 20),bg='pink')
            #lb_welcome1.grid(row=0, column=0)
        

        menubar.add_cascade(label = '关于', menu = menu_help)


        menu_system.add_command(label='修改密码', command=self.change_password)
        menu_system.add_command(label='重新登陆', command=self.relog)
        menu_system.add_command(label='退出系统', command=self.Exit)
        menu_jw.add_command(label='用户管理', command=self.Menu_Users)
        menu_jw.add_command(label='课程管理', command=self.Menu_Course)
        menu_jw.add_command(label='开课管理', command=self.Menu_JXB)
        menu_student.add_command(label='学生选课', command=self.Menu_Students)
        menu_teacher.add_command(label='成绩登录', command=self.Menu_Teacher)
        menu_help.add_command(label='关于', command=self.Aboutus)
        self.window['menu'] = menubar


        self.window.mainloop()


    def Welcome(self, type):
        type.welcome()

    #各菜单栏按钮
    def change_password(self):
        """ 事件处理函数：保存文件 """
        userid = self.userid
        changepasswordFrame = ui_change_password.ChangePasswordWindow(userid)
        changepasswordFrame.userid  =  self.userid

    def relog(self):
        import ui_login
        self.window.destroy()
        root = tk.Tk() # 创建tkinter的主窗口
        ui_login.LoginWindow(root)


    def Exit(self):
        self.window.destroy()


    def Menu_Users(self):
        window = self.window
        """ 事件处理函数：用户管理 """
        ui_user.UserWindow(window)
        
        
    
    def Menu_Course(self):
        """ 事件处理函数：课程管理 """
        ui_course.CourseWindow()
        

    def Menu_JXB(self):
        """ 事件处理函数：开课计划 """
        ui_jxb.JXBWindow()
        

    def Menu_Students(self):
        window = self.window
        """ 事件处理函数：学生选课 """
        ui_student.StudentWindow(window,self.userid)
        

    def Menu_Teacher(self):
        window = self.window
        """ 事件处理函数：教师登录成绩 """
        ui_teacher.TeacherWindow(window,self.userid)
        

    def Aboutus(self):
        """事件处理函数：显示消息对话框"""
        tkinter.messagebox.showinfo(title="Aboutus", message="简易教务管理系统\n V1.0.0\n by Yck")





class student:
    def welcome(self):
        message = '欢迎使用学生系统！'
        return message

class jxb:
    def welcome(self):
        message = '欢迎使用教务系统！'
        return message

class teacher:
    def welcome(self):
        message = '欢迎使用教师系统!'
        return message

