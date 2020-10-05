import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        values = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        day = datetime.date(year, month, day)

        return values[day.weekday()]



so = Solution()

print(so.dayOfTheWeek(26, 10, 2019))