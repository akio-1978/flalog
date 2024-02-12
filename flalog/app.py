from flask import Flask, url_for, render_template, redirect, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from .user import my_user

app = Flask(__name__)
# flaskのセッション用キー
app.config['SECRET_KEY'] = 'secret-key-for-flask-session'

# Flask-Loginの初期化
login_manager = LoginManager()
login_manager.init_app(app)
# ログインしていない時に送り返す先（ログイン画面）
login_manager.login_view = 'login_gamen'
# ログインしていない時に表示するメッセージ
login_manager.login_message = 'ログインしていないのでログイン画面に戻しました。'


@login_manager.user_loader
def get_user(id):
    """
    Flask-Loginからコールバックされる。今回はIDの照合だけします
    """
    user = my_user(id)
    return user if id == user.id else None 

@app.route('/')
@app.route('/login_gamen')
def login_gamen():
    """ログイン画面の表示"""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = my_user(request.form['id'])
    """認証は自分でパスワードを照合して、ログインはlogin_userでやる。※ここわかりにくい"""
    if request.form['id'] == user.id and request.form['password'] == user.password:
        # Flask-Login的にはここでログイン完了
        login_user(user) 
        return redirect(url_for('login_success'))
    else:
        # ログイン失敗 ログイン画面に戻す
        flash('ログインに失敗しました。')
        return redirect(url_for('login_gamen'))

# @login_required がログイン必須route
@app.route('/login_success')
@login_required
def login_success():
    """ログイン成功画面を表示する。"""
    # current_userが今ログイン中のユーザ
    return render_template('login_success.html', id=current_user.id)

# ログアウト
@app.route('/logout', methods=['POST'])
def logout():
    """ログアウト（特に引数なし）"""
    logout_user()
    return render_template('logout_success.html')
