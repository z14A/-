# 编写机构：金小意微科工作室
# 编   写：
# 开发时间： 下午 3:04
print('欢迎使用由New Planet Studio发行的收据管理系统 v1.7.27！\n')

#代码段正常运行，请勿随意修改！

filename='student.txt' #filename='student.txt'
import os

def main():
    while True:
        abb = int(input('请输入管理员密码；或输入0退出系统：\t'))
        if abb in [999999,0]:#默认密码999999
            if abb == 0:
                answer = input("你确定要退出系统吗？   y/n \t")
                if answer == 'y' or answer == 'Y':
                    print('感谢你的使用！！！')
                    break
                else:
                    continue
            elif abb == 999999:
                print('欢迎使用❤')
                amain()
        else:
            print('密码输入错误！！！请重新输入或退出系统！')

#启动密码确认7.26测试完毕！


def amain():
    while True:
            menm()
            choice=int(input('请选择功能你所需要的功能(回复数字即可)：\t'))
            if choice in [0,1,2,3,4,5,6,7]:
                if choice==0:
                    main()
                    '''
                    answer=input("你确定要退出系统管理吗？   y/n \t")
                    if answer=='y' or answer=='Y':
                        print('感谢你的使用！！！')
                        break
                    else:
                        continue
                        '''
                elif choice==1:
                    insert()       #录入信息
                elif choice==2:
                    search()
                elif choice==3:
                    delete()
                elif choice==4:
                    modify()
                elif choice==5:
                    total()
                elif choice==6:
                    show()
                elif choice==7:
                    gethelp()

def menm():
    print('==========================收据管理系统==========================')
    print('\t\t\t1.录入收据信息')
    print('\t\t\t2.查找收据信息')
    print('\t\t\t3.删除收据信息')
    print('\t\t\t4.修改收据信息')
    print('\t\t\t5.统计收据总数')
    print('\t\t\t6.显示所有信息')
    print('\t\t\t7.获取帮助途径')
    print('\t\t\t0.退出系统管理')
    print('----------------------------------------------------------------')

def gethelp():
    print('\n\n\n')
    print('本管理产品由NewPlanet Studio开发，请尊重著作权!\n系统默认密码999999，如需修改请在源码的基础上修改，或者联系官方管理员，谢谢合作！\n官方客服QQ:750471358  官网：http://box1618915628615.nb3.site.my-qcloud.com/')
    abg=input('回车返回菜单：\t')

#菜单模块

def insert():
    student_list=[]
    while True:
        id=input('请输入收据单号：\t')
        if not id:
            break
        name=input('请输入绑定的电话号码: \t')
        if not name:
            break

        try:
            money=int(input('请输入押金金额: \t'))
            phone=(input('请输入押金产品名称（个数）；\t'))
            whether=(input('是否已退款0/1（可用中文登记）：\t'))
        except:
            print('输入无效，请重新输入！\t')
            continue
        #录入单号信息到字典中
        student={'id':id,'name':name,'money':money,'phone':phone,'whether':whether}
        #将信息添加到列表中
        student_list.append(student)
        answer=input('是否继续添加？  y/n \t')
        if answer=='y':
            continue
        else:
            break

    #调用sava函数
    sava(student_list)
    print('收据信息录入完毕！')

#添加信息模块

def sava(lst):
    try:
        stu_txt=open(filename,'a',encoding='utf-8')
    except:
        stu_txt=open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

#保存数据控制模块

def search():
    student_query=[]
    while True:
        id=''
        name=''
        if os.path.exists(filename):
            mode=input('按单号查找请输入1，按电话号码查找请输入2 \t')
            if mode=='1':
                id=input('请输入收据单号 \t')
            elif mode=='2':
                name=(input('请输入电话号码 \t'))
            else:
                print('您的输入有误，请重新输入：\t')
                search()
            with open(filename,'r',encoding='utf-8')as rfile:#rfile
                student=rfile.readlines()
                for item in student:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    elif name!='':
                        if d['name']==name:
                            student_query.append(d)

            #显示查询结果
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer=input('是否继续查找？    y/n \t')
            if answer=='y':
                continue
            else:
                break
        else:
            print("未保存信息")
            return
def show_student(lst):
    if len(lst)==0:
        print('没有查询到信息，无法显示！')
        return
    #定义标题格式
    print('\n')
    print("---单号------------电话号码------------金额（元）---------------产品-----------------是否退款0/1")
    '''
    format_title='{:^8}\t{:^14}\t{:^6}\t{:^8}\t{:^10}'
    print(format_title.format('单号','产品','金额','电话号码','是否退款0/1'))
    #定义内容格式
    '''
    format_data='{:^10}\t{:^16}\t{:^2}\t{:^22}\t{:^8}'#原'{:^10}\t{:^16}\t{:^2}\t{:^22}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('money'),
                                 item.get('phone'),
                                 item.get('whether')
                                 ))

#查找信息模块
''''
def ade():
    while True:
        abf = input('请输入管理员删除密码')
        if abf ==190414:
            delete()
        else:
            print('密码输入错误，已自动退出删除模块')
            break
'''
#查找信息加密删除验证模块

def delete():
    while True:
        student_id = input("请输入要删除的信息的单号：\t")
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8')as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8')as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转化成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的单号信息已被删除')
                    else:
                        print(f'没有找到ID为{student_id}的单号信息')
            else:
                print('无单号信息')
                break
            show()
            answer = input("是否继续删除？ y/n \t")
            if answer == 'y':
                continue
            else:
                break

#删除信息模块
#可以根据此模块开发程序初始化（请输入密码），清空所有数据！

def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()
    else:
        return
    student_id=input('请输入要修改信息的单号:\t')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print(f'找到{student_id}单号的信息，你现在可以选择修改了！')
                '''
                aone=int(input('请选择要修改的信息序列（如下）\n'+'1.修改产品  2.修改金额  3.修改电话号码  4.修改登记退款  5.返回重新选择'))
                if aone in [1,2,3,4,5,]:
                    if aone==5:
                        atwo=int(input('您确定要返回上一级吗？ y/n'))
                        if atwo=='y' or atwo=='Y':
                            break
                        else:
                            continue

                    elif aone==1:
                        while True:
                            try:
                                d['name']=input('请输入产品')
                    elif aone==2:
                        while True:
                            try:
                                d['money']=input('请输入金额')
                    elif aone==3:
                        while True:
                            try:
                                d['phone']=input('请输入电话码')
                    elif aone==4:
                        while True:
                            try:
                                d['whether']=input('请输入登记是否退款')
                    '''
                while True:
                    try:

                        d['name']= input('请输入电话号码: \t')
                        d['money'] = input('请输入押金金额：\t')
                        d['phone'] = input('请输入产品名称：\t')
                        d['whether'] = input('请登记是否已退款：\t')
                    except:
                        print('您的输入有误，请重新输入！！！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其他id信息？ y/n \t')
        if answer=='y':
            modify()

#修改信息模块

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as rfile:
            students=rfile.readlines()
            if students:
                print(f'一共有{len(students)}项收据信息存在数据库里！')
            else:
                print('数据库里暂时没有收据信息！')
    else:
        print('暂未保存任何收据信息')

#计算总数模块

def show():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8')as  rfile:
            students=rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存任何数据！！！')

#显示所有模块

if __name__ == '__main__':
    main()

