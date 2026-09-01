# [Codewars Python](https://www.codewars.com/kata/search/python?beta=false) in VS Code

[![Download](https://img.shields.io/badge/Download-gray?style=for-the-badge&logo=github)](https://github.com/pokvi8/leetcode-and-codewars-in-vscode/releases/latest/download/start.py)

This repository allows you to solve Codewars problems in VS Code.

## Repository Structure

- **Numbered folders** (e.g., `8/`, `7/`, `6/`, etc.) correspond to the rank (kyu) of the Codewars kata.  
  The smaller the number, the harder the kata.
- **Python files placed outside the `solutions/` folder will not be run through the Codewars system.**

## Solution Formatting Rules

To ensure your solutions work correctly in the automated environment, please follow these rules:

1. **Use the `result` variable instead of `return`**  
   Any value that should be returned from your solution must be stored in the variable `result`.  
   *Example:*
   ```python
   # Instead of:
   def solution(x: int) -> int:
       return x * 2

   # Write:
   result = x * 2
   ```

2. **For recursive solutions, use the `results()` function**  
   If your solution uses recursion, use the built-in `results()` function (its implementation is provided by the environment).  
   *Example:*
   ```python
   # Instead of:
   def factorial(x: int) -> int:
       return x < 2 or x * factorial(x - 1)

   # Write:
   result = x < 2 or x * results(x - 1)
   ```

3. **File template**  
   The following import suppresses `NameError` for parameters in your code and adds parameter hints. Hover over a parameter to see which values it accepts.  
   *Example:*
   ```python
   from solution import results, x, y  # type:ignore
   ```

4. **Parameter hints**  
   The expected output must be provided in this sequence.  
   *Example:*
   ```python
   results: Literal[1, 7, 2, 42, -1, -7, -2, -42, 0, 852]
   ```
   The parameter values that produce those results (also in the same order)  
   *Example:*
   ```python
   x: Literal[-22, 595, 932, -273, 630, -218, -424, 600, -537, -653]
   y: Literal[725, -920, -69, 385, -640, 608, 407, 925, -711, 497]
   ```
   That means:  
   *Example:*
   ```python
   result: Literal[7]
   x: Literal[595]
   y: Literal[-920]
   ```

5. **Do not delete the comment with the task link**  
   At the top of each solution file, there is a comment containing the kata URL. This comment is **mandatory** – it is used to automatically fetch the kata data if the local kata info file has been deleted.

6. **GitHub**  
   If you want to save your solutions to GitHub, the `.gitignore` is already configured.  
   The following will be saved to GitHub: `start.py`, the `solutions/` folder, and any files you create yourself.

## Note

`start.py` will install the Chromium driver for Playwright and the VS Code extension **Code Runner**.

## Launch

- `start.py` takes a kata URL and creates a Python file where you can solve that task.  
   *Example:*
   ```
   Codewars kata URL: https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
   ```
- To run your solution through the Codewars system, click the **Run Code** button.