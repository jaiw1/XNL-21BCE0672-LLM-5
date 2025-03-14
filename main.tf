###############
# gcp/main.tf #
###############

# Use the Google provider
provider "google" {
  # Replace with your project ID
  project = "my-terraform-project-453713"
  # Region can be set if you plan to create region-specific resources
  region  = "us-central1"
}

# Create a VPC network
resource "google_compute_network" "vpc_network" {
  name                    = "my-gcp-test-network"
  auto_create_subnetworks = false
}
