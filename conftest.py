import pytest
import requests

'''单独管理一些预置的操作场景，登录接口可以写入conftest文件中，并放入根目录，所有测试用例均可以调用 
    
   host/email 等可以放到配置文件中（在项目的根目录一般会放一个 pytest.ini 写一些配置参数）
   
   字典接口可以放到json参数文件
'''


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )
    # 添加参数到配置文件pytest.ini
    #type 是类型，默认None，可以设置：None, "pathlist", "args", "linelist", "bool"
    parser.addini('host_url', type=None, default="https://api.apiopen.top/", help='添加 host 访问地址参数')
    parser.addini('smtp_server', type=None, default="smtp.163.com", help='smtp服务器')
    parser.addini('port', type=None, default="465", help='端口号')
    parser.addini('sender', type=None, default="xtgao@huaxing.com", help='发送人')
    parser.addini('emailpsw', type=None, default="1234567", help='密码')
    parser.addini('receiver', type=None, default="xtgao@huaxing.com", help='收件人')
    parser.addini('cookie', type=None, default="_quiver_session=R2diSWkvclR5alBpenE", help='cookie不一定要用')
    parser.addini('username', type=None, default="xtgao@huaxing.com", help='系统登录账号')
    parser.addini('userpsw', type=None, default="1234567", help='系统登录密码')


# 在FA系统中暂时不用login方式进行登陆授权，force系统可以使用
# def login_index(username,psw,pytestconfig):
#     #登录方法
#     url = pytestconfig.getini('host_url')+"/api/login"
#     param ={"username":username,"password":psw}
#     method = "post"
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
#         'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     }
#     r=requests.post(url,data=param,headers=header)
#     return r.json()
   
# @pytest.fixture(scope="session")
'''使用@pytest.fixture装饰器'''
# def login(pytestconfig):
#     #从管理配置中获取用户名和密码
#     username=pytestconfig.getini('username')
#     psw=pytestconfig.getini('userpsw')
#     #调用登录方法
#     r=login_index(username,psw,pytestconfig)
#     idtoken = r['result']['idToken']
#     return idtoken
