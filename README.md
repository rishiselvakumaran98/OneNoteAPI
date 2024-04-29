## OneNote API Script

Hmm... Are you tired of creating multiple sections of notes in OneNote and typing the sections one by one painfully and then studying from them? Well I have a solution for you! The OneNote API script in this repo will help you to create multiple pages and any possible contents in each individual section of your given OneNote notebook. Feel free to clone this project and start using it right away! The best part is this project is open-sourced (Yes it is MIT licensed). So feel free to clone it and modify it to your needs. Please fork my project and like it if you find it useful. Thanks!!

## How to use this project

1. First clone the project into your local environment
   1. Do ```git clone https://github.com/rishiselvakumaran98/OneNoteAPI.git``` in your local environment

2. Create a .txt file at the root of this project in the name of the section you wish to populate in your Notebook. Eg. `Breakfast Menu.txt`

3. Now is the part that might be challenging for some of you especially if you have a notebook that is stored in Enterprise/Corporate Microsoft 365 accounts. 
    
    Using Graph Explorer:
     - Log in to Graph Explorer:
        Access Graph Explorer at [Graph Explorer](!https://developer.microsoft.com/en-us/graph/graph-explorer).
      - Sign in with the account that has access to the OneNote notebooks.
    
    Make the API Request:
      You can use the following GET request to retrieve all notebooks:
      `https://graph.microsoft.com/v1.0/me/onenote/notebooks?$select=id,displayName,createdDateTime,isDefault,userRole,isShared`
      
      Manually Search for your notebook under `displayName` parameter from the API response.
      
      Use the browser’s search feature (usually Ctrl+F or CMD+f in Mac) to find your `notebook_name`.

