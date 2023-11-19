# Pricing Module

Brief project description.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-project.git
    ```
2. **Create a Virtual Environment:**
    ```bash
    cd your-project
    python -m venv venv
    ```
3. **Activate the Virtual Environment:**
    ```bash
        On Windows:
        venv\Scripts\activate
        On macOS/Linux:
        source venv/bin/activate
    ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    ```bash
    python manage.py makemigrattions
    python manage.py migrate
    ```

## Usage

1.  **Run the Development Server::**
    ```bash
    python manage.py runserver
    ```

2. **Access the Admin Interface:**

Visit http://localhost:8000/admin/ and log in with the superuser credentials, to craete pricing config

Visit http://localhost:8000/ to explore the product use case. 

# Use Case: Calculate Price for a Journey

## Overview

The application provides a feature to calculate the price for a journey based on various factors such as the total distance traveled, the day of the week, waiting time, and the total time taken in the journey.

## Steps

1. **Input Data:**
   - User provides the following input data:
     - **Total Distance Traveled (in kilometers):** The total distance covered during the journey.
     - **Day of the Week:** The day on which the journey is taking place.
     - **Waiting Time (in minutes):** The total time spent waiting during the journey.
     - **Total Time Taken (in minutes):** The overall time taken for the journey.

2. **Submit Data:**
   - User submits the input data through a form or API endpoint.

3. **Calculate Price:**
   - The application processes the input data to calculate the price for the journey.
   - The pricing algorithm considers factors such as distance, day of the week, waiting time, and total time taken.

4. **Display Result:**
   - The calculated price is displayed to the user.

## Example

Suppose a user wants to calculate the price for a journey:
   - Total Distance Traveled: 20 km
   - Day of the Week: Tuesday
   - Waiting Time: 15 minutes
   - Total Time Taken: 45 minutes

