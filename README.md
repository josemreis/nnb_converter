# nnb_converter

Python script for converting [Node.js notebooks](https://github.com/DonJayamanne/typescript-notebook) to Markdown or to a JavaScript script, and writes it in the directory of the nnb file.

# Usage 

```bash
usage: nnb_converter.py [-h] [-f FILE_TO_CONVERT] [-o CONVERT_TO]

Convert node.js notebook to Markdown or js scripts.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_TO_CONVERT, --file-to-convert FILE_TO_CONVERT
                        Node.js notebook file to convert
  -o CONVERT_TO, --convert-to CONVERT_TO
                        Convert the nnb file to 'md' or 'js'.
```

* Convert Node.js notebook to markdown

```bash
python3 nnb_converter.py -f "resources/sample.nnb" -o "md"
```

* Convert Node.js notebook to JavaScript

```bash
python3 nnb_converter.py -f "resources/sample.nnb" -o "js"
```