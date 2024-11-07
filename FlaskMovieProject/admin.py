# Import các module cần thiết
from FlaskMovieProject import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from FlaskMovieProject.models import Movie

# Sử dụng thư viện flask-admin để tạo trang quản trị
# Tạo đối tượng admin để quản lý giao diện admin
admin = Admin(app=app, name="SickMovieAdmin", template_mode='bootstrap4')

# Định nghĩa class MovieView để quản lý Model Movie
class MovieView(ModelView):
    # Cho phép xem chi tiết
    can_view_details = True
    # Cho phép xuất dữ liệu
    can_export = True
    # Cho phép danh sách hiển thị khóa chính
    column_display_pk = True
    # Xác định các cột có thể tìm kiếm
    column_searchable_list = ['title', 'genres', 'year', 'country']
    # Ẩn đi các cột không cần thiết
    column_exclude_list = ['description', 'thumbnail', 'actors']
    # Đặt tên lại cho các cột bằng tiếng việt
    column_labels = {
        'title' : 'Tên phim',
        'description' : 'Mô tả',
        'genres' : 'Thể loại',
        'year' : 'Năm',
        'directors' : 'Nhà sản xuất',
        'actors' : 'Diễn viên',
        'country' : 'Quốc gia',
        'duration' : 'Thời lượng (phút)',
        'thumbnail' : 'Poster phim'

    }
    # Cho phép các cột nào có thể sắp xếp tăng hoặc giảm dần
    column_sortable_list = ['id', 'year', 'title']

# Thêm MovieView vào giao diện quản trị
admin.add_view(MovieView(Movie, db.session))
