from datetime import datetime

def day():
    today = datetime.now().strftime('%m')
    mon = ""
    if today == '01':
        mon = "января"
    if today == '02':
        mon = "февраля"
    if today == '03':
        mon = "марта"
    if today == '04':
        mon = "апреля"
    if today == '05':
        mon = "мая"
    if today == '06':
        mon = "июня"
    if today == '07':
        mon = "июля"
    if today == '08':
        mon = "августа"
    if today == '09':
        mon = "сентября"
    if today == '10':
        mon = "октября"
    if today == '11':
        mon = "ноября"
    if today == '12':
        mon = "декабря"
    return datetime.now().strftime('%d') +' ' +mon +" "+ datetime.now().strftime('%Y') + " года"
