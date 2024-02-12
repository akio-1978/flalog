from flask_login import UserMixin
# すごく簡略化したユーザオブジェクト

class User(UserMixin):
    """ユーザを表すオブジェクト、ただIDとパスワードを持つ"""
    def __init__(self ,id, password) -> None:
        self.id = id
        self.password = password

# 簡略化のため、ユーザはひとりだけ
user = User('myuser', 'mypassword')

def my_user(id):
    """常に同じユーザを返す（idはそれっぽく書いたダミー）"""
    return user
