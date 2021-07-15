import  tkinter as tk
import tkinter.messagebox
import data
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.constants import END


class StudentWindow():
    def __init__(self,window,userid):
        self.window = window
        self.userid = userid
        self.window.title('教务管理系统——选课管理')
        self.window.geometry('800x600')
        
        #创建控件ttk列表
        columns = ('教学班号','课程ID','课程名称','教师ID','教师姓名','时间地点','成绩')
        
         #已选的课
        self.tree = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree.grid(row=2,rowspan=5, columnspan=3)
        self.tree.column("教学班号", anchor = "center",width=110)
        self.tree.column("课程ID", anchor = "center",width=90)
        self.tree.column("课程名称", anchor = "center",width=110)
        self.tree.column("教师ID", anchor = "center",width=90)
        self.tree.column("教师姓名", anchor = "center",width=110)
        self.tree.column("时间地点", anchor = "center",width=170)
        self.tree.column("成绩", anchor = "center",width=90)

        
        self.tree.heading("教学班号", text = "教学班号")
        self.tree.heading("课程ID", text = "课程ID")
        self.tree.heading("课程名称", text = "课程名称")
        self.tree.heading("教师ID", text = "教师ID")
        self.tree.heading("教师姓名", text = "教师姓名")
        self.tree.heading("时间地点", text = "时间地点")
        self.tree.heading("成绩", text = "成绩")
        '''
        self.VScroll1 = ttk.Scrollbar(self.window, orient='vertical', command=self.tree.yview)
        self.VScroll1.grid(row=1,column=0)
        # 给treeview添加配置
        self.tree.configure(yscrollcommand=self.VScroll1.set)
        '''


        #未选的课
        self.tree1 = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree1.grid(row=8,rowspan=5,columnspan=3)
        self.tree1.column("教学班号", anchor = "center",width=110)
        self.tree1.column("课程ID", anchor = "center",width=90)
        self.tree1.column("课程名称", anchor = "center",width=110)
        self.tree1.column("教师ID", anchor = "center",width=90)
        self.tree1.column("教师姓名", anchor = "center",width=110)
        self.tree1.column("时间地点", anchor = "center",width=170)
        self.tree1.column("成绩", anchor = "center",width=90)

        
        self.tree1.heading("教学班号", text = "教学班号")
        self.tree1.heading("课程ID", text = "课程ID")
        self.tree1.heading("课程名称", text = "课程名称")
        self.tree1.heading("教师ID", text = "教师ID")
        self.tree1.heading("教师姓名", text = "教师姓名")
        self.tree1.heading("时间地点", text = "时间地点")
        self.tree1.heading("成绩", text = "成绩")




         #输出文本框
        self.lb_jxbid = tk.Label(self.window, text = '已选的课：',font = tkFont.Font(size = 14))
        self.lb_jxbid.grid(row=1, column=1)
        self.lb_jxbid = tk.Label(self.window, text = '所有课程：',font = tkFont.Font(size = 14))
        self.lb_jxbid.grid(row=7, column=1)
        self.lb_jxbid = tk.Label(self.window, text = '教学班号',bg = 'red', font = ('Verdana', 20))
        self.lb_jxbid.grid(row=0, column=0)
        
        
        self.ety_jxbid = tk.Entry(self.window)
        self.ety_jxbid.grid(row=0, column=1)

        
        self.btn_alter = tk.Button(self.window, text = '选课', command = self.OnChoose)
        self.btn_alter.grid(row=13, column=0)
        self.btn_delete = tk.Button(self.window, text = '退课', command = self.OnQuit)
        self.btn_delete.grid(row=13, column=1)
        self.btn_exit = tk.Button(self.window, text = '退出', command = self.exit)
        self.btn_exit.grid(row=13, column=2)



        self.tree_show() #已选的课
        self.tree_show_all() #所有的课
        self.window.mainloop() 


        #已选的课
    def tree_show(self):
        #在TREE(已选成绩)中显示数据   
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        grade_list = data.get_grades_list_by_student(self.userid)
        for i in range(len(grade_list)):
            self.tree.insert('',i,values = grade_list[i])


    def tree_show_all(self):
        #在TREE1（所有成绩）中显示数据
        x = self.tree1.get_children()
        for item in x:
            self.tree1.delete(item)
        list = data.get_all_grades_list_by_student()
        for i in range(len(list)):
            self.tree1.insert('',i,values = list[i])



    def OnChoose(self):
        jxbid = self.ety_jxbid.get()
        userid = self.userid
        if data.check_grade_id(jxbid,userid):
            tkinter.messagebox.showinfo(title = '通知', message = '该课程已存在！')
        elif len(jxbid.strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入信息')
        else:
            data.insert_grade(jxbid, userid)
        self.tree_show()



    def OnQuit(self):
        jxbid = self.ety_jxbid.get()
        userid = self.userid
        if len(jxbid.strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入信息')
        else:
            data.delete_grade(jxbid, userid)
        self.tree_show()
        

    def exit(self):
        self.window.destroy()
