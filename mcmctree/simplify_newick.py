import re
import argparse
import sys
from typing import List

# Core logic function
def simplify_newick(s: str) -> str:
    """Removes branch lengths and support values from a single Newick string."""
    # Pattern to match: :[branch_length][optional_support]
    # Example match: :0.00045[100]
    pattern_to_remove = r':[0-9.eE\-]+(\[.*?\])?'
    return re.sub(pattern_to_remove, '', s)

def main():
    # 1. Setup argument parsing for robustness
    parser = argparse.ArgumentParser(
        description="Simplifies Newick tree files by removing branch lengths and node support values (e.g., :0.01[99])."
    )
    # Required positional arguments for input and output paths
    parser.add_argument(
        'input_file', 
        type=str, 
        help='Path to the input file containing one or more complex Newick strings.'
    )
    parser.add_argument(
        'output_file', 
        type=str, 
        help='Path to the output file for the simplified Newick strings.'
    )
    
    args = parser.parse_args()

    input_path = args.input_file
    output_path = args.output_file

    try:
        # 2. Read input file content
        with open(input_path, 'r', encoding='utf-8') as infile:
            # Read all lines, remove whitespace, and filter out blank lines
            lines = [line.strip() for line in infile if line.strip()]

        if not lines:
            print(f"Warning: Input file '{input_path}' is empty. No operation performed.")
            return

        # 3. Process all strings using the core function
        simplified_trees = [simplify_newick(tree_string) for tree_string in lines]

        # 4. Write output file
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(simplified_trees) + '\n')
            
        print(f"Success: {len(simplified_trees)} Newick string(s) simplified and saved to '{output_path}'.")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'. Please check the path.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
