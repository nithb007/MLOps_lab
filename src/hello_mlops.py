import sys
import pandas as pd
import numpy as np
import sklearn
import dvc
import mlflow

print("="*60)
print("✓ MLOps Environment Ready!")
print("="*60)

print("\nPython Environment:")
print("Python version:", sys.version.split()[0])
print("Python location:", sys.executable)

print("\nCore Libraries:")
print("pandas:", pd.__version__)
print("numpy:", np.__version__)
print("scikit-learn:", sklearn.__version__)
print("dvc:", dvc.__version__)
print("mlflow:", mlflow.__version__)

print("\n" + "="*60)
print("Ready to start MLOps adventures! 🚀")
print("="*60)