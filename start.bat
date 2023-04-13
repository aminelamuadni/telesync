@echo off
rem Batch script to run the Telesync application.
rem Author: Amine Lamuadni
rem Version: 1.0.0
rem GitHub: https://github.com/aminelamuadni/telesync

set PYTHONPATH=%PYTHONPATH%;%cd%
python src\main.py
