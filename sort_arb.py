import json
import os

def sort_arb_file(input_file, output_file):
  """Sorts an .arb file by key and writes it to a new file, preserving meta-data."""

  with open(input_file, 'r') as f:
    data = json.load(f)

  meta_data = [key for key in data.keys() if key.startswith('@')]
  keys = [key for key in data.keys() if key not in meta_data]

  locale = [i for i in meta_data if i.startswith('@@')][0]
  sorted_data = {
    locale: data[locale]
  }

  for key in sorted(keys):
    sorted_data[key] = data[key]
    meta = f'@{key}'

    if meta in meta_data:
      sorted_data[meta] = data[meta]

  with open(output_file, 'w') as f:
    json.dump(sorted_data, f, indent=2)

def process_arb_files(directory):
  """Processes all .arb files in the specified directory."""

  for file in os.listdir(directory):
    if file.startswith("app_") and file.endswith(".arb") and not file.endswith('_sorted.arb'):
      input_file = os.path.join(directory, file)
      output_file = os.path.join(directory, file[:-4] + "_sorted.arb")
      sort_arb_file(input_file, output_file)

if __name__ == "__main__":
  current_directory = os.getcwd()
  process_arb_files(current_directory)