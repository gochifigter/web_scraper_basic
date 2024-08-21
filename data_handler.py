"""
Data handling and storage module
Handles saving extracted data to various formats
"""
import json
import csv
import os
from datetime import datetime

class DataHandler:
    def __init__(self, output_dir="output"):
        """
        Initialize data handler
        
        Args:
            output_dir (str): Directory to save output files
        """
        self.output_dir = output_dir
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def save_to_json(self, data, filename=None):
        """
        Save data to JSON file
        
        Args:
            data: Data to save (should be JSON serializable)
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_data_{timestamp}.json"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def save_to_csv(self, data, filename=None):
        """
        Save data to CSV file
        
        Args:
            data (list): List of dictionaries
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if not data:
            return None
            
        if not filename:
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
    
    def save_to_txt(self, text, filename=None):
        """
        Save text to file
        
        Args:
            text (str): Text content to save
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_text_{timestamp}.txt"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        
        return filepath