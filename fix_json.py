import json

input_file = r"c:\Users\Administrator\Downloads\My workflow 2 (1).json"
output_file = r"c:\Users\Administrator\Downloads\My workflow 2 FIXED.json"

try:
    # Read the JSON file with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Show context around error position
    pos = 16562
    start = max(0, pos - 100)
    end = min(len(content), pos + 100)
    
    print(f"Content around position {pos}:")
    print(f"[{start}:{pos}] = {repr(content[start:pos])}")
    print(f"[{pos}:{end}] = {repr(content[pos:end])}")
    print()
    
    # Try to parse
    data = json.loads(content)
    
    # Write the corrected JSON with proper formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ JSON validated and fixed successfully!")
    print(f"  Nodes: {len(data['nodes'])}")
    print(f"  Output: {output_file}")
    
except json.JSONDecodeError as e:
    print(f"✗ JSON Error: {e}")
    print(f"  Line: {e.lineno}, Column: {e.colno}")
    print(f"  Position: {e.pos}")
except Exception as e:
    print(f"✗ Error: {e}")
