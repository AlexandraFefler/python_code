import enum
class Weekdays(enum.Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6

schedule = []
days = int(input("Enter the amount of days: "))
for day in range(days): #0-(days-1)
    day_in_week = []
    hours = int(input("How many hours for "+Weekdays(day+1).name))
    # for hour in range(hours): #0-(hours-1) -> 8-(hours-1+8) -> 8-(hours+7) $$
    #     day_in_week.append("Free")
    # day_in_week.append(["Free"]*hours)
    for lesn in range(hours):
        day_in_week.append("Free")
    schedule.append(day_in_week)
#check:
for day in range(days):
    print(schedule[day])

lessons = [] #initializing a list
lesson = input("Enter the lesson you want to put into the schedule, to end enter 'done': (name_duration_day_hour) ")
while (lesson.upper()!="DONE"):
    splitted_lesson_info = lesson.split("_") #it's a list
    # saving each thing in list 'splitted_lesson_info' in a dict thing
    lesson_info = {"name":splitted_lesson_info[0],"duration":splitted_lesson_info[1],"day":splitted_lesson_info[2], "hour":splitted_lesson_info[3]}
    lessons.append(lesson_info)
    lesson = input("Enter the lesson you want to put into the schedule, to end enter 'done': (name_duration_day_hour) ")

# first placing of the lessons into the schedule
for lesson_to_put in range(len(lessons)):
    name = lessons[lesson_to_put]["name"]
    duration = int(lessons[lesson_to_put]["duration"])
    day = int(lessons[lesson_to_put]["day"])
    hour = int(lessons[lesson_to_put]["hour"])
    not_placed_first = []

    # counting if there's place for the lesson (enough free lessons)
    free_lssn_counter = 0
    for day_in_sch in range(len(schedule)):
        if day_in_sch+1 == day:
            for lesson_in_day in range(len(schedule[day-1])):
                # first_bool = lesson_in_day+8 >= hour
                # second_bool = schedule[day-1][lesson_in_day] == "Free"
                # check = str(schedule[0][0])
                if ((lesson_in_day+8) >= hour) and (str(schedule[day-1][lesson_in_day]) == "Free"): #lesson in day starts at 0, as in line marked as $$ (line 15)
                    free_lssn_counter += 1
    if free_lssn_counter >= duration:
        duration_counter = duration
        # right_day = schedule[day]
        for lesson_in_day_put in range(len(schedule[day-1])):
            if ((lesson_in_day_put + 8) >= hour) and (schedule[day-1][lesson_in_day_put] == "Free") and (duration_counter > 0):
                schedule[day-1][lesson_in_day_put] = name
                duration_counter -= 1 # adding lesson name until the count of duration hours become 0, but by saving the original duration just in case. Or maybe it can be a good identifier to an already well put lesson? hmmm
    else: # in case there are not enough free lessons
        not_placed_lesson_info = {"name": splitted_lesson_info[0], "duration": splitted_lesson_info[1],
                       "day": splitted_lesson_info[2], "hour": splitted_lesson_info[3]}
        not_placed_first.append(not_placed_lesson_info)

print(schedule)
print("-------------------------")
print(not_placed_first)