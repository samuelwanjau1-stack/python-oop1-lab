# Python Object-Oriented Programming (OOP) - Bookstore Lab

## Overview
This lab demonstrates the implementation of Object-Oriented Programming (OOP) principles in Python. The goal was to build a digital model for a bookstore that handles "Book" and "Coffee" objects with specific attributes, validation rules, and methods.

## Features

### Book Class (`lib/book.py`)
- **Attributes**: `title` and `page_count`.
- **Validation**: Uses a setter to ensure `page_count` is an integer. If a non-integer is provided, it prints an error message.
- **Methods**: `turn_page()` which outputs a confirmation message.

### Coffee Class (`lib/coffee.py`)
- **Attributes**: `size` and `price`.
- **Validation**: Uses a setter to ensure `size` is strictly "Small", "Medium", or "Large".
- **Methods**: `tip()` which prints a thank-you message and increases the object's `price` by 1.

## Project Structure
```text
.
├── lib
│   ├── book.py            # Book class implementation
│   ├── coffee.py          # Coffee class implementation
│   └── testing            # Unit tests for both classes
├── pytest.ini             # Testing configuration
└── Pipfile                # Environment dependencies