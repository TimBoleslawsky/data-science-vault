## Definition
Strings are stored numerically in computers; that is, each character is assigned an unambiguous numerical value according to a character set. This is **character encoding**.
- This is a potential source of error if different users of the same data interpret the numbers as different characters!

**Important terminology**
- **ASCII**: A 7-bit encoding character set for basic English characters (128 characters).
- **Unicode**: A universal character set that assigns a unique code point to every character in every language and script (more than 1 million possible characters).
- **UTF-8**: A variable-length encoding used to represent Unicode characters, using 1 to 4 bytes per character, with compatibility for ASCII.

**Relationship**: ASCII is a subset of Unicode, and UTF-8 is a way to encode Unicode characters into bytes while being compatible with ASCII.