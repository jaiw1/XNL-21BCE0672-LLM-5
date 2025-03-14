# terraform/variables.tf

variable "aws_region" {
  type        = string
  description = "AWS region to deploy resources."
  default     = "us-east-1"   # or ap-south-1 if you want Mumbai
}

variable "gcp_project_id" {
  type        = string
  description = "GCP project ID"
  default     = "my-terraform-project-453713"  # Replace with your actual GCP project ID
}

variable "gcp_region" {
  type        = string
  description = "GCP region where resources will be created."
  default     = "us-central1"  # or asia-south1, etc.
}

variable "gcp_zone" {
  type        = string
  description = "GCP zone for zonal resources."
  default     = "us-central1-a"
}
