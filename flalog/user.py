from flask_login import UserMixin

# ユーザオブジェクトの例 とりあえずUserMixinは継承しておく
# ほとんどの記事ではSQLAlchemyのModelとして構築しているけど、Flask-LoginとDBは関係ない
class User(UserMixin):
    def __init__(self ,id, password) -> None:
        self.id = id
        self.password = password

# DBとか使わないでひとりだけユーザを作る
my_user = User('myuser', 'mypassword')
