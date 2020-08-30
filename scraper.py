import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

class applicant:
    GPA = 0
    Date = ""

    def __init__(self, file):
        splits = str.split(file)

        for split in splits:
            print(split)

            if "Expected" in split:
                applicant.Date = split + splits.pop() + splits.pop()
                print(applicant.Date)

            if "." in split:
                if split.replace('.', '', 1).isdigit():
                    applicant.GPA = float(split)
                    print(applicant.GPA)

def extract_text_from_pdf(fh):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    
    for page in PDFPage.get_pages(fh, 
                                caching=True,
                                check_extractable=True):
        page_interpreter.process_page(page)
            
        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()
    
    if text:
        return text
    

file = open('Saha Cazenove Resume.pdf', 'rb') 
temp = extract_text_from_pdf(file)
app = applicant(temp)
