students = ["John", "Doe", "Mark", "Tyson"]

print(students)
#rem index starts from 0.to find out the index of a list,check the position then subtract by 1
#length: total no. of items in a variaable list
print(len(students))
print(students[0])
print(students[-1])

students.insert(1, "Alex")
students.append("Jack")
students.remove("Mark")
students[0] = "Alice"  #change value
print(students)
print(students[-1:-3])#not so clear

#lstudent= len(students)-1

# students.insert -index 1, _object"Alex"
#append adds at the very end
#lists allows duplicates