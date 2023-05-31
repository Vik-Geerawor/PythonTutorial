from urllib.request import urlopen
import smtplib


def urllib_demo():
    """
    Prerequisites - a local mailserver
    """
    with urlopen('https://docs.python.org/3/tutorial/stdlib.html') as response:
        for line in response:
            line = line.decode()            # NOTE: byte --> str
            print(line)


def smtplib_demo():
    server = smtplib.SMTP('localhost')
    server.sendmail('vik.geerawor@natwest.com', 'sgeerawor@gmail.com',
                    """
                    To: sgeerawor@gmail.com
                    From: vik.geerawor@natwest.com

                    Beware - send from python code
                    """
                    )
    server.quit()


# urllib_demo()
smtplib_demo()
