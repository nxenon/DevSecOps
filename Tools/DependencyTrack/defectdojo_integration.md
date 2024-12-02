# Dependency Track & DefectDojo Integration
[Dptrack-To-Defectdojo-Integration.py](dptrack-to-defectdojo-integration.py) code generates engagement IDs in
Defect Dojo by projects names in dependency track (by tag names) and then creates integration properties in Dependency Track.
This will be needed when you enabled Defect Dojo integration in Dependency Track and want to specify engagement ID of each project in Dependency Track.

## Requirements

    pip install requests

## Usage
- Replace these variables:

    
    DEFECT_DOJO_API_KEY = 'REPLACE_DEFECT_DOJO_API_KEY'
    DEFECT_DOJO_URL = 'REPLACE_DEFECT_DOJO_URL'
    PRODUCT_ID_IN_DEFECT_DOJO = "REPLACE_PRODUCT_ID_IN_DEFECT_DOJO"
    DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID = "REPLACE_DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID"
    NEW_ENGAGEMENT_TAG_IN_DEFECT_DOJO = ["REPLACE_TAG1", "REPLACE_TAG2"]
    DEPENDENCY_TRACK_URL = 'REPLACE_DEPENDENCY_TRACK_URL'
    DEPENDENCY_TRACK_API_KEY = 'REPLACE_DEPENDENCY_TRACK_API_KEY'
    PRODUCT_TAG_IN_DEPENDENCY_TRACK = 'REPLACE_PRODUCT_TAG_IN_DEPENDENCY_TRACK'

- Run the script:


    python3 dptrack-to-defectdojo-integration.py


## Output

    Project test-project1 --E ID-> 74 Done.
    Project test-project2 --E ID-> 73 Done.
