# Python 檔案操作：一步一步練習

這份教學會帶你練習讀取文字檔、逐行處理資料，以及寫入和追加內容。請先把本教學、`read_file_practice.py` 和 `sample.txt` 放在同一個資料夾。

## 開始前

1. 用 VS Code 開啟這個資料夾。
2. 確認資料夾內有 `sample.txt` 和 `read_file_practice.py`。
3. 開啟終端機，執行：

   ```text
   python read_file_practice.py
   ```

   如果你的電腦使用 `py` 啟動 Python，也可以執行 `py read_file_practice.py`。

範例程式使用 `__file__` 找到和程式放在一起的 `sample.txt`，所以即使終端機目前所在的位置不同，也能找到範例檔。

## 第 1 步：認識範例檔

打開 `sample.txt`，你會看到幾行文字。每一行代表一筆簡單的閱讀紀錄。Python 讀取這個檔案後，就能把內容放進變數，再印出或進一步處理。

## 第 2 步：讀取整個檔案

```python
from pathlib import Path

sample_path = Path(__file__).with_name("sample.txt")

with sample_path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

逐行看這段程式：

- `Path(...)` 用來表示檔案路徑。
- `with` 會在程式離開區塊時自動關閉檔案，不需要自己呼叫 `close()`。
- `"r"` 表示以讀取模式開啟檔案。
- `encoding="utf-8"` 可正確處理繁體中文等文字。
- `read()` 會一次讀取整個檔案，結果是字串。

執行後應會印出 `sample.txt` 的全部內容。

## 第 3 步：逐行讀取

檔案較大時，可以一次處理一行，不必把全部內容都放進記憶體：

```python
from pathlib import Path

sample_path = Path(__file__).with_name("sample.txt")

with sample_path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

`for line in file` 會依序讀出每一行。文字行的結尾通常帶有換行符號；`rstrip()` 會移除行尾的空白和換行符號，避免輸出中間多出空行。

## 第 4 步：數一數有幾行

```python
from pathlib import Path

sample_path = Path(__file__).with_name("sample.txt")

with sample_path.open("r", encoding="utf-8") as file:
    lines = file.readlines()

print(f"共有 {len(lines)} 行")
```

`readlines()` 會把每行放進一個清單。清單的長度就是讀到的行數。若檔案很大，使用上一個步驟的逐行讀取通常更合適。

## 第 5 步：尋找包含關鍵字的行

```python
from pathlib import Path

sample_path = Path(__file__).with_name("sample.txt")
keyword = "Python"

with sample_path.open("r", encoding="utf-8") as file:
    for line in file:
        if keyword in line:
            print(line.rstrip())
```

`keyword in line` 可以檢查這一行是否包含指定文字。請試著把 `keyword` 改成 `閱讀` 或 `練習`。

## 第 6 步：寫入新檔案

以下程式會在範例檔旁建立 `notes.txt`：

```python
from pathlib import Path

notes_path = Path(__file__).with_name("notes.txt")

with notes_path.open("w", encoding="utf-8") as file:
    file.write("我的第一個文字檔\n")
    file.write("我正在練習 Python 檔案操作。\n")

print(f"已寫入：{notes_path}")
```

`"w"` 是寫入模式：檔案不存在時會建立檔案；檔案已存在時會先清除舊內容，再寫入新內容。若不想覆蓋重要資料，請改用新檔名。

## 第 7 步：追加內容

```python
from pathlib import Path

notes_path = Path(__file__).with_name("notes.txt")

with notes_path.open("a", encoding="utf-8") as file:
    file.write("這一行是後來追加的。\n")
```

`"a"` 是追加模式：新內容會加在檔案末尾，不會清除原有內容。再次執行這段程式時，同一行也會再增加一次。

## 常見開啟模式

| 模式 | 用途 | 注意事項 |
|---|---|---|
| `"r"` | 讀取檔案 | 檔案必須已存在 |
| `"w"` | 寫入檔案 | 會清除已存在檔案的舊內容 |
| `"a"` | 在檔案末尾追加 | 不會清除原有內容 |
| `"x"` | 建立新檔案 | 若檔案已存在會發生錯誤 |

## 找不到檔案怎麼辦？

檔案路徑錯誤或檔案不存在時，Python 會發生 `FileNotFoundError`。你可以先確認：

1. 檔名是否拼對，例如 `sample.txt`。
2. 範例檔是否和程式放在同一個資料夾。
3. 程式是否使用上面示範的 `Path(__file__).with_name(...)`。

初學時先把檔案和程式放在一起，並使用 `encoding="utf-8"`，會比較容易避免路徑和中文編碼問題。

## 練習題

1. 用 `read()` 讀出 `sample.txt`，並印出內容。
2. 改用逐行讀取，印出每一行前面加上行號，例如 `1: ...`。
3. 找出所有含有 `Python` 的行。
4. 把你最喜歡的一行寫到 `notes.txt`。
5. 再執行一次追加程式，觀察 `notes.txt` 有什麼變化。

## 範例程式做了什麼？

執行 `read_file_practice.py` 後，程式會：

1. 開啟同資料夾中的 `sample.txt`。
2. 讀取並印出全部文字。
3. 再逐行印出內容，並計算行數。

你可以從這支程式開始，逐步修改並完成上面的練習題。
