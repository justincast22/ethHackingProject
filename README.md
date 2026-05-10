# Ethical Hacking Final Project

## Overview

This project was created for the Ethical Hacking final project.

The tool automates host enumeration by scanning targets, collecting service and operating system information, and generating a Markdown report. The project also supports optional AI-assisted analysis using a local Ollama instance.

The script supports:
- IPv4 targets
- DNS targets
- CIDR subnet ranges
- Excluded targets
- Windows-specific enumeration
- Markdown report generation
- Optional Ollama AI analysis

---

# Features

- TCP service enumeration
- OS detection
- Windows SMB and NetBIOS enumeration
- Active Directory related checks
- AI-assisted host analysis
- Markdown report output
- Command-line options
- Scope exclusions
- DNS safety confirmation

---

# Requirements

- Python 3.12
- Nmap
- Ollama (optional)

Python packages:
- requests
- python-nmap

---

# Installation

## Clone the repository

- git clone https://github.com/justincast22/ethHackingProject.git
- cd ethHackingProject

## Create a Virtual Environment
    
#### python3.12 -m venv venv
- source venv/bin/activate

## Install Dependencies
- pip install -r requirements.txt

## Nmap Installation
- sudo apt install nmap

## Ollama Setup (Optional)
- ollama pull gemma4:e4b
- ollama serve


## Basic Syntax
- python main.py [targets] [options]
- python main.py --help

## Usage Examples

### Scan a Single Host
- python main.py 192.168.1.10

### Scan a Subnet
- python main.py 192.168.1.0/24

### Scan Multiple Targets
- python main.py 192.168.1.10,192.168.1.15

### Exclude Targets
- python main.py 192.168.1.0/24 --exclude 192.168.1.1

### Disable AI Analysis
- python main.py 192.168.1.10 --no-ai

## Report Output
- Reports are generated in Markdown format.
- Default naming format:
    - host_enumeration_report_YYYYMMDD_HHMM_UTC.md

