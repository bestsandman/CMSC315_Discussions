# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Created and populated a dictionary: Built a simple restaurant reservation tracker with 5 initial bookings using reservation IDs as keys and guest info as values.
2. Demonstrated lookup operations: Pulled records by ID directly in O(1) time without needing to loop through the whole structure.
3. Demonstrated update operations: Changed a guest's reservation details by assigning new values directly to an existing key without duplicating entries.
4. Demonstrated delete operations: Removed an entry using `del`, which lowered the total count and freed up the key.
5. *ested edge cases* Handled missing lookups with `.get()`, avoided deletion errors using `.pop()` with default fallbacks, and tested behavior on an empty dictionary.
6. Real world scenario: Focused on a host stand at a busy restaurant needing fast lookups for reservations during a rush.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.