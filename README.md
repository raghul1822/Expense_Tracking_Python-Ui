# Expense Tracker (CLI Simulation)

A professional Python-based expense tracker project inspired by a **Figma-designed** mobile finance interface. This project simulates the core logic of a modern expense tracking application and is structured as a strong foundation for building a future web application.

The project combines:
- **Python** for application logic and CLI simulation
- **Figma** for interface planning and design thinking
- **Icons and visual assets** stored in the project folder for UI consistency in future frontend development

| Home | Analytics – Overview | Analytics – Breakdown | Goals |
|---|---|---|---|
| Dashboard with balance & recent transactions | Income/Expense summary + trend charts | Category-wise spending breakdown | Savings goals with progress tracking |

Project Purpose

This project is more than a basic command-line app. It is designed as a backend and workflow simulation of a finance product, helping translate a Figma UI concept into working Python application logic.

It is useful for:
- Practicing Python application structure and state management
- Converting a Figma design into functional software logic
- Preparing the project for future expansion into a web application
- Demonstrating product thinking, not just coding

## Features

- **Dashboard Overview** — Displays current balance and recent transactions.
- **Transaction Logging** — Add income and expense entries across multiple categories.
- **Analytics Breakdown** — Review spending or income by category using percentage summaries and text-based bar visuals.
- **Goal Tracking** — Manage savings goals with progress, target amount, and deadlines.
- **Design-Ready Structure** — Built with future UI integration in mind using Figma assets and planned icon usage.

## Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,figma" />
</p>

- **Python 3**
- **Figma** for UI/UX design reference
- **CLI Simulation** for application logic testing

## Getting Started

### Prerequisites
- Python 3.7+

### Run it

```bash
git clone https://github.com/<your-username>/expense-tracker.git
cd expense-tracker
python3 expense_tracker.py
```

### Usage

You'll see a main menu like this:

```
📱 APP NAVIGATION MENU:
[1] Log New Transaction (Expense/Income)
[2] Analytics & Category Breakdown
[3] Financial Goals Tracker
[4] Exit App Simulation
```

Just enter the number for the action you want, and follow the prompts.

## Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py          # Main Python source code
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies (if any)
│
├── assets/
│   ├── Home.png                # Home screen screenshot from Figma/app reference
│   ├── dashboard.png           # Dashboard UI image
│   ├── analytics.png           # Analytics screen image
│   ├── goals.png               # Goals tracker image
│   └── icons/                  # Icons used from Figma or exported assets
│
└── .gitignore                  # Optional
```

## Roadmap

- [ ] Add persistent storage for transactions and goals
- [ ] Export icons directly from Figma into the assets folder
- [ ] Convert CLI features into a web interface
- [ ] Create API endpoints for transaction and goal management
- [ ] Add charts and visual analytics in the web version
- [ ] Improve validation and error handling

## License

This project is open source — Feel Free to use and modify it.
