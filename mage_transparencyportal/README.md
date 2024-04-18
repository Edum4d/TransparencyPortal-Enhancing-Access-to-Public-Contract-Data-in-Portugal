### 1. Create .env File

Navigate to the  project root directory and then to the `mage` directory with the name `mage_transparencyportal`:

```
cd ..
cd mage_transparencyportal
```
Copy the dev.env file to create a new file named .env. This new file will contain the necessary variables for the project to run:

```
cp dev.env .env
```

After copying, open the .env file and update the GCP credentials to match the credentials set up in `terraform/variables.tf`. Ensure that the credentials match to avoid any authentication issues during project execution.
Update the following variables:

- `STORAGE_BUCKET_NAME`: Change to `gcs_bucket_name` to match the Terraform variable.
- `BIGQUERY_DATASET_NAME`: Change to `bq_dataset_name` to match the Terraform variable.
- `GCLOUD_PROJECT_NAME`: Change to `project` to match the Terraform variable.


Ensure that the credentials match to avoid any authentication issues during project execution.


### 2. Place Your GCP Credentials File

Additionally, place your Google Cloud Platform (GCP) credentials file in the `secrets` folder within the `mage_transparencyportal` directory:

```
mage_transparencyportal/
└── secrets/
    └── go-de-zoomcamp-project-2024.json
```
Ensure that the credentials file is named appropriately and matches the path specified in your application for authentication.

Update the following variables in your `.env` file:

- `GOOGLE_APPLICATION_CREDENTIALS`: Update this variable with the relative path to your service account credentials JSON file inside `mageai`. For example: `home/src/secrets/go-de-zoomcamp-project-2024.json`.

- `SERVICE_ACCOUNT_KEY_FILEPATH`: Update this variable with the relative path to your service account credentials JSON file within the project directory. For example: `secrets/go-de-zoomcamp-project-2024.json`.

### 3. Running MageAI Docker Container

    Follow these steps to run the `mageai` Docker container:

    1. **Ensure Docker is Installed**: Make sure Docker is installed on your machine.
    2. **Build Docker Image**: Open a terminal or command prompt, navigate to your project directory, and execute the following command to build the Docker image:
    ```
    docker-compose build
    ```
    2. **Run Docker Compose**: After the Docker image is built, execute the following command to start the Docker containers defined in the docker-compose.yml file:
    ```
    docker-compose up -d
    ```

    3. **Access the Container**: Once the containers are running, access the `mageai` service at `http://localhost:6789` in your web browser.

### 4: Run Pipeline

To execute the entire pipeline, follow these steps:
![Start Run Pipe](images/start_pipeline.gif)

1. Access the Mage AI web interface by navigating to http://localhost:6789/ in your web browser.
2. Click on the "url_to_gcs" pipeline.
3. Click on the "Run@once" button and select "Run Now" to initiate the pipeline execution.
4. Enter the necessary trigger details and monitor the pipeline's progress and results.