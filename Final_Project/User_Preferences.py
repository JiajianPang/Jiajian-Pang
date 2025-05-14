import datetime


class UserPreferences:
    def __init__(self, daily_limit=4, include_weekends=True, prefer_night=False):
        """
        Initialize user preferences for study scheduling.

        :param daily_limit: Maximum number of hours available for studying per day
        :param include_weekends: Whether the user wants to study on weekends
        :param prefer_night: Whether the user prefers studying at night (currently unused)
        """
        self.daily_limit = daily_limit
        self.include_weekends = include_weekends
        self.prefer_night = prefer_night
        self.blocked_times = {}  # Dictionary format: {date_obj: blocked_hours}

    def block_time(self, date_str, hours):
        """
        Add a blocked time for a specific date (e.g. due to work, class, etc.)

        :param date_str: Date string in 'YYYY-MM-DD' format
        :param hours: Number of hours unavailable on that date
        """
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        self.blocked_times[date] = hours

    def get_blocked_hours(self, date):
        """
        Retrieve how many hours are already blocked/unavailable on a given date.

        :param date: A datetime.date object
        :return: Integer number of blocked hours (defaults to 0 if not set)
        """
        return self.blocked_times.get(date, 0)
