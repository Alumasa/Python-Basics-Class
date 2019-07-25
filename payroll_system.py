class Payroll:
    name = ""
    age = 0
    gender = ""
    basic_salary = 0
    benefits = 0
    taxable_pay = 0
    gross_salary = 0
    nssf_deductions = 0
    net_salary = 0
    paye = 0
    nhif_deductions = 0
    chargeable_income = 0
    net_income = 0

    def __init__(self, n, a, g, b, ben):
        Payroll.name = n
        Payroll.age = a
        Payroll.gender = g
        Payroll.basic_salary = b
        Payroll.benefits = ben
        #Payroll.paye(self)
        #Payroll.gross_salary = gs
        #Payroll.nssf_deductions = nssf
        Payroll.nssf_deductions(self)
        #Payroll.paye = p
        #Payroll.chargeable_income = ci
        #Payroll.net_salary = ns

    def nssf_deductions(self):
        if self.basic_salary > 18000:
            self.nssf_deductions = 18000 * 0.06
        else:
            self.nssf_deductions = self.basic_salary * 0.06
        return

    def paye(self):
        self.taxable_income = (self.basic_salary + self.benefits - self.nssf_deductions)
        if (self.taxable_income <= 12298):
            self.paye = (self.taxable_income * 0.1) - 1408
            tax_brack1 = self.taxable_income - 12298
            if (tax_brack1 == 12299 <= 23885):
                self.paye = (tax_brack1 * 0.15) - 1408
                tax_brack2 = tax_brack1 - 23885
                if (tax_brack2 == 23886 <= 35472):
                    self.paye = (tax_brack2 * 0.2) - 1408
                    tax_brack3 = tax_brack2 - 35472
                    if (tax_brack3 == 35473 <= 47059):
                        self.paye = (tax_brack3 * 0.25) - 1408
                        tax_brack4 = tax_brack3 - 47059
                        if tax_brack4 > 47059:
                            self.paye = (tax_brack4 * 0.3) - 1408
        return

    def nhif_deductions(self):
        self.chargeable_income = (self.taxable_income - self.paye)
        if self.chargeable_income <= 5999:
            self.chargeable_income -= 150
        if self.chargeable_income == 6000 <= 7999:
            self.chargeable_income -= 300
        if self.chargeable_income == 8000 <= 11999:
            self.chargeable_income -= 400
        if self.chargeable_income == 12000 <= 14999:
            self.chargeable_income -= 500
        elif self.chargeable_income == 15000 <= 19999:
            self.chargeable_income -= 600
        elif self.chargeable_income == 20000 <= 24999:
            self.chargeable_income -= 750
        elif self.chargeable_income == 25000 <= 29999:
            self.chargeable_income -= 850
        elif self.chargeable_income == 30000 <= 34999:
            self.chargeable_income -= 900
        elif self.chargeable_income == 35000 <= 39999:
            self.chargeable_income -= 950
        elif self.chargeable_income == 40000 <= 44999:
            self.chargeable_income -= 1000
        elif self.chargeable_income == 45000 <= 49999:
            self.chargeable_income -= 1100
        elif self.chargeable_income == 50000 <= 59999:
            self.chargeable_income -= 1200
        elif self.chargeable_income == 60000 <= 69999:
            self.chargeable_income -= 1300
        elif self.chargeable_income == 70000 <= 79999:
            self.chargeable_income -= 1400
        elif self.chargeable_income == 80000 <= 89999:
            self.chargeable_income -= 1500
        elif self.chargeable_income == 90000 <= 99999:
            self.chargeable_income -= 1600
        else:
            self.chargeable_income >= 100000
            self.chargeable_income -= 1700


    def gross_salary(self):
        self.gross_salary = self.basic_salary + self.benefits - self.nssf_deductions



    def net_salary(self):
        #self.net_salary = self.gross_salary - (self.paye + self.nssf_deductions + self.nhif_deductions)
        self.net_salary = self.chargeable_income
















