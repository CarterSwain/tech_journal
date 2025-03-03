Tech Journal 

A personal learning log for documenting your coding journey. Built with Django, this app helps users track what they learn, organize entries by topic, and reflect on their progress.

🚀 Features:

📝 Create & Manage Entries – Log your daily coding experiences.

📂 Organize by Topics – Categorize your entries for easy reference.

👤 User Authentication – Secure personal journal with login/signup.

📊 Progress Reflection – Track your learning over time.

🛠 Tech Stack

Backend: Django, PostgreSQL

Frontend: HTML, CSS, Bootstrap

Deployment: Platform.sh

🏗 Installation & Setup

Clone the repository:

git clone https://github.com/yourusername/tech_journal.git
cd tech_journal

Create and activate a virtual environment:

python -m venv ll_env
source ll_env/bin/activate  # Mac/Linux
ll_env\Scripts\activate  # Windows

Install dependencies:

pip install -r requirements.txt

Run database migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

Access the app:

Open http://127.0.0.1:8000/ in your browser.

Deployment on Platform.sh (See Platform.sh docs for more details)..
To deploy your project:

platform push

For troubleshooting, check logs:

platform logs 

📚 Acknowledgment
This project was inspired by Python Crash Course by Eric Matthes. The book provided a strong foundation for Django and web development, shaping this learning log application. 📖✨

🤝 Contributing
Have suggestions or want to improve the app? Feel free to fork, create a PR, or open an issue! 

📜 License
MIT License – Feel free to use and modify this project.
