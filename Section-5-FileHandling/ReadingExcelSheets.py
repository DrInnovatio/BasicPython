import pandas as pd

file = pd.ExcelFile("sales.xlsx.cpgz")
print(file.sheet_names)