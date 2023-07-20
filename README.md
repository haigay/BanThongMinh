# BanThongMinh
## 1. Những thư viện cần dùng và file haarcascade
- Thư viện OpenCV
- File Haarcascade_frontalface_default.xml
    - File này để detect ra khuôn mặt trong hình.
    - Link tham khảo: https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
- Thư viện Socket 
- Ngoài ra còn các thư viện ngoại vi khác như Picamera cho camera và Openyxl để tương tác với file excel v.v.

Link source code: https://github.com/haigay/BanThongMinh \
Nhớ kết nối pi với máy tính bằng cổng lan hoặc kết nối chung 1 mạng wifi

## 2. Chạy chương trình bên raspberry
### B1: Chuẩn bị 
- Cài thư viện và down file đầy đủ.
- Copy 3 file .py ở bên ngoài vào 1 thư mục mới tên là gì cũng được ở đây mình đặt là FACE_RECOGNITON.
- Tạo 1 folder trống trong FACE_RECOGNITON đăt tên là dataSet.

### B2: Thu thập dữ liệu
- Chạy file input.py.
- Nhập id (id là mã định danh của từng người nhập số gì cũng được).
- Nhìn vào camera để chụp hình. Ở code mình chụp 120 tấm.
- Xong thì chương trình sẽ tự tắt và ta có thể vào mục dataSet để xem mặt mình.
- Thêm người mới thì chạy lại file input.py và nhập id khác nhé. Nhập trùng id thì sẽ gi đè mất hình cũ đó.

### B3: Training 
- Chạy file train.py rồi chờ chương trình chạy hết là xong.
- Lưu ý 1 chút là nhớ sửa tên thư mục để hình cho đúng.

### B4: Chạy file recognition.py
- Nhớ sửa tên ở mảng names[].
- Sửa ip cho phù hợp với máy chủ
- Nhớ command các đoạn code liên quan tới server mình có note trong file để test riêng phần nhận diện.

## 3. Chạy chương trình bên laptop(server)
- File data.xlsx là danh sách có thể chỉnh sửa cho phù hợp với id và tên của các bạn.
- Lưu ý nhớ đóng file excel trước khi chạy nếu để thì sẽ bị lỗi đó.
- Chạy file main.py, file tmp là hàm điểm danh. Nhớ chỉnh cái host thành ip của máy nhé.
- Nhấn nút q bên pi để thoát chương trình ở cả 2 bên.

## 4. Phần Website và đăng nhập
- Phần này mình làm là nó sẽ quét mặt và tự động đăng nhập vào web luôn nma làm không được nên mình chỉ không ghi ra.
- Lời khuyên nếu bạn nào như mình thì đừng viết web bằng django vì nó khó gọi ý nên viết bằng flask

#### Mình có giải thích ngay trong code và các bạn cũng có thể xem demo hay đọc báo cáo của tụi mình để hiểu hơn. \
#### Link tham khảo: https://drive.google.com/drive/folders/1Y6GL-uOe5hVTg4f-BYcKyYA_C8gvCM-I?usp=drive_link
### Staycool !!! 

