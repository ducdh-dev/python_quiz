import calendar


def website_calendar(month, year):
    return calendar.HTMLCalendar().formatmonth(year, month).replace("\n", "")


print(website_calendar(11, 2016))
