import  tkinter as tk
import tkinter.messagebox
import data
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import pylab as mpl
from tkinter.constants import END


class UserWindow():
    def __init__(self,window):
        self.window = window
        self.window.title('教务管理系统——用户管理')
        self.window.geometry('800x600')

        
        #创建控件ttk列表
        columns = ('用户ID','姓名','性别','院系','电话号码','出生年月')
        self.tree = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree.grid(row=0,rowspan=5)
        self.tree.column("用户ID", anchor = "center",width=50)
        self.tree.column("姓名", anchor = "center",width=50)
        self.tree.column("性别", anchor = "center",width=50)
        self.tree.column("院系", anchor = "center",width=70)
        self.tree.column("电话号码", anchor = "center",width=90)
        self.tree.column("出生年月", anchor = "center",width=90)
        self.tree.heading("用户ID", text = "用户ID")
        self.tree.heading("姓名", text = "姓名")
        self.tree.heading("性别", text = "性别")
        self.tree.heading("院系", text = "院系")
        self.tree.heading("电话号码", text = "电话号码")
        self.tree.heading("出生年月", text = "出生年月")

        
    
        #创建控件按钮、文本、输入

        self.lbf_status = tk.LabelFrame(self.window, text = '身份')
        self.lbf_status.grid(row=0, column=2, columnspan=2)
        self.v2 = tk.StringVar()
        self.v2.set('教务')
        self.rdbtn_a = tk.Radiobutton(self.lbf_status, text = '教务', value = '教务', variable = self.v2)
        self.rdbtn_t = tk.Radiobutton(self.lbf_status, text = '教师', value = '教师', variable = self.v2)
        self.rdbtn_s = tk.Radiobutton(self.lbf_status, text = '学生', value = '学生', variable = self.v2)
        self.rdbtn_a.grid(row=0,column=0)
        self.rdbtn_t.grid(row=0,column=1)
        self.rdbtn_s.grid(row=0,column=2)


        self.lb_userid = tk.Label(self.window, text = '用户ID')
        self.lb_userid.grid(row=1, column=1)
        self.lb_name = tk.Label(self.window, text = '用户姓名')
        self.lb_name.grid(row=2, column=1)
        self.lb_birthday = tk.Label(self.window, text = '出生年月')
        self.lb_birthday.grid(row=2, column=3)
        self.lb_department = tk.Label(self.window, text = '院系')
        self.lb_department.grid(row=3, column=1)
        self.lb_number = tk.Label(self.window, text = '电话号码')
        self.lb_number.grid(row=3, column=3)

        self.ety_userid = tk.Entry(self.window)
        self.ety_userid.grid(row=1, column=2)
        self.ety_name = tk.Entry(self.window)
        self.ety_name.grid(row=2, column=2)
        self.ety_birthday = tk.Entry(self.window)
        self.ety_birthday.grid(row=2, column=4)
        self.ety_department = tk.Entry(self.window)
        self.ety_department.grid(row=3, column=2)
        self.ety_number = tk.Entry(self.window)
        self.ety_number.grid(row=3, column=4)

        self.lbf_gender = tk.LabelFrame(self.window, text = '性别')
        self.lbf_gender.grid(row=1, column=3,columnspan = 2)
        self.v3 = tk.StringVar()
        self.v3.set('男')
        self.rdbtn_male = tk.Radiobutton(self.lbf_gender, text = '男', value = '男', variable = self.v3)
        self.rdbtn_female = tk.Radiobutton(self.lbf_gender, text = '女', value = '女', variable = self.v3)
        self.rdbtn_male.grid(row=1,column=0)
        self.rdbtn_female.grid(row=1,column=1)


        self.btn_insert = tk.Button(self.window, text = '确定', command = self.show, fg='white', bg='gray', activebackground='black', activeforeground='white')
        self.btn_insert.grid(row=0, column=4)
        self.btn_insert = tk.Button(self.window, text = '插入', command = self.onInsert)
        self.btn_insert.grid(row=4, column=1)
        self.btn_alter = tk.Button(self.window, text = '更新/刷新', command = self.onAlter)
        self.btn_alter.grid(row=4, column=2)
        self.btn_delete = tk.Button(self.window, text = '删除', command = self.onDelete)
        self.btn_delete.grid(row=4, column=3)
        self.btn_exit = tk.Button(self.window, text = '退出', command = self.exit)
        self.btn_exit.grid(row=4, column=4)

        def get_tree(event):
            self.ety_userid.delete(0, END)
            self.ety_name.delete(0, END)
            self.ety_birthday.delete(0, END)
            self.ety_department.delete(0, END)
            self.ety_number.delete(0, END)
            for item in self.tree.selection():
                item_text = self.tree.item(item,"values")
                self.ety_userid.insert(0,item_text[0])
                self.ety_name.insert(0,item_text[1])
                self.ety_birthday.insert(0,item_text[2])
                self.ety_department.insert(0,item_text[3])
                self.ety_number.insert(0,item_text[4])
        
        
        self.tree.bind('<ButtonRelease-1>', get_tree)

        self.tree_show()
        self.window.mainloop() 


    def tree_show(self):
        #在TREE中显示数据   
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        user_type = self.v2.get()
        user_list = data.get_user_list(user_type)
        for i in range(len(user_list)):
            self.tree.insert('',i,values = user_list[i])

        vbar = ttk.Scrollbar(self.window, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        #tree.grid(row=0, column=0, sticky=NSEW)
        vbar.grid(row=0, column=1, sticky='ns')


    
    def show(self):   
        mpl.rcParams['font.sans-serif'] = ['FangSong']    #设置字体，不然是乱码
        self.tree_show() 
        user_type = self.v2.get()
        if user_type == '学生':
            fig = plt.figure(figsize=(8.5,3.2), dpi = 100)
            ax1 = fig.add_subplot(1,2,1)
            ax2 = fig.add_subplot(1,2,2)

            user_list = data.get_user_list(user_type)
            values = list(zip(*user_list))

            #birthday = [datetime.datetime.strptime(t, '%Y/%m/%d') for t in values[5]]
            _data = {'gender':list(values[2]),
                      'major':list(values[3]),
                      'birthday':list(values[5])}
            students = DataFrame(_data, columns = ['gender', 'major', 'birthday'])
            #major
            students['major'].value_counts().plot(kind = 'bar', color = 'pink', title = 'Major Proportion of Students', ax = ax1)
            for tick in ax1.get_xticklabels():
                tick.set_rotation(30)
            plt.gcf().subplots_adjust(bottom=0.2)
            #gender
            students['gender'].value_counts().plot(kind='pie',title='Gender Proportion of Students',autopct='%1.1f%%',ax=ax2,startangle=60)
            #students['birthday'].plot(kind='hist',bins=6,normed=True,title= 'Birthday distribution', ax=ax3)


            canvas = FigureCanvasTkAgg(fig, self.window)
            canvas.draw() # 注意show方法已经过时了,这里改用draw
            canvas.get_tk_widget().grid(row = 5, column = 0, columnspan = 5)


        if user_type == '教师':
            fig = plt.figure(figsize=(8.5,3.2), dpi = 100)
            ax1 = fig.add_subplot(1,2,1)
            ax2 = fig.add_subplot(1,2,2)

            user_list = data.get_user_list(user_type)
            values = list(zip(*user_list))

            #birthday = [datetime.datetime.strptime(t, '%Y/%m/%d') for t in values[5]]
            _data = {'gender':list(values[2]),
                      'major':list(values[3]),
                      'birthday':list(values[5])}
            students = DataFrame(_data, columns = ['gender', 'major', 'birthday'])
            #major
            students['major'].value_counts().plot(kind = 'bar', color = 'pink', title = 'Major Proportion of Teachers', ax = ax1)
            for tick in ax1.get_xticklabels():
                tick.set_rotation(30)
            plt.gcf().subplots_adjust(bottom=0.2)
            #gender
            students['gender'].value_counts().plot(kind='pie',title='Gender Proportion of Teachers',autopct='%1.1f%%',ax=ax2,startangle=60)
            #students['birthday'].plot(kind='hist',bins=6,normed=True,title= 'Birthday distribution', ax=ax3)


            canvas = FigureCanvasTkAgg(fig, self.window)
            canvas.draw() # 注意show方法已经过时了,这里改用draw
            canvas.get_tk_widget().grid(row = 5, column = 0, columnspan = 5)



    def onInsert(self):
        try:
            usertype = self.v2.get()
            userid = self.ety_userid.get()
            username = self.ety_name.get()
            gender = self.v3.get()
            birthday = self.ety_birthday.get()
            department = self.ety_department.get()
            phone = self.ety_number.get()
            if data.check_user_id(userid):
                tkinter.messagebox.showinfo(title = '通知', message = 'ID已存在！')
            else:
                data.insert_user(usertype, userid, username, gender, birthday, department, phone)
            
            self.tree_show()
            self.show()
        except:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入用户ID和姓名')


    def onAlter(self):
        usertype = self.v2.get()
        userid = self.ety_userid.get()
        username = self.ety_name.get()
        gender = self.v3.get()
        birthday = self.ety_birthday.get()
        department = self.ety_department.get()
        phone = self.ety_number.get()
        if userid:
            data.update_user(usertype, userid, username, gender, birthday, department, phone)
        else:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入用户名')
        self.tree_show()
        self.show()


    def onDelete(self):
        userid = self.ety_userid.get()
        if userid: 
            data.delete_user(userid)
        else:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入用户名')
        self.tree_show()
        self.show()
        

    def exit(self):
        self.window.destroy()