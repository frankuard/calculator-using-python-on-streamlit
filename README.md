# Streamlit Calculator

A simple **web-based calculator** built with **Streamlit**.  
It supports basic arithmetic operations like **Addition, Subtraction, Multiplication, and Division**, including error handling for division by zero.  

---

## ⚙️ How It Works

1. **logic.py**  
   Contains the core calculation functions:
   - `add(a, b)` → Returns the sum of `a` and `b`.
   - `subtract(a, b)` → Returns the difference.
   - `multiply(a, b)` → Returns the product.
   - `divide(a, b)` → Returns the quotient. Handles division by zero.

2. **main.py**  
   - Loads custom CSS for styling.
   - Accepts user input for two numbers and an operator.
   - Calls the appropriate function from `logic.py` based on the selected operator.
   - Displays the result in the browser.
   - Handles errors like division by zero and invalid operations.

---

## 🎨 Styling

The app uses `style/style.css` to enhance input boxes, buttons, and result display.  
Custom classes are applied for headings, input labels, buttons, and results.

---

## 🚀 How to Run

1. Install Streamlit if you haven’t already:

```bash
pip install streamlit
```

2. Run the app:
```bash
streamlit run main.py
```
---

## 👤 Author

**Roshan Karki**  
- GitHub: [Frankuard](https://github.com/frankuard) 
- LinkedIn: [Roshan Karki](https://www.linkedin.com/in/roshan-karki-98188837b)   
- Email: roshankarki4956@gmail.com 

---

⭐️ If you like this project, consider giving it a star on GitHub!

