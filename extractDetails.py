import PyPDF2
import re

import criteria as cr


class Extractor:
    def __init__(self, resume, choice):
        self.resume = resume
        self.choice = choice

    @staticmethod
    def __manCount(p):
        c = 0
        for m in cr.mandatory:
            if m in p:
                c += 1
        return c

    @staticmethod
    def __backCount(p):
        c = 0
        for b in cr.backend:
            if b in p:
                c += 1
        return c

    @staticmethod
    def __fullCount(p):
        c = 0
        for f in cr.fullStack:
            if f in p:
                c += 1
        return c

    @staticmethod
    def __skillCount(p):
        c = 0
        for skill in cr.skills:
            if skill in p:
                c += 1
        return c

    def __extractPDF(self):
        resumePdf = open(self.resume, 'rb')
        resumeRead = PyPDF2.PdfFileReader(resumePdf)
        pageObj = resumeRead.getPage(0)
        m = pageObj.extractText()
        resumePdf.close()
        return m

    def extractMail(self):
        s = self.__extractPDF()
        match = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",s)
        for x in match:
            return x

    def extractSkill(self):
        s = self.__extractPDF()
        eligible = len(cr.mandatory)
        cm = self.__manCount(s)
        cs = self.__skillCount(s)
        if self.choice == 1:
            if cm == eligible and cs > 0:
                print("you are eligible, you will be recieving our email soon")
                return 1
            else:
                print("Try next time")
                return 0

        elif self.choice == 2:
            cb = self.__backCount(s)
            if cm == eligible and cb > 0 and cs > 0:
                print("you are eligible, you will be recieving our email soon")
                return 1
            else:
                print("Try next time")
                return 0

        elif self.choice == 3:
            cf = self.__fullCount(s)
            if cm == eligible and cf > 2 and cs > 1:
                print("you are eligible, you will be recieving our email soon")
                return 1
            else:
                print("Try next time")
                return 0
