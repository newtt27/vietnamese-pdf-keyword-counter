import os
import re
from collections import Counter
from keywords import keywords
from pdf_utils import extract_text_from_pdf  # import từ file pdf_utils.py

def count_keywords_in_text(text, keywords):
    text_lower = text.lower()
    counts = Counter()
    for kw in keywords:
        kw_lower = kw.lower()
        pattern = re.escape(kw_lower)
        matches = re.findall(pattern, text_lower)
        counts[kw] = len(matches)
    return counts

def count_keywords_in_pdfs(pdf_folder, keywords):
    result = {}
    for filename in os.listdir(pdf_folder):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_folder, filename)
            text = extract_text_from_pdf(filepath)
            counts = count_keywords_in_text(text, keywords)
            result[filename] = counts
    return result
