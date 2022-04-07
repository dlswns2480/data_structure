class Employee:
    """직원 클래스"""
    Company_cnt = 0

    def __init__(self, name = "NULL", salary = 0):
        self.__name = name
        self.__salary = salary
        Employee.Company_cnt += 1

    def get_name(self):
        return self.__name
    
    def get_salary(self):
        return self.__salary

    def get_emp_cnt(self):
        return self.Company_cnt


if __name__ == "__main__":
    Company = []
    data = {"Alice":200, "Bob":300, "Mike":100}

    for key in data:
        emp = Employee(key, data[key])
        Company.append(emp)
    
    ### 총 employee의 숫자 ###
    print("Total number of employees: ", Company[0].get_emp_cnt())

    ### 최대 월급 직원 정보를 리스트를 탐색하여 찾는 경우 ###
    max_salary = 0
    max_name = ""
    for emp in Company:
        if int(emp.get_salary()) > max_salary:
            max_name = emp.get_name()
            max_salary = int(emp.get_salary())

    print("Max-salary employee: ", max_name, max_salary)