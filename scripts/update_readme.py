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
import re

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
                'created_at': data.get('created_at', ''),
                'name': data.get('name', username),
                'bio': data.get('bio', ''),
                'location': data.get('location', ''),
                'company': data.get('company', '')
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
    
    # Update GitHub stats section with Anurag's style
    stats_section = f"""## 📊 GitHub Stats

![GitHub Stats](https://happy-status.vercel.app/api?username={username}&show_icons=true&theme=radical&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=FFFFFF&icon_color=58A6FF)

![Top Languages](https://happy-status.vercel.app/api/top-langs/?username={username}&layout=compact&theme=radical&hide_border=true&bg_color=0D1117&title_color=58A6FF&text_color=FFFFFF)

![GitHub Streak](https://streak-stats.demolab.com/?user={username}&theme=radical&hide_border=true&background=0D1117&stroke=58A6FF&ring=58A6FF&fire=58A6FF&currStreakNum=FFFFFF&sideNums=FFFFFF&currStreakLabel=FFFFFF&sideLabels=FFFFFF&dates=FFFFFF)

### 📈 Profile Stats
- 📁 **Public Repositories**: {github_stats.get('public_repos', 0)}
- 👥 **Followers**: {github_stats.get('followers', 0)}
- 👤 **Following**: {github_stats.get('following', 0)}
- 🏢 **Company**: {github_stats.get('company', 'N/A')}
- 📍 **Location**: {github_stats.get('location', 'N/A')}

"""
    
    # Replace GitHub stats section
    stats_pattern = r"## 📊 GitHub Stats\n.*?\n\n"
    if re.search(stats_pattern, content, re.DOTALL):
        content = re.sub(stats_pattern, stats_section, content, flags=re.DOTALL)
    else:
        # Add stats section after About Me if it doesn't exist
        about_pos = content.find("## 🚀 About Me")
        if about_pos != -1:
            end_pos = content.find("## ", about_pos + 1)
            if end_pos == -1:
                end_pos = len(content)
            content = content[:end_pos] + stats_section + content[end_pos:]
    
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
    print(f"📊 GitHub Stats: {github_stats.get('public_repos', 0)} repos, {github_stats.get('followers', 0)} followers")

if __name__ == "__main__":
    update_readme() 