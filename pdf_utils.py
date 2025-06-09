from PyPDF2 import PdfReader
import pdfplumber
import re
# import hashlib

def extract_text_by_page(pdf_path, similarity_threshold=0.85):

    def tokenize(text):
        # Tách từ, loại bỏ ký tự đặc biệt, chuyển về chữ thường
        return set(re.findall(r'\b\w+\b', text.lower()))
    
    with pdfplumber.open(pdf_path) as pdf:
        unique_pages = []
        unique_tokens = []
        
        for page in pdf.pages:
            text = page.extract_text() or ''
            tokens = tokenize(text)
            
            # Nếu chưa có trang nào thì thêm luôn
            if not unique_pages:
                unique_pages.append(text)
                unique_tokens.append(tokens)
                continue
            
            # Tính Jaccard similarity với tất cả các trang đã lưu
            is_duplicate = False
            for utokens in unique_tokens:
                intersection = len(tokens & utokens)
                union = len(tokens | utokens)
                similarity = intersection / union if union != 0 else 0
                
                if similarity >= similarity_threshold:
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                unique_pages.append(text)
                unique_tokens.append(tokens)
                
    return unique_pages
