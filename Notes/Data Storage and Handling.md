When discussing data storage and data handling we differentiate between these main types:
1. **Direct storage**
	→ Save the raw data in memory or disk (e.g., variables, text files).
2. **[[Hashing]]**
	→ Transform data into a fixed-size code for fast lookup, verification, or security (e.g., dictionaries, password hashing).
3. **Compression**
	→ Shrink data to a smaller size for storage or transmission (e.g., ZIP files, image compression like JPEG).
	- Example: You save a file using .zip → it’s compressed storage.
4. **Encryption**
	→ Protect data by scrambling it, so only someone with the right key can read it (e.g., HTTPS, encrypted hard drives).
	- Example: Secure emails or banking apps.
5. **Serialization**
	→ Convert complex data (like an object) into a format that can be stored or transmitted (e.g., JSON, pickle in Python).
	- Example: Save a Python object to a file using pickle.dump().
6. **Indexing**
	→ Store extra structures (like database indexes) to make searching faster.
	- Example: SQL databases automatically create indexes on important columns.