# iNote - Take Your Note

## Overview

iNote is a simple and user-friendly note-taking web application built using FastAPI and Jinja2 templates. It allows users to create, edit, delete, and manage their notes efficiently. The application also supports marking notes as important and provides a clean and responsive user interface using Bootstrap.

## Features

- Create new notes with a title, description, and an optional "Important" flag.
- View a list of all notes.
- Edit existing notes inline.
- Delete notes.
- Responsive design using Bootstrap for a seamless experience across devices.

## Project Structure

```
FastAPI/
├── index.py                # Main entry point of the application
├── config/
│   └── db.py              # Database configuration and connection
├── learning/
│   ├── main.py            # Learning and testing FastAPI features
│   ├── pydantictest.py    # Pydantic model testing
│   └── pythontypes.py     # Python type hints and examples
├── models/
│   └── note.py            # Database models for notes
├── routes/
│   └── note.py            # API routes for note operations
├── schemas/
│   └── note.py            # Pydantic schemas for request and response validation
├── static/
│   └── style.css          # Custom CSS styles
├── templates/
│   └── index.html         # HTML template for the application
└── README.md              # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FastAPI
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn index:app --reload
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

## Dependencies

- FastAPI
- Jinja2
- Uvicorn
- Bootstrap (via CDN)

## How to Use

1. Open the application in your browser.
2. Add a new note by filling in the title, description, and marking it as important if needed.
3. View your notes in the "Your Notes" section.
4. Edit or delete notes directly from the list.

## Future Enhancements

- Add user authentication and authorization.
- Implement search functionality for notes.
- Add support for file uploads.
- Integrate with a database like PostgreSQL or MongoDB.
- Add API documentation using FastAPI's built-in OpenAPI support.

