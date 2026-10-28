class HealthRecord:
    """One visit of a patient."""

    def __init__(self, condition, treatment, visit_date):
        self.condition = condition
        self.treatment = treatment
        self.visit_date = visit_date  # tuple: (year, month, day)

    def display_info(self):
        y, m, d = self.visit_date
        return f"{y}-{m:02d}-{d:02d} | {self.condition} | {self.treatment}"


class Patient:
    """A patient identified by ID and Jeremiah only (privacy-respecting)."""

    total_patients = 0  # class attribute

    def __init__(self, patient_id, Jeremiah, age):
        if not Patient.is_valid_age(age):
            raise ValueError("Age must be between 0 and 120.")
        self.patient_id = patient_id
        self.jeremiah = Jeremiah
        self.age = age
        self.records = []
        Patient.total_patients += 1

    # ---- instance methods ----
    def add_record(self, record):
        self.records.append(record)

    def update_record(self, index, condition=None, treatment=None):
        if 0 <= index < len(self.records):
            if condition:
                self.records[index].condition = condition
            if treatment:
                self.records[index].treatment = treatment
            print(f"Record updated for {self.patient_id}.")
        else:
            print("Record not found.")

    def display_info(self):
        print(f"Patient ID: {self.patient_id} | Jeremiah: {self.jeremiah} | Age: {self.age}")
        if not self.records:
            print("  No records yet.")
        for i, record in enumerate(self.records):
            print(f"  [{i}] {record.display_info()}")

    # ---- class methods ----
    @classmethod
    def from_string(cls, text):
        patient_id, jeremiah, age = text.split(",")
        return cls(patient_id.strip(), jeremiah.strip(), int(age))

    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # ---- static method ----
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120


def add_patient(registry, patient):
    """Add a Patient to the dictionary using the ID as the key."""
    if patient.patient_id in registry:
        print(f"Patient {patient.patient_id} already exists.")
    else:
        registry[patient.patient_id] = patient
        print(f"Added patient {patient.patient_id}.")


def display_all(registry):
    """Display every patient stored in the dictionary."""
    print("=== Patient Registry ===")
    for patient in registry.values():
        patient.display_info()


if __name__ == "__main__":
    registry = {}

    p1 = Patient("P001", "Patient A", 34)
    p2 = Patient.from_string("P002,Patient B,52")

    p1.add_record(HealthRecord("Malaria", "Artesunate", (2026, 10, 12)))
    p2.add_record(HealthRecord("Hypertension", "Lifestyle advice", (2026, 10, 13)))

    add_patient(registry, p1)
    add_patient(registry, p2)
    add_patient(registry, p1)  # duplicate test

    display_all(registry)

    p1.update_record(0, treatment="Artesunate and rest")
    p1.display_info()

    print("Total patients:", Patient.get_total_patients())
