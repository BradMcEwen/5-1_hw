# ============== Question 1 ================

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades, "are the grades from highest to lowest")

# ============== Task 2 =================

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
import statistics
print(statistics.mean(grades,), "is the average score!")


# ================= Question 2 ================


submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
passed =[]
for element in attended:
    if element in submitted:
        passed.append(element)
        print(passed, "completed both tasks!")
    else:
        print("the others failed to complete both!")

# ================ Question 3 ==================

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])


# =============== Task 2 =================

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
sorted_temperatures = sorted(temperatures)
print(sorted_temperatures[23:])
new_temp = sorted_temperatures[23:]
print(new_temp)