
# 判断用户是否登陆
def register():
    username = input('输入用户名:')
    while True:
        password = input('输入密码:')
        if len(password) >= 5:
            break
        else:
            print('请输入大于5位数的密码')

register()