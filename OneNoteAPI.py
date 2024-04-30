import argparse
import requests
from dotenv import load_dotenv
import os

class CreateOneNoteSections:
    def __init__(self, notebook_name: str, section_name: str):
        load_dotenv('OneNoteAPI.env')
        self.user_url = "https://graph.microsoft.com/v1.0/users/"+os.getenv('USER_ID')
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
        self.sections_url = self.find_notebook_url(notebook_name) + "/sections"
        self.specific_section_url = self.find_section_url(section_name)
    
    def find_notebook_url(self, notebook_name) -> str:
        """Fetches the notebook ID matching the notebook_name."""
        url = f"{self.user_url}/onenote/notebooks"
        response = requests.get(url, headers=self.headers)
        notebooks = response.json().get('value', [])
        
        for notebook in notebooks:
            if notebook['displayName'].lower() == notebook_name.lower():
                notebook_id = notebook['id']
                sections_url = f"{self.user_url}/onenote/notebooks/{notebook_id}"
                return sections_url
        print(f"Section '{notebook_name}' not found!")
        return None

    def find_section_url(self, section_name) -> str:
        response = requests.get(self.sections_url, headers=self.headers)
        sections = response.json().get('value', [])
        
        specific_section_url = None
        for section in sections:
            if section['displayName'] == section_name:
                target_section_id = section['id']
                # Define page creation endpoint based on the found section ID
                specific_section_url = f"{self.sections_url}/{target_section_id}/pages"
                return specific_section_url
        print(f"Section '{section_name}' not found in Notebook!")
        return specific_section_url
    
    def read_page_titles(self, file_path):
        with open(file_path, 'r') as file:
            page_titles_sublists = [line.split("\n")[0] for line in file.readlines() if line != '\n']
        return page_titles_sublists
    
    # Function to create titles and pages
    def create_pages(self, page_titles_sublists) -> bool:
        for title in page_titles_sublists:
            # Loop through titles and create pages under the found section
            page_content = self.page_content_template.format(title=title)
            response = requests.post(self.specific_section_url, headers=self.headers, data=page_content)
            if response.status_code == 201:
                print(f"Page '{title}' created successfully.")
            else:
                print(f"Failed to create page '{title}'. Error: {response.text}")
                return False
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("notebook_name", help="Name of the notebook")
    parser.add_argument("section_name", help="Name of the section in the notebook")
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), f"{args.section_name}.txt")
    create_one_note_section = CreateOneNoteSections(args.notebook_name, args.section_name)
    page_title_sublists = create_one_note_section.read_page_titles(file_path)
    result = create_one_note_section.create_pages(page_title_sublists)
    if result:
        print("All pages created successfully!")
    else:
        print("Failed to create some pages!")