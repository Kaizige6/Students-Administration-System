import tkinter as tk
import data
import tkinter.messagebox 
import ui_main
import webbrowser
import tkinter.font as tkFont
import json



class LoginWindow(tk.Frame):
    def __init__(self,master):
        self.window = master
        tk.Frame.__init__(self,master)
        self.window.geometry('230x250')
        self.window.title('系统登陆')
        self.createWidgets()
        

    def createWidgets(self):
        #创建控件
        self.lb_userid = tk.Label(self.window, text = '用户ID')
        self.lb_userid.grid(row=1, column=0)
        self.lb_pass = tk.Label(self.window, text = '密码')
        self.lb_pass.grid(row=2, column=0)

        self.ety_userid = tk.Entry(self.window)
        self.ety_userid.grid(row=1, column=1, columnspan=2)
        self.ety_userid.insert(0,'J001')
        self.ety_pass = tk.Entry(self.window, show='*')
        self.ety_pass.grid(row=2, column=1, columnspan=2)
        self.ety_pass.insert(0,'123456')

        self.lbf = tk.LabelFrame(self.window, text = '身份')
        self.lbf.grid(row=3, column=0, columnspan=3)
        self.v = tk.StringVar()
        self.v.set('教务')
        self.rdbtn_a = tk.Radiobutton(self.lbf, text = '教务', value = '教务', variable = self.v)
        self.rdbtn_t = tk.Radiobutton(self.lbf, text = '教师', value = '教师', variable = self.v)
        self.rdbtn_s = tk.Radiobutton(self.lbf, text = '学生', value = '学生', variable = self.v)
        self.rdbtn_a.grid(row=4, column=0)
        self.rdbtn_t.grid(row=4, column=1)
        self.rdbtn_s.grid(row=4, column=2)


        self.btn_login = tk.Button(self.window, text = '登录', command = self.login, fg='white', bg='gray', activebackground='black', activeforeground='white')
        self.btn_login.grid(row=5, column=1, sticky='w')
        self.btn_cancel = tk.Button(self.window, text = '取消', command = self.cancel, fg='white', bg='gray', activebackground='black', activeforeground='white')
        self.btn_cancel.grid(row=5, column=2, sticky='w')

        #东华大学图片
        self.photo = tk.PhotoImage(file = r"C:\Users\86187\Desktop\作业\大二下\OOP\学生信息管理系统\dhu.gif")#file：t图片路径
        self.imgLabel = tk.Label(self.window, image = self.photo)#把图片整合到标签类中
        self.imgLabel.grid(row=0, column =0, columnspan = 3)#自动对齐

        #创建链接
        link = tk.Label(self.window, text='进入东华服务大厅',  font = tkFont.Font(size = 8))
        link.grid(row=6, column=2, sticky='w')
        # 此处必须注意，绑定的事
        # 件函数中必须要包含event参数
    
        def open_url(event):
            webbrowser.open("http://ehall.dhu.edu.cn/_web/fusionportal/dhlogin.jsp?_p=YXM9MSZwPTEmbT1OJg__", new=0)
        # 绑定label单击时间
        link.bind("<Button-1>", open_url)


        self.window.mainloop()

    #登陆函数
    def login(self):
        userid = self.ety_userid.get()
        password = self.ety_pass.get()
        usertype = self.v.get()
        if len(userid.strip()) == 0:
            tkinter.messagebox.showinfo(title = '系统登陆', message = '请输入用户ID！')
            return None
        if len(password.strip()) == 0:
            tkinter.messagebox.showinfo(title = '系统登陆', message = '请输入登陆密码！')
            return None
        username = data.check_login(userid, password, usertype)
        if not username:
            tkinter.messagebox.showinfo(title = '系统登陆', message = '用户名或密码或角色错误，请重新输入！')
        else:
            self.window.destroy()
            ui_main.MainWindow(userid, username, usertype)
        
        #登陆痕迹记录
        track = [userid, usertype]
        with open(r'C:\Users\86187\Desktop\OOP\学生信息管理系统\track.json','a') as f:
            json.dump(track,f)


    def get_user_id(self):
        return self.ety_userid.get()
            
    
    def cancel(self):
        self.window.destroy()


if __name__ == '__main__':
    root = tk.Tk() # 创建tkinter的主窗口
    app = LoginWindow(root)