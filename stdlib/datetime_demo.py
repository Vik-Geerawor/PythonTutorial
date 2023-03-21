from datetime import date


def datetime_demo():
    now = date.today()
    print(now)
    print(now.strftime("%y-%m-%d. %d %b %Y is a %A on the %dth day of %B"))

    dob = date(1981, 10, 15)
    age = now - dob
    print(f"I'm {age.days} days old")
    print(dob.strftime("%y-%m-%d. %d %b %Y is a %A on the %dth day of %B"))


datetime_demo()
