from openpyxl import load_workbook

from datetime import datetime, date, time
from pathlib import Path
import xlwings as xw
import shutil

## Source Workbook
source_path = Path("Day 88 - Rota automation/GCCU_Blank_Rota_Template.xlsx")

output_path = Path("Day 88 - Rota automation/output/output.xlsm")



wb_source = load_workbook(source_path, data_only=True)
print(wb_source)

ws_source = wb_source["GCCU Rota"]
print(ws_source.title)

# ## Original destination template
# template_path = Path("Test.xlsm")

# ## Get source headers
# day_of_week_headers = [cell.value for cell in ws_source[3]]

# for row in range(28, ws_source.max_row + 1):
#     cell = ws_source.cell(row=row, column=30)
#     print(cell.value)



# finally:

#     ## Close source workbook
#     wb_source.close()

#     ## Close Excel
#     app.quit()