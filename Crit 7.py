# This is dictionary associated with course numbers and room numbers
room_numbers = {'CSC101': '3004', 'CSC102': '4501', 'CSC103': '6755', 'NET110': '1244', 'COM241': '1411'}

# This is a dictionary associating course numbers and instructors
instructors = {'CSC101': 'Haynes', 'CSC102': 'Alvarado', 'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}

# This is a dictionary associating course numbers and meeting times
meeting_times = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.', 'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'}

#  create function to get course details
def get_course_details(course_number):
    if course_number in room_numbers:
        room_number = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_time = meeting_times[course_number]
        return room_number, instructor, meeting_time
    else:
        return None, None, None

# Main function
def main():
    course_number = input("Enter a course number: ")
    room_number, instructor, meeting_time = get_course_details(course_number)
    if room_number is not None:
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Course not found.")

if __name__ == "__main__":
    main()