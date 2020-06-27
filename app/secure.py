"""
 Created by ldh on 18-11-22
"""
__author__ = "ldh"

"""
数据库密码，账号，flask appkey等机密的配置放在这里
"""
DEBUG = True  #  False
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:2255@47.98.177.221:3306/jingchuang'
SECRET_KEY = 'this is a secret key build by your dad'


# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '1151375085@qq.com'  # 自己QQ邮箱
MAIL_PASSWORD = 'puxkebbknyqwigja'
