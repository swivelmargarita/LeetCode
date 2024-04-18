from collections import deque
class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        n = len(students)
        students_left = deque(students)
        n_didnt_eat = 0
        while len(students_left) > 0 and n_didnt_eat < len(students_left):
            if sandwiches[-1] == students_left[0]:
                sandwiches.pop()
                students_left.popleft()
                n_didnt_eat = 0
            else:
                students_left.append(students_left.popleft())
                n_didnt_eat += 1

        return(len(students_left))


if __name__ == "__main__":
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    solution = Solution().countStudents(students=students, sandwiches=sandwiches)
    print(solution)

        
