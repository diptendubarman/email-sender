FROM python:3.10-slim

WORKDIR /usr/src

# Copy only the required files
COPY ./app /usr/src/app
COPY ./requirements.txt /usr/src/requirements.txt
COPY ./entry.sh /usr/src/entrypoint.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for the FastAPI server
EXPOSE 8000

# Run the Uvicorn server
ENTRYPOINT [ "/usr/src/entrypoint.sh" ]  
