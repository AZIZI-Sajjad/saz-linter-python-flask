terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "1.7.5"
    }
  }
}

variable "api_key" {
  type = string
}

variable "owner_id" {
  type = string
}

variable "environment" {
  type = string
}

provider "render" {
  api_key  = var.api_key
  owner_id = var.owner_id
}

resource "render_project" "saz-linter-python-flask" {
  name = "saz-linter-python-flask"
  environments = {
    "production" = {
      name             = "production"
      protected_status = "unprotected"
    },
    "development" = {
      name             = "development"
      protected_status = "unprotected"
    }
  }
}

resource "render_web_service" "saz-linter-python-flask-app" {
  name           = "monapp"
  plan           = "starter"
  region         = "frankfurt"
  environment_id = render_project.saz-linter-python-flask.environments[var.environment].id
  runtime_source = {
    image = {
      image_url = "ghcr.io/azizi-sajjad/saz-linter-python-flask/monapp"
      tag       = "latest"
    }
  }
}