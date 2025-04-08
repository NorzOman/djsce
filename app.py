from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple College - Home</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 0; padding: 0; }
            header { background-color: #004080; color: white; padding: 20px; text-align: center; }
            nav { background-color: #0066cc; padding: 10px; text-align: center; }
            nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
            .content { padding: 20px; }
            footer { background-color: #222; color: white; text-align: center; padding: 10px; margin-top: 20px; }
            .btn { background-color: #ff6600; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <header>
            <h1>Simple College</h1>
            <p>Empowering the Future, One Student at a Time</p>
        </header>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About Us</a>
            <a href="/courses">Courses</a>
            <a href="/contact">Contact</a>
        </nav>
        <div class="content">
            <h2>Welcome to Simple College!</h2>
            <p>We offer a variety of courses designed to help you achieve your academic and professional goals.</p>
            <p>Click below to visit our special page (vulnerable to open redirect):</p>
            <a href="/redirect?url=http://malicious.com" class="btn">Go to Special Page</a>
        </div>
        <footer>
            <p>&copy; 2025 Simple College. All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''

# About page
@app.route('/about')
def about():
    return '''
    <h2>About Simple College</h2>
    <p>Founded in 1990, Simple College is committed to providing quality education and fostering academic excellence.</p>
    <a href="/">Back to Home</a>
    '''

# Courses page
@app.route('/courses')
def courses():
    return '''
    <h2>Our Courses</h2>
    <ul>
        <li>Computer Science</li>
        <li>Business Administration</li>
        <li>Electrical Engineering</li>
        <li>Psychology</li>
        <li>Art and Design</li>
    </ul>
    <a href="/">Back to Home</a>
    '''

# Contact page
@app.route('/contact')
def contact():
    return '''
    <h2>Contact Us</h2>
    <p>Email: info@simplecollege.com</p>
    <p>Phone: +123-456-7890</p>
    <a href="/">Back to Home</a>
    '''

# Vulnerable open redirect
@app.route('/redirect')
def redirect_vulnerable():
    target_url = request.args.get('url')
    if target_url:
        return redirect(target_url)
    return 'No URL provided.'

if __name__ == '__main__':
    app.run(debug=True)

