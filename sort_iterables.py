# sort() method = used with lists
# sort () function = used with iterables

# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
#
# # students.sort(reverse=True)
# sorted_students = sorted(students,reverse=True)
#
# for i in sorted_students:
#     print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

age = lambda ages: ages[2]
# students.sort(key=grade, reverse=True)
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)
