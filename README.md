# CSV to JSON

Script that converts a CSV file into a JSON file, preserving the structure of rows and columns.

The resulting JSON file is saved in the directory where the script is executed, using the original filename.

## Steps to run the app

Default usage with coma `,` as delimiter in the source file:
```bash
python csv_to_json.py /path/to/file.csv
```

With custom delimiter:

```bash
python csv_to_json.py /path/to/file.csv -d ,
```

Show help and usage:
```bash
python csv_to_json.py -h
```

or:
```bash
python csv_to_json.py --help
```
