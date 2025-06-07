import pandas as pd

def export_results_to_excel(results, output_file):
    # results: dict {filename: Counter{keyword: count}}
    rows = []
    for filename, counts in results.items():
        row = {"File": filename}
        row.update(counts)
        rows.append(row)
    df = pd.DataFrame(rows)
    df = df.fillna(0).sort_values(by="File")
    df.to_excel(output_file, index=False)
