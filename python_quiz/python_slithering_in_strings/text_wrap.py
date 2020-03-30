import textwrap


def feedback_review(feedback, size):
    return textwrap.wrap(feedback, size)


def feedback_review_2(feedback, size):
    return textwrap.fill(feedback, size)


def feedback_review_3(feedback, size):
    return textwrap.shorten(feedback, size)


print(feedback_review("Dude, do you even review these feedbacks?", 16))
print()
print(feedback_review_2("Dude, do you even review these feedbacks?", 16))
print()
print(feedback_review_3("Dude, do you even review these feedbacks?", 16))
