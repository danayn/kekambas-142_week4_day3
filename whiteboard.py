# You are given a string s representing an attendance record for a student where each character
#  signifies whether the student was absent, late, or present on that day. The record only 
# contains the following three characters:

# 'A': Absent.
# 'L': Late.
# 'P': Present.
# The student is eligible for an attendance award if they meet both of the following criteria:
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutivedays.
# Return true if the student is eligible for an attendance award, or false otherwise.

# Example 1:
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

attendance = 'PAPPPAPPPPL'

def solution(attendance):
    return attendance.count('A') < 2 and 'LLL' not in attendance


def solution(attendance):
    total_absent = 0
    day = 0
    while day < len(attendance):
        if attendance[day] == 'A':
            total_absent += 1
            if total_absent >= 2:
                return False
            day += 1
        elif attendance[day] == 'L':
            consec_late = 1
            day += 1
            while day < len(attendance) and attendance[day] == 'L':
                consec_late += 1
                day += 1
                if consec_late >= 3:
                    return False
        else:
            day += 1
    return True
        

