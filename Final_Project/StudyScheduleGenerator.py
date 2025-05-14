import datetime


class StudyScheduleGenerator:
    def __init__(self, preferences):
        """
        Initialize the study schedule generator.

        :param preferences: UserPreferences object containing user study preferences
        """
        self.courses = []
        self.preferences = preferences

    def add_course(self, course):
        """
        Add a course to the schedule.

        :param course: Course object
        """
        self.courses.append(course)

    def generate(self):
        """
        Generate a study plan based on course priorities, deadlines, and user preferences.

        :return: Dictionary mapping each study day to a list of (course name, hours) tuples
        """
        today = datetime.date.today()
        plan = {}

        # Determine the last exam date
        end_date = max(c.exam_date for c in self.courses)

        # Create an entry for each valid study day between today and the last exam date
        date_cursor = today
        while date_cursor <= end_date:
            if self.preferences.include_weekends or date_cursor.weekday() < 5:
                plan[date_cursor] = []
            date_cursor += datetime.timedelta(days=1)

        # Adjust course priority dynamically:
        # If a course is within 7 days of its exam, increase its weight
        for course in self.courses:
            if course.days_until_exam(today) <= 7:
                course.weight += 1

        # Compute total weighted study need across all courses
        total_weight = sum(c.weight * c.hours_needed for c in self.courses)

        # Allocate daily study hours to each course proportionally
        for course in self.courses:
            available_days = [d for d in plan if d <= course.exam_date]
            total_available_hours = sum(self.preferences.daily_limit for _ in available_days)

            # Portion of total time this course should get
            portion = (course.weight * course.hours_needed) / total_weight if total_weight else 0
            total_hours = portion * total_available_hours

            # Evenly distribute this course's time across its available days
            daily_hours = total_hours / len(available_days) if available_days else 0
            for day in available_days:
                plan[day].append((course.name, round(daily_hours, 1)))

        return plan
