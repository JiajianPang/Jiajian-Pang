import datetime

class Course:
    # Define priority weight mapping
    PRIORITY_WEIGHTS = {'high': 3, 'medium': 2, 'low': 1}

    def __init__(self, name, exam_date, hours_needed, priority='medium'):
        """
        Initialize a Course object.
        :param name: Name of the course
        :param exam_date: Exam date as string in 'YYYY-MM-DD'
        :param hours_needed: Total hours needed for revision
        :param priority: Course priority ('high', 'medium', or 'low')
        """
        self.name = name
        self.exam_date = datetime.datetime.strptime(exam_date, "%Y-%m-%d").date()
        self.hours_needed = hours_needed
        self.priority = priority.lower()
        self.weight = self.PRIORITY_WEIGHTS.get(self.priority, 2)  # Default to medium if not matched

    def days_until_exam(self, today=None):
        """
        Calculate number of days from today to the exam date.
        :param today: Optional datetime.date object, defaults to current date
        :return: Integer number of days
        """
        if today is None:
            today = datetime.date.today()
        return max((self.exam_date - today).days + 1, 0)

