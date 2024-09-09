import os
import re
import yaml
from datetime import datetime

def parse_frontmatter(content):
    frontmatter = {}
    if (match := re.match(r'^---\n(.*?)\n---', content, re.DOTALL)):
        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            pass
    return frontmatter, match

def update_frontmatter(file_path, frontmatter, match, content, date_key):
    if date_key in frontmatter:
        original_date = frontmatter[date_key]
        try:
            parsed_date = datetime.strptime(original_date, '%B %d, %Y')
            formatted_date = parsed_date.strftime('%Y-%m-%d')
            frontmatter[date_key] = formatted_date
            
            new_frontmatter = yaml.safe_dump(frontmatter, default_flow_style=False).strip()
            updated_content = content.replace(match.group(1), new_frontmatter)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
                
            print(f"Updated {file_path}: {original_date} -> {formatted_date}")
        
        except ValueError:
            print(f"Skipping {file_path}: Invalid date format in '{original_date}'")

def mass_update_markdown_dates(vault_path, date_key):
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter, match = parse_frontmatter(content)
                
                if match:
                    update_frontmatter(file_path, frontmatter, match, content, date_key)

if __name__ == "__main__":
    # Path to your markdown vault
    vault_path = "/home/nibir/Documents/GH/eleventy-garden/d"
    
    # The key in the front matter that contains the date
    date_key = 'date'  # Adjust this key according to your front matter
    
    mass_update_markdown_dates(vault_path, date_key)
