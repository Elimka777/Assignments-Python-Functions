#Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and 
# duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
#Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

def fitness_activities(activities, durations):
    if len(activities) != len(durations):
        print("Error: The number of activities does not match the number of durations.")
        return  
    for activity, dur in zip(activities, durations):
        print(f"{activity} corresponds to {dur} minutes.")

activities = ['Swimming', 'Biking', 'Dancing', 'Running']
durations = [25, 20, 15, 30]

fitness_activities(activities, durations)

def estimate_calories_burned(durations):            
    return [dur * float(3.5) for dur in durations]

total_burned = estimate_calories_burned(durations)
print(total_burned)

def summary(activities, durations, total_burned):
    for activity, dur, burned in zip(activities, durations, total_burned):
        print(f'While {activity} for {dur} minutes you lost {burned} calories.')

summary(activities, durations, total_burned)