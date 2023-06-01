# PDF Parser
PDF Parser is a Python package that leverages the Camelot library to parse tables from PDF documents.

## Installation
- Before using the library, the dependency libGL.so should be present in the system. This can be installed in Ubuntu/Debian by using apt
`sudo apt install libgl-dev`
- You can install this library by using pip
`
pip install .
`

## Usage

<pre><code>from pdf_parser import parse_pdf

pdf_file_path = '/path/to/your/pdf_file.pdf'
results = parse_pdf(pdf_file_path)
</code></pre>

The result should be a JSON structure containing student data along with other details


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
