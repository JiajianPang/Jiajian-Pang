from Course import Course
from User_Preferences import UserPreferences
from MotivationEngine import MotivationEngine
from ScheduleConflictDetector import ScheduleConflictDetector
from StudyScheduleGenerator import StudyScheduleGenerator
import random

# Step-by-step input for all courses
def input_courses():
    courses = []
    print("🧠 Let's add your courses one by one!")

    num_courses = int(input("How many courses do you want to add? (e.g., 3) 👉 "))
    for i in range(1, num_courses + 1):
        print(f"\n➤ Course {i}")

        name = input("Course name 🏷️: ")
        date = input("Exam date 📅 (YYYY-MM-DD): ")

        hours_input = input("Estimated study time (in hours) ⌛ (Default: 10): ")
        hours = int(hours_input) if hours_input.strip() else 10

        priority = input("Priority (high / medium / low) ⚖️ (Default: medium): ")
        if priority.strip() == "":
            priority = "medium"

        courses.append(Course(name, date, hours, priority))

        # Fun encouragements to keep the user engaged
        if i == 1:
            print("💡 Great! The first step is half the battle!")
        elif i == num_courses:
            print("🎉 All courses added! You're ready to go!")
        else:
            print(random.choice([
                "📘 Keep it up! More courses, more planning power!",
                "💪 Almost there! Stay strong!",
                "📈 Just a little more and you'll be ahead of the game!"
            ]))

    return courses

# Ask user for their daily study preferences
def setup_preferences():
    print("\n🛠️ Let's configure your study preferences (press Enter to use defaults)")

    prefs = UserPreferences()

    limit_input = input("Max study hours per day? (Default: 4) 👉 ")
    prefs.daily_limit = int(limit_input) if limit_input.strip() else 4

    weekend_input = input("Do you want to study on weekends? (y/n, default: y) 👉 ")
    prefs.include_weekends = False if weekend_input.strip().lower() == 'n' else True

    night_input = input("Do you prefer to study at night? (y/n, default: n) 👉 ")
    prefs.prefer_night = night_input.strip().lower() == 'y'

    block_count = input("\nHow many days do you have pre-booked (work, club, etc)? (Default: 0): ")
    block_count = int(block_count.strip()) if block_count.strip() else 0
    for _ in range(block_count):
        d = input("Enter conflict date 📆 (YYYY-MM-DD): ")
        h = int(input("How many hours are blocked on that day ⛔: "))
        prefs.block_time(d, h)

    print("✅ Preferences saved! Generating your study plan...\n")
    return prefs

# Main execution
def main():
    print("🎓 Welcome to SmartStudy Pro - Your Personalized Study Planner!\n")

    # Set user preferences
    prefs = setup_preferences()

    # Add courses
    gen = StudyScheduleGenerator(prefs)
    courses = input_courses()
    for c in courses:
        gen.add_course(c)

    # Generate the study schedule
    plan = gen.generate()

    # Display the generated schedule with motivational quotes
    print("\n📅 Here is your personalized study plan:")
    for day in sorted(plan):
        if plan[day]:
            print(f"\n{day}:")
            for course, h in plan[day]:
                print(f"  📘 {course}: {h} hours")
            print("  💬 Motivation: " + MotivationEngine.get_daily_quote())

    # Check for schedule conflicts
    conflicts = ScheduleConflictDetector.check(plan, prefs)
    if conflicts:
        print("\n⚠️ The following days exceed your available study hours:")
        for day, total in conflicts:
            print(f"  {day}: Total {total} hours (exceeds limit)")
    else:
        print("\n✅ No conflicts found. You're good to go!")

    # Ask user whether to save the plan
    save = input("\nWould you like to save the schedule to a file? (y/n): ").strip().lower()
    if save == 'y':
        gen.save_to_file(plan)

# Entry point
if __name__ == "__main__":
    main()
