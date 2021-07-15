import  tkinter as tk
from tkinter.constants import END
import tkinter.messagebox
from typing import Text
import data
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import pylab as mpl


class TeacherWindow():
    def __init__(self,window,userid):
        self.window = window
        self.userid = userid
        self.window.title('教务管理系统——成绩管理')
        self.window.geometry('800x600')
        
        #创建控件ttk列表
        columns = ('学生ID','学生姓名','性别','所在院系','成绩')
        self.tree = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree.grid(row=5, column=0,columnspan=5)
        self.tree.column("学生ID", anchor = "center",width=100)
        self.tree.column("学生姓名", anchor = "center",width=150)
        self.tree.column("性别", anchor = "center",width=100)
        self.tree.column("所在院系", anchor = "center",width=150)
        self.tree.column("成绩", anchor = "center",width=100)

        
        
        self.tree.heading("学生ID", text = "学生ID")
        self.tree.heading("学生姓名", text = "学生姓名")
        self.tree.heading("性别", text = "性别")
        self.tree.heading("所在院系", text = "所在院系")
        self.tree.heading("成绩", text = "成绩")



         #输出文本框
        self.lb_jxbid = tk.Label(self.window, text = '教学班号')
        self.lb_jxbid.grid(row=0, column=0)
        self.lb_name = tk.Label(self.window, text = '姓名')
        self.lb_name.grid(row=2, column=0)
        self.lb_score = tk.Label(self.window, text = '成绩')
        self.lb_score.grid(row=3, column=0)
        self.lb_jxbid = tk.Label(self.window, text = '学生ID')
        self.lb_jxbid.grid(row=1, column=0)
        self.lb_average = tk.Label(self.window, text = '平均分:')
        self.lb_average.grid(row=4, column=0)
        self.lb_max = tk.Label(self.window, text = '最高分:')
        self.lb_max.grid(row=4, column=2)


        #OPTIONMUNE
        jxbid_list = data.get_jxbid_list_by_user(self.userid)
        self.v = tk.StringVar()
        self.v.set(jxbid_list[0])
        self.om_jxbid = ttk.OptionMenu(self.window,self.v,'',*jxbid_list)
        self.om_jxbid['width'] = 6
        self.om_jxbid.grid(row=0, column=1)

        #输入框
        self.ety_course = tk.Entry(self.window)
        self.ety_course.grid(row=0, column=2)
        self.ety_name = tk.Entry(self.window)
        self.ety_name.grid(row=2, column=1)
        self.ety_score = tk.Entry(self.window)
        self.ety_score.grid(row=3, column=1)
        self.ety_studentid = tk.Entry(self.window)
        self.ety_studentid.grid(row=1, column=1)
        self.ety_average = tk.Entry(self.window)
        self.ety_average.grid(row=4, column=1)
        self.ety_max = tk.Entry(self.window)
        self.ety_max.grid(row=4, column=3)

        #输出按钮
        self.btn_update = tk.Button(self.window, text = '确定(显示对应课程)', command = self.show, fg='white', bg='gray', activebackground='black', activeforeground='white')
        self.btn_update.grid(row=0, column=3)

        self.btn_alter = tk.Button(self.window, text = '录入', command = self.OnInput,fg='white', bg='gray', activebackground='black', activeforeground='white')
        self.btn_alter.grid(row=2, column=2)

        def get_tree(event):
            self.ety_studentid.delete(0, END)
            self.ety_name.delete(0, END)
            self.ety_score.delete(0, END)
            
            for item in self.tree.selection():
                item_text = self.tree.item(item,"values")
                self.ety_studentid.insert(0,item_text[0])
                self.ety_score.insert(0,item_text[4])
                self.ety_name.insert(0,item_text[1])
                
        
        
        self.tree.bind('<ButtonRelease-1>', get_tree)

        self.OnMax()
        self.OnAverage()
        self.show()
        self.tree_show()
        self.window.mainloop() 

    

    def tree_show(self):
        #在TREE中显示数据   
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        jxbid = self.v.get()
        grade_list = data.get_grade_list_by_jxbid(jxbid)
        for i in range(len(grade_list)):
            self.tree.insert('',i,values = grade_list[i])

    
    def show(self):
        self.OnMax()
        self.OnAverage()

        #信息可视化
        mpl.rcParams['font.sans-serif'] = ['FangSong']    #设置字体，不然是乱码
        self.tree_show() 
        jxbid = self.v.get()   
        fig = plt.figure(figsize=(7.5,2.2), dpi = 100)
        ax1 = fig.add_subplot(1,3,1)
        ax2 = fig.add_subplot(1,3,2)
        ax3 = fig.add_subplot(1,3,3)

        grade_list = data.get_grade_list_by_jxbid(jxbid)
        values = list(zip(*grade_list))

        _data = {'gender':list(values[2]),
                'major':list(values[3]),
                'score':list(values[4])}
        students = DataFrame(_data, columns = ['gender', 'major', 'score'])
        #major
        students['major'].value_counts().plot(kind = 'bar', color = 'pink', title = 'Major Distribution of Students', ax = ax1)
        for tick in ax1.get_xticklabels():
            tick.set_rotation(20)
        plt.gcf().subplots_adjust(bottom=0.25)
        #gender
        students['gender'].value_counts().plot(kind='pie',title='Gender Proportion of Students',autopct='%1.1f%%',ax=ax2,startangle=60)
        #score
        students['score'].plot(kind='hist', bins=3, title= 'Score Distribution', ax=ax3)
        plt.gcf().subplots_adjust(bottom=0.18)

        canvas = FigureCanvasTkAgg(fig, self.window)
        canvas.draw() # 注意show方法已经过时了,这里改用draw
        canvas.get_tk_widget().grid(row = 8, column = 0, columnspan = 5)


        #根据JXB显示课程信息
        self.ety_course.delete(0, END)
        jxbid = self.v.get()
        course = data.get_course_by_jxbid(jxbid)
        course = str(course)
        self.ety_course.insert(0,course)

        self.OnMax()
        self.OnAverage()



    def OnMax(self):
        self.ety_max.delete(0, END)
        jxbid = self.v.get()
        grade_list = data.get_grade_list_by_jxbid(jxbid)
        grades_list = []
        score = []
        for i in grade_list:
            grades_list.append(list(i))
        for i in range(len(grade_list)):
            if grades_list[i][4] == None:
                grades_list[i][4] = 0
            score.append(grades_list[i][4])
        self.ety_max.insert(0,max(score))



    def OnAverage(self):
        self.ety_average.delete(0, END)
        jxbid = self.v.get()
        grade_list = data.get_grade_list_by_jxbid(jxbid)
        grades_list = []
        score = []
        for i in grade_list:
            grades_list.append(list(i))
        for i in range(len(grade_list)):
            if grades_list[i][4] == None:
                grades_list[i][4] = 0
            score.append(grades_list[i][4])
        self.ety_average.insert(0,np.mean(score))


    #分数录入按钮函数
    def OnInput(self):
        jxbid = self.v.get()
        userid = self.ety_studentid.get()
        score = self.ety_score.get()
        data.update_grade_score(score, jxbid, userid)
        self.tree_show()
