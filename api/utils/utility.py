import datetime

# 現在の日付と時刻を保持
timedelta = datetime.timedelta(hours=9)
JST = datetime.timezone(timedelta, 'JST')
now = datetime.datetime.now(JST)

# 今日の日付 YYYY-MM-DD
def current_date_str() -> datetime:
    return now.strftime('%Y-%m-%d')

# 今日の日付と時刻 YYYY-MM-DD H:M:S
def current_datetime_str() -> datetime:
    return now.strftime('%Y-%m-%d %H:%M:%S')

# 今の時刻 H:M:S
def current_time_str() -> datetime:
    return now.strftime('%H:%M:%S')
