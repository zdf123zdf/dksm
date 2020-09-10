from socket import *
from tkinter import *

# 端口扫描
def port_scan():
    # 获取用户输入的IP,端口，超时
    ip=entry1.get()
    port=entry2.get()
    time=entry3.get()
    try:
        sock = socket(AF_INET, SOCK_STREAM)  # 实例化socket
        sock.settimeout(int(time))   #限制重连时间
        sock.connect((ip, int(port)))  # 对对应主机的对应端口发起连接
        result = f'{port}端口开放'
        sock.close()  # 关闭连接
    except Exception as e:
        result = f'{port}端口关闭'
    listb.insert(0, result)

root = Tk()  # 创建窗口对象的背景色
root.title('端口扫描')    # 标题
# 窗口大小 窗口位置
root.geometry("220x320+200+300")

# 标签控件
label1=Label(root,text="输入IP",font=('微软雅黑',14))
label1.grid(padx=0,pady=0)   # 网格布局
label2=Label(root,text="输入端口号",font=('微软雅黑',14))
label2.grid(row=2)
label3=Label(root,text="超时(毫秒)",font=('微软雅黑',14))
label3.grid(row=4)
label4=Label(root,text="扫描结果",font=('微软雅黑',14))
label4.grid(row=6)

# 输入框

entry1=Entry(root,font=('微软雅黑',10))
entry1.grid(row=1)
entry2=Entry(root,font=('微软雅黑',10))
entry2.grid(row=3)
entry3=Entry(root,font=('微软雅黑',10))
entry3.grid(row=5)

# 点击按纽
buttom1=Button(root,text="开始扫描",font=('微软雅黑',14),command=port_scan)
buttom1.grid(row=8)


# 创建列表组件
listb = Listbox(root)
listb['width']=30
listb['height']=4
listb.grid(row=7)
root.mainloop()

