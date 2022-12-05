from datetime import datetime
import pytz

# dt = datetime
# tz = timezone
def datetime_to_utc(naive_dt, tz = self.env.context["tz"]):
    client_date = pytz.timezone(tz).localize(naive_dt)
    utc_date = client_date.astimezone(pytz.utc)
    return utc_date