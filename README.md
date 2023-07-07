# ToDo List App

This is a simple web application for managing a todo list. It allows users to sign up, log in, add tasks, update tasks, and delete tasks.

## Features

- **User authentication:** Users can sign up for an account and log in to access their todo list.
- **Task management:** Users can add tasks with a title and description, update existing tasks, and delete tasks.
- **User-specific tasks:** Each user has their own set of tasks that are only accessible to them.

## File Structure

The file structure of the application is as follows:
  **ToDo List**
        **└──├── app.py** 
		   **├── requirements.txt** 
		   **├── templates** 
		     **└──signin.html** 
			 **├── signup.html** 
			 **└── tasks.html** 
		   **├── static** 
			 **└── style.css** 
		   **├──  instance**
			 **└── todos.db** 

## File Descriptions

-   **`app.py`:** The main Flask application file that contains the core logic and routes for the todo list application.
-   **`requirements.txt`:** A file that lists the dependencies required for running the application.
-   **`templates/`:** A directory that contains the HTML templates used for rendering the different pages of the application.
    -   **`signin.html`:** The sign-in page template.
    -   **`signup.html`:** The sign-up page template.
    -   **`tasks.html`:** The task list page template.
-   **`static/`:** A directory that contains static assets such as CSS stylesheets and JavaScript files.
    -   **`style.css`:** The CSS styles for the HTML templates.
-   **`todos.db`:** The SQLite database file that stores the tasks and user information.

## Getting Started

To run the News Classifier web application, follow these steps:

* Clone the repository or download the source code files.
*  Navigate to the project directory: ```cd ToDo List```

* (Optional) Create a virtual environment: ```python3 -m venv venv``` (for Linux/macOS) or ```python -m venv venv``` (for Windows).

* Activate the virtual environment:

     * For Linux/macOS: ```source venv/bin/activate```

     * For Windows: ```venv\Scripts\activate.bat```

* Install the required packages: ```pip install -r requirements.txt```

* Run the application: ```python app.py```

* Open a web browser and visit http://localhost:5000 to access the ToDo List application.
## Usage
* Create a new account by signing up with your email address, username, and password.
    
* Log in with your credentials to access your todo list.
    
* On the task list page, you can add new tasks by providing a title and description in the input fields and clicking the "Add Task" button.
    
* Existing tasks will be displayed with their title and description. You can update a task by clicking the edit icon and delete a task by clicking the delete icon.
    
*  To log out, click the "Logout" link.


## requirements.txt
```
- Flask

- Flask-Login

- SQLAlchemy

- Flask-WTF
```


## Configuration

The application uses SQLite as the default database. You can change the database configuration in the `app.py` file:

```app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'```

Feel free to modify this configuration to use a different database system if needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request. Make sure to follow the existing code style and include tests for any new features or bug fixes.

## License

This project is licensed under the MIT License. 
