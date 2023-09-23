import json

def schedule_lessons(lesson_requests):
    # Sort lesson requests by potential earnings per hour (earnings/duration)
    lesson_requests.sort(key=lambda x: x['potentialEarnings'] / x['duration'], reverse=True)
    
    schedule = {}
    total_earnings = 0
    
    # Initialize schedule for each day
    for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        schedule[day] = []
    
    # Initialize work hours per day
    work_hours_per_day = {day: 0 for day in schedule}
    
    # Iterate through lesson requests and allocate them to available days
    for request in lesson_requests:
        lesson_id = request["lessonRequestId"]
        duration = request["duration"]
        earnings = request["potentialEarnings"]
        available_days = request["availableDays"]
        
        # Iterate through available days and schedule the lesson if possible
        for day in available_days:
            if work_hours_per_day[day] + duration <= 12:
                schedule[day].append(lesson_id)
                work_hours_per_day[day] += duration
                total_earnings += earnings
                break
    
    return {"schedule": schedule, "totalEarnings": total_earnings}

# Sample lesson requests
lesson_requests = [
    {
        "lessonRequestId": "LR1",
        "duration": 1,
        "potentialEarnings": 100,
        "availableDays": ["monday", "wednesday"]
    },
    {
        "lessonRequestId": "LR2",
        "duration": 2,
        "potentialEarnings": 50,
        "availableDays": ["monday"]
    },
    {
        "lessonRequestId": "LR3",
        "duration": 12,
        "potentialEarnings": 1000,
        "availableDays": ["wednesday"]
    },
    {
        "lessonRequestId": "LR4",
        "duration": 13,
        "potentialEarnings": 10000,
        "availableDays": ["friday"]
    }
]

# Call the scheduling function
result = schedule_lessons(lesson_requests)

# Print the output in the desired format
output = {}
for day, lessons in result["schedule"].items():
    if lessons:
        output[day] = lessons

output_json = json.dumps(output, indent=4)
print(output_json)
