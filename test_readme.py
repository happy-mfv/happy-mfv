#!/usr/bin/env python3
"""
Test script to verify README structure and update it manually
"""

import os
from datetime import datetime
import pytz

def test_readme_structure():
    """Test the README structure and update timestamp"""
    
    # Read current README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("📋 Current README Structure:")
    print("=" * 50)
    
    # Check for key sections
    sections = [
        "## 📊 GitHub Stats",
        "## 🛠️ Skills & Tools", 
        "## 📈 Recent Activity",
        "## 🌟 Current Status"
    ]
    
    for section in sections:
        if section in content:
            print(f"✅ {section}")
        else:
            print(f"❌ {section} - Missing!")
    
    # Update timestamp
    now = datetime.now()
    jst = pytz.timezone('Asia/Tokyo')
    current_time = now.astimezone(jst)
    timestamp = current_time.strftime('%Y-%m-%d %H:%M JST')
    
    print(f"\n🕐 Current Time (JST): {timestamp}")
    
    # Check if status section exists and update it
    if "## 🌟 Current Status" in content:
        print("✅ Status section found")
        
        # Update the timestamp
        import re
        pattern = r"- 📅 \*\*Last Updated\*\*: .*"
        replacement = f"- 📅 **Last Updated**: {timestamp}"
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content)
            
            # Write updated content
            with open('README.md', 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ Timestamp updated successfully!")
        else:
            print("❌ Timestamp pattern not found")
    else:
        print("❌ Status section not found")
    
    print("\n🎯 Next Steps:")
    print("1. Follow the setup guide in setup_pat.sh")
    print("2. Or use the 'Simple README Update' workflow")
    print("3. Test the workflow manually")

if __name__ == "__main__":
    test_readme_structure() 