import hashlib


from FlaskMovieProject import app, db, login
from flask import render_template, request, flash, url_for, redirect
from FlaskMovieProject.models import User
from flask_login import LoginManager, login_user, logout_user

# Khởi tạo LoginManager để quản lý đăng nhập
login = LoginManager()
login.init_app(app)

# Route trang chủ
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html") # HIển thị trang chủ

# Xác thực người dùng khi đăng nhập
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id) # Tìm kiếm User theo ID

# Trang đăng nhập 
@app.route('/login', methods=['get', 'post'])
def login():
    # Nếu như phương thức của request là POST
    if request.method.__eq__('POST'):
        # Lấy email đã nhập
        email = request.form.get('email')
        # Lấy mật khẩu đã nhập
        password = request.form.get('password')
        # Mã hóa mật khẩu bằng MD5
        password_hashed = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        # Kiểm tra email và mật khẩu có khớp với tài khoản trong database
        check_user = User.query.filter(User.email.__eq__(email.strip()),
                                  User.password.__eq__(password_hashed)).first()
        # Nếu khớp
        if check_user:
            login_user(user=check_user) # Đăng nhập user
            flash(f'Đăng nhập thành công', 'success') # Hiển thị thông báo thành công
            return redirect(url_for('home')) # Chuyển hướng về trang chủ
        # Ngược lại không tìm thấy tài khoản nào
        else:
            flash(f'Email hoặc tài khoản không đúng', 'danger') # Hiển thị thông báo lỗi

    return render_template('login.html', title='Đăng Nhập') # Hiển thị trang đăng nhập



# Trang đăng ký
@app.route('/register', methods=['get', 'post'])
def register():
    mess = "" # Khởi tạo biến thông báo
    if request.method.__eq__('POST'):
        username = request.form.get('username') # Lấy username đã nhập
        email = request.form.get('email') # Lấy email đã nhập
        password = request.form.get('password') # Lấy mật khẩu đã nhập
        # Mã hóa mật khẩu bằng MD5
        password_hashed = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
         # Tạo user mới
        user = User(username=username.strip(), email=email.strip(), password=password_hashed)
        try:
            # Thêm user mới vào database
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login')) # Chuyển hướng về trang đăng nhập
        except:
            mess = "Xảy ra lỗi khi đăng ký tài khoản" # Thông báo lỗi
            return redirect(url_for('home'))  # Chuyển hướng về trang chủ

        mess = "Đăng ký tài khoản thành công"
        flash(mess, 'success')
    return render_template('register.html', title='Đăng Ký') # Hiển thị trang đăng ký

@app.route('/logout')
def logout():
    logout_user() # Đăng xuất user
    return redirect(url_for('login'))  # Chuyển hướng về trang đăng nhập

@app.route("/movies")
def movie_list():
    movies = Movie.query.all() # Lấy tất cả phim từ database
    return render_template("movies.html", movies = movies) # Hiển thị trang danh sách phim

@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    movie = Movie.query.get(movie_id) # Lấy phim theo ID
    return render_template('movie.html', movie=movie) # Hiển thị trang chi tiết phim

if __name__ == '__main__':
    from FlaskMovieProject.admin import *
    app.run(debug=True)