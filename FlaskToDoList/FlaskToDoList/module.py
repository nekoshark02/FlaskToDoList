# generate_password_hashとcheck_password__hashをimport
from werkzeug.security import generate_password_hash, check_password_hash

# パスワードをハッシュ化
def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# 入力されたパスワードが登録されているパスワードハッシュと一致するかを確認
def check_password(self, password):
        return check_password_hash(self.password_hash, password)
