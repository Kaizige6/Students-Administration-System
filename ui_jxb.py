import  tkinter as tk
import tkinter.messagebox
import data
from tkinter import ttk
from tkinter.constants import END

class JXBWindow():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('教务管理系统——开课管理')
        self.window.geometry('850x300')
        
        #创建控件ttk列表
        columns = ('教学班号','课程ID','课程名称','教师ID','教师姓名','时间地点')
        self.tree = ttk.Treeview(self.window, show='headings',columns = columns)
        self.tree.grid(row=0,rowspan=5)
        self.tree.column("教学班号", anchor = "center",width=67)
        self.tree.column("课程ID", anchor = "center",width=45)
        self.tree.column("课程名称", anchor = "center",width=67)
        self.tree.column("教师ID", anchor = "center",width=45)
        self.tree.column("教师姓名", anchor = "center",width=67)
        self.tree.column("时间地点", anchor = "center",width=105)
        self.tree.heading("教学班号", text = "教学班号")
        self.tree.heading("课程ID", text = "课程ID")
        self.tree.heading("课程名称", text = "课程名称")
        self.tree.heading("教师ID", text = "教师ID")
        self.tree.heading("教师姓名", text = "教师姓名")
        self.tree.heading("时间地点", text = "时间地点")
        

        #输出文本框
        self.lb_jxbid = tk.Label(self.window, text = '教学班号')
        self.lb_jxbid.grid(row=0, column=1)
        self.lb_courseid = tk.Label(self.window, text = '课程ID')
        self.lb_courseid.grid(row=1, column=1)
        self.lb_teacherid = tk.Label(self.window, text = '教师ID')
        self.lb_teacherid.grid(row=2, column=1)
        self.lb_detail = tk.Label(self.window, text = '时间地点')
        self.lb_detail.grid(row=3, column=1)
        self.lb_teachername = tk.Label(self.window, text = '教师姓名')
        self.lb_teachername.grid(row=1, column=3)
        self.lb_coursename = tk.Label(self.window, text = '课程名称')
        self.lb_coursename.grid(row=2, column=3)


        self.ety_jxbid = tk.Entry(self.window)
        self.ety_jxbid.grid(row=0, column=2)
        self.ety_courseid = tk.Entry(self.window)
        self.ety_courseid.grid(row=1, column=2)
        self.ety_coursename = tk.Entry(self.window)
        self.ety_coursename.grid(row=1, column=4)
        self.ety_teacherid = tk.Entry(self.window)
        self.ety_teacherid.grid(row=2, column=2)
        self.ety_teachername = tk.Entry(self.window)
        self.ety_teachername.grid(row=2, column=4)
        self.ety_detail = tk.Entry(self.window,width=40)
        self.ety_detail.grid(row=3, column=2,columnspan=3)
        
        


        #按钮
        self.btn_insert = tk.Button(self.window, text = '插入', command = self.onInsert)
        self.btn_insert.grid(row=4, column=1)
        self.btn_alter = tk.Button(self.window, text = '更新', command = self.onAlter)
        self.btn_alter.grid(row=4, column=2)
        self.btn_delete = tk.Button(self.window, text = '删除', command = self.onDelete)
        self.btn_delete.grid(row=4, column=3)
        self.btn_exit = tk.Button(self.window, text = '退出', command = self.exit)
        self.btn_exit.grid(row=4, column=4)


        def get_tree(event):
            self.ety_jxbid.delete(0, END)
            self.ety_courseid.delete(0, END)
            self.ety_coursename.delete(0, END)
            self.ety_teacherid.delete(0, END)
            self.ety_teachername.delete(0, END)
            self.ety_detail.delete(0, END)
            for item in self.tree.selection():
                item_text = self.tree.item(item,"values")
                self.ety_jxbid.insert(0,item_text[0])
                self.ety_courseid.insert(0,item_text[1])
                self.ety_coursename.insert(0,item_text[2])
                self.ety_teacherid.insert(0,item_text[3])
                self.ety_teachername.insert(0,item_text[4])
                self.ety_detail.insert(0,item_text[5])
        self.tree.bind('<ButtonRelease-1>', get_tree)

        

        self.tree_show()
        self.window.mainloop() 



    def tree_show(self):
        #在TREE中显示数据   
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        jxb_list = data.get_jxb_list()
        for i in range(len(jxb_list)):
            self.tree.insert('',i,values = jxb_list[i])



    def onInsert(self):
        jxbid = self.ety_jxbid.get()
        courseid = self.ety_courseid.get()
        userid = self.ety_teacherid.get()
        description = self.ety_detail.get()
        if data.check_jxb_id(jxbid):
            tkinter.messagebox.showinfo(title = '通知', message = '该课程已存在！')
        if len(jxbid.strip()) == 0 or len(courseid.strip()) == 0 or len(userid.strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入完整信息')
        else:
            data.insert_jxb(jxbid, courseid, userid, description)
        self.tree_show()


    def onAlter(self):
        jxbid = self.ety_jxbid.get()
        courseid = self.ety_courseid.get()
        userid = self.ety_teacherid.get()
        description = self.ety_detail.get()
        if len(jxbid.strip()) == 0 and len(courseid.strip()) == 0 and len(userid.strip()) == 0 and len(description.strip()) == 0:
            tkinter.messagebox.showinfo(title = '通知', message = '请输入完整信息')
        else:
            data.update_jxb(jxbid, courseid, userid, description)
        self.tree_show()


    def onDelete(self):
        jxbid = self.ety_jxbid.get()
        if len(jxbid.strip()) == 0: 
            tkinter.messagebox.showinfo(title = '通知', message = '请输入教学班号')
        else:
            data.delete_user(jxbid)
        self.tree_show()
        

    def exit(self):
        self.window.destroy()


