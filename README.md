# PYTHON SELENIUM AUTOMATION TEST DEMO

Demo kiểm thử tự động chức năng đăng nhập của website SauceDemo bằng Python, Selenium WebDriver và pytest.

## 1. Yêu cầu

- Windows 10/11
- Python 3.10 trở lên
- Google Chrome đã cài đặt
- Kết nối Internet
- Visual Studio Code (khuyến nghị, không bắt buộc)

Selenium 4 hiện hành có Selenium Manager hỗ trợ tìm/cấu hình driver tương thích. Thông thường không cần tải ChromeDriver thủ công.

## 2. Cấu trúc thư mục

```text
python_selenium_demo/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   ├── conftest.py
│   └── test_login.py
├── screenshots/
├── requirements.txt
└── README.md
```

## 3. Cài đặt

Mở thư mục dự án trong VS Code. Chọn Terminal → New Terminal, sau đó chạy:

```bash
python --version
```

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt trên Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn script, có thể dùng Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Cài thư viện:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Kiểm tra:

```bash
python -m pip show selenium
python -m pip show pytest
```

## 4. Website và dữ liệu thử nghiệm

Website: https://www.saucedemo.com/

Tài khoản demo công khai dùng trong bài thực hành:
- Username: `standard_user`
- Password: `secret_sauce`

Không dùng tài khoản cá nhân hoặc mật khẩu thật.

## 5. Chạy kiểm thử

Đảm bảo đã kích hoạt môi trường `.venv`, đang đứng tại thư mục gốc dự án, rồi chạy:

```bash
python -m pytest -v
```

Chrome sẽ tự mở và lần lượt chạy bốn test case. Sau khi mỗi test kết thúc, fixture sẽ đóng trình duyệt.

## 6. Các test case

| Mã | Trường hợp | Kết quả mong đợi |
|---|---|---|
| TC_LOGIN_01 | Đăng nhập đúng | URL chuyển đến `/inventory.html` |
| TC_LOGIN_02 | Sai mật khẩu | Hiển thị thông báo sai username/password |
| TC_LOGIN_03 | Bỏ trống cả hai trường | Hiển thị `Username is required` |
| TC_LOGIN_04 | Kiểm tra sau đăng nhập | Trang có tiêu đề `Products` và URL inventory |

## 7. Đọc kết quả

- `PASSED`: test case đạt, kết quả thực tế khớp kết quả mong đợi.
- `FAILED`: test case không đạt; đọc phần traceback để xác định assertion hoặc thao tác lỗi.
- Nếu test thất bại ở bước thực thi, chương trình cố gắng lưu ảnh tại thư mục `screenshots/`.

Kết quả `4 passed` nghĩa là bốn test case đều đạt trong lần chạy đó. Chỉ ghi kết quả vào báo cáo sau khi thực sự chạy và lưu bằng chứng.

## 8. Một số lỗi thường gặp

**`python is not recognized`**: Python chưa được cài hoặc chưa thêm vào PATH. Cài Python và chọn tùy chọn Add Python to PATH, sau đó mở terminal mới.

**`No module named selenium` hoặc `No module named pytest`**: kiểm tra đã kích hoạt `.venv`, sau đó chạy `pip install -r requirements.txt`.

**Chrome không mở / lỗi driver**: cập nhật Chrome, kiểm tra Internet để Selenium Manager có thể lấy driver phù hợp; sau đó chạy lại.

**Không truy cập được website**: mở URL bằng Chrome thủ công, kiểm tra Internet, VPN hoặc proxy.

**PowerShell không cho kích hoạt môi trường ảo**: dùng Command Prompt và lệnh `.venv\\Scripts\\activate.bat`.

## 9. Lưu ý

Website demo có thể thay đổi giao diện hoặc nội dung thông báo theo thời gian. Nếu locator hoặc thông báo thay đổi, cần kiểm tra HTML thực tế và cập nhật `pages/login_page.py` hoặc test tương ứng. Không sửa expected result chỉ để làm test chuyển sang PASS khi chưa xác minh hành vi website.
