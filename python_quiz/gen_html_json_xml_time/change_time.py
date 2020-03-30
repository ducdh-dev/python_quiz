def malicious_program(cur_date, changes):
    import datetime

    time = datetime.datetime.strptime(cur_date, '%d %b %Y %H:%M:%S')
    d, m, y, h, m, s = changes
    try:
        new_time = time.replace(year=time.year + y,
                                month=time.month + m,
                                day=time.day + d,
                                hour=time.hour + h,
                                minute=time.minute + m,
                                second=time.second + s)
    except ValueError:
        return cur_date
    return new_time.strftime('%d %b %Y %H:%M:%S')


print(malicious_program("01 Jul 2016 16:53:24", [2, 3, -1, 0, 5, 4]))
