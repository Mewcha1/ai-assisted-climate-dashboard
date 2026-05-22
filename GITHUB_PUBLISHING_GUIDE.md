# GitHub Publishing Guide

This folder is ready to publish as a GitHub repository and deploy using GitHub Pages.

## Recommended repository name
`florida-nasa-power-dashboard`

## What to upload
Upload the entire folder contents to GitHub, including:

- `index.html`
- `dashboard/`
- `data/`
- `code/`
- `notebooks/`
- `report/`
- `figures/`
- `prompts/`
- `proposal/`
- `references/`
- `README.md`
- `.nojekyll`
- `.gitignore`
- `LICENSE`

## Deploy with GitHub Pages

1. Create a new GitHub repository.
2. Upload all files from this folder.
3. Go to **Settings** > **Pages**.
4. Under **Build and deployment**, choose:
   - Source: **Deploy from a branch**
   - Branch: **main**
   - Folder: **/root**
5. Click **Save**.
6. Wait for GitHub Pages to publish the site.

## Dashboard URL format

After deployment, the dashboard link will usually be:

`https://YOUR-GITHUB-USERNAME.github.io/florida-nasa-power-dashboard/`

Use that URL as the required dashboard link in the capstone submission.

## Notes

The dashboard works as a standalone static page. The data are embedded in `index.html`, so the online dashboard does not need to read the CSV at runtime. The CSV remains in `data/` for transparency and reproducibility.
