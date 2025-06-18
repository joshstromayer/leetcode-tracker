# � LeetCode Tracker Template

This repository is a simple and clean personal tracker for solving LeetCode problems. It automatically generates:

- A folder for each LeetCode problem in `swe/leetcode/`
- A folder for each day you solve problems in `swe/leetcode_progress/YYYY-MM-DD/`
- A script that lets you input a problem number and paste your code once — it will be saved to both folders automatically.

-----

🚀 Getting Started

1. Fork the Repository
Click the **Fork** button on GitHub to create your own copy.

2. Clone Your Fork

git clone https://github.com/YOUR_USERNAME/leetcode-tracker.git
cd leetcode-tracker-template

-----

✅ Daily Workflow
After solving a problem:

1. Run the script

2. Enter the problem number

3. Paste your solution when prompted

4. Commit and push:

git add .
git commit -m "Solved problem 1234 – Two Sum"
git push

-----

📝 Usage
To log a new problem solution, run the script:

"python swe/script.py"

The script will:

- Ask for a LeetCode problem number (e.g. 1)
- Ask you to paste your solution code
   
- Automatically retrieve the problem title and slug
- Save your solution to both:

swe/leetcode/XXXX-title-slug.py
swe/leetcode_progress/YYYY-MM-DD/XXXX-title-slug.py

Example filename: swe/leetcode/0001-two-sum.py

📂 Folder Structure
text
swe/
├── data.csv                    # Contains LeetCode problem metadata
├── leetcode/                   # All problems with empty templates or your solutions
├── leetcode_progress/          # Your dated solutions
└── script.py                   # The main script to run

-----

💡 Features
Automatically creates files for all problems in the LeetCode dataset

One command to log your daily progress and keep everything in sync

Clean structure for showcasing your GitHub activity and portfolio

Zero manual file management once set up

-----

🙌 Contributing
This repo is designed for personal use, but improvements and pull requests are welcome if you'd like to extend its functionality.

-----

🧠 Optional Enhancements (Coming Soon Ideas)
Daily streak tracker

Web dashboard or markdown summary generator

Leaderboard for those using the template via GitHub API

Happy coding!
