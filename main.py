from keyword_counter import count_keywords_in_pdf
from pdf_utils import extract_text_by_page
from keywords import keywords

if __name__ == "__main__":
    file_path = "sample_pdfs/VIB_2015.pdf"  # file bạn muốn quét
    print(f"📄 Bắt đầu quét file: {file_path}")

    results = count_keywords_in_pdf(file_path, keywords, extract_text_by_page)

    for kw, data in results.items():
        print(f"🔍 '{kw}' xuất hiện {data['count']} lần tại trang: {data['pages']}")
