import openpyxl

# Load the workbook
wb = openpyxl.load_workbook('file.xlsx')

# Get a list of all sheets
sheets = wb.sheetnames

# Sort the sheets
sheets.sort()

# Reorder the sheets in the workbook
wb._sheets = [wb[sht] for sht in sheets]

# Save the workbook
wb.save('file.xlsx')

# ChatGPT Jan 30 Version. Free Research Preview (20230130)
