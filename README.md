# My Personal Portfolio (Django)

Welcome to my personal portfolio! This project showcases my skills, projects, and professional experiences, built with Django.

## Features

- **Portfolio Showcase**: Displays detailed descriptions of my projects.
- **Responsive Design**: Optimized for mobile and desktop views.
- **Contact Form**: Users can reach out directly through a built-in form.
- **Dynamic Animations**: Smooth animations for better user interaction.

## Installation

To run this Django portfolio locally, follow these steps:

### Prerequisites

- [Python](https://www.python.org/) (version 3.x)
- [Django](https://www.djangoproject.com/) (version 3.x or higher)
- A modern web browser (Chrome, Firefox, Safari)
- [Node.js](https://nodejs.org/) (for frontend dependencies if applicable)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/logotommiber/Personal-Portfolio.git
2. Navigate into the project directory:
   ```sh
   cd personal-portfolio\myportfolio
3. Set up a virtual environment:
   ```sh
   python -m venv venv
4. Activate the virtual environment:
   ### On Windows
       
       venv\Scripts\activate
    ### On macOS/Linux
    ```sh
    source venv/bin/activate


5. Apply database migrations:
    ```sh
    python manage.py migrate
6. Start the Django development server:
    ```sh
    python manage.py runserver

