import pandas as pd

# Load the Excel file
file_path = "sarmad.xlsx"  # Update this with your file path
sheet_name = "Sheet1"  # Specify the sheet name if needed

# Read the sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the first few rows of the DataFrame
print(df.head())
