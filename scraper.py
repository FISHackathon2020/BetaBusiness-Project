import io
import csv
import pandas as pd
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

class applicant:
    GPA = 0
    WinAsOneTeam = 0
    LeadWithIntegrity = 0
    BeTheChange =0

    def __init__(self, file):
        splits = str.split(file)

        btc = pd.read_csv("BeTheChange.csv")
        lwi = pd.read_csv("LeadWithIntegrity.csv")
        waot = pd.read_csv("WinAsOneTeam.csv")
  
        for split in splits:

            for item in btc:
                if item.lower() == split.lower():
                    applicant.BeTheChange=applicant.BeTheChange+1

            for item2 in lwi:
                if item2.lower() == split.lower():
                    applicant.LeadWithIntegrity=applicant.LeadWithIntegrity+1

            for item3 in waot:
                if item3.lower() == split.lower():
                    applicant.WinAsOneTeam=applicant.WinAsOneTeam+1

            if "." in split:
                if split.replace('.', '', 1).isdigit():
                    applicant.GPA = float(split)

    def getWinAsOneTeam(self):
        if(applicant.WinAsOneTeam>3):
            return 3
        elif(applicant.WinAsOneTeam>1):
            return 2
        else:
            return 1

    def getLeadWithIntegrity(self):
        if(applicant.LeadWithIntegrity>3):
            return 3
        elif(applicant.LeadWithIntegrity>1):
            return 2
        else:
            return 1

    def getBeTheChange(self):
        if(applicant.BeTheChange>3):
            return 3
        elif(applicant.BeTheChange>1):
            return 2
        else:
            return 1

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
    

##===========================================Driver
file = open('Saha Cazenove Resume.pdf', 'rb') 
temp = extract_text_from_pdf(file)
app = applicant(temp)
print(app.getWinAsOneTeam())
print(app.getLeadWithIntegrity())
print(app.getBeTheChange())
print(app.GPA)
