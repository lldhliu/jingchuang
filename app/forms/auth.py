"""
 Created by ldh on 18-12-3
"""
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from app.models.user import User

__author__ = "ldh"


class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                        Email(message='电子邮箱不符合规范')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空, 请输入你的密码'),
                             Length(5, 32)])

    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符, 最多十个字符')])

    # 自定义验证器
    def validate_email(self, field):
        # db.session
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    # 自定义验证器
    def validate_nickname(self, field):
        # db.session
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


class LoginForm(Form):
    nickname = StringField(validators=[DataRequired(message='用户名不能为空'),
                                       Length(2, 10, message='昵称至少需要两个字符, 最多十个字符')])

    password = PasswordField(validators=[DataRequired(message='密码不可以为空, 请输入你的密码'),
                                         Length(5, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])


class ResetPasswordForm(Form):
    password1 = PasswordField(validators=[
        DataRequired(), Length(5, 32, message='密码长度至少需要在5到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField(validators=[
        DataRequired(), Length(5, 32)])


class ChangePasswordForm(Form):
    old_password = PasswordField(validators=[DataRequired(
        message='密码不可以为空, 请输入你的密码'), Length(5, 32)])

    new_password1 = PasswordField(validators=[
        DataRequired(), Length(5, 32, message='密码长度至少需要在5到32个字符之间'),
        EqualTo('new_password2', message='两次输入的新密码不相同')])
    new_password2 = PasswordField(validators=[
        DataRequired(), Length(5, 32)])


