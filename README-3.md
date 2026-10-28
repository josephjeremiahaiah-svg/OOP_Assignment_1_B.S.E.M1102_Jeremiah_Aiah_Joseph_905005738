# Patient Record System

A simple Python program that uses Object-Oriented Programming (OOP) to record patients and their health visits. Built for **PROG211 Object-Oriented Programming 1** at Limkokwing University of Creative Technology, Sierra Leone (Semester 3, September 2026 to February 2027).

**Domain:** Health
**Problem solved:** Small clinics often keep patient information on paper, which is slow to search and easy to lose. This program stores patients and their visits as objects so a health worker can add, view and update records quickly.

## Features

- Add patients to a registry (duplicate IDs are refused)
- Add health records (condition, treatment, visit date) to a patient
- Update an existing record
- Display all patients with their full visit history
- Count how many patients have been created

## How It Works

| Component | Type | Purpose |
|---|---|---|
| `HealthRecord` | Class | Stores one visit: condition, treatment and visit date |
| `Patient` | Class | Stores patient ID, name, age and a list of `HealthRecord` objects |
| `registry` | Dictionary | Stores `Patient` objects with the patient ID as the key |
| `add_patient()` | Function | Adds a patient to the registry |
| `display_all()` | Function | Displays every patient and their records |

**OOP concepts used**

- **Classes and objects:** two classes that interact (a `Patient` holds many `HealthRecord` objects)
- **Data structure:** one dictionary, keyed by patient ID
- **Tuple (optional):** visit dates are stored as `(year, month, day)`
- **Instance methods:** `add_record()`, `update_record()`, `display_info()`
- **Class methods:** `from_string()` and `get_total_patients()` (`@classmethod`)
- **Static method:** `is_valid_age()` (`@staticmethod`)

## Digital Public Goods (DPG) Alignment

| DPG principle | How this project meets it |
|---|---|
| **Open-source** | The full source code and this README are in a public GitHub repository. Anyone can read, copy and improve it. |
| **Inclusive and accessible design** | Plain-language messages and simple text output. No special hardware or paid software; it runs on any computer with Python 3. |
| **Privacy-respecting** | No sensitive personal data is stored. Patients are identified only by an ID and a first name. No phone numbers, addresses or national ID numbers are collected. |
| **Modular and reusable** | Each class has one job and the functions are separate from the classes. The classes can be imported into other projects, such as a vaccination tracker. |

## Requirements

- Python 3.8 or newer (no extra libraries needed)

## How to Run

1. Clone the repository:

   ```
   git clone <your-repository-link>
   cd <your-repository-folder>
   ```

2. Run the program:

   ```
   python patient_record_system.py
   ```

## Example Usage

**Sample input** (set inside the program's main section):

```python
p1 = Patient("P001", "Jeremiah", 34)
p2 = Patient.from_string("P002,Patient B,52")

p1.add_record(HealthRecord("Malaria", "Artesunate", (2026, 10, 12)))
p2.add_record(HealthRecord("Hypertension", "Lifestyle advice", (2026, 10, 13)))
```

**Sample output**

```
Added patient P001.
Added patient P002.
Patient P001 already exists.
=== Patient Registry ===
Patient ID: P001 | Name: Jeremiah | Age: 34
  [0] 2026-10-12 | Malaria | Artesunate
Patient ID: P002 | Name: Patient B | Age: 52
  [0] 2026-10-13 | Hypertension | Lifestyle advice
Record updated for P001.
Patient ID: P001 | Name: Jeremiah | Age: 34
  [0] 2026-10-12 | Malaria | Artesunate and rest
Total patients: 2
```

## Add and Delete Patients (Menu)

The file `patient_menu.py` adds an interactive menu on top of the original program. It **imports** the code from `patient_record_system.py`, so the original file is not changed. With it, a user can add a new patient and delete an existing one while the program is running.

| Option | What it does |
|---|---|
| 1. Add a patient | Asks for an ID, name and age, then stores a new `Patient` in the dictionary. Duplicate IDs and invalid ages are refused. |
| 2. Delete a patient | Asks for a patient ID, asks for confirmation (y/n), then removes that patient from the dictionary. |
| 3. View all patients | Displays every patient using `display_all()`. |
| 4. Exit | Closes the program. |

**How to run the menu**

```
python patient_menu.py
```

**Sample session**

```
=== Patient Record System ===
1. Add a patient
2. Delete a patient
3. View all patients
4. Exit
Choose an option (1-4): 1
Patient ID: P001
Name: Jeremiah
Age: 34
Added patient P001.

Choose an option (1-4): 2
Patient ID to delete: P001
Delete P001? (y/n): y
Removed patient P001.
```

Deleting uses `del registry[patient_id]`, which works because patients are stored in a dictionary keyed by patient ID.

## Project Structure

```
.
├── patient_record_system.py   # Original classes, dictionary and demo
├── patient_menu.py            # Menu to add and delete patients
└── README.md                  # This file
```

## Author

[Your Full Name]
Student ID: [Your Student ID]
Lecturer: Amandus Benjamin Coker
Module: PROG211 Object-Oriented Programming 1

## License

Released under the MIT License so others can reuse and adapt it.
