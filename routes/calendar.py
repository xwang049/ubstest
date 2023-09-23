import json
import logging

from flask import request
from flask import Response
from routes import app

logger = logging.getLogger(__name__)


def schedule_lessons(lesson_requests):
    # Sort lesson requests by potential earnings per hour (earnings/duration)
    lesson_requests = [request for request in lesson_requests if request['duration'] > 0]
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

@app.route('/calendar-scheduling', methods=['GET','POST'])
def calendar():
    data = request.get_json()
    result = schedule_lessons(data)
    output = {}
    for day, lessons in result["schedule"].items():
        if lessons:
            output[day] = lessons
    return Response(json.dumps(output))