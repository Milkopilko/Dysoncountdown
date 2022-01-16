import datetime
def dysontimefunction():
    patcharrival = datetime.datetime(year=2022,month=1,day=20,hour=2)
    now = datetime.datetime.now()
    countdown = patcharrival - now
    shortcountdown = str(countdown).split('.')[0]
    shortcountdown = shortcountdown.replace(',','')
    cdlist = shortcountdown.split(':')
    final = f"Dyson update countdown: {cdlist[0]} hours {cdlist[1]} minutes {cdlist[2]} seconds"
    return final