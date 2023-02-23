import os
import glob
from PyPDF2 import PdfMerger

path = str(r"C:\Users\340\Downloads")


def list_all_files(path):
    dir_list = os.listdir(path)
    return dir_list



def get_pdf_files(path):
    list_pdfs=glob.glob(str(f"{path}\*.pdf"))
    return list_pdfs


def pdf_merge(path):
    list_pdfs_=get_pdf_files(path)
    merger = PdfMerger()
    for pdf in list_pdfs_:
        merger.append(pdf)
    merger.write(str(f"{path}/result.pdf"))
    merger.close()
    return

# pdf_merge(path)



# l=get_pdf_files(path)
# print(l)