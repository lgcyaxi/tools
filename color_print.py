'''
Author       : AXIBA leolihao@arizona.edu
Date         : 2025-03-20 10:00:00
FilePath     : /EasyCalib/tools/color_print.py
Description  : Utility functions for colorful console output
Copyright (c) 2025 by AXIBA (leolihao@arizona.edu), All Rights Reserved.
'''

# ANSI color codes
class Colors:
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    
    # Reset
    RESET = '\033[0m'

def colorize(text, color=Colors.WHITE, style=None):
    """Apply color and optional style to text
    
    Args:
        text (str): The text to colorize
        color (str): Color code from Colors class
        style (str, optional): Style code from Colors class
        
    Returns:
        str: Colorized text
    """
    if style:
        return f"{style}{color}{text}{Colors.RESET}"
    return f"{color}{text}{Colors.RESET}"

def print_info(text, prefix="ℹ️ "):
    """Print information message in cyan""" 
    print(colorize(prefix + " " + text, Colors.CYAN))

def print_success(text, prefix="✅"):
    """Print success message in green"""
    print(colorize(prefix + " " + text, Colors.GREEN))

def print_warning(text, prefix="⚠️"):
    """Print warning message in yellow"""
    print(colorize(prefix + " " + text, Colors.YELLOW))

def print_error(text, prefix="❌"):
    """Print error message in red"""
    print(colorize(prefix + " " + text, Colors.RED, Colors.BOLD))

def print_header(text):
    """Print header message in bold blue"""
    print(colorize(text, Colors.BLUE, Colors.BOLD))

def print_step(step_number, text, prefix="🔍"):
    """Print a numbered step in magenta"""
    print(colorize(prefix + " " + f"[{step_number}] {text}", Colors.MAGENTA))

def print_command(cmd, prefix="💻"):
    """Print a command in yellow with bold"""
    print(colorize(prefix + " " + f"$ {cmd}", Colors.YELLOW, Colors.BOLD)) 