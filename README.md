# Event Planner

Event Planner is a web application built with Django that allows users to create, manage, and attend events.

## Features

- User registration and authentication
- User profiles with customizable information
- Create and manage events
- View event details and attendee list
- Join events as an attendee

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/event-planner.git
   cd event-planner
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (admin) account:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

- Register a new account or log in with an existing one.
- Create new events by clicking on the "New Event" button.
- View event details and join events from the event list.
- Update your profile information in the user profile section.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
