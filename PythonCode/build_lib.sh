#!/bin/bash

# Get the source file name
source_file="$1"

# Check if a filename was provided
if [ -z "$source_file" ]; then
  echo "Error: Please provide a source file name as an argument."
  exit 1
fi

# Get the file extension
extension="${source_file##*.}"

# Compile based on the extension
if [[ "$extension" == "cpp" ]]; then
  clang++ -c -std=c++20 -fPIC "$source_file" -o "${source_file%.cpp}.o"
  clang++ -shared -o "lib${source_file%.cpp}.so" "${source_file%.cpp}.o"
elif [[ "$extension" == "c" ]]; then
  clang -c -fPIC "$source_file" -o "${source_file%.c}.o"
  clang -shared -o "lib${source_file%.c}.so" "${source_file%.c}.o"
else
  echo "Error: Unsupported file extension. Only .c and .cpp files are allowed."
  exit 1
fi

echo "Built library for ${source_file}"

