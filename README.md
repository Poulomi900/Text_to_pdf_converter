# Text_to_pdf_converter

This script is a simple text to PDF converter that takes text from multiple text files and compiles them into a single PDF file. It uses the fpdf library in Python for generating the PDF. This tool can be helpful for converting text-based content into a more portable and presentable format for sharing or archiving.

## Installation
Make sure you have Python installed. You can download it from here.

## Install the required dependencies by running the following command:

Copy code
pip install fpdf
Usage
Place all the text files you want to convert into the same directory as the script.

Run the script by executing the following command:

Copy code
python main.py
After execution, a PDF file named output.pdf will be generated in the same directory.

## Customization
You can customize the script by modifying the following parameters:

Adjusting the font size and style in the set_font method.
Changing the output PDF filename by modifying the argument of the output method.
