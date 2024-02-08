from flask import Flask, url_for, render_template, redirect, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from .user import get_user

app = Flask(__name__)
# flaskのセッション用キー
app.config['SECRET_KEY'] = 'secret-key-for-flask-session'

# Flask-Loginの初期化
login_manager = LoginManager()
login_manager.init_app(app)
# ログインしていない時に送り返す先
login_manager.login_view = 'login_gamen'
# ログインしていない時に表示するメッセージ
login_manager.login_message = 'ログインしてないからログイン画面に戻します！'


@login_manager.user_loader
def get_user(id):
    """
    Flask-Loginからのコールバック
    本当はDBとか見るけど、今回はユーザひとりなのでIDだけ合ってればよし
    """
    user = get_user()
    return user if id == user.id else None 

@app.route('/')
@app.route('/login_gamen')
def login_gamen():
    """ログイン画面の表示"""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    自分で認証して、login_user()を呼んでFlask-Loginにログインを伝える。
    ※認証がただのif文なのでサンプルを見ても気付きにくい
    """
    user = get_user()
    if request.form['id'] == user.id and request.form['password'] == user.password:
        # Flask-Login的ログイン完了はここ
        login_user(user) 
        return redirect(url_for('login_success'))
    else:
        # ログイン失敗 ログイン画面に戻す
        flash('ログインに失敗したよ！')
        return redirect(url_for('login_gamen'))

# @login_required がログイン必須route
@app.route('/login_success')
@login_required
def login_success():
    """ログイン中のユーザはcurrent_userで参照可能"""
    return render_template('login_success.html', id=current_user.id)

# ログアウト
@app.route('/logout', methods=['POST'])
def logout():
    """ログアウト"""
    logout_user()
    return render_template('logout_success.html')
