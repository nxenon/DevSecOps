# DefectDojo Pentest Vulnerability (Finding) Uploader
This script helps you by uploading findings (vulnerabilities) which you have found in your pentest (penetration tests). 
You can simply create and fill a CSV file and then upload all findings to DefectDojo.

## Requirements
1. Python Requirements:


    pip install -r requirements.txt


2. DefectDojo
- Create an Engagement
- Create a Test in Engagement
- You need the `Test ID` (for the python Script)
- Get your DefectDojo `API Token` (for the python Script)


3. Script Parameters:
You have to fill following parameters in the code:
- DEFECT_DOJO_BASE_URL
- DEFECT_DOJO_API_TOKEN
- DEFECT_DOJO_TEST_ID
- FINDING_TAGS
- LEAD_ID (User ID of user in DefectDojo who found the bug)


4. CSV Findings (Vulnerabilities) File
You have to fill the CSV file with the desired columns. Required (mandatory) columns are:
- Title
- Finding Date
- Publish Date
- Severity
- Description
- Other columns must be in CSV file but can be empty values. Date data must be in this format `YYYY-MM-DD`. like 2024-10-06.


5. Run the Script


        python defectdojo_finding_uploader.py defectdojo_finding.csv

