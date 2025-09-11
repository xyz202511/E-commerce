🛍️ E-Commerce Flask App – Setup & Usage Guide
Welcome to the E-Commerce Flask App! This guide will walk you through setting up the project, running it locally, and using both admin and user functionalities without conflicts.

⚙️ Setup Instructions
1. Enable Script Permissions (Windows Only)
If you're on Windows and using PowerShell, run this command to allow virtual environment activation:

powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
2. Create Virtual Environment
bash
python -m venv venv
Activate it:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3. Install Dependencies
Make sure you're in the project root directory, then run:

bash
pip install -r requirements.txt
4. Run the Application
bash
python app.py
The app will start on http://localhost:5000.

👨‍💼 Admin Usage Flow
Access Admin Dashboard

Visit: http://localhost:5000/dashboard

Log in with admin credentials

Add Products

Use the dashboard interface to add product details and images

Logout Immediately After Admin Tasks

Always log out after admin actions to prevent session conflicts with user flows

👤 User Usage Flow
Register a New User

Visit: /register

Fill in valid username, email, and password

Log In as User

Visit: /login

Access user features like:

View products

Add to cart

Checkout

Submit reviews

Check Updated Products

Newly added products by admin will appear in the user interface

🚨 Important Notes
Admin and User roles must remain isolated

Admin should always log out before switching to user mode

Avoid accessing user routes while logged in as admin

Session Conflicts

If admin accesses user routes without logging out, it may cause cart/order issues

Role-Based Access

Admins should only use /dashboard and related management routes

Users should only interact with /cart, /checkout, /orders, etc.

📦 Dependencies
Flask==3.0.0
Flask-Login==0.6.3
Flask-WTF==1.2.1
Flask-SQLAlchemy==3.1.1
WTForms==3.1.1
email-validator==2.0.0.post2
gunicorn==21.2.0
Flask-Migrate==4.0.5
