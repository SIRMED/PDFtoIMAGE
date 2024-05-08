# Python PDF to PNG/JPG
Converting a PDF to a PNG using wand, --pythonMagic-- and --PythonMagicWand-- as a comparison

I found that wand seems to be the only currently supported imagemagick library for python.

It was also found that jpeg results in better image output that PNG files. This could be dependant on the PDF, but it's worth a try if your output needs improvement.

## Setup
Clone the repository into your machine using `git clone https://github.com/nycynik/PythonPDFtoPNG.git` and extract the folder. Open the folder
in the terminal and follow these steps:

- Copy over the PDF file you want to convert to PNG/JPG inside the main folder as such so the PDF file is along side `pdfToPNGWand.py`
- In the terminal run `pip install -r requirements.txt` to install the required packages. If installing through pip doesn't work install wand
through [this link](https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows)
- In the terminal run `python3 pdfToPNGWand.py` to start the program
- Follow the steps the program takes you through and the output files will be in the `/output` folder
