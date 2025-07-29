#!/usr/bin/env python3
"""
Dynamic README Generator
Updates README.md with real-time information
"""

import os
import json
import requests
from datetime import datetime, timedelta
import pytz

def load_config():
    """Load configuration from JSON file"""
    config_path = "config/readme_config.json"
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_github_stats(username):
    """Get GitHub statistics for a user"""
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            data = response.json()
            return {
                'public_repos': data.get('public_repos', 0),
                'followers': data.get('followers', 0),
                'following': data.get('following', 0),
                'created_at': data.get('created_at', '')
            }
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
    return {}

def get_current_status(config):
    """Get current working status and goals from config"""
    now = datetime.now()
    timezone = config.get('timezone', 'Asia/Tokyo')
    tz = pytz.timezone(timezone)
    current_time = now.astimezone(tz)
    
    status_config = config.get('status', {})
    status = {
        'working_on': status_config.get('working_on', 'Cloud Security Automation'),
        'learning': status_config.get('learning', 'Advanced Kubernetes Security'),
        'goal': status_config.get('goal', 'Implementing AI-powered DevSecOps workflows'),
        'last_updated': current_time.strftime('%Y-%m-%d %H:%M JST')
    }
    return status

def update_readme():
    """Update README.md with dynamic content"""
    config = load_config()
    username = config.get('github_username', 'happy-mfv')
    
    # Get dynamic data
    github_stats = get_github_stats(username)
    current_status = get_current_status(config)
    
    # Read current README
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update status section
    status_section = f"""## 🌟 Current Status
- 🔒 **Working on**: {current_status['working_on']}
- 🚀 **Learning**: {current_status['learning']}
- 🎯 **Goal**: {current_status['goal']}
- 📅 **Last Updated**: {current_status['last_updated']}

"""
    
    # Replace status section if it exists, otherwise add it
    if "## 🌟 Current Status" in content:
        # Find and replace the status section
        start = content.find("## 🌟 Current Status")
        end = content.find("---", start)
        if end == -1:
            end = content.find("\n\n", start)
        
        if end != -1:
            content = content[:start] + status_section + content[end:]
    else:
        # Add status section before the final separator
        separator_pos = content.rfind("---")
        if separator_pos != -1:
            content = content[:separator_pos] + status_section + content[separator_pos:]
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("README updated successfully!")

if __name__ == "__main__":
    update_readme() 