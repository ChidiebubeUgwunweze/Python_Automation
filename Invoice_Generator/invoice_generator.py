import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from datetime import datetime

# ---------- CONFIG ----------
SHEET_NAME = "Invoice Data"          # your Google Sheet title
WORKSHEET_NAME = "Sheet1"        # tab name (change if needed)
CREDENTIALS_FILE = "credentials.json"  # your credentials file
OUTPUT_DIR = "invoices"
ONLY_UNPAID = True               # if True, only generate for rows where Status != "Paid"
# ----------------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Authenticate and open sheet
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).worksheet(WORKSHEET_NAME)

# Read all rows (list of lists). First row = headers
rows = sheet.get_all_values()
if not rows or len(rows) < 2:
    print("No data found in sheet.")
    exit()

headers = [h.strip() for h in rows[0]]
data_rows = rows[1:]

# Helper to get column by name
def get_val(row, col_name):
    try:
        idx = headers.index(col_name)
        return row[idx].strip()
    except ValueError:
        return ""

# Function to draw a simple invoice



# Loop rows and generate invoices
generated = []
for row in data_rows:
    status = get_val(row, "Status").lower()
    if ONLY_UNPAID and status == "paid":
        continue
    pdf_path = create_invoice_pdf(row)
    generated.append(pdf_path)
    print("Generated:", pdf_path)

print(f"\nDone. {len(generated)} invoice(s) created in '{OUTPUT_DIR}' folder.")
