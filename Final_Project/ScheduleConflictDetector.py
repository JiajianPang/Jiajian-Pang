class ScheduleConflictDetector:
    @staticmethod
    def check(plan, preferences):
        """
        Check for study time conflicts where planned study hours exceed daily limits.

        :param plan: Dictionary mapping each date to a list of (course, hours) tuples
        :param preferences: UserPreferences object containing study limits and blocked time
        :return: List of tuples (date, total_hours) where total study + blocked time exceeds the daily limit
        """
        conflicts = []
        for day, items in plan.items():
            study_total = sum(hours for _, hours in items)
            limit = preferences.daily_limit
            blocked = preferences.blocked_times.get(day, 0)

            # If total planned study time + blocked time exceeds the daily limit
            if study_total + blocked > limit:
                conflicts.append((day, study_total + blocked))

        return conflicts

