"""
File handling utilities for saving scraped data
"""

import json
import csv
import os
from datetime import datetime

class FileHandler:
    @staticmethod
    def ensure_directory(directory):
        """
        Create directory if it doesn't exist
        
        Args:
            directory (str): Directory path
        """
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    @staticmethod
    def save_json(data, filename, directory='output'):
        """
        Save data as JSON file
        
        Args:
            data: Data to save
            filename (str): Output filename
            directory (str): Output directory
        """
        FileHandler.ensure_directory(directory)
        filepath = os.path.join(directory, f"{filename}.json")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Data saved to: {filepath}")
    
    @staticmethod
    def save_csv(data, filename, directory='output'):
        """
        Save data as CSV file
        
        Args:
            data (list): List of dictionaries or lists
            filename (str): Output filename
            directory (str): Output directory
        """
        FileHandler.ensure_directory(directory)
        filepath = os.path.join(directory, f"{filename}.csv")
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if data and isinstance(data[0], dict):
                # List of dictionaries
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                # List of lists
                writer = csv.writer(f)
                writer.writerows(data)
        
        print(f"Data saved to: {filepath}")
    
    @staticmethod
    def save_text(text, filename, directory='output'):
        """
        Save text to file
        
        Args:
            text (str): Text to save
            filename (str): Output filename
            directory (str): Output directory
        """
        FileHandler.ensure_directory(directory)
        filepath = os.path.join(directory, f"{filename}.txt")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print(f"Text saved to: {filepath}")
    
    @staticmethod
    def generate_filename(prefix='scraped_data'):
        """
        Generate timestamped filename
        
        Args:
            prefix (str): Filename prefix
            
        Returns:
            str: Generated filename
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}"