import os
import re
import sys

def validate_skills(skills_dir):
    print(f"🔍 Validating skills in: {skills_dir}")
    errors = []
    skill_count = 0

    if not os.path.exists(skills_dir):
        print(f"❌ Skills directory not found: {skills_dir}")
        return False

    for root, dirs, files in os.walk(skills_dir):
        # Skip .disabled directories
        dirs[:] = [d for d in dirs if d != '.disabled']
        if "SKILL.md" in files:
            skill_count += 1
            skill_path = os.path.join(root, "SKILL.md")
            # Calculate relative path from the script execution point or skills dir
            rel_path = os.path.relpath(skill_path, skills_dir)
            
            try:
                with open(skill_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                errors.append(f"❌ {rel_path}: Could not read file. Error: {e}")
                continue
            
            # Check for Frontmatter or Header
            has_frontmatter = content.strip().startswith("---")
            has_header = re.search(r'^#\s+', content, re.MULTILINE)
            
            if not (has_frontmatter or has_header):
                errors.append(f"❌ {rel_path}: Missing frontmatter or top-level heading")
            
            if has_frontmatter:
                # Basic check for name and description in frontmatter
                fm_match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
                if fm_match:
                    fm_content = fm_match.group(1)
                    if "name:" not in fm_content:
                        errors.append(f"⚠️  {rel_path}: Frontmatter missing 'name:'")
                    if "description:" not in fm_content:
                        errors.append(f"⚠️  {rel_path}: Frontmatter missing 'description:'")
                else:
                    errors.append(f"❌ {rel_path}: Malformed frontmatter")

    print(f"✅ Found and checked {skill_count} skills.")
    if errors:
        print("\n⚠️  Validation Results:")
        for err in errors:
            print(err)
        return False
    else:
        print("✨ All skills passed basic validation!")
        return True

if __name__ == "__main__":
    # If a path is provided as argument, use it. Otherwise assume parent of directory containing script (standard skills layout)
    if len(sys.argv) > 1:
        skills_path = sys.argv[1]
    else:
        # Assuming script is in skills/creador-de-habilidades/scripts/validate_skills.py
        # We want to go up 3 levels to reach 'skills' root? 
        # No, usually this script is at root/scripts/validate.py in the repo.
        # Here it is inside a skill. So we might want to validate the PARENT directory of this skill.
        # current: .../Skills/creador-de-habilidades/scripts/validate_skills.py
        # parent: .../Skills/creador-de-habilidades/scripts
        # parent^2: .../Skills/creador-de-habilidades
        # parent^3: .../Skills
        base_dir = os.path.dirname(os.path.abspath(__file__))
        skills_path = os.path.abspath(os.path.join(base_dir, "../../../"))
    
    validate_skills(skills_path)
