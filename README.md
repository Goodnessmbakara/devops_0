# Number Classification API

A REST API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies various number properties (armstrong, odd/even)
- Calculates digit sum
- Retrieves fun facts about numbers from Numbers API

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Goodnessmbakara/hng12.git
cd number-classifier
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python run.py
```

The API will be available at `http://localhost:5000`

## API Documentation

### Classify Number

Get mathematical properties and fun facts about a number.

**Endpoint:** `GET /api/classify-number`

**Parameters:**
- `number` (required): The integer to analyze

**Success Response (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Error Response (400 Bad Request):**
```json
{
    "number": "invalid",
    "error": true,
    "message": "Invalid number format"
}
```

## Development

- The application uses Flask for the web framework
- CORS is enabled for cross-origin requests
- Number facts are retrieved from the Numbers API (http://numbersapi.com)

## Testing

To test the API, you can use curl:

```bash
curl "http://localhost:5000/api/classify-number?number=371"
```

Or use a tool like Postman to make GET requests to the endpoint.
