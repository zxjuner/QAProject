import os

COUNT = 0
WHETHER_LOGIN = {'is_login': 'error'}
USER_LIST = []

# 用户注册
def register():
    username = input('输入用户名:')
    while True:
        password = input('输入密码:')
        if len(password) >= 5:
            break
        else:
            print('请输入大于5位数的密码')

register()


def user_login(func):
    def inner(*args,**kwargs):
           if WHETHER_LOGIN['is_login'] == 'success':
               r = func()
               return r
           else:
               user_no = input('请登录后再试【1：用户登录；2：返回】:')
               if user_no == '1':
                   login()
               else:
                   print('返回成功')
                   main()
    return inner


# 修改密码
@user_login
def alter():
    print('当前用户为:{}'.format(USER_LIST[0]))
    while True:
        old_user_password = input('请输入当前用户的旧密码:')
        if old_user_password == USER_LIST[1]:
            flag = True
            count = 3
            while flag:
                count -= 1
                new_user_password = input('请输入当前用户的新密码:')
                new_user_password = input('再次输入当前用户的新密码:')
                if len(new_user_password) >= 5:
                    flag = False
                elif count == 0:
                    print('输入多次，程序不合法！！！')
                    main()
                else:
                    print('输入不合法，请输入大于5位数的密码')
        if new_user_password == new_user_password:
            with open('user.txt','r') as user_info:
                old_user_info = '|'.join(USER_LIST)
                for line in user_info:
                    if USER_LIST[0] in line:
                        USER_LIST[1] = new_user_password
                        new_user_info = '｜'.join(USER_LIST)
                        break
            with open('user.txt','r') as old_user:
                lines = old_user.readlines()
            with open('user.txt','w') as new_user:
                for line in lines:
                    if old_user_info in line:
                        line = line.replace(old_user_info,new_user_info)
                    new_user.write(line)
            print('修改成功!')
            break

        else:
            print('两次输入的密码不相同，程序自动返回。。。')
            main()
    else:
        print('当前用户密码输入错误，程序自动返回。。。')
        main()

def verifi_password():
    with open('user.txt','r') as old_user:
        lines = old_user.readlines()
    flag = True
    cout = 3
    while flag:
        cout -= 1
        user_info = input('请输入用户名:')
        if user_info == '':
            print('你没有输入任何用户。。。\n')
            manage()
        for line in lines:
            user_all_info = line.strip('\n').split('|')
            if user_info == user_all_info[0]:
                current_user = user_all_info
                flag = False
        if cout == 0:
            print('然而，你可能不知道有哪些用户，赶紧去查看吧。。。')
            manage()

    lines_user = [lines,current_user]
    return lines_user













# 用户信息
@user_login
def see():
    if USER_LIST[3] == '1':
        user_level = '管理员用户'
    else:
        user_level = '普通用户'
    user_see = '''
    ----------------------------------
    用户名:    [%s]
    密码:      [%s]
    邮箱:      [%s]
    用户等级:   [%s]
    ----------------------------------
    ''' % (USER_LIST[0],USER_LIST[1],USER_LIST[2],user_level)
    print(user_see)

def error_password():
    counter = 3
    while True:
        counter -= 1
        if counter == 0:
            print('你输入的错误太多，程序自动返回。。。。')
        else:
            print('两次输入的密码不相同。。。')
            continue




# 用户管理
def manage():
    pass

# 退出登录
def exit_login():
    global USER_LIST
    if USER_LIST:
        quit_login = input('当前用户为{},确定要退出【Y/N】'.format[0])
        if quit_login in ('Y','y','yes','yES','yeS','yEs','YES','Yes','YEs'):
            WHETHER_LOGIN['is_login'] = 'error'
            USER_LIST = []
        elif quit_login in ('N','no','No','NO','nO'):
            print('退出失败')
    else:
        print('没有用户登录。。。')


def login():
    print('用户登录'.center(82,'='))
    username = input('请输入用户名:')
    password = input('请输入密码:')
    with open('user.txt','r') as user:
        for line in user:
            f_user_list = line.strip('\n').split('|')
            if f_user_list[0] == username == username and f_user_list[1] == password:
                print('登录成功')
                global USER_LIST
                USER_LIST = f_user_list
                WHETHER_LOGIN['is_login'] = 'success'
                WHETHER_LOGIN['is_login'] = username
                return f_user_list
        else:
            print('登录失败')


# 用户管理系统主界面
def main():
    print('用户管理系统'.center(80,'*') + '\n')
    print('1.用户登录；2.用户注册；3.修改密码；4.用户信息；5.用户管理；6.退出登录；7.退出程序')
    inp = input('请输入序号:')
    if inp == '1':
        user_login()
    elif inp == '2':
        register()
    elif inp == '3':
        alter()
    elif inp == '4':
        see()
    elif inp == '5':
        manage()
    elif inp == '6':
        exit_login()
    elif inp == '7':
        exit('程序已退出！！！')
    else:
        if COUNT == 3:
            exit('输入错误次数太多，程序自动退出。。。')
        else:
            print('输入有误，请重新输入。。。\n')


main()