# framework for obsidian-finder-thingey

import os
import re
from datetime import datetime
import yaml

def parse_frontmatter(content):
    frontmatter = {}
    if (match := re.match(r'^---\n(.*?)\n---', content, re.DOTALL)):
        try:
            frontmatter = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            pass
    return frontmatter

def get_matching_files(tag  : str, stat : str):
    matching_files = []

    for root, _, files in os.walk(vault_path := "/home/nibir/Documents/Quantumania/000 Zettelkasten"):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(os.path.join(root, file), vault_path)

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter = parse_frontmatter(content)
                
                if 'tags' in frontmatter and 'status' in frontmatter:
                    tags = frontmatter['tags']
                    status = frontmatter['status']

                    bruh = ' '.join(map(str, tags)) if isinstance(tags, list) else tags
                    huh = ' '.join(map(str, status)) if isinstance(status, list) else status
                    
                    if str(type(bruh)) != "<class 'NoneType'>" and tag in bruh and stat in huh:
                        print(relative_path)
                        # matching_files.append(relative_path)

def main():
    matching_files = get_matching_files("Study", "needs work")
    
    # output = '\n'.join(file_path for file_path, _ in matching_files)
    
    # with open("test.txt", 'w', encoding='utf-8') as f:
    #     f.write()
    # print (matching_files)
    # print(f"Created file 'study_needs_work.txt' with {len(matching_files)} entries.")

if __name__ == "__main__":
    main()