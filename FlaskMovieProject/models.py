from FlaskMovieProject import db, app
from sqlalchemy import Column, Integer, String, Text, Enum
from enum import Enum as UserEnum
from flask_login import UserMixin

# Model cho một bộ phim
class Movie(db.Model):
    # tên bảng trong database
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True) # Khóa chính của movie
    title = Column(String(100), nullable=False) # tên phim
    genres = Column(String(200), nullable=False)  # Lưu trữ nhiều thể loại, ngăn cách bởi dấu phẩy
    year = Column(Integer, nullable=False) # Năm phát hành
    directors = Column(String(200), nullable=False)  # Lưu trữ nhiều đạo diễn, ngăn cách bởi dấu phẩy
    actors = Column(String(200), nullable=False)  # Lưu trữ nhiều diễn viên, ngăn cách bởi dấu phẩy
    country = Column(String(100), nullable=False) # Quốc gia phim
    duration = Column(Integer, nullable=False) #  Thời lượng
    description = Column(Text, nullable=False) # mô tả ngắn
    thumbnail = Column(String(200), nullable=False) # ảnh bìa phim
    # Phuowng thức __str__ hiển thị thông tin phim khi in ra 
    def __str__(self):
        return self.title

# Định nghĩa vai trò người dùng
class UserRole(UserEnum):
    ADMIN = 1 #Vai trò quản trị viên
    USER = 2 #Vai trò người dùng thường

# Model của user
class User(db.Model, UserMixin):

    id = Column(Integer, primary_key=True, autoincrement=True) # Khóa chính của user cấu hình id tự tăng
    username = Column(String(50), nullable=False, unique=True) # Tên đăng nhập
    password = Column(String(50), nullable=False) # Mật khẩu
    email = Column(String(50), nullable=False) # Email
    user_role = Column(Enum(UserRole), default=UserRole.USER) # Vai trò của người dùng
    def __str__(self):
        return self.username




if __name__ == '__main__':
    with app.app_context():  # Bắt đầu application context
        db.create_all() # tạo các bảng trong database

