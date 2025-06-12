# 🗓️ Simple Habit Tracker

print("Welcome to your Habit Tracker!")

habit = input("What habit do you want to track? ").strip().lower()

# For demo, we'll just simulate last streak days
last_streak = 3

print(f"Your current streak for '{habit}' is {last_streak} days.")

done_today = input(f"Did you do '{habit}' today? (yes/no): ").strip().lower()

if done_today == "yes":
    last_streak += 1
    print(f"Great! Your new streak is {last_streak} days. Keep going!")
else:
    last_streak = 0
    print(f"Don’t worry! Your streak resets to {last_streak}. Start again tomorrow!")

print("Keep up the good work! 💪")
