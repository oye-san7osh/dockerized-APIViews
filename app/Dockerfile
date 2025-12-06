# Use an official python runtime as a parent image
FROM python:3.11-slim

# Prevents python from writing .pye file
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents python from buffering stdout & stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project file into container
COPY . /app/

# Expose port (for Django)
EXPOSE 8000

# Run entrypoints script
ENTRYPOINT [ "/app/entrypoint.sh" ]

# Run the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
