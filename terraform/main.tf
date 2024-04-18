terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

# Provider Configuration
provider "google" {
  # Path to the Google Cloud service account credentials JSON file.
  credentials = file(var.credentials)
  # The Google Cloud project ID.
  project     = var.project
  # The region where resources will be provisioned.
  region      = var.region
}

# Google Cloud Storage Bucket Resource
resource "google_storage_bucket" "transparencyportal_bucket" {
  # The name of the Google Cloud Storage bucket.
  name          = var.gcs_bucket_name
  # The location for the Google Cloud Storage bucket.
  location      = var.location
  # Destroy all objects in the bucket when destroying the resource.
  force_destroy = true

  # Lifecycle rule for the bucket.
  lifecycle_rule {
    condition {
      # Object age in days.
      age = 1
    }
    action {
      # Abort incomplete multipart uploads older than the specified days.
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# Google BigQuery Dataset Resource
resource "google_bigquery_dataset" "transparencyportal_bq" {
  # The name of the BigQuery dataset.
  dataset_id                = var.bq_dataset_name
  # The location for the BigQuery dataset.
  location                  = var.location
  # Delete all contents of the dataset when destroying the resource.
  delete_contents_on_destroy = true
}