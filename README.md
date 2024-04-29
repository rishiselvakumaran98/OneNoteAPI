## OneNote API Script

Hmm... Are you tired of creating multiple sections of notes in OneNote and typing the sections one by one painfully and then studying from them? Well I have a solution for you! The OneNote API script in this repo will help you to create multiple pages and any possible contents in each individual section of your given OneNote notebook. Feel free to clone this project and start using it right away! The best part is this project is open-sourced (Yes it is MIT licensed). So feel free to clone it and modify it to your needs. Please fork my project and like it if you find it useful. Thanks!!

## How to use this project

1. First clone the project into your local environment
   1. Do ```git clone https://github.com/rishiselvakumaran98/OneNoteAPI.git``` in your local environment

2. Create a .txt file at the root of this project in the name of the section you wish to populate in your Notebook. Eg. `Breakfast Menu.txt`

3. Now comes the part that might be challenging for some of you especially if you have a notebook that is stored in Enterprise/Corporate Microsoft 365 accounts. 
    
    Using Graph Explorer:
     - Log in to Graph Explorer:
        Access Graph Explorer at [Graph Explorer](!https://developer.microsoft.com/en-us/graph/graph-explorer).
      - Sign in with the account that has access to the OneNote notebooks.
    
## Step 1: Gather Information Using Microsoft Graph Explorer
 ### A. Finding the User ID and Notebook Name
    
 Go to Microsoft Graph Explorer: Open Graph Explorer and sign in with your Microsoft account.
   Retrieve User Profile: To get your user ID, execute the following API request:
   `https://graph.microsoft.com/v1.0/me?$select=id`
   The response will include your user ID. Note this `id`.

   Retrieve Notebooks: To find the name of your notebooks, execute:
   `https://graph.microsoft.com/v1.0/me/onenote/notebooks`
   From the JSON response, find the displayName of the notebook you want to use.
       
 ### B. Accessing the Bearer Token
 **Authentication Token**: In Graph Explorer, after you sign in, your OAuth2.0 Bearer Token (Access Token) can be viewed and copied from the ```Access Token``` tab on the left panel.

## Step 2: Setup OneNoteAPI.env File
Use the file named OneNoteAPI.env in the root of your project with the following content, replacing `<user_id>, <notebook_name>, <base_url>, and <bearer_token>` with the actual values you gathered:


 ```sh
 USER_ID=<user_id>
 NOTEBOOK_NAME=<notebook_name>
 BASE_URL=https://graph.microsoft.com/v1.0
 BEARER_TOKEN=<bearer_token>
 ```