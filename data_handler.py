"""
Data handling module for saving and loading scraped data
"""
import json
import csv
import os
from datetime import datetime

class DataHandler:
    def __init__(self, output_dir="scraped_data"):
        """
        Initialize data handler
        
        Args:
            output_dir (str): Directory to save output files
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def save_json(self, data, filename=None):
        """
        Save data as JSON file
        
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
        
        print(f"Data saved to: {filepath}")
        return filepath
    
    def save_csv(self, data, filename=None):
        """
        Save data as CSV file
        
        Args:
            data (list): List of dictionaries
            filename (str): Output filename
            
        Returns:
            str: Path to saved file
        """
        if not data:
            print("No data to save")
            return None
            
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"scraped_data_{timestamp}.csv"
        
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            if data:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        
        print(f"Data saved to: {filepath}")
        return filepath
    
    def save_text(self, text, filename=None):
        """
        Save text data to file
        
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
        
        print(f"Text saved to: {filepath}")
        return filepath