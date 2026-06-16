# 🚀 LolaFort

A GitHub Profile Analytics Dashboard built with Python, Streamlit, Plotly, and the GitHub REST API.

LolaFort transforms raw GitHub profile data into interactive visual insights, helping developers analyze repository activity, language usage, popularity metrics, and overall GitHub presence.

## Features

* GitHub Profile Lookup
* Profile Avatar Display
* Repository Statistics
* Language Distribution Visualization
* Top Repository Ranking
* Developer Score Calculation
* Interactive Dashboard
* Real-Time GitHub API Integration

---

## Architecture

```text
┌──────────────────────┐
│      Streamlit UI    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       app.py         │
│ Presentation Layer   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     analyzer.py      │
│ Analytics Engine     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   GitHub REST API    │
└──────────────────────┘
```

---

## Project Structure

```text
LolaFort/
│
├── app.py
├── analyzer.py
├── requirements.txt
└── README.md
```

---

## Tech Stack

* Python
* Streamlit
* Plotly
* Requests
* GitHub REST API

---

The application will be available at:

```text
http://localhost:8501
```

---

## Example Insights

* Followers Count
* Public Repository Count
* Developer Score
* Programming Language Distribution
* Top Starred Repositories

---

## Future Enhancements

* GitHub Contribution Analytics
* Commit Activity Tracking
* AI-Powered Profile Review
* Repository Comparison
* PDF Report Export
* Developer Ranking Algorithm

---

## Author

Developed by CodeDivaa

Built with Python ❤️
