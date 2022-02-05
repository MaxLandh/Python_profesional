from datetime import datetime
import pytz

#Los codigos de zonas horarias vienen de https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

berlin_time = pytz.timezone('Europe/Berlin')
print(datetime.now(berlin_time))


