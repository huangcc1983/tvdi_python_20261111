from pathlib import Path


def main():
    sample_path = Path(__file__).with_name("sample.txt")

    with sample_path.open("r", encoding="utf-8") as file:
        content = file.read()

    print("=== 檔案全部內容 ===")
    print(content)

    print("=== 逐行讀取 ===")
    with sample_path.open("r", encoding="utf-8") as file:
        line_count = 0
        for line in file:
            line_count += 1
            print(f"{line_count}: {line.rstrip()}")

    print(f"總行數：{line_count}")


if __name__ == "__main__":
    main()
