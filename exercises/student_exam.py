def get_exam_student(written_exam, practical_exam):
    final_vote = int(written_exam) + int(practical_exam)
    if (written_exam <= 0 and final_vote > 18) or (written_exam <= 0 and practical_exam < 18) or (written_exam > 0 and final_vote < 18):
        print("I'm sorry, you were rejected")
    else:
        if final_vote == 31 or final_vote == 32:
            print("Congratulations, 30 and praise")
        else:
            print("You're promoted and your final grade is: " + str(final_vote))


if __name__ == "__main__":
    written_exam = int(input("Written exam vote: "))
    practical_exam = int(input("Practical exam vote: "))
    get_exam_student(written_exam, practical_exam)
