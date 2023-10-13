import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('Files/*.txt')
#Create one pdf file
pdf = FPDF(orientation="P",unit="mm",format="A4")

#loop through the list of filenames
for filepath in filepaths:

    # add a page to the pdf
    pdf.add_page()

    #Get the filename without extension
    filename = Path(filepath).stem
    #Convert the filename to uppercase
    name  = filename.title()


    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8,txt=name,ln=1)

 #Get the contents of the txt file
    with open(filepath, "r") as f:
        text = f.read()
        pdf.set_font("Arial", size=12)
        # Add content to the PDF
        pdf.multi_cell(0, 10, txt=text)
pdf.output("output.pdf")
#print(df)