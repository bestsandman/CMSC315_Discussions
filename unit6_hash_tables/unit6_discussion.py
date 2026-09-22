"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Dicts work like hash tables under the hood: python hashes the key to calculate
    # an index, so lookups and inserts run in average O(1) time without scanning a list.
    reservations = {}

    reservations["RES-101"] = {"name": "Jordan Lee", "party": 2, "time": "6:00 PM"}
    reservations["RES-102"] = {"name": "Marcus Vance", "party": 4, "time": "6:30 PM"}
    reservations["RES-103"] = {"name": "Taylor Reed", "party": 6, "time": "7:00 PM"}
    reservations["RES-104"] = {"name": "Samira Khan", "party": 2, "time": "7:15 PM"}
    reservations["RES-105"] = {"name": "Chris Ortiz", "party": 3, "time": "8:00 PM"}

    print("Initial reservations:")
    for k, v in reservations.items():
        print(f"  {k}: {v['name']} ({v['party']} guests, {v['time']})")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Direct key lookup hashes the string and jumps straight to that bucket in memory
    res_1 = reservations["RES-102"]
    res_2 = reservations["RES-105"]

    print("Lookup RES-102:", res_1["name"], "-", res_1["time"])
    print("Lookup RES-105:", res_2["name"], "-", res_2["time"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    # Assigning a new value to an existing key just overwrites the reference at that hash slot
    print("Before update:", reservations["RES-101"])
    reservations["RES-101"] = {"name": "Jordan Lee", "party": 5, "time": "6:45 PM"}
    print("After update: ", reservations["RES-101"])

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    # del removes the key-value pair and drops the dictionary size by 1
    print("Bookings count before del:", len(reservations))
    del reservations["RES-103"]
    print("Bookings count after del:", len(reservations))
    print("Is RES-103 still present?", "RES-103" in reservations)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Accessing a missing key with [] throws KeyError, so use .get() with fallback
    missing_key = "RES-999"
    found = reservations.get(missing_key, "Not found")
    print(f"Looking for {missing_key}: {found}")

    # del on a missing key also throws an error, but pop() with None avoids the crash
    removed = reservations.pop(missing_key, None)
    print(f"Safely removing {missing_key} (returned: {removed})")

    # Empty dictionary check
    empty = {}
    print("Empty dict lookup:", empty.get("RES-101", "No entries"))


if __name__ == "__main__":
    main()