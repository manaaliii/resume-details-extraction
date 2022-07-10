from sendMail import SendEmail
from extractDetails import Extractor

#project by Disha And Manali...

file = input("Enter your resume file: ")
ch = int(input(("""1. to apply for front end development
2. to apply for back end development.
3. to apply for full stack development.
Enter your choice: """)))

extract = Extractor(file, ch)
mail = extract.extractMail()
eligible = extract.extractSkill()

if eligible:
    mailing = SendEmail(mail)
    mailing.sendmail()
