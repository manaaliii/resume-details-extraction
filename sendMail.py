import smtplib

#created class which will send mail to client whether they are qualified for job.

class SendEmail:
    __sender = 'yourmail@doamin'
    __password = 'yourpassword'

    def __init__(self, reciever):
        self.reciever = reciever

    def sendmail(self):
        port = 587
        smtp_server = "smtp.gmail.com"
        message = """\
        Subject: Hi there

        This message is sent from Python."""

        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls()
                server.ehlo()  # Can be omitted
                server.login(self.__sender, self.__password)
                server.sendmail(self.__sender, self.reciever, message)
                server.quit()
                print("Email sent successfully!")

        except Exception as ex:
            print("Something went wrong....", ex)

