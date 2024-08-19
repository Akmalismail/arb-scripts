import json
import os


def find_missing_keys(main_file, other_files, output_file):
    with open(main_file, 'r') as f:
        main = json.load(f)

    missing = {}

    for other_file in other_files:
        with open(other_file) as f:
            other = json.load(f)

        for key in main.keys():
            if key not in other.keys():
                if other_file in missing:
                    missing[other_file].append(key)
                else:
                    missing[other_file] = [key]

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(missing, f, indent=2)


def process_arb_files(directory):
    """Processes all .arb files in the specified directory."""

    arb_files = [file for file in os.listdir(
        directory) if file.startswith('app_') and file.endswith('.arb')]

    for arb_file in arb_files:
        output_file = os.path.join(
            f'{directory}/missing/', arb_file[:-4] + ".json")
        find_missing_keys(
            arb_file, [file for file in arb_files if file != arb_file], output_file)


if __name__ == "__main__":
    current_directory = os.getcwd()
    process_arb_files(current_directory)
