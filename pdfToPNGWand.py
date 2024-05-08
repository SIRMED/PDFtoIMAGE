from __future__ import print_function
from wand.image import Image
import os

program_directory = os.path.dirname(os.path.realpath(__file__))

def pdf2png(path_to_file, png_or_jpg, resolution):
    if not os.path.exists('output'):
        os.makedirs('output')

    with Image(filename=path_to_file, resolution=resolution) as img:
        with img.convert(png_or_jpg) as converted:
            converted.save(filename=f'output/page.{png_or_jpg}')

def start_program():
    print("\33[1m\33[96m* PDF to PNG/JPG Converter *\33[0m")
    print()

    print("\33[93mWhat is the name of the PDF file?\33[0m")
    print("The file should be in the same directory as this program.")
    file_name = str(input("Enter the name of the file: \33[93m"))
    print("\33[0m")

    # Check if the file exists
    try:
        with open(file_name):
            pass
    except FileNotFoundError:
        # Check if any part of the file name matches any pdf file in the directory
        pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]

        if len(pdf_files) > 1:
            print("\33[91mMultiple PDF files were found in this directory, can't autofill file name. Please enter the full name of the file.\33[0m")
            return

        for pdf_file in pdf_files:
            if file_name in pdf_file:
                print(f'The file \33[93m"{pdf_file}"\33[0m was found wich matches \33[93m"{file_name}"\33[0m. Use this file instead?')
                use_file = str(input("Enter Y or N: \33[93m"))
                print("\33[0m")

                if use_file == 'Y' or use_file == 'y' or use_file == 'yes' or use_file == 'Yes' or use_file == 'YES':
                    file_name = pdf_file
                    break
                else:
                    return
        else:
            print("\33[91mFile not found. Please make sure the file is in the same directory as this program.\33[0m")
            return
    

    print("\33[93mConvert the file to PNG or JPG?\33[0m")
    print("PNG images are transparent while JPG images are not.")
    print("Enter 'png' or 'jpg' to convert the file to PNG or JPG respectively.")
    png_or_jpg = str(input("Enter your choice: \33[93m"))
    print("\33[0m")

    if png_or_jpg != 'png' and png_or_jpg != 'jpg':
        print("\33[91mInvalid choice. Please enter 'png' or 'jpg'.\33[0m")
        return
    
    print("\33[93mWhat resolution should the output image be?\33[0m")
    print("Enter a number between 10 and 1000. Reccomended resolution is 100.")
    resolution = int(input("Enter the resolution: \33[93m"))
    print("\33[0m")

    if resolution < 10 or resolution > 1000:
        print("\33[91mInvalid resolution. Please enter a number between 10 and 1000.\33[0m")
        return

    print(f"\33[92mConverting {file_name} to {png_or_jpg}...\33[0m")
    pdf2png(file_name, png_or_jpg, resolution)
    print(f"Conversion successful. The images are in \33[92m{program_directory}\output\33[0m")
    

start_program()