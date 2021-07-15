import  tkinter as tk
import tkinter.messagebox
import data

class ChangePasswordWindow(tk.Frame):
    def __init__(self,userid, master = None):
        tk.Frame.__init__(self,master)
        self.window = master
        self.window = tk.Tk()
        self.window.title('修改密码')
        self.window.geometry('230x90')
        self.userid = userid
        self.createWidgets()
    

    def createWidgets(self):
        self.lb_password1 = tk.Label(self.window, text = '输入新密码')
        self.lb_password1.grid(row=0, column=0)
        self.lb_password2 = tk.Label(self.window, text = '确认新密码')
        self.lb_password2.grid(row=1, column=0)

        self.ety_password1 = tk.Entry(self.window,show='*')
        self.ety_password1.grid(row=0, column=1, columnspan=2)
        self.ety_password2 = tk.Entry(self.window, show='*')
        self.ety_password2.grid(row=1, column=1, columnspan=2)

        self.btn_check = tk.Button(self.window, text = '确定', command = self.check)
        self.btn_check.grid(row=2, column=1, sticky='w')
        self.btn_cancel = tk.Button(self.window, text = '取消', command = self.cancel)
        self.btn_cancel.grid(row=2, column=2, sticky='w')

        self.window.mainloop()
    

    def check(self):
        password1 = self.ety_password1.get()
        password2 = self.ety_password2.get()
        if len(password1.strip()) == 0:
            tkinter.messagebox.showinfo(title = '修改密码', message = '请输入新密码！')
            return None
        if password1 != password2:
            tkinter.messagebox.showinfo(title = '修改密码', message = '两次输入的新密码不一致！')
            return None
        data.change_password(self.userid, password1) #调用data模块的方法，修改密码
        tkinter.messagebox.showinfo(title = '修改密码', message = '修改成功！')
        self.window.destroy()



    def cancel(self):
        self.window.destroy()
