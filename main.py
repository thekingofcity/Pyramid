import subprocess
from gtts import gTTS
from PIL import ImageGrab


def main():
    # snip()
    # status, error_string = tesseract("snip1.jpg", "out1")
    # if status:
    #     print('Something wrong.')
    #     return
    # status, error_string = tesseract("snip2.jpg", "out2")
    # if status:
    #     print('Something wrong.')
    #     return
    if tts("out1.txt", "out2.txt", "out.mp3") == 0:
        print("Something wrong")


def snip():
    img = ImageGrab.grab((1770, 90, 1850, 115))
    img.save("snip1.jpg", "JPEG", quality=75)
    img = ImageGrab.grab((1770, 115, 1850, 140))
    img.save("snip2.jpg", "JPEG", quality=75)
    # img = ImageGrab.grab((23, 0, 133, 20))
    # img.save("snip3.jpg", "JPEG", quality=90, dpi=(96,96))


def tesseract(input_filename, output_filename, lang="eng"):
    '''
    An easy fork to pytesseract
    From https://github.com/madmaze/pytesseract/blob/95457153ca232eb854a6e80da17090f2fdb3c708/src/pytesseract.py
    By thekingofcity 06/25/17
    '''
    command = [
        'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe',
        input_filename,
        output_filename,
        "-l " + lang
        ]
    proc = subprocess.Popen(command, stderr=subprocess.PIPE)
    status = proc.wait()
    error_string = proc.stderr.read()
    proc.stderr.close()
    return status, error_string


def read(output_filename):
    """
    No longer used
    """
    filestream = open(output_filename, 'rb')
    try:
        print(filestream.read().decode('utf-8').strip())
    finally:
        filestream.close()


def tts(input_filename1="out1.txt", input_filename2="out2.txt", output_filename="out.mp3"):
    """
    Convert text to sound
    """
    string = "卖 "
    filestream = open(input_filename1)
    try:
        tmp = int(filestream.readline())
    except ValueError:
        return 0
    string += str(tmp)
    # print(line, end='')
    filestream.close()
    filestream = open(input_filename2)
    try:
        tmp = int(filestream.readline())
    except ValueError:
        return 0
    string += "买 " + str(tmp)
    filestream.close()
    tts_ = gTTS(text=string, lang='zh-cn', slow=False)
    tts_.save(output_filename)


main()
