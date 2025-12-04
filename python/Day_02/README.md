# Day 2: Working With Data Types in Python

**Date:** 04/12/2025

---

## Concepts Learned
* **Data Types:** Understanding the primitive data types in Python: Strings, Integers (`int`), Floats (`float`), and Booleans (`bool`).
* **Numbers:** Working with numerical data and understanding the difference between whole numbers (Integers) and decimal numbers (Floating Point Numbers).
* **Operations:** Performing mathematical calculations using arithmetic operators like `+`, `-`, `*`, `/`, and exponents `**`.
* **Type Conversion:** Converting values from one data type to another (Casting) using functions like `str()`, `int()`, and `float()`.
* **f-Strings:** Simplifying string formatting by embedding variables and expressions directly inside string literals using `f"..."`.


## Today's Project: Tip Calculator
**Description:**
A CLI (Command Line Interface) program that helps groups split a bill. The user inputs the total bill amount, the desired tip percentage (e.g., 10, 12, or 15), and the number of people splitting the bill. The program then calculates the precise amount each person owes.
### Features
* **User Input:** Accepts distinct inputs for the bill total, tip percentage, and group size.
* **Math Operations:** Calculates the total tip and adds it to the base bill before dividing.
* **Formatting:** Uses f-Strings to round the final result to strictly two decimal places (e.g., $12.50 instead of $12.5), solving common floating-point formatting issues.
