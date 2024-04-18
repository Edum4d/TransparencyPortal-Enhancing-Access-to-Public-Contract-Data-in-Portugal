# This variable defines the path to your Google Cloud service account credentials JSON file.
variable "credentials" {
  description = "Path to the Google Cloud service account credentials JSON file."
  default     = "/secrets/transparencyportal-420117-a63d0e28ae3a.json"
  # Example: if your credentials file is saved in a directory named 'keys' as 'my-creds.json', you could use default = "./keys/my-creds.json"
}

# This variable specifies the Google Cloud project ID.
variable "project" {
  description = "The Google Cloud project ID."
  default     = "transparencyportal-420117"
}

# This variable specifies the region where resources will be provisioned.
variable "region" {
  description = "The region where resources will be provisioned."
  default     = "us-central1"
}

# This variable specifies the location for the Google Cloud project.
variable "location" {
  description = "The location for the Google Cloud project."
  default     = "US"
}

# This variable defines the name of the BigQuery dataset.
variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset."
  default     = "transparencyportal_bq"
}

# This variable defines the name of the Google Cloud Storage bucket.
variable "gcs_bucket_name" {
  description = "The name of the Google Cloud Storage bucket."
  default     = "transparencyportal_bucket"
}

# This variable specifies the storage class for the Google Cloud Storage bucket.
variable "gcs_storage_class" {
  description = "The storage class for the Google Cloud Storage bucket."
  default     = "STANDARD"
}