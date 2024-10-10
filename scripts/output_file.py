"""
Module name: output_file
This module provides a function to output the contents of a list to a specified file.
"""

from typing import List


def output_file(fname: str, txt_list: List[str]) -> None:
    """
    Writes the contents of the list to the specified file.

    Args:
        fname (str): The name of the output file.
        txt_list (List[str]): The list of texts to write.

    Raises:
        IOError: If an input/output error occurs.
    """
    try:
        with open(fname, 'w', encoding='utf-16') as f:
            f.writelines(f"{item}\n" for item in txt_list)
        print(f"Data successfully written to '{fname}'")

    except IOError as e:
        print(f"File I/O error occurred: {e}")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    output_file(fname="test.csv", txt_list=["aaa,bbb,ccc", "ddd,eee"])
