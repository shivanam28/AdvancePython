# 💸 ExpenseManager — Your Money, Your Rules.

A Python-powered personal finance tracker to keep your money moves in check. Track income, manage expenses, set budgets, and figure out where your money actually goes. 👀

Built from scratch as a hands-on Python project — because the best way to learn programming is to build something real.

## ✨ What's the Game Plan?

ExpenseManager is a console-based application designed to make personal finance tracking simple, organized, and practical.

**The mission:** Spend smarter, track better, and stay within budget. No more wondering where the money disappeared. 💀

## 🚀 Features

### 👤 User Management
- Create and manage user profiles.
- View, update, and delete account details.

### 💰 Income & Expense Tracking
- Record income and expenses.
- Organize transactions by category.
- Update, delete, and view transaction history.
- Search and filter transactions.

### 🎯 Budget Management
- Set monthly spending limits.
- Track remaining budgets.
- Get alerts when spending reaches 80% of the budget.
- Know when you're going over budget.

### 📊 Financial Insights
- Calculate total income and expenses.
- Track monthly savings.
- Get category-wise spending summaries.
- Identify your highest expense.
- Generate monthly financial reports.

### 💾 Data Persistence
- Store data using JSON files.
- Load saved records whenever the application starts.
- Handle missing files, invalid data, and unexpected errors.

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 🐍 |
| Storage | JSON |
| Libraries | `json`, `pathlib`, `datetime`, `os` |
| Programming | Object-Oriented Programming |
| Interface | Command-Line Interface |

## 🧠 What I'm Practising

Not just another CRUD project. This is my playground for getting better at Python.

- OOP — Classes, Objects, Inheritance, Encapsulation & Polymorphism
- Class methods, Static methods & Instance methods
- `*args` and `**kwargs`
- List and Dictionary Comprehensions
- Lambda Functions
- `map()`, `filter()` and `zip()`
- Decorators
- Modules and Packages
- File Handling and JSON
- Exception Handling
- Clean code and modular design

## 📂 Project Structure

```text
ExpenseManager/
│
├── main.py
├── data/
│   ├── users.json
│   └── transactions.json
│
├── models/
│   ├── user.py
│   └── transaction.py
│
├── services/
│   ├── expense_manager.py
│   └── budget_manager.py
│
└── utils/
    ├── file_handler.py
    └── decorators.py
```

## ⚡ Getting Started

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Enter the project directory**

```bash
cd ExpenseManager
```

**3. Run the application**

```bash
python main.py
```

No external dependencies needed for the initial version. Just Python and a little curiosity. 😉

## 🗺️ Build Roadmap

- [ ] Phase 1 — Basic user and transaction management
- [ ] Phase 2 — JSON-based data persistence
- [ ] Phase 3 — Monthly budget management
- [ ] Phase 4 — Financial reports and insights
- [ ] Phase 5 — Apply intermediate Python concepts
- [ ] Phase 6 — Refactor into clean modules and packages
- [ ] Phase 7 — Improve validation and error handling
- [ ] Phase 8 — Add extra features and polish

## 🔮 What's Next? — The Fun Stuff

The goal is to evolve ExpenseManager from a simple expense tracker into a personal finance companion. Here's what's on the wishlist:

### 🧠 1. Spending Personality
Discover your spending personality based on your transaction patterns.

- The Budget Boss 👑
- The Foodie 🍕
- The Impulse Shopper 🛍️
- The Silent Spender 👀

### 🔥 2. Savings Streaks & Achievements
Make saving money a little more fun.

- Track consecutive days of mindful spending.
- Earn badges for reaching savings milestones.
- Celebrate savings goals and achievements.

### 💬 3. Money Buddy
A friendly, rule-based financial assistant that gives contextual feedback.

- "Whoa! Your food expenses are up 30% this month."
- "You've got ₹2,000 left in your budget. Stay strong!"
- "Your savings game is getting better!"

### 👀 4. Where Did My Money Go?
A monthly financial recap with useful insights.

- Top spending category.
- Biggest purchase.
- Most expensive day.
- Monthly savings percentage.
- Spending comparison with previous months.

### 🎯 5. Main Character Goals
Set personal savings goals and track progress.

- Save for a new laptop 💻
- Plan a dream vacation ✈️
- Build an emergency fund 🛡️
- Track progress towards each goal.


## 💭 The Dev Note

This project is part of my journey to move beyond just learning Python syntax and start thinking like a developer.

The focus is on writing code that's clean, reusable, modular, and actually solves a problem.

**Learn it. Build it. Break it. Debug it. Make it better.**

*One project at a time. One bug at a time. 🚀*