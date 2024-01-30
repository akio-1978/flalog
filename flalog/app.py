from flask import Flask, url_for, render_template, redirect, request, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from .user import my_user

app = Flask(__name__)
# flaskのセッション用キー
app.config['SECRET_KEY'] = 'secret-key-for-flask-session'

# Flask-Login初期設定
login_manager = LoginManager()
login_manager.init_app(app)
# ログインしていない時に送り返す先
login_manager.login_view = 'login_gamen'
# ログインしていない時に表示するメッセージ
login_manager.login_message = '先にログインしてから来て！'

# Flask-Loginがユーザオブジェクトを取得したいときのコールバック
@login_manager.user_loader
def get_user(id):
    # 普通はここでidをキーにDBとか参照する
    return my_user if id == my_user.id else None

# ログイン画面表示
@app.route('/login_gamen')
def login_gamen():
    return render_template('login.html')

# ログイン処理
@app.route('/login', methods=['POST'])
def login():
    # 認証処理は自分でやる
    if request.form['id'] == my_user.id and request.form['password'] == my_user.password:
        # login_userを呼び出すとログインしたことになる
        login_user(my_user) 
        return redirect(url_for('login_success'))
    else:
        # ログイン失敗 ログイン画面に戻す
        flash('ログインに失敗したよ！')
        return redirect(url_for('login_gamen'))

# ログインしないと入れない画面
@app.route('/login_success')
@login_required
def login_success():
    # ログイン中のユーザはcurrent_userで取得可能
    return render_template('login_success.html', id=current_user.id)

# ログアウト
@app.route('/logout', methods=['POST'])
def logout():
    # 現在のユーザをログアウトする
    logout_user()
    return render_template('logout_success.html')
