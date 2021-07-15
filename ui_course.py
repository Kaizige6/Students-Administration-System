import  tkinter as tk
import tkinter.messagebox
import data
from tkinter import ttk
from tkinter.constants import END

class CourseWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('教务管理系统——课程管理')
        self.window.geometry('600x300')
        
        #创建控件ttk列表
        columns = ('课程ID','课程名称','学分','说明')
        self.tree = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree.grid(row=0,rowspan=5)
        self.tree.column("课程ID", anchor = "center",width=50)
        self.tree.column("课程名称", anchor = "center",width=70)
        self.tree.column("学分", anchor = "center",width=50)
        self.tree.column("说明", anchor = "center",width=100)
        
        self.tree.heading("课程ID", text = "课程ID")
        self.tree.heading("课程名称", text = "课程名称")
        self.tree.heading("学分", text = "学分")
        self.tree.heading("说明", text = "说明")

        

        self.lb_courseid = tk.Label(self.window, text = '课程ID')
        self.lb_courseid.grid(row=0, column=1)
        self.lb_name = tk.Label(self.window, text = '课程名称')
        self.lb_name.grid(row=1, column=1)
        self.lb_score = tk.Label(self.window, text = '学分')
        self.lb_score.grid(row=2, column=1)
        self.lb_description = tk.Label(self.window, text = '说明')
        self.lb_description.grid(row=3, column=1)
        

        self.ety_courseid = tk.Entry(self.window)
        self.ety_courseid.grid(row=0, column=2,columnspan=2)
        self.ety_name = tk.Entry(self.window)
        self.ety_name.grid(row=1, column=2,columnspan=2)
        self.ety_score = tk.Entry(self.window)
        self.ety_score.grid(row=2, column=2,columnspan=2)
        self.ety_description = tk.Entry(self.window)
        self.ety_description.grid(row=3, column=2,columnspan=3)


        self.btn_insert = tk.Button(self.window, text = '插入', command = self.onInsert)
        self.btn_insert.grid(row=4, column=1)
        self.btn_alter = tk.Button(self.window, text = '更新', command = self.onAlter)
        self.btn_alter.grid(row=4, column=2)
        self.btn_delete = tk.Button(self.window, text = '删除', command = self.onDelete)
        self.btn_delete.grid(row=4, column=3)
        self.btn_exit = tk.Button(self.window, text = '退出', command = self.exit)
        self.btn_exit.grid(row=4, column=5, sticky = 'e')


        def get_tree(event):
            self.ety_courseid.delete(0, END)
            self.ety_name.delete(0, END)
            self.ety_score.delete(0, END)
            self.ety_description.delete(0, END)
            for item in self.tree.selection():
                item_text = self.tree.item(item,"values")
                self.ety_courseid.insert(0,item_text[0])
                self.ety_name.insert(0,item_text[1])
                self.ety_score.insert(0,item_text[2])
                self.ety_description.insert(0,item_text[3])
        
        
        self.tree.bind('<ButtonRelease-1>', get_tree)
        self.tree_show()
        self.window.mainloop() 


    def tree_show(self):
        #在TREE中显示数据   
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        course_list = data.get_course_list()
        for i in range(len(course_list)):
            self.tree.insert('',i,values = course_list[i])



    def onInsert(self):
        courseid = self.ety_courseid.get()
        coursename = self.ety_name.get()
        if len(self.ety_score.get().strip()) == 0:
            credit = self.ety_score.get()
        else: credit = float(self.ety_score.get())
        description = self.ety_description.get()

        if data.check_course_id(courseid):
            tkinter.messagebox.showinfo(title = '通知', message = '该课程已存在！')
        elif len(courseid.strip()) == 0 or len(coursename.strip()) == 0 or len(self.ety_score.get().strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入完整信息')
        else:
            data.insert_course(courseid, coursename, credit, description)
        self.tree_show()


    def onAlter(self):
        courseid = self.ety_courseid.get()
        coursename = self.ety_name.get()
        if len(self.ety_score.get().strip()) == 0:
            credit = self.ety_score.get()
        else: credit = float(self.ety_score.get())
        description = self.ety_description.get()

        if len(courseid.strip()) == 0 or len(coursename.strip()) == 0 or len(self.ety_score.get().strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入完整信息')
        else:
            data.update_course(courseid, coursename, credit, description)
            
        self.tree_show()


    def onDelete(self):
        courseid = self.ety_courseid.get()
        if len(courseid.strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入课程ID')
        else:
            data.delete_course(courseid)
        self.tree_show()
        

    def exit(self):
        self.window.destroy()
