import argparse
import requests
from dotenv import load_dotenv
import os

class CreateOneNoteSections:
    def __init__(self, section_name: str):
        load_dotenv('OneNoteAPI.env')
        self.section_name = section_name
        self.base_url = os.getenv('BASE_URL')
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.headers = {
                        "Authorization": f"Bearer {self.bearer_token}",
                        "Accept": "application/json",
                        "Content-Type": "application/xhtml+xml"  # For page creation
                    }
        self.page_content_template = """
                                        <!DOCTYPE html>
                                        <html>
                                            <head>
                                                <title>{title}</title>
                                            </head>
                                        </html>
                                    """
    
    # def sanitize_for_onenote(self, input_string: str) -> str:
    #     # Define specific replacements
    #     replacements = {
    #         '&': 'and',   # Replace '&' with 'and'
    #         '#': 'number' # Replace '#' with 'number'
    #     }
    #     # Apply specific replacements
    #     for key, value in replacements.items():
    #         input_string = input_string.replace(key, value)
    #     # Remove any remaining special characters not specifically replaced
    #     # This regex will keep only alphanumeric characters, spaces and underscores
    #     sanitized_string = re.sub(r'[^\w\s]', '', input_string)
    #     # Replace spaces with underscores
    #     sanitized_string = sanitized_string.replace(' ', '_')
    #     return sanitized_string

    def fetch_sections(self):
        response = requests.get(self.base_url, headers=self.headers)
        sections = response.json().get('value', [])
        return sections
    
    def read_page_titles(self, file_path):
        with open(file_path, 'r') as file:
            page_titles_sublists = [line.split("\n")[0] for line in file.readlines() if line != '\n']
        return page_titles_sublists
    
    # Function to create titles and pages
    def create_pages(self, page_titles_sublists):
        sections = self.fetch_sections()
        target_section_id = None
        for section in sections:
            if section['displayName'] == self.section_name:
                target_section_id = section['id']
                break
        
        if not target_section_id:
            print(f"Section '{self.section_name}' not found in Notebook!")
            return
        
        # Define page creation endpoint based on the found section ID
        page_creation_endpoint = f"https://graph.microsoft.com/v1.0/me/onenote/sections/{target_section_id}/pages"

        for title in page_titles_sublists:
            # Loop through titles and create pages under the found section
            page_content = self.page_content_template.format(title=title)
            response = requests.post(page_creation_endpoint, headers=self.headers, data=page_content)
            if response.status_code == 201:
                print(f"Page '{title}' created successfully.")
            else:
                print(f"Failed to create page '{title}'. Error: {response.text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("section_name", help="Name of the notebook")
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), f"{args.section_name}.txt")
    create_one_note_section = CreateOneNoteSections(args.section_name)
    page_title_sublists = create_one_note_section.read_page_titles(file_path)
    create_one_note_section.create_pages(page_title_sublists)