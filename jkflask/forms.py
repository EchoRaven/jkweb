import wtforms
from wtforms.validators import length, email
from models import EmailInfo, UserInfo


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    email = wtforms.StringField(validators=[email()])
    vcode = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])

    def validate_vcode(self, field):
        vcode = field.data
        temail = self.email.data
        vcode_m = EmailInfo.query.filter_by(email=temail).first().vcode
        if not vcode == vcode_m:
            raise wtforms.ValidationError("验证码错误")


    def validate_email(self, field):
        temail = field.data
        email_m = UserInfo.query.filter_by(email=temail).first()
        if email_m:
            raise wtforms.ValidationError("该邮箱已注册过账户")

