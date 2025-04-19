# MongoDB Docker Environment

This repository provides a Dockerized environment for running a MongoDB instance, facilitating easy setup and management of MongoDB for development and testing purposes.

## Project Structure

The repository is organized as follows:

- `mongodb/` – Contains MongoDB configuration files and initialization scripts.
- `flask/` – Contains flask api.
- `nginx/` – Contains nginx configuration file.
- `web/` – Contains a HTML test page for the api.
- `docker-compose.yml` – Defines and manages the multi-container Docker application.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/voirinprof/mongodb_docker.git
   cd mongodb_docker
   ```


2. **Build and run the containers:**

   ```bash
   docker-compose up --build
   ```


3. **Access MongoDB:**

   - MongoDB will be accessible at `mongodb://localhost:27017`.
   - Use a MongoDB client or GUI (e.g., MongoDB Compass) to connect.

## Usage

This setup allows you to:

- Run a MongoDB instance in a Docker container.
- Easily manage the MongoDB service using Docker Compose.
- Customize MongoDB configurations as needed.
- Check the flask api providing a web service with the connected db (check `http://localhost`).

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).