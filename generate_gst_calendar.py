from fpdf import FPDF

calendar_data = [
    ("January", "11 Jan", "GSTR-1", "Sales Return"),
    ("January", "20 Jan", "GSTR-3B", "Summary Return"),
    ("February", "11 Feb", "GSTR-1", "Sales Return"),
    ("February", "20 Feb", "GSTR-3B", "Summary Return"),
    ("March", "11 Mar", "GSTR-1", "Sales Return"),
    ("March", "20 Mar", "GSTR-3B", "Summary Return"),
    ("April", "11 Apr", "GSTR-1", "Sales Return"),
    ("April", "20 Apr", "GSTR-3B", "Summary Return"),
    ("May", "11 May", "GSTR-1", "Sales Return"),
    ("May", "20 May", "GSTR-3B", "Summary Return"),
    ("June", "11 Jun", "GSTR-1", "Sales Return"),
    ("June", "20 Jun", "GSTR-3B", "Summary Return"),
    ("July", "11 Jul", "GSTR-1", "Sales Return"),
    ("July", "20 Jul", "GSTR-3B", "Summary Return"),
    ("August", "11 Aug", "GSTR-1", "Sales Return"),
    ("August", "20 Aug", "GSTR-3B", "Summary Return"),
    ("September", "11 Sep", "GSTR-1", "Sales Return"),
    ("September", "20 Sep", "GSTR-3B", "Summary Return"),
    ("October", "11 Oct", "GSTR-1", "Sales Return"),
    ("October", "20 Oct", "GSTR-3B", "Summary Return"),
    ("November", "11 Nov", "GSTR-1", "Sales Return"),
    ("November", "20 Nov", "GSTR-3B", "Summary Return"),
    ("December", "11 Dec", "GSTR-1", "Sales Return"),
    ("December", "20 Dec", "GSTR-3B", "Summary Return"),
]

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "GST Calendar 2025 - Due Dates for GSTR Filing", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", 'B', 12)
pdf.set_fill_color(200, 220, 255)
pdf.cell(40, 10, "Month", 1, 0, 'C', 1)
pdf.cell(30, 10, "Due Date", 1, 0, 'C', 1)
pdf.cell(40, 10, "Return Form", 1, 0, 'C', 1)
pdf.cell(80, 10, "Description", 1, 1, 'C', 1)

pdf.set_font("Arial", '', 12)
for row in calendar_data:
    pdf.cell(40, 10, row[0], 1, 0, 'C')
    pdf.cell(30, 10, row[1], 1, 0, 'C')
    pdf.cell(40, 10, row[2], 1, 0, 'C')
    pdf.cell(80, 10, row[3], 1, 1, 'C')

pdf.output("gst-calendar-2025.pdf")
