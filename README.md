# API_Challenge

## Pre Requisites

Before running the API, ensure you have the following installed:
- **Python 3.8 or higher**
- **pip** (Python package installer)
- **Postman** (for testing the API)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine:
git clone git@github.com:gdal19/API_Challenge.git
cd API_Challenge

### 2.Set up virtual environment
#### On macOS/Linux
python3 -m venv venv
source .venv/bin/activate

#### On Windows
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install flask requests

## Running the API
### 1. Activate the virtual environment
#### On macOS/Linux
source .venv/bin/activate

#### On Windows
venv\Scripts\activate

### 2. Run the script
python3 main.py

## Testing
Testing can be done on the local host (URL found in terminal) or through Postman. If you are making a request that uses JSON, it must be tested through Postman (steps below).
### 1. Create a new Request in Postman
Can be done by clicking the "+" button.

### 2. Go in "Body"
Select "raw" and on the drop down at the right choose "JSON".

### 3. Go to "Headers"
Type "Content-Type" under "Key". Type "application/json" under "value".

### 4. Go back to "Body"
Now you can add the JSON that you want to use to make the request.