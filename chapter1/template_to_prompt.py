import os

def replace_placeholders_in_files(input_folder, output_folder, placeholders, replacements):
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            with open(input_path, 'r') as input_file:
                content = input_file.read()
                
                for placeholder in placeholders:
                    if placeholder in content:
                        content = content.replace(placeholder, replacements.get(placeholder, ""))
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with open(output_path, 'w') as output_file:
                    output_file.write(content)

# Example usage
input_folder = r'prompts'
output_folder = r'ready_prompts'

placeholders = ['[INDUSTRY]', '[SPECIALITY]', '[EMPLOYER]', '[PRODUCT]', '[ROLE]', '[PROJECT_DETAIL]']
replacements = {
    '[INDUSTRY]': 'Construction of domestic buildings',
    '[SPECIALITY]': 'contract for construction of domestic buildings',
    '[EMPLOYER]': 'the UK government',
    '[PRODUCT]': 'Buildings',
    '[ROLE]': 'Project Manager',
    '[PROJECT_DETAIL]': 'construction of a domestic buildings.'
}

replace_placeholders_in_files(input_folder, output_folder, placeholders, replacements)
