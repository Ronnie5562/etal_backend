# etal_backend

A Django backend project with cloud storage, email functionality, and database configuration.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (recommended)
- Git

## Getting Started

### 1. Clone the Repository

```bash
git clone <repository-url>
cd etal_backend
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Copy the example environment file and configure your credentials:

```bash
cp .env.example .env
```

Open `.env` and update the following variables:

#### Django Settings
- `SECRET_KEY`: Generate a secret key using `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- `DEBUG`: Set to `True` for development, `False` for production

#### SMTP Server (Email Configuration)
- `EMAIL_USE_TLS`: Set to `True` to use TLS
- `EMAIL_HOST`: Your SMTP server (e.g., `smtp.gmail.com`)
- `EMAIL_HOST_USER`: Your email address
- `EMAIL_HOST_PASSWORD`: Your email password or app-specific password
- `EMAIL_PORT`: SMTP port (usually `587` for TLS)

#### Cloudinary (Media Storage)
- `CLOUDINARY_CLOUD_NAME`: Your Cloudinary cloud name
- `CLOUDINARY_API_KEY`: Your Cloudinary API key
- `CLOUDINARY_API_SECRET`: Your Cloudinary API secret

Get these credentials by signing up at [Cloudinary](https://cloudinary.com/)

#### Database Configuration
- `USE_DEFAULT_DATABASE`: Set to `True` to use SQLite (default), `False` to use Neon PostgreSQL
- `DATABASE_URL`: Your Neon PostgreSQL connection string (only needed if `USE_DEFAULT_DATABASE=False`)

Get Neon credentials by signing up at [Neon](https://neon.tech/)

### 5. Database Setup

Run migrations to set up your database:

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
etal_backend/
├── manage.py
├── requirements.txt
├── .env.example
├── .env (create this)
└── [other Django apps and files]
```

## Common Commands

```bash
# Make migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files (for production)
python manage.py collectstatic

# Run tests
python manage.py test
```

## Troubleshooting

### Database Connection Issues
- If using Neon, ensure your `DATABASE_URL` is correctly formatted
- Check that your IP is whitelisted in Neon dashboard

### Email Issues
- For Gmail, you may need to use an [App Password](https://support.google.com/accounts/answer/185833)
- Ensure "Less secure app access" is enabled if not using app passwords

### Cloudinary Issues
- Verify your credentials are correct
- Check that your Cloudinary account is active

## Contributing

1. Create a new branch for your feature: `git checkout -b feature-name`
2. Make your changes and commit: `git commit -m "Description of changes"`
3. Push to the branch: `git push origin feature-name`
4. Submit a pull request

## Security Notes

- Never commit your `.env` file to version control
- Keep your `SECRET_KEY` and API credentials secure
- Use environment-specific settings for production deployment
