# Sales Tracking System

##  Domain
 Sales Operations

## Problem Statement
Build a system that manages products in inventory and tracks their sales.
The system must:
- Store product details (ID, Name, Price, Stock).
- Record sales transactions.
- Update stock automatically after each sale.
- Prevent overselling with proper error handling.
- Generate reports on inventory and sales.

---

## Topics Covered
- Python basics (loops, conditionals, functions)
- Object-Oriented Programming
- Exception handling
- Modular programming
- Reports & Summaries
- (Optional) Database Integration (SQLite/MySQL)

---

## Project Structure

sales_system/
│── main.py # Menu-driven program
│── product.py # Product class
│── sale.py # Sale class
│── inventory_manager.py # Handles inventory operations
│── sales_manager.py # Handles sales operations
│── reports.py # Reporting module
│── exceptions.py # Custom exceptions
│── README.md # Project documentation


## Student Task Breakdown
- **Student A (Inventory):** `product.py`,`inventory_manager.py`
- **Student B (Sales):** `sale.py`, `sales_manager.py`
- **Student C (Reports & UI):** `reports.py`, `exceptions.py`, `main.py`

## How to Run
1. Create this repository.
2. Open a terminal and navigate into the project folder.
3. Run the program:
   python main.py
