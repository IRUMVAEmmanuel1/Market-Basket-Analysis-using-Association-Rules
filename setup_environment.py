#!/usr/bin/env python3
"""
Environment Setup Script for Market Basket Analysis Quiz
Course: MSDA9223 - Data Mining and Information Retrieval
Author: Student Name
Date: June 29, 2025

This script sets up the environment and checks all required packages for Market Basket Analysis.
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    print("=== PYTHON VERSION CHECK ===")
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ WARNING: Python 3.8+ is recommended for this project")
        return False
    else:
        print("✅ Python version is compatible")
        return True

def install_package(package_name):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def check_and_install_packages():
    """Check and install required packages"""
    print("\n=== PACKAGE INSTALLATION ===")
    
    required_packages = {
        'pandas': 'pandas>=1.5.0',
        'numpy': 'numpy>=1.21.0',
        'matplotlib': 'matplotlib>=3.5.0',
        'seaborn': 'seaborn>=0.11.0',
        'mlxtend': 'mlxtend>=0.21.0',
        'jupyter': 'jupyter>=1.0.0',
        'notebook': 'notebook>=6.4.0'
    }
    
    installed_packages = []
    failed_packages = []
    
    for package, pip_name in required_packages.items():
        print(f"\nChecking {package}...")
        try:
            __import__(package)
            print(f"✅ {package} is already installed")
            installed_packages.append(package)
        except ImportError:
            print(f"❌ {package} not found. Installing...")
            if install_package(pip_name):
                print(f"✅ {package} installed successfully")
                installed_packages.append(package)
            else:
                print(f"❌ Failed to install {package}")
                failed_packages.append(package)
    
    return installed_packages, failed_packages

def create_project_structure():
    """Create project folder structure"""
    print("\n=== PROJECT STRUCTURE SETUP ===")
    
    # Get current directory (should be Quiz folder)
    current_dir = Path.cwd()
    print(f"Current directory: {current_dir}")
    
    # Create subdirectories
    directories = [
        "outputs",
        "outputs/figures", 
        "outputs/results",
        "temp_files"
    ]
    
    created_dirs = []
    for dir_name in directories:
        dir_path = current_dir / dir_name
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            created_dirs.append(dir_name)
            print(f"✅ Created directory: {dir_name}")
        except Exception as e:
            print(f"❌ Failed to create {dir_name}: {e}")
    
    return created_dirs

def check_dataset():
    """Check if the grocery dataset exists"""
    print("\n=== DATASET CHECK ===")
    
    dataset_path = Path("groceries.csv")
    
    if dataset_path.exists():
        file_size = dataset_path.stat().st_size
        print(f"✅ Dataset found: groceries.csv")
        print(f"   File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        # Quick check if file is readable
        try:
            with open(dataset_path, 'r') as f:
                first_line = f.readline().strip()
            print(f"   First line preview: {first_line[:50]}...")
            return True
        except Exception as e:
            print(f"❌ Error reading dataset: {e}")
            return False
    else:
        print("❌ Dataset not found: groceries.csv")
        print("   Please ensure groceries.csv is in the current directory")
        return False

def create_requirements_file():
    """Create requirements.txt file"""
    print("\n=== CREATING REQUIREMENTS.TXT ===")
    
    requirements_content = """# Market Basket Analysis Requirements
# Course: MSDA9223 - Data Mining and Information Retrieval

pandas>=1.5.0
numpy>=1.21.0
matplotlib>=3.5.0
seaborn>=0.11.0
mlxtend>=0.21.0
jupyter>=1.0.0
notebook>=6.4.0

# Optional packages for enhanced analysis
plotly>=5.0.0
wordcloud>=1.8.0
"""
    
    try:
        with open("requirements.txt", "w") as f:
            f.write(requirements_content)
        print("✅ requirements.txt created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create requirements.txt: {e}")
        return False

def test_imports():
    """Test importing all required packages"""
    print("\n=== TESTING PACKAGE IMPORTS ===")
    
    import_tests = [
        ("pandas", "import pandas as pd"),
        ("numpy", "import numpy as np"),
        ("matplotlib", "import matplotlib.pyplot as plt"),
        ("seaborn", "import seaborn as sns"),
        ("mlxtend frequent_patterns", "from mlxtend.frequent_patterns import apriori, association_rules"),
        ("mlxtend preprocessing", "from mlxtend.preprocessing import TransactionEncoder")
    ]
    
    successful_imports = []
    failed_imports = []
    
    for name, import_statement in import_tests:
        try:
            exec(import_statement)
            print(f"✅ {name} import successful")
            successful_imports.append(name)
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed_imports.append(name)
    
    return successful_imports, failed_imports

def print_next_steps():
    """Print instructions for next steps"""
    print("\n" + "="*60)
    print("🎯 SETUP COMPLETE - NEXT STEPS")
    print("="*60)
    print()
    print("1. Open Jupyter Notebook:")
    print("   jupyter notebook")
    print()
    print("2. Create a new notebook called:")
    print("   market_basket_analysis.ipynb")
    print()
    print("3. Your project structure:")
    print("   📁 Current folder/")
    print("   ├── 📄 groceries.csv")
    print("   ├── 📄 market_basket_analysis.ipynb (to be created)")
    print("   ├── 📄 requirements.txt")
    print("   ├── 📄 setup_environment.py (this file)")
    print("   └── 📁 outputs/")
    print("       ├── 📁 figures/")
    print("       └── 📁 results/")
    print()
    print("4. Ready to start Step 1: Data Loading and Exploration!")
    print()

def main():
    """Main setup function"""
    print("🚀 MARKET BASKET ANALYSIS - ENVIRONMENT SETUP")
    print("="*60)
    print("Course: MSDA9223 - Data Mining and Information Retrieval")
    print("Quiz: Market Basket Analysis using Association Rules")
    print("="*60)
    
    # Run all setup checks
    python_ok = check_python_version()
    installed_packages, failed_packages = check_and_install_packages()
    created_dirs = create_project_structure()
    dataset_ok = check_dataset()
    requirements_ok = create_requirements_file()
    successful_imports, failed_imports = test_imports()
    
    # Summary
    print("\n" + "="*60)
    print("📋 SETUP SUMMARY")
    print("="*60)
    print(f"✅ Python version compatible: {python_ok}")
    print(f"✅ Packages installed: {len(installed_packages)}/{len(installed_packages) + len(failed_packages)}")
    print(f"✅ Project directories created: {len(created_dirs)}")
    print(f"✅ Dataset found: {dataset_ok}")
    print(f"✅ Requirements file: {requirements_ok}")
    print(f"✅ Package imports working: {len(successful_imports)}/{len(successful_imports) + len(failed_imports)}")
    
    if failed_packages:
        print(f"\n⚠️  Failed packages: {', '.join(failed_packages)}")
    if failed_imports:
        print(f"⚠️  Failed imports: {', '.join(failed_imports)}")
    
    if not failed_packages and not failed_imports and dataset_ok:
        print("\n🎉 SETUP SUCCESSFUL! Ready to start analysis.")
        print_next_steps()
    else:
        print("\n⚠️  Setup completed with some issues. Please resolve them before proceeding.")

if __name__ == "__main__":
    main()