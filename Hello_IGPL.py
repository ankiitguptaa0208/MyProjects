import pyodbc
import pandas as pd

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=OMS_DEMO;"
    "Trusted_Connection=yes;"
)
print ("Connection successful!")
df = pd.read_sql("SELECT * FROM MstEmployee", conn)

print(df)
print("\n" + "="*50)
print("EMPLOYEE STATISTICS")
print("="*50)

# Calculate total active employees (IsActive = True)
active_employees = df[df['IsActive'] == True].shape[0]
print(f"\nTotal Active Employees (IsActive = True): {active_employees}")

# Count of OnRoll employees
onroll_employees = df[df['EmployeeType'].str.lower() == 'onroll'].shape[0]
print(f"Total OnRoll Employees: {onroll_employees}")

# Count of Contractual employees
contractual_employees = df[df['EmployeeType'].str.lower() == 'contractual'].shape[0]
print(f"Total Contractual Employees: {contractual_employees}")

# Show breakdown of all employee types
print("\nEmployee Type Breakdown:")
print(df['EmployeeType'].value_counts())

conn.close()