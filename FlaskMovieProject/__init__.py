from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager

# tạo ứng dụng Flask
app = Flask(__name__)
# Khởi tạo LoginManager để quản lý đăng nhập
login = LoginManager()
login.init_app(app)
# Thiết lập khóa bí mật cho ứng dụng
app.config['SECRET_KEY'] = secrets.token_hex(16)
# Cấu hình kết nối cơ sở dữ liệu MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/sickmoviedb?charset=utf8mb4'
# Thiết lập tùy chọn theo dõi thay đỏi của SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Khởi tạo đối tượng SQLALchemy để tương tác với cơ sở dữ liệu
db = SQLAlchemy(app=app)
