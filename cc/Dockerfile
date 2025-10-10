# Step 1: Use an official Python runtime as a base image
FROM python:3.10-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of your project code
COPY . .

# Step 5: Expose the port Flask will run on
EXPOSE 5000

# Step 6: Command to run your Flask app
CMD ["python", "app.py"]
