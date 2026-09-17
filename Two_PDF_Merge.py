from pypdf import PdfReader, PdfWriter

# Create a writer object
writer = PdfWriter()

# Read and add pages from the first PDF
reader1 = PdfReader("1295735989-113518-1.pdf")
for page in reader1.pages:
    writer.add_page(page)

# Read and add pages from the second PDF
reader2 = PdfReader("1295735989-113520-2.pdf")
for page in reader2.pages:
    writer.add_page(page)

# Write out the merged PDF
with open("output.pdf", "wb") as f:
    writer.write(f)

print("PDF merge successful! Check output.pdf")
