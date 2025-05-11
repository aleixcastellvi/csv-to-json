import csv
import json
import os
import sys
import argparse
from datetime import datetime

def parse_value(value):
    value = value.strip()
    if value == "":
        return None
    if value.lower() == "false":
        return False
    if value.lower() == "true":
        return True
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    try:
        return datetime.fromisoformat(value).isoformat()
    except ValueError:
        pass
    return value

def run(input_file, delimiter=","):
    if not os.path.isfile(input_file):
        print("File not found")
        return

    # Constants definition
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    output_path = os.path.join(os.getcwd(), f"{file_name}.json") # Absolute path where the script is located

    try:
        with open(input_file, mode="r", encoding="utf-8") as csv_file:
            # Read the CSV as a list of dictionaries, using the first row as keys
            reader = csv.DictReader(csv_file, delimiter=delimiter)

            # List of elements. Each element is a dictionary (row) with key-value pairs
            data_parsed = [
                {key.strip(): parse_value(value) for key, value in row.items()}
                for row in reader
            ]

        with open(output_path, mode="w", encoding="utf-8") as json_file:
            json.dump(data_parsed, json_file, indent=2, ensure_ascii=False)

        print(f"The file {file_name}.json has been successfully generated at: {output_path}")

    except Exception as e:
        print(f"Error processing the file: {e}")

if __name__ == "__main__":
    # Configuration of the application's help and command-line interface
    parser = argparse.ArgumentParser(
        description="Convert a CSV file to JSON format.",
        epilog=(
            "Example:\n"
            "  python csv_to_json.py /path/to/file.csv\n"
            "By default, the delimiter is ','. Use -d to specify a different one.\n"
            "Example with another delimiter:\n"
            "  python csv_to_json.py /path/to/file.csv -d ;\n\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("csv_path", help="Absolute path to the CSV file to convert.")
    parser.add_argument(
        "-d", "--delimiter",
        default=",",
        help="CSV delimiter to use (default: ',')"
    )

    # Parse the command-line arguments provided
    args = parser.parse_args()

    # Run the application
    run(args.csv_path, args.delimiter)
