from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Đọc toàn bộ nội dung text từ file PDF.
    Trả về chuỗi text hoặc chuỗi rỗng nếu có lỗi.
    """
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        print(f"Lỗi khi đọc file PDF '{pdf_path}': {e}")
        return ""
