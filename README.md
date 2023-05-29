# PDF Parser
PDF Parser is a Python package that leverages the Camelot library to parse tables from PDF documents.

## Installation

`pip install pdf_parser
`

## Usage

`<pre><code>from pdf_parser import parse_pdf

pdf_file_path = '/path/to/your/pdf_file.pdf'
results = parse_pdf(pdf_file_path)

for result in results:
    register_no = result["regno"]
    branch = extract_branch_from_regno(register_no)
    print(branch)
`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
