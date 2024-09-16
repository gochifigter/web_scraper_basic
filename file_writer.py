"""
File writing utilities for saving scraped data
"""
import json
import csv
import os
from datetime import datetime

class FileWriter:
    @staticmethod
    def ensure_directory(filepath):
        """
        Ensure directory exists for filepath
        
        Args:
            filepath (str): Path to file
        """
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
    
    @staticmethod
    def save_json(data, filename, indent=2):
        """
        Save data as JSON file
        
        Args:
            data: Data to save
            filename (str): Output filename
            indent (int): JSON indentation
        """
        FileWriter.ensure_directory(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        print(f"Data saved to {filename}")
    
    @staticmethod
    def save_csv(data, filename, headers=None):
        """
        Save data as CSV file
        
        Args:
            data (list): List of dictionaries or lists
            filename (str): Output filename
            headers (list): Column headers for CSV
        """
        FileWriter.ensure_directory(filename)
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            if data and isinstance(data[0], dict):
                # Data is list of dictionaries
                writer = csv.DictWriter(f, fieldnames=headers or data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                # Data is list of lists
                writer = csv.writer(f)
                if headers:
                    writer.writerow(headers)
                writer.writerows(data)
        
        print(f"Data saved to {filename}")
    
    @staticmethod
    def save_text(text, filename):
        """
        Save text to file
        
        Args:
            text (str): Text content to save
            filename (str): Output filename
        """
        FileWriter.ensure_directory(filename)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text saved to {filename}")
    
    @staticmethod
    def generate_filename(base_name, extension, timestamp=True):
        """
        Generate filename with timestamp
        
        Args:
            base_name (str): Base name for file
            extension (str): File extension
            timestamp (bool): Whether to add timestamp
            
        Returns:
            str: Generated filename
        """
        if timestamp:
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            return f"{base_name}_{timestamp_str}.{extension}"
        else:
            return f"{base_name}.{extension}"