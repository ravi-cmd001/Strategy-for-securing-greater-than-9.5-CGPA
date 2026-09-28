# Strategy-for-securing-greater-than-9.5-CGPA
Strategy for securing greater than 9.5 CGPA....simple python code
CGPA Strategy Planner

A simple command-line Python program that calculates your expected CGPA from your expected grade points, checks it against a 9.5 target, and suggests which subjects to prioritise and how many extra study hours per week to put into each.

Features
Calculates the expected CGPA (credit-weighted average of grade points)
Labels your performance level (Excellent / Very good / Good / Needs Improvement)
Tells you whether the 9.5 CGPA target is achieved
If not achieved, shows how many additional weighted grade points you still need
Ranks subjects by study priority (highest potential gain first)
Suggests extra weekly study hours for each subject
Requirements
Python 3.x
No external libraries needed
How to Run
bash
python cgpa_strategy.py

(Replace cgpa_strategy.py with whatever you named the file.)

Inputs

The program first asks for the number of subjects, then for each subject:

Input	Description
Name	Name of the subject
Credits	Credit value of the subject (can be decimal)
Expected grade point	Grade point you expect to get, on a 0–10 scale
Available study hours/week	Hours you can spend on the subject per week
How It Works
1. Expected CGPA
CGPA = Σ (credit × grade point) / Σ credits
2. Performance Level
CGPA	Level
9.5 and above	Excellent
9.0 – 9.49	Very good
8.0 – 8.99	Good
Below 8.0	Needs Improvement
3. Target Check (9.5)

If the CGPA is below 9.5, the program shows the additional weighted points needed:

Additional points needed = 9.5 × total credits − current total weighted points
4. Study Priority

Each subject gets a priority score based on how much room for improvement it has:

Priority = credits × (10 − expected grade point)

Subjects are sorted from highest to lowest priority. A high-credit subject with a low grade appears at the top.

5. Study Strategy

Extra weekly study hours are suggested based on the priority score:

Priority score	Suggested extra hours/week
Greater than 3	2
Greater than 1 (up to 3)	1
1 or less	0
Sample Run
Enter number of subjects: 3

Subject 1
Name: Maths
Credits: 4
Expected grade point(0-10): 8
Available study hours/week: 6

Subject 2
Name: Physics
Credits: 3
Expected grade point(0-10): 9
Available study hours/week: 5

Subject 3
Name: English
Credits: 2
Expected grade point(0-10): 10
Available study hours/week: 3

========== CGPA ANALYSIS ==========
Expected CGPA: 8.78
Performance: Good
TARGET: 9.5 + NOT YET ACHIEVED
Additional weighted points needed: 6.5

========= STUDY PRIORITY ==========
1 . Maths | Grade: 8.0 |credits: 4.0 |Priority: 8.0
2 . Physics | Grade: 9.0 |credits: 3.0 |Priority: 3.0
3 . English | Grade: 10.0 |credits: 2.0 |Priority: 0.0

========== STRATEGY==========
Maths -Study 2 extra hour(s)/week
Physics -Study 1 extra hour(s)/week
English -Study 0 extra hour(s)/week
Code Structure
Function	Purpose
grade_level(g)	Returns a performance label for a given CGPA
cgpa_strategy()	Main function: takes input, calculates CGPA, prints the analysis, priority list and study strategy
Limitations and Possible Improvements
The available study hours/week value is collected but not yet used in the calculations. It could be used to cap or distribute the suggested extra hours.
There is no input validation (e.g. non-numeric input, grade points outside 0–10, or zero credits will cause errors or wrong results).
The 9.5 target and the priority thresholds (3 and 1) are hard-coded and could be made configurable.
Results could be saved to a file or shown in a table format.
