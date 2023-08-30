import pandas as pd
from PyPDF2 import PdfFileReader

def ingest_policies(filepath):
  pdf = PdfFileReader(filepath)
  text = ""

  for page in pdf.pages:
    text += page.extractText()

  return text
  print("hey2")
  def ingest_logs(filepath):
  logs = pd.read_csv(filepath)
  return logs