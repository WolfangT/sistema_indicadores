"""__init__.py.

Application starting point
"""

import importlib.metadata

DISTRIBUTION_METADATA = importlib.metadata.metadata("sistema-indicadores")

print("hello world!")
print("Data:")
for key, val in DISTRIBUTION_METADATA.items():
    print(f"\t{key}\t= {val}")