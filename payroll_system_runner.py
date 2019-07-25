from payroll_system import Payroll

employee1 = Payroll("Vanessa", 27, "Female", 200000, 90000)
print(employee1.nssf_deductions)
print(employee1.paye)