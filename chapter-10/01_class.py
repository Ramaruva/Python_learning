class Employee:
    language="Py"
    salary=120000
    def getinfo(self):
        print(f"The language is {self.language}")

ram = Employee()
ram.name="Ram"
ram.language="Java"
print(ram.name,ram.salary,ram.language)
print(ram.getinfo())