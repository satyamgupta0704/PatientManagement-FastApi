# PatientManagement-FastApi

A REST API for managing patient records built with FastAPI.

## Features

- View all patients
- View patient by ID
- Search patients by name
- RESTful API endpoints
- JSON data storage

## API Endpoints

- `GET /`: Welcome message
- `GET /view`: Get all patients
- `GET /patient/{patient_id}`: Get patient by ID
- `GET /search?name={name}`: Search patients by name

## Getting Started

### Prerequisites

- Python 3.12+
- FastAPI
- Uvicorn

### Installation

1. Clone the repository
```sh
git clone https://github.com/yourusername/PatientManagement-FastApi.git
cd PatientManagement-FastApi
```

2. Create and activate virtual environment
```sh
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

3. Install dependencies
```sh
pip install fastapi uvicorn
```

### Running the Application

Start the server with:
```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

FastAPI provides automatic interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Data Structure

Patient data is stored in `patients.json` with the following structure:

```json
{
    "patient_id": {
        "name": "Patient Name",
        "age": "Patient Age",
        "gender": "Patient Gender"
    }
}
```
