from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

# 1. Configure the pipeline to disable OCR
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False

# 2. Initialize the converter with the custom options
converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

# 3. Proceed with conversion
doc = converter.convert("GMguide.pdf").document

with open("gmguide.md", "w", encoding="utf-8") as f:
    f.write(doc.export_to_markdown())

print("Done.")
