import os
from pypdf import PdfReader, PdfWriter

# Path to the folder containing PDFs
folder_path = r"C:\Users\P00880029\AppData\Local\Programs\Python\Python313\Project Individual\pdf\Data"

# Create a writer object
writer = PdfWriter()

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(folder_path, filename)
        print(f"Adding: {filename}")
        
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

# Save the merged PDF
output_path = os.path.join(folder_path, "merged_output.pdf")
with open(output_path, "wb") as f:
    writer.write(f)

print(f"PDF merge successful! Check {output_path}")
