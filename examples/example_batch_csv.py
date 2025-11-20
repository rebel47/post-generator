"""
Example: Batch Generation from CSV
Demonstrates batch generation from a CSV file
"""

import sys
import os
# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from batch_generator import BatchGenerator

# Create batch generator
batch = BatchGenerator(output_dir="output/batch_csv")

# First, create a sample CSV file
print("Creating sample CSV file...")
batch.create_sample_csv("sample_posts.csv")

# Generate posts from the CSV
print("\nGenerating posts from CSV...")
generated_files = batch.generate_from_csv(
    csv_path="sample_posts.csv",
    logo_path=None  # Add your logo path here if you have one
)

print(f"\n✓ Batch generation completed!")
print(f"✓ Generated {len(generated_files)} posts")
print("\nGenerated files:")
for file in generated_files:
    print(f"  - {file}")
