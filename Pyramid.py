import subprocess
from multiprocessing import Process, Queue, freeze_support
from gtts import gTTS
from PIL import ImageGrab
import time


class Pyramid(Process):
    """ A Pyramid class
        Q for args {"isTTS": False, "buy": 0, "sell": 0}
    """
    isTTS = False
    buy = 0
    sell = 0


    def __init__(self, INQ, OUTQ):
        self.args = INQ
        self.results = OUTQ
        Process.__init__(self) # This will immediately start run() , but why?


    def snip(self):
        """ Capture a screenshot
        """
        img = ImageGrab.grab((1770, 90, 1850, 115))
        img.save("snip1.jpg", "JPEG", quality=75)
        img = ImageGrab.grab((1770, 115, 1850, 140))
        img.save("snip2.jpg", "JPEG", quality=75)
        # img = ImageGrab.grab((23, 0, 133, 20))
        # img.save("snip3.jpg", "JPEG", quality=90, dpi=(96,96))


    def tesseract(self, input_filename, output_filename, lang="eng"):
        '''
        An easy fork to pytesseract
        From https://github.com/madmaze/pytesseract/blob/
            95457153ca232eb854a6e80da17090f2fdb3c708/src/pytesseract.py
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


    def read(self, input_filename1="out1.txt", input_filename2="out2.txt"):
        """ Read text from file and store it in self.buy & self.sell
        """
        filestream = open(input_filename1)
        try:
            tmp = int(filestream.readline())
        except ValueError:
            return 0
        self.sell = tmp
        filestream.close()
        filestream = open(input_filename2)
        try:
            tmp = int(filestream.readline())
        except ValueError:
            return 0
        self.buy = tmp
        filestream.close()
        self.results.put({"buy": self.buy, "sell": self.sell})


    def tts(self, output_filename="out.mp3"):
        """ Convert text to sound
        """
        string = "卖 " + str(self.sell) + "买 " + str(self.buy)
        tts_ = gTTS(text=string, lang='zh-cn', slow=False)
        tts_.save(output_filename)


    def run(self):
        """ Main process of the class
        """
        while True:
            # if self.args.empty():
            #     raise Exception("self.args.empty()")
            while not self.args.empty():
                tmp = self.args.get()
                if tmp["isTTS"] == 'false' or tmp["isTTS"] == False:
                    self.isTTS = False
                else:
                    self.isTTS = True
            self.snip()
            status, error_string = self.tesseract("snip1.jpg", "out1")
            if status:
                print('Something wrong.')
                return
            status, error_string = self.tesseract("snip2.jpg", "out2")
            if status:
                print('Something wrong.')
                return
            if self.read("out1.txt", "out2.txt") == 0:
                print("Something wrong")
                return
            if self.isTTS:
                self.tts("static\out.mp3")
            time.sleep(15)


if __name__ == '__main__':
    INQ = Queue()
    OUTQ = Queue()
    ARGS = {"isTTS": 'true', "buy": 0, "sell": 0}
    INQ.put(ARGS)
    PYR = Pyramid(INQ, OUTQ)
    PYR.run()
    PYR.join()
