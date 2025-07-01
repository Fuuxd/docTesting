#!/usr/bin/env python3
import os
import json
import sys

def generate_index_files(root_dir):
    """Generate index.json files for all directories in the given root directory."""
    print(f"Starting index generation for: {root_dir}")
    
    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist!")
        return
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Filter out hidden files and existing index.json files
        filtered_files = [f for f in filenames if not f.startswith('.') and f != 'index.json']
        
        index_data = {
            "directories": dirnames,
            "files": filtered_files
        }
        
        index_path = os.path.join(dirpath, 'index.json')
        
        try:
            with open(index_path, 'w') as f:
                json.dump(index_data, f, indent=2)
            print(f"Generated: {index_path}")
            print(f"  - Directories: {len(dirnames)}")
            print(f"  - Files: {len(filtered_files)}")
        except Exception as e:
            print(f"Error writing {index_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_index.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    generate_index_files(root_dir)
    print("Index generation complete!")