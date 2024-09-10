def unique(lst, key=None):
    seen = set()
    result = []
    
    for item in lst:
        value = key(item) if key else item
        
        if value not in seen:
            seen.add(value)
            result.append(item)
    
    return result

print(unique(["python", "java", "Python", "Java"], key=lambda s: s.lower()))
# Output: ["python", "java"]
