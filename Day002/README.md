# 📅 Day 2 – Data Types, Operations & Tip Calculator Project 💰🐍

On Day 2 of my #100DaysOfCode with Python, I dove deep into how Python
handles different types of data. I learned how to convert between them, 
perform mathematical operations, and use f-strings for clean and readable 
output. I wrapped up with a project: a Tip Calculator that does the math so
I don’t have to at restaurants 🍽️.

---

## 🧠 What I Learned

### 🔡 Data Types in Python

1. **String** (`str`)
   - Any sequence of characters (in quotes).
   - Supports indexing/subscripting:
     ```python
     print("Hello"[0])  # Output: H
     print("Hello"[-1]) # Output: o
     ```

2. **Integer** (`int`)
   - Whole numbers without decimals.
     ```python
     print(123 + 456)  # Output: 579
     ```

3. **Float** (`float`)
   - Numbers with decimal points.
     ```python
     print(3.14)  # Output: 3.14
     ```

4. **Boolean** (`bool`)
   - Represents `True` or `False`.
     ```python
     print(True)
     print(False)
     ```

---

### 🔄 Type Conversion

- Use `int()`, `str()`, `float()` to convert between data types.
  ```python
  print(int("123") + int("456"))  # Output: 579
  name = input("Enter your name: ")
  print("Letters in name: " + str(len(name)))
