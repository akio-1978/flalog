from flask_login import UserMixin

class User(UserMixin):
    """ユーザを表すオブジェクト"""
    """説明用なのでDBに格納もしないし、パスワードのハッシュ化とかもなし"""
    def __init__(self ,id, password) -> None:
        self.id = id
        self.password = password

def get_user():
    """ユーザはmyuserひとりだけ（簡略化）"""
    return User('myuser', 'mypassword')