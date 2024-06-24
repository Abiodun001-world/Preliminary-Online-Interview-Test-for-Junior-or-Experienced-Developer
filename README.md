# Election Results Management System

This Python script manages and displays election results from the 2011 elections in Delta State, Nigeria.

## Features

1. Display results for an individual polling unit
2. Display summed total results for all polling units under a particular local government
3. Store results for a new polling unit

## Requirements

- Python 3.x
- SQLite3

## Setup

1. Ensure Python is installed on your system.
2. Place the `bincom_test.sql` file in the project directory.
3. No additional dependencies are required as the script uses Python's built-in sqlite3 module.

## Usage

Run the script from the command line:
Follow the on-screen prompts to:
- View results for a specific polling unit
- View total results for an LGA
- Add results for a new polling unit

## Database Structure

The SQLite database (bincom_test.sql) contains the following key tables:

- polling_unit: Information about polling units (uniqueid, lga_id, etc.)
- announced_pu_results: Results for each party in each polling unit
- lga: Information about Local Government Areas

## Notes

- This implementation focuses on Delta State (state_id: 25) as specified in the test.