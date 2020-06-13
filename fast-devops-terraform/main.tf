provider "google" {
  project = "site-randocat"
}

data "google_project" "project" {
}

output "project_id" {
  value = data.google_project.project.id
}