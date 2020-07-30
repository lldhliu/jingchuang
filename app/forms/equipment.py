"""
 Created by ldh on 18-11-22
"""
from wtforms.validators import Length, NumberRange, DataRequired, Regexp, AnyOf
from wtforms import Form, StringField, IntegerField

from app.setting import QUERY_TYPE_LIST

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


class CreateEquipmentForm(Form):
    no = StringField(validators=[DataRequired(message='设备编号不可以为空')])
    cm_no = StringField(validators=[DataRequired(message='4G通信模块标识不可以为空')])
    name = StringField()
    # type = StringField()
    address = StringField()
    producer = StringField()


class QueryForm(Form):
    filter_by = StringField(validators=[AnyOf(values=QUERY_TYPE_LIST, message='请输入正确的查询选项')])
    filter_content = StringField()

