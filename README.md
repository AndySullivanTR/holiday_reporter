# Reuters Reporter Holiday Shifts System

## Overview
Simple web application for managing holiday shift signups and assignments for Reuters reporters.

## Features
- Reporters can indicate interest in any holiday shifts
- Each reporter can be assigned a MAXIMUM of 1 shift
- Random allocation from interested reporters
- Manager dashboard with statistics and allocation controls
- Excel export functionality

## Holiday Shifts (10 total)
1. **Christmas** - December 25, 2025
2. **New Year's Day** - January 1, 2026
3. **Martin Luther King Day** - January 19, 2026
4. **President's Day** - February 16, 2026
5. **Good Friday** - April 3, 2026

Each holiday has 2 shifts (morning 8am-4pm, evening 3pm-10pm), with 2 slots per shift = 20 total slots.

## Hard-Coded Deadline
**December 8, 2025 at 12:00 PM**

## Authentication
- **Manager**: Username: `admin` | Password: `admin123`
- **Reporters**: Same credentials as weekend_reporter system (loaded from reporter_credentials.csv)

## Installation & Setup

1. Navigate to directory:
   ```
   cd C:\Users\8010317\projects\scheduler\reporter_holiday
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access at: http://localhost:5001

## File Structure
```
reporter_holiday/
├── app.py                          # Main Flask application
├── data/
│   ├── reporters.json              # Auto-generated from CSV
│   ├── holidays.json               # 10 holiday shifts
│   ├── signups.json                # Reporter interest data
│   ├── assignments.json            # Final assignments
│   └── settings.json               # Deadline & lock status
├── templates/
│   ├── login.html                  # Dark green themed
│   ├── reporter_dashboard.html     # Reporter interface
│   └── manager_dashboard.html      # Admin interface
└── README.md
```

## How It Works

### For Reporters:
1. Login with your username/password
2. Check boxes for any shifts you're interested in
3. Click "Save My Selections"
4. Wait for allocation (after Dec 8)
5. See your assignment on dashboard

### For Managers:
1. Login as admin
2. View submission statistics
3. See interest levels per shift
4. Click "Run Allocation" when ready
5. Export results to Excel

## Allocation Algorithm
1. Collect all reporters who expressed interest
2. Randomize the order (for fairness)
3. For each reporter (in random order):
   - Skip if already assigned
   - Get their interested shifts
   - Filter to shifts with open slots
   - Randomly pick one if available
   - Assign and mark slot as filled
4. Each reporter gets max 1 shift

## Color Scheme
**Dark Green**: #1a4d2e to #2d7a4f gradient

## Port
Runs on port **5001** (weekend_reporter uses 5000)

## Data Persistence
All data stored in JSON files in `data/` directory.

## Notes
- Reporters use same credentials as weekend_reporter system
- System auto-generates reporters.json from reporter_credentials.csv on first run
- Signups lock automatically after deadline OR when manager runs allocation
- Unfilled shifts are left vacant (no forced assignment)
