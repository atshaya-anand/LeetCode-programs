# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        studentsCount = 0
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                studentsCount += 1
        return studentsCount