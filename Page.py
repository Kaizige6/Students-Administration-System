import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox
import Login
import pymssql
import AdminManage
import StudentsView



def StartPage(self, parent_window):
    parent_window.destroy()  #销毁主界面
    self.window = tk.Tk() #初始框
    self.window.title('学生信息管理系统')
    self.window.geometry('600x470')  #Attention!!!

    label = tk.Label(self.window, text = '学生信息管理系统', font = ('Verdana', 20))
    label.pack(pady = 80)

    #四个按钮
    btnAdministrator = tk.Button(self.window, text="管理员登陆", font = tkFont.Font(size = 16), command = lambda: AdminPage(self.window), 
                                width = 30, height = 2, fg = 'white', bg = 'gray', activebackground = 'black', activeforeground = 'white')
    btnAdministrator.pack()
    btnStudents = tk.Button(self.window, text = '学生登陆', font = tkFont.Font(size = 16), command = lambda: StudentsPage(self.window),
                            width = 30, height = 2, fg = 'white', bg = 'grey', activebackground = 'black', activeforeground = 'white')
    btnStudents.pack()
    btnAboutus = tk.Button(self.window, text = '关于我们', font = tkFont.Font(size = 16), command = lambda: AboutusPage(self.window), 
                            width = 30, height = 2, fg = 'white', bg = 'grey', activebackground = 'black', activeforeground = 'white')
    btnAboutus.pack()
    btnQuit = tk.Button(self.window, text = '退出', font = tkFont.Font(size = 16), command = lambda: self.window.destroy(), 
                        width = 30, height = 2, fg = 'white', bg = 'grey', activebackground = 'black', activeforeground = 'white')
    btnQuit.pack()

    self.window.mainloop()

    
def AdminPage(self, parent_window):
    parent_window.destroy() # 销毁主界面
    self.window = tk.Tk()
    self.window.title('管理员登陆页面')
    self.window.geometry('600x450')  
    lblog = tk.Label(self.window, text = '管理员登陆', bg = 'green', font = ('Verdana', 20), width = 30, height = 2)
    lblog.pack()
 
    lbName = tk.Label(self.window, text = '管理员账号：', font = tkFont.Font(size = 14))
    lbName.pack(pady = 25)
    self.admin_id = tk.Entry(self.window, width = 30, font = tkFont.Font(size = 14), bg = 'Ivory')
    self.admin_id.pack()
 
    lbPass = tk.Label(self.window, text = '管理员密码：', font = tkFont.Font(size = 14))
    lbPass.pack(pady = 25)
    self.admin_pass = tk.Entry(self.window, width = 30, font = tkFont.Font(size = 14), bg = 'Ivory', show = '*')
    self.admin_pass.pack()
 
    btLog = tk.Button(self.window, text = "登陆", width = 8, font = tkFont.Font(size = 12), command = Login.adminLogin())
    btLog.pack(pady=40)
    btnBack = tk.Button(self.window, text="返回首页", width = 8, font = tkFont.Font(size = 12), command = Login.back())
    btnBack.pack()
 
    self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
    self.window.mainloop()
    



def StudentsPage(self, parent_window):
    parent_window.destroy()
    self.window = tk.Tk()
    self.window.title('学生登录')
    self.window.geometry('600x450')

    lbLog = tk.Label(self.window, text = '学生登录', bg = 'green', font = ('Verdana', 20), width = 30, height = 2)
    lbLog.pack()

    lbName = tkinter(self.window, text = '学生学号', font = tkFont.Font(size = 14))
    lbName.pack(pady = 25)
    self.stu_id = tk.Entry(self.window, width = 30, font = tkFont.Font(sezi = 14), bg = 'Ivory')
    self.stu_id.pack()

    lbName = tk.Label(self.window, text = '学生密码', font = tkFont.Font(size = 14))
    lbName.pack(pady = 25)
    self.stu_pass = tk.Entry(self.window, width = 30, font = tkFont.Font(size = 14), bg = 'Ivory', show = '*')
    self.stu_pass.pack()

    btnLog = tk.Button(self.window, text = '登录', width = 8, font = tkFont.Font(size = 12), command = Login.StudentsLogin())
    btnLog.pack()
    btnBack = tk.Button(self.window, text = '返回首页', width = 8, font = tkFont.Font(size = 12), command = Login.back())
    btnBack.pack()

    self.Window.protocol('WM_DELETE_WINDOW', self.Back)
    self.window.mainloop()


def AboutusPage(self, parent_window):
    parent_window.destroy()
    self.window = tk.Tk()
    self.window.title('关于我们')
    self.window.geometry('600x450')

    lb1 = tk.Label(self.window, text = '学生信息管理系统', bg = 'green', font = ('Verdana,20'), width = 30, height = 2)
    lb1.pack()

    lb2 = tk.Label(self.window, text = '190750233', font = ('Verdana', 18))
    lb2.pack(pady = 30)

    btn1 = tk.Button(self.window, text = '返回主页', font = tkFont(size = 12), width = 8, command = Login.back)

    self.window.protocol("WM_DELETE_WINDOW", self.back)
    self.window.mainloop()