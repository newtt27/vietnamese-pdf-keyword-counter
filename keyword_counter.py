import re

def count_keywords_in_pdf(pdf_path, keywords, extract_text_by_page):
    pages_text = extract_text_by_page(pdf_path, similarity_threshold=0.8)
    print(f"Unique pages extracted: {len(pages_text)}")
    result = {}

    for kw in keywords:
        print(f"\n--- {kw} ---")
        kw_words = kw.lower().split()
        # Tạo regex pattern tìm chính xác từ khóa với khoảng trắng linh hoạt
        pattern = r'\b' + r'\s+'.join(map(re.escape, kw_words)) + r'\b'

        total_count = 0
        match_pages = []

        for i, page_text in enumerate(pages_text):
            if not page_text:
                continue
            page_text_lower = page_text.lower()
            matches = list(re.finditer(pattern, page_text_lower))
            if matches:
                count = len(matches)
                total_count += count
                match_pages.append((i+1, count))  # trang đánh số từ 1

                # for m in matches:
                #     print(f"📌 Page {i+1} — Match: {repr(m.group(0))} at {m.start()}-{m.end()}")

        print(f"✅ Total matches for '{kw}': {total_count}")
        result[kw] = {
            "count": total_count,
            "pages": match_pages
        }

    return result