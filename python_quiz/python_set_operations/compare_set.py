"""
Every id in bestStudents is in scholarships;
Every id in scholarships is in allStudents;
Not every id in scholarships is in allStudents;
"""


def correct_scholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)


bestStudents = [3, 5]
scholarships = [3, 5, 7]
allStudents = [1, 2, 3, 4, 5, 6, 7]
print(correct_scholarships(bestStudents, scholarships, allStudents))
