# Dynamic README Scripts

This directory contains scripts to automatically update your GitHub profile README with dynamic content.

## Files

- `update_readme.py` - Main script that updates README.md with dynamic content
- `README.md` - This documentation file

## Usage

### Manual Update
```bash
cd scripts
python update_readme.py
```

### Automated Updates
The GitHub Actions workflow (`.github/workflows/dynamic-readme.yml`) will automatically run this script every 6 hours.

## Configuration

Edit `config/readme_config.json` to customize:
- GitHub username
- Timezone
- Current working status
- Skills and technologies
- Social links
- Theme colors

## Features

- **Real-time Status**: Updates current working status and goals
- **Timezone Support**: Uses your local timezone for timestamps
- **GitHub Stats**: Fetches live GitHub statistics
- **Automated Updates**: Runs via GitHub Actions
- **Customizable**: Easy configuration via JSON file

## Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

## Customization

1. Edit `config/readme_config.json` to update your information
2. Modify `update_readme.py` to add new dynamic features
3. The script will automatically update your README.md

## GitHub Actions

The workflow will:
- Run every 6 hours automatically
- Run manually when triggered
- Run when script files are updated
- Commit and push changes automatically 