# Dynamic README Scripts

This directory contains the script to automatically update your GitHub profile README.

## Files

- `update_readme.py` - Main script that updates README.md with dynamic content

## Usage

### Automated (Recommended)
The GitHub Actions workflow (`.github/workflows/update-readme.yml`) runs automatically every 6 hours.

### Manual Update
```bash
cd scripts
python update_readme.py
```

## Configuration

Edit `config/readme_config.json` to customize:
- GitHub username
- Timezone
- Current working status
- Skills and technologies

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

## GitHub Token Setup

1. Go to repository Settings → Actions → General
2. Enable "Read and write permissions"
3. The workflow will use the built-in GitHub Token automatically

---

Your README will update automatically every 6 hours! 🎉 