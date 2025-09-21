# 🧮 HW2 Team Calculator

> A simple Python calculator that evaluates mathematical expressions in the format: `number operator number`.

---

## 📌 Description

This repository contains a team-developed implementation of a basic calculator as part of a homework assignment.  
The program accepts an expression via `input()`, for example:  

`5 + 3`

and prints the result of the calculation.

Supported operations: `+`, `-`, `*`, `/`.

Each mathematical operation is implemented in a separate function:  
- `add(x, y)` — addition  
- `sub(x, y)` — subtraction  
- `mul(x, y)` — multiplication  
- `div(x, y)` — division (with error handling for division by zero)  

The main logic for parsing and routing the expression is handled in the `main()` function.

## ⚠️ Input Errors

The calculator validates your input and will show error messages in the following cases:

- Missing spaces:  
  `5+3` → Error: the expression must be in the format `<number> <operator> <number>`

- Comma as decimal separator:  
  `3,5 + 2` → Error: use a dot for the decimal part, not a comma.

- Unsupported operator:  
  `5 ^ 2` → Error: operator '^' is not supported. Available: +, -, *, /

- Division by zero:  
  `7 / 0` → Error: Division by zero is not allowed

---

## 👥 Development Team

| Contributor         | Contribution                              |
|---------------------|-------------------------------------------|
| Natalia Laskina     | `main()` — main logic                     |
| Daria Bobrova       | `add()` — addition                        |
| Vadim Bolshakov     | `sub()` — subtraction                     |
| Nikita Maksimov     | `mul()` — multiplication                  |
| Artem Stetoi        | `div()` — division, `main()`, `parse_number()` |

---

## 🚀 How to Use

### Requirements:
- Python 3.6 or higher

### Running the Program:

1. Clone the repository (if not already done):
   ```bash
   git clone -b HW2_Laskina https://github.com/NataliaLaskina/HW2_NBLaskina.git

2. Navigate to the project folder:
   ```bash
   cd HW2_NBLaskina
3. Run the calculator:
   ```bash
   python HW2_Laskina/calculator.py
4. Enter an expression in the format:
   ```bash
   <number> <operator> <number>

   #Example: 10 - 4
5. The program will output the result:
   6

📂 Project Structure

- `HW2_NBLaskina/` — root folder
  - `HW2_Laskina/` — main project folder
    - `calculator.py` — main script with 6 functions:
      - `add(x, y)`
      - `sub(x, y)`
      - `mul(x, y)`
      - `div(x, y)`
      - `parse_number(token)`
      - `main()`
  - `imgs/` — folder for project screenshots 
  - `README.md` — this file

✨ Completed as part of a course assignment. All team members contributed equally to the development.

![Разработчики за работой](imgs/my-image.jpg)