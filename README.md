

# AI-Powered Content Generator

This project is an AI-Powered Content Generator web application built with Django and Python. The application allows users to generate content based on a topic and desired tone. The front end is styled using Bootstrap for a modern, responsive design, and JavaScript is used for form validation and interactivity.

## Features

- **Topic-Based Content Generation**: Users can input a topic, and the AI will generate content related to that topic.
- **Tone Selection**: Users can choose the tone of the generated content (Formal, Casual, or Informative).
- **Responsive Design**: The form and interface are fully responsive, ensuring a seamless experience on all devices.
- **Client-Side Validation**: JavaScript is used to ensure the topic field is filled before submission.

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Python**: The programming language used for backend logic and AI content generation.
- **Bootstrap**: A powerful front-end framework for faster and easier web development with a focus on responsive design.
- **JavaScript**: Enhances user experience by providing form validation and interactivity.

## Installation

To get started with the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-powered-content-generator.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd ai-powered-content-generator
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the application**:
   - Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. Enter a topic in the "Topic" field.
2. Select the tone of the content from the dropdown menu.
3. Click the "Generate Content" button.
4. The AI will process the request and generate content based on your input.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:
- **Ahmed Hussain** - ahmedhn400@gmail.com
