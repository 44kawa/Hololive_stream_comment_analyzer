def output_file(fname: str, txt_list: list):
    try:
        with open(fname, 'w', encoding='utf-16') as f:
            f.writelines(f"{item}\n" for item in txt_list)
        print(f"Data successfully written to '{fname}'")

    except IOError as e:
        print(f"File I/O error occurrd: {e}")
        raise

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    output_file(fname="test.csv", txt_list=["aaa,bbb,ccc", "ddd,eee"])
