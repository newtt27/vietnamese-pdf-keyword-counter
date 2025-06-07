import re
from collections import Counter
from pdf_utils import extract_text_from_pdf
from keywords import keywords

def count_keywords_in_pdf(pdf_path, keywords):
    # Đọc text từ PDF
    text = extract_text_from_pdf(pdf_path).lower()

    counts = Counter()
    for kw in keywords:
        kw_lower = kw.lower()
        # Escape từ khóa để search chính xác, có thể chứa dấu đặc biệt
        pattern = re.escape(kw_lower)
        matches = re.findall(pattern, text)
        counts[kw] = len(matches)
    
    return counts

if __name__ == "__main__":
    # Ví dụ gọi hàm với 1 file cụ thể
    path_pdf = "sample_pdfs/VCB_2015_1.pdf"  # sửa đường dẫn file PDF ở đây
    keyword_counts = count_keywords_in_pdf(path_pdf, keywords)

    print(f"Kết quả đếm từ khóa trong file {path_pdf}:")
    for kw, count in keyword_counts.items():
        print(f"{kw}: {count}")
