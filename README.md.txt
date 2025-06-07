## Thiết lập và Cài đặt

## 1. Tạo Môi Trường Ảo (Virtual Environment)

### Trên Windows:

```bash
  python -m venv myvenv
```

- Cho phép thực thi script trong PowerShell (Windows):

```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- Kích hoạt môi trường ảo:

```bash
    myvenv\Scripts\activate
```

### MacOS:
- Tạo môi trường ảo:
```bash
    python3 -m venv myvenv
```
-Chạy môi trường ảo:
```bash
source myvenv/bin/activate
```
## 2. Cài đặt Thư viện Cần Thiết

- Chạy:

```bash
  pip install -r requirements.txt
```

## 3.Cách chạy Project
### 3.1 Thay đổi dường dẫn pdf:
```bash
path_pdf = "sample_pdfs/file_name.pdf"
```
### 3.2 Chạy Project:
```bash
python main.py
```