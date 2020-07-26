"""
 Created by ldh on 18-11-22
"""
from wtforms.validators import Length, NumberRange, DataRequired, Regexp
from wtforms import Form, StringField, IntegerField

__author__ = "ldh"


# 第三方验证器库wtforms使用
class SearchForm(Form):
    # DataRequired()防止参数只有空格
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])  # message='自定义错误提示'
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(validators=[DataRequired(), Length(
        min=2, max=20, message='收件人姓名长度必须在2到20个字符之间')])
    mobile = StringField(validators=[DataRequired(), Regexp(
        '^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField()
    address = StringField(validators=[DataRequired(), Length(
        min=10, max=70, message='地址还不到10个字吗？尽量写详细一点吧')])

class CreateForm(Form):
    pass