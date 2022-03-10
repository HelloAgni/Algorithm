def check_exam(arr1, arr2):
    """
    The first input array is the key to the correct answers.
    The second one contains a student's submitted answers.
    Return the score for this array of answers,
    giving +4 for each correct answer,
    -1 for each incorrect answer, and +0 for each blank answer.
    If the score < 0, return 0.
    checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
    checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
    """
    total = 0
    for count, x in enumerate(arr2):
        if x == arr1[count]:
            total += 4
        elif x == "":
            total += 0
            print('нет ответа')
        elif x != arr1[count]:
            total -= 1
    if total < 0:
        return 0
    print(total)


# v2
def check_exam_v2(arr1, arr2):
    print(max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b)))


arr1 = ["a", "a", "c", "b"]
arr2 = ["a", "a", "b",  ""]
check_exam(arr1, arr2)
check_exam_v2(arr1, arr2)
