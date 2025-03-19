"""
excel_export.py - Utility functions for exporting formatted Excel files
"""

import os
from datetime import datetime
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill, Font, Border, Side
from openpyxl.utils import get_column_letter

def export_state_tables(state_name, tables_data, winning_combos, related_combos, output_dir):
    """
    Export state tables to a formatted Excel file with side-by-side layout
    
    Args:
        state_name (str): Name of the state
        tables_data (dict): Dictionary containing DataFrames for each section
        winning_combos (set): Set of winning number combinations
        related_combos (set): Set of related number combinations
        output_dir (str): Directory to save the Excel file
    """
    # Create timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{state_name}_{timestamp}.xlsx"
    filepath = os.path.join(output_dir, filename)
    
    # Create Excel writer
    with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
        # Get the workbook and create a sheet
        workbook = writer.book
        sheet_name = "Combined Tables"
        worksheet = workbook.create_sheet(sheet_name)
        
        # Define styles
        header_fill = PatternFill(start_color='CCCCCC', end_color='CCCCCC', fill_type='solid')
        winner_font = Font(color='FF0000', bold=True)  # Red
        related_font = Font(color='0000FF')  # Blue
        border = Border(
            left=Side(style='thin'),
            right=Side(style='thin'),
            top=Side(style='thin'),
            bottom=Side(style='thin')
        )
        
        # Starting columns for each section
        section_starts = {
            'Midday': 1,
            'Evening': 15,
            'Combined': 29
        }
        
        # Write each section
        for section_name, start_col in section_starts.items():
            if section_name in tables_data:
                df = tables_data[section_name]
                if df is not None:
                    # Write section header
                    header_cell = worksheet.cell(row=1, column=start_col, value=section_name)
                    header_cell.font = Font(bold=True, size=14)
                    
                    # Write DataFrame
                    for i, col in enumerate(df.columns):
                        col_letter = get_column_letter(start_col + i)
                        # Write header
                        cell = worksheet.cell(row=2, column=start_col + i, value=col)
                        cell.fill = header_fill
                        cell.border = border
                        
                        # Write data
                        for j, val in enumerate(df[col]):
                            cell = worksheet.cell(row=j + 3, column=start_col + i, value=val)
                            cell.border = border
                            
                            # Apply highlighting for string values
                            if isinstance(val, str):
                                if any(combo in val for combo in winning_combos):
                                    cell.font = winner_font
                                elif any(combo in val for combo in related_combos):
                                    cell.font = related_font
                    
                    # Set column widths
                    for i in range(len(df.columns)):
                        col_letter = get_column_letter(start_col + i)
                        worksheet.column_dimensions[col_letter].width = 15
        
        # Remove default sheet if it exists
        if 'Sheet' in workbook.sheetnames:
            workbook.remove(workbook['Sheet'])
    
    return filepath

def setup_logging_directories():
    """
    Set up necessary directories for logging if they don't exist
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    archive_dir = os.path.join(base_dir, 'data', 'archive')
    os.makedirs(archive_dir, exist_ok=True)
    return archive_dir 