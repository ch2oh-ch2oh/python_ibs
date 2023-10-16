import argparse
import csv
import sys


def validate_csv(file_path, has_header=False, delimiter=','):
    try:
        with open(file_path, newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            if has_header:
                header = next(reader)
                for row in reader:
                    assert len(row) == len(header), f"Количество столбцов в строке {reader.line_num} не соответствует заголовку"
            else:
                last_row = next(reader)
                for row in reader:
                    assert len(row) == len(last_row), f"Количество столбцов в строках {reader.line_num - 1}, {reader.line_num} различается"
        return "csv файл валиден"
    except Exception as e:
        return f"Ошибка: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description="csv валидатор")
    parser.add_argument("file_path", help="Путь к файлу")
    parser.add_argument("--header", action="store_true", help="Наличие заголовка")
    parser.add_argument("--delimiter", default=",", help="Разделитель")

    args = parser.parse_args()

    # print(args)
    result = validate_csv(args.file_path, has_header=args.header, delimiter=args.delimiter)
    print(result)

    if "Ошибка" in result:
        sys.exit(1)
    else:
        sys.exit(0)


main()
