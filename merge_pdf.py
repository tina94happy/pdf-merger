import argparse
from PyPDF2 import PdfFileMerger, PdfFileReader

def merge_pdf(cover_name, footer_name, output_name):
    try:
        merge_list = [cover_name, footer_name]
        merged_pdf = PdfFileMerger()

        for f in merge_list:
            file = PdfFileReader(open(f, 'rb'))  # 開啟檔案並以二進位制讀取
            merged_pdf.append(file)

        with open(output_name, 'wb') as new_file:  # 寫入合併後的檔案
            merged_pdf.write(new_file)
        
        print("Merge successful! Output file:", output_name)
    except Exception as e:
        print("Merge failed:", e)

def parse_args():
    parser = argparse.ArgumentParser(description="Merge two PDF files.")
    parser.add_argument("cover", help="File path of the cover PDF")
    parser.add_argument("footer", help="File path of the footer PDF")
    parser.add_argument("-o", "--output", help="File path of the output PDF", default="merged_pdf.pdf")
    return parser.parse_args() 

if __name__ == '__main__':
    args = parse_args()   
    merge_pdf(args.cover, args.footer, args.output)
        
