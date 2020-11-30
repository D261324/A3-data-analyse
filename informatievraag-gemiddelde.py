salaries = [ 42000, 55000, 35000 ]
count = 0
totalSalary = 0 

for salary in salaries:
    print(f"salary for employee {count}: {salary}")
    totalSalary = salaries[0] + salaries[1] + salaries[2]
    count += 1 
    
meanSalary = totalSalary / count

print(f"total salary: {totalSalary}")
print(f"total employees: {count}")
print(f"mean salary: {meanSalary}")