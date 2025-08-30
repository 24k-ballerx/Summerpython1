# Someret College Portal

A modern, responsive school portal for Someret College built with Python Flask, featuring a beautiful sky blue and grey theme with background images.

## Features

- 🎨 **Modern Design**: Sky blue and grey theme with beautiful gradients and animations
- 📱 **Responsive**: Fully responsive design that works on all devices
- 🏫 **School Portal**: Complete portal with students, teachers, courses, and announcements
- 🔐 **Authentication**: Simple login system (demo credentials included)
- 📊 **Dashboard**: Statistics and overview of school data
- 📢 **Announcements**: News and updates section
- 📞 **Contact**: Contact form and information
- ✨ **Animations**: Smooth animations and transitions
- 🎯 **Interactive**: JavaScript-powered interactions

## Screenshots

The portal includes:
- Home page with hero section and features
- Students directory with profiles and courses
- Teachers directory with contact information
- Course catalog with details
- Announcements page
- Contact page with form
- Login system

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Summerpython1
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the portal**
   Open your browser and go to: `http://localhost:5000`

## Usage

### Demo Credentials
- **Username**: `admin`
- **Password**: `password`

### Navigation
- **Home**: Overview of the school with features and statistics
- **Students**: View student profiles, grades, and courses
- **Teachers**: Faculty directory with contact information
- **Courses**: Course catalog with details and enrollment
- **Announcements**: Latest news and updates
- **Contact**: Contact form and school information
- **Login/Logout**: Access restricted features

## Project Structure

```
Summerpython1/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── students.html     # Students page
│   ├── teachers.html     # Teachers page
│   ├── courses.html      # Courses page
│   ├── announcements.html # Announcements page
│   ├── login.html        # Login page
│   └── contact.html      # Contact page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Main stylesheet
    ├── js/
    │   └── script.js     # JavaScript functionality
    └── images/           # Image assets
```

## Features in Detail

### Design Theme
- **Primary Colors**: Sky blue (#87CEEB) and grey (#B0C4DE)
- **Background**: Gradient backgrounds with subtle patterns
- **Typography**: Modern Poppins font family
- **Animations**: Smooth hover effects and transitions

### Responsive Design
- Mobile-first approach
- Hamburger menu for mobile devices
- Flexible grid layouts
- Optimized for all screen sizes

### Interactive Elements
- Smooth scrolling navigation
- Hover effects on cards and buttons
- Form validation
- Flash messages
- Loading animations

## Customization

### Adding New Students
Edit the `students` list in `app.py`:
```python
students = [
    {
        'id': 4,
        'name': 'New Student',
        'grade': '9th',
        'gpa': 3.7,
        'courses': ['Mathematics', 'Science', 'English']
    }
]
```

### Adding New Teachers
Edit the `teachers` list in `app.py`:
```python
teachers = [
    {
        'id': 4,
        'name': 'Dr. New Teacher',
        'subject': 'Computer Science',
        'email': 'newteacher@someret.edu'
    }
]
```

### Modifying the Theme
Edit `static/css/style.css` to change colors:
```css
:root {
    --primary-color: #87CEEB;
    --secondary-color: #4682B4;
    --accent-color: #B0C4DE;
}
```

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For support or questions, please contact:
- Email: info@someret.edu
- Phone: (555) 123-4567

---

**Someret College Portal** - Excellence in Education, Innovation in Learning

