

## Permissions

Actual permissions needed to deploy a Cloud Run container:

    https://github.com/GoogleCloudPlatform/github-actions/issues/92

Or, as a hack, grant these perms among others:

    gcloud projects add-iam-policy-binding site-randocat --member="serviceAccount:june13@site-randocat.iam.gserviceaccount.com" --role="roles/run.admin"