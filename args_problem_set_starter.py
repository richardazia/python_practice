# ============== PART 1 ============== 
# Write a function called contains_pickle that accepts any number of arguments. 
# The function should return True if it is passed "pickle" as one of the args
# Otherwise it should return False

#  contains_pickle("red", 45, "pickle", [])  --> True
#  contains_pickle(1,2, "blue") ---------------> False

def contains_pickle(*args):
    return "pickle" in args #We do not need to write an if else statement because this is built in to "in"

# ============== PART 2 ============== 
# Write a function called count_fails that counts up the number of failing test scores it is passes
# It should accept any number of arguments
# It should return a count of how many args are less than or equal to 50

# count_fails(99,48,79,36) -------> 2
# count_fails(85,78,91) ----------> 0
# count_fails(50,41,47,74,76,81) -> 3

def grades(*count_fails):
    failed = 0
    for fail in count_fails:
        if int(fail) <= 50:
            print("one more fail")
            failed += 1
    print(f"There were {failed} fails  in the class")
print("1.")
print(grades(99,48,79,36)) # Two fails
print("2.")
print(grades(85,78,91))
print("3.")
print(grades(50,41,47,74,76,81))



# ============== PART 3 ============== 
# Write a function called get_top_students that helps teachers find their A-grade students!
# It should accept any number of student=score keyword arguments like colt=78 or elton=98
# It should return a list containing the names of students who scored 90 or above

# get_top_students(tim=91, stacy=83, carlos=97, jim=69) -> ['tim', 'carlos']
# get_top_students(colt=61, elton=76) -------------------> []
# get_top_students(kitty=80, blue=95, toad=91)-----------> ['blue', 'toad']

def get_top_students(**kwargs):
    top_students = []
    for student, score in kwargs.items():
        if score >= 90:
            top_students.append(student)
    print(top_students)

print(get_top_students(tim=91, stacy=83, carlos=97, jim=69))
print(get_top_students(colt=61, elton=76))
print(get_top_students(kitty=80, blue=95, toad=91))