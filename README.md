```markdown
# Customer Management API

This is a Django REST API designed to manage customer information for businesses. The API allows you to store and retrieve data related to customers, their businesses, and locations.

## Features

- **Customer Management**: Store customer details such as name, contact information, date of birth, and nationality.
- **Business Management**: Store business details such as name, category, registration date, and location.
- **Location Management**: Store hierarchical location information, including county, sub-county, ward, building name.
- **Efficient Data Storage**: The API is designed to minimize server resource consumption by using optimized data models and relationships.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:

```
git clone https://github.com/brianmwevi/customer-management-api.git
```

2. Navigate to the project directory:

```
cd customer-management-api
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Apply the database migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

The following endpoints are available:

- `GET /api/counties/`: List all counties
- `POST /api/counties/`: Create a new county
- `GET /api/counties/{id}/`: Retrieve a specific county
- `PUT /api/counties/{id}/`: Update a specific county
- `DELETE /api/counties/{id}/`: Delete a specific county
- ... (Similar endpoints for sub-counties, wards, business categories, and customers)

For detailed information about the request and response formats, please refer to the API documentation.

## Contributing

No need for contribution on this project.

## License

Apache License
```
