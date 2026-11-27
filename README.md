# PYTHON SELENIUM AUTOMATION TEST DEMO

Demo kiểm thử tự động website [SauceDemo](https://www.saucedemo.com/) bằng Python, Selenium WebDriver và pytest, tổ chức theo mô hình **Page Object Model (POM)**.

Các chức năng được kiểm thử:

- Đăng nhập (Login)
- Danh sách sản phẩm (Inventory)
- Giỏ hàng (Cart)
- Thanh toán (Checkout)

Tổng cộng **10 test case**.

## 1. Yêu cầu

- Windows 10/11
- Python 3.10 trở lên
- Google Chrome đã cài đặt
- Kết nối Internet
- Visual Studio Code (khuyến nghị, không bắt buộc)

Selenium 4 có sẵn Selenium Manager để tự tìm ChromeDriver phù hợp, nên không cần tải ChromeDriver thủ công.

## 2. Cấu trúc thư mục

```text
kiem_thu_python_selenium/
├── pages/                      # Page Object: locator + thao tác của từng trang
│   ├── __init__.py
│   ├── login_page.py           # Trang đăng nhập
│   ├── inventory_page.py       # Trang danh sách sản phẩm
│   ├── cart_page.py            # Thêm/xóa sản phẩm, trang giỏ hàng
│   └── checkout_page.py        # Trang thanh toán (bước nhập thông tin)
├── tests/                      # Các test case pytest
│   ├── conftest.py             # Fixture khởi tạo / đóng Chrome
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── screenshots/                # Ảnh chụp minh họa kết quả chạy test
├── requirements.txt
└── README.md
```

## 3. Cài đặt

Tải mã nguồn về:

```bash
git clone https://github.com/nguyenmyhanhneh/kiem_thu_python_selenium.git
cd kiem_thu_python_selenium
```

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt trên Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu PowerShell chặn script, dùng Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

Cài thư viện (`selenium>=4.20`, `pytest>=8.0`):

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Website và dữ liệu thử nghiệm

Website: https://www.saucedemo.com/

Tài khoản demo công khai được dùng trong test:

| Username | Password | Mục đích |
|---|---|---|
| `standard_user` | `secret_sauce` | Tài khoản hợp lệ |
| `locked_out_user` | `secret_sauce` | Tài khoản bị khóa |
| `invalid_user` | `secret_sauce` | Tài khoản không tồn tại |

## 5. Chạy kiểm thử

Kích hoạt `.venv`, đứng tại thư mục gốc dự án, rồi chạy toàn bộ test:

```bash
python -m pytest -v
```

Chạy riêng từng nhóm:

```bash
python -m pytest tests/test_login.py -v
python -m pytest tests/test_inventory.py -v
python -m pytest tests/test_cart.py -v
python -m pytest tests/test_checkout.py -v
```

Mỗi test case mở một cửa sổ Chrome mới (chế độ ẩn danh, toàn màn hình). Khi test xong, trình duyệt chờ 3 giây rồi tự đóng (cấu hình trong `tests/conftest.py`).

## 6. Các test case

### Đăng nhập (`tests/test_login.py`)

| Mã | Hàm test | Trường hợp | Kết quả mong đợi |
|---|---|---|---|
| TC_LOGIN_01 | `test_login_with_valid_account` | Đăng nhập đúng | URL chuyển đến `/inventory.html` |
| TC_LOGIN_02 | `test_login_with_wrong_password` | Sai mật khẩu | Thông báo `Username and password do not match` |
| TC_LOGIN_03 | `test_login_with_empty_fields` | Bỏ trống cả hai trường | Thông báo `Username is required` |
| TC_LOGIN_04 | `test_inventory_page_after_login` | Kiểm tra trang sau đăng nhập | Tiêu đề `Products` và URL `/inventory.html` |
| TC_LOGIN_05 | `test_login_with_invalid_username` | Username không tồn tại | Thông báo `Username and password do not match` |
| TC_LOGIN_06 | `test_login_with_locked_out_account` | Tài khoản bị khóa | Thông báo có chữ `locked out` |

### Danh sách sản phẩm (`tests/test_inventory.py`)

| Mã | Hàm test | Trường hợp | Kết quả mong đợi |
|---|---|---|---|
| TC_INV_01 | `test_inventory_products_displayed` | Hiển thị danh sách sản phẩm sau đăng nhập | Tiêu đề `Products`; có ít nhất 1 sản phẩm; tên và giá không rỗng |

### Giỏ hàng (`tests/test_cart.py`)

| Mã | Hàm test | Trường hợp | Kết quả mong đợi |
|---|---|---|---|
| TC_CART_01 | `test_add_product_to_cart` | Thêm "Sauce Labs Backpack" vào giỏ | Biểu tượng giỏ hiện `1`; giỏ có 1 sản phẩm đúng tên |
| TC_CART_02 | `test_remove_product_from_cart` | Thêm rồi xóa sản phẩm trong giỏ | Giỏ trống; biểu tượng giỏ không còn số lượng |

### Thanh toán (`tests/test_checkout.py`)

| Mã | Hàm test | Trường hợp | Kết quả mong đợi |
|---|---|---|---|
| TC_CHECKOUT_01 | `test_checkout_with_empty_information` | Bấm Continue khi bỏ trống thông tin thanh toán | Thông báo `First Name is required` |

## 7. Đọc kết quả

- `PASSED`: test case đạt, kết quả thực tế khớp kết quả mong đợi.
- `FAILED`: test case không đạt; đọc phần traceback để biết assertion hoặc thao tác bị lỗi.
- Kết quả `10 passed` nghĩa là cả 10 test case đều đạt trong lần chạy đó.

Thư mục `screenshots/` chứa ảnh chụp màn hình minh họa một số test case. Code hiện tại **không tự động chụp ảnh** khi test thất bại.

## 8. Một số lỗi thường gặp

**`python is not recognized`**: Python chưa được cài hoặc chưa thêm vào PATH. Cài lại Python, chọn "Add Python to PATH", rồi mở terminal mới.

**`No module named selenium` / `No module named pytest`**: kiểm tra đã kích hoạt `.venv`, sau đó chạy `pip install -r requirements.txt`.

**`ModuleNotFoundError: No module named 'pages'`**: phải chạy lệnh `python -m pytest` tại thư mục gốc dự án (thư mục chứa `pages/` và `tests/`).

**Chrome không mở / lỗi driver**: cập nhật Chrome, kiểm tra Internet để Selenium Manager tải driver phù hợp, rồi chạy lại.

**Không truy cập được website**: mở https://www.saucedemo.com/ bằng Chrome thủ công, kiểm tra Internet, VPN hoặc proxy.

## 9. Lưu ý

Website demo có thể thay đổi giao diện hoặc nội dung thông báo theo thời gian. Khi đó cần kiểm tra HTML thực tế và cập nhật locator trong thư mục `pages/` hoặc test tương ứng. Không sửa kết quả mong đợi chỉ để test chuyển sang PASS khi chưa xác minh hành vi thật của website.
