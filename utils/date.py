from datetime import datetime

def get_date_sdt():
    current_date = datetime.now()
    year = current_date.year
    month = f"{current_date.month:02}"
    day = f"{current_date.day:02}"
    hours = f"{current_date.hour:02}"
    minutes = f"{current_date.minute:02}"
    seconds = f"{current_date.second:02}"
    milliseconds = f"{current_date.microsecond // 1000:03}"

    return f"{year}{month}{day}{hours}{minutes}{seconds}{milliseconds}"

def get_date_ymd():
    current_date = datetime.now()
    year = current_date.year
    month = f"{current_date.month:02}"
    day = f"{current_date.day:02}"

    return f"{year}{month}{day}"