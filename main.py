'''
    An easy fork to pytesseract
    From https://github.com/madmaze/pytesseract/blob/95457153ca232eb854a6e80da17090f2fdb3c708/src/pytesseract.py
    By thekingofcity 06/25/17
'''

from PIL import ImageGrab
import subprocess


def main():
    snip()
    status, error_string = tesseract("snip1.jpg", "out1")
    if status:
        print('Something wrong.')
        return
    status, error_string = tesseract("snip2.jpg", "out2")
    if status:
        print('Something wrong.')
        return
    read("out1.txt")
    read("out2.txt")


def snip():
    img = ImageGrab.grab((1770, 90, 1850, 115))
    img.save("snip1.jpg", "JPEG", quality=75)
    img = ImageGrab.grab((1770, 115, 1850, 140))
    img.save("snip2.jpg", "JPEG", quality=75)


def tesseract(input_filename, output_filename):
    command = ['C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe', input_filename, output_filename]
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    status = proc.wait()
    error_string = proc.stderr.read()
    proc.stderr.close()
    return status, error_string


def read(output_filename):
    f = open(output_filename, 'rb')
    try:
        print(f.read().decode('utf-8').strip())
    finally:
        f.close()


main()
