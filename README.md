## Flask Application Design for Russian Language Teaching Website

### HTML Files

**1. Home.html:**
- The main page of the website.
- Contains a brief introduction to the website and a list of available lessons.

**2. Lesson1.html:**
- The first lesson on Russian grammar or vocabulary.
- Includes interactive exercises and quizzes to reinforce learning.

**3. Exercise1.html:**
- A page for Exercise 1 of Lesson 1.
- Provides a practice activity to test user understanding.

### Routes

**1. /:**
- Maps to the root URL and displays the **Home.html** page.

**2. /lesson1:**
- Maps to the URL for Lesson 1 and displays the **Lesson1.html** page.

**3. /exercise1:**
- Maps to the URL for Exercise 1 of Lesson 1 and displays the **Exercise1.html** page.

**4. /submit:**
- Maps to a URL where users can submit answers to exercises.
- Receives user input and provides feedback based on the correctness of the answers.

**5. /progress:**
- Maps to a URL where users can track their progress through the lessons.
- Displays a summary of completed lessons and exercises, and allows users to resume their learning from where they left off.