import fitz


class ConversionBackend(object):
    def convert(self, pdf_path, png_path):
        # Open the PDF file
        doc = fitz.open(pdf_path)

        # Read the PDF page
        page = doc.load_page(0)

        # Convert PDF page to image
        pix = page.get_pixmap()

        # Write image to PNG file
        pix.save(png_path)

        # Close the PDF file
        doc.close()
