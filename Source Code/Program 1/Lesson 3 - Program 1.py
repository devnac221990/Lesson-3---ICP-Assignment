class Employee:
    _numberOfEmployees=0
    _employeeSalaryList=[]

    def __init__(self, name, family, salary, department):
        self._name=name
        self._family=family
        self._salary=salary
        self._department=department
        Employee._employeeSalaryList.append(salary)
        Employee._numberOfEmployees+=1


    def getName(self):
        return self._name
    def getFamily(self):
        return self._family
    def getSalary(self):
        return self._salary
    def getDepartment(self):
        return self._department

    def average_Salary(self):
        return sum(Employee._employeeSalaryList)/Employee._numberOfEmployees
class FullTimeEmployee(Employee):
    def __init__(self,name, family, salary, department,hours):
        super.__init__(name, family, salary, department)
        self._hoursPerWeek=hours
    def getHoursPerWeek(self):
        return self._hoursPerWeek





c =Employee("Avni",'Chats',400000,'IT')
d=Employee("Rina",'Mehta',55500000,'HR')
e=Employee("Anthony",'Carvalho',60000, 'HR')

print(c.average_Salary(),'is average salary')
print(d.getName(), d.getFamily())
print("get number of employees: ", d._numberOfEmployees)




