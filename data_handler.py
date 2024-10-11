"""
Data handling and storage module
"""
import json
import csv
import os
from datetime import datetime

class DataHandler:
    def __init__(self, output_dir='output'):
        """
        Initialize data handler
        
        Args:
            output_dir (str): Output directory for saved files
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def save_json(self, data, filename=None):
        """
        Save data as JSON file
        
        Args:
            data: Data to save
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_data_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def save_csv(self, data, filename=None):
        """
        Save data as CSV file
        
        Args:
            data (list): List of dictionaries to save
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if not data:
            return None
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_data_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        # Get all unique keys from all dictionaries
        fieldnames = set()
        for item in data:
            fieldnames.update(item.keys())
        fieldnames = list(fieldnames)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        
        return filepath
    
    def save_text(self, text, filename=None):
        """
        Save text data to file
        
        Args:
            text (str): Text to save
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_text_{timestamp}.txt"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        
        return filepath