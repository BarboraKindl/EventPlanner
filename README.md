# Event Planner

Event Planner is a comprehensive web application built with Django that allows users to create, manage, and attend events. It provides a user-friendly interface for event organization and participation.

## Features

- User Authentication:
  - User registration with email confirmation
  - Login and logout functionality
  - Password reset option

- User Profiles:
  - Customizable user profiles with bio, location, and profile picture
  - View and edit profile information

- Event Management:
  - Create, edit, and delete events
  - Set event details including title, description, date, time, and location
  - Assign resources to events
  - View event details and attendee list
  - Join or leave events as an attendee

- Location and Resource Management:
  - Add and manage event locations
  - Create and assign resources to events

- Search and Filtering:
  - Search events by title, description, or location
  - Filter events by date range or category

- Responsive Design:
  - Mobile-friendly interface for easy access on various devices

- API:
  - RESTful API for programmatic access to events, locations, and resources

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
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
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

1. Register a new account or log in with an existing one.
2. Complete your user profile with additional information.
3. Browse existing events or create a new event by clicking on the "New Event" button.
4. To create an event, fill in the event details, select a location, and assign any necessary resources.
5. View event details, including the attendee list, from the event list or detail page.
6. Join events you're interested in attending.
7. Manage your created events from your user dashboard.
8. Use the search functionality to find specific events.

## API Usage

The Event Planner provides a RESTful API for programmatic access:

- API endpoints:
  - `/api/events/`: List or create events
  - `/api/locations/`: List or create locations
  - `/api/resources/`: List or create resources
  - `/api/profiles/`: List or update user profiles

Refer to the API documentation for detailed usage instructions.

## Contributing

Contributions to the Event Planner project are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

Please ensure your code adheres to the project's coding standards and include tests for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.
