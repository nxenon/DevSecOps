"""
Automation Integration of DefectDojo and Dependency Track
GitHub: Amin Nasiri -> https://github.com/nxenon
Project: DevSecOps -> https://github.com/nxenon/DevSecOps
"""

import warnings
from datetime import datetime, timedelta
from urllib3.exceptions import InsecureRequestWarning
import requests

# Suppress only the InsecureRequestWarning
warnings.filterwarnings("ignore", category=InsecureRequestWarning)


DEFECT_DOJO_API_KEY = 'REPLACE_DEFECT_DOJO_API_KEY'
DEFECT_DOJO_URL = 'REPLACE_DEFECT_DOJO_URL'
PRODUCT_ID_IN_DEFECT_DOJO = "REPLACE_PRODUCT_ID_IN_DEFECT_DOJO"
DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID = "REPLACE_DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID"
NEW_ENGAGEMENT_TAG_IN_DEFECT_DOJO = ["REPLACE_TAG1", "REPLACE_TAG2"]

DEPENDENCY_TRACK_URL = 'REPLACE_DEPENDENCY_TRACK_URL'
DEPENDENCY_TRACK_API_KEY = 'REPLACE_DEPENDENCY_TRACK_API_KEY'
PRODUCT_TAG_IN_DEPENDENCY_TRACK = 'REPLACE_PRODUCT_TAG_IN_DEPENDENCY_TRACK'

# conversion
PRODUCT_ID_IN_DEFECT_DOJO = int(PRODUCT_ID_IN_DEFECT_DOJO)
DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID = int(DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID)

# Set today time for new engagement (start)
current_time = datetime.now()
start_formatted_date = current_time.strftime("%Y-%m-%d")

# Set tomorrow time for new engagement (end)
tomorrow_date = current_time + timedelta(days=1)
end_formatted_tomorrow_date = tomorrow_date.strftime("%Y-%m-%d")


def create_engagement_in_defect_dojo(
        project_name: str,
) -> int:
    """
    returns new engagement ID
    :param project_name:
    :return:
    """
    data = {
        "tags": NEW_ENGAGEMENT_TAG_IN_DEFECT_DOJO,
        "name": f"SCA {project_name}",
        "description": f"SCA Engagement for {project_name} project",
        "version": None,
        "first_contacted": None,
        "target_start": start_formatted_date,
        "target_end": end_formatted_tomorrow_date,
        "reason": "string",
        "tracker": None,
        "test_strategy": "https://TEST-STRATEGY-URI-HERE.example.com/",
        "threat_model": True,
        "api_test": True,
        "pen_test": True,
        "check_list": True,
        "status": "In Progress",
        "engagement_type": "CI/CD",
        "build_id": "string",
        "commit_hash": "string",
        "branch_tag": "string",
        "source_code_management_uri": "https://YOUR-SOURCE-CODE-URI-HERE.example.com/",
        "deduplication_on_engagement": True,
        "lead": DEFECT_DOJO_ENGAGEMENT_TESTING_LEADER_ID,
        "requester": None,
        "preset": None,
        "report_type": None,
        "product": PRODUCT_ID_IN_DEFECT_DOJO,
        "build_server": None,
        "source_code_management_server": None,
        "orchestration_engine": None
    }
    h = {
        'Authorization': f"token {DEFECT_DOJO_API_KEY}"
    }

    u = DEFECT_DOJO_URL + '/api/v2/engagements/'
    req = requests.post(
        u,
        json=data,
        headers=h,
        verify=False
    )
    return req.json()['id']


def get_project_engagement_id_from_defect_dojo_if_exists(
        project_name: str
) -> int:
    """
    if output is -1, it means there is no engagement
    :param project_name:
    :return:
    """
    u = DEFECT_DOJO_URL + '/api/v2/engagements/'
    h = {
        'Authorization': f"token {DEFECT_DOJO_API_KEY}"
    }
    req = requests.get(
        u,
        params={'name': f'SCA {project_name}'},
        headers=h, verify=False
    )
    try:
        e_id = req.json()['results'][0]['id']
        return e_id
    except IndexError:
        return -1


def get_projects_by_tag_from_dependency_track() -> dict:
    u = DEPENDENCY_TRACK_URL + f'/api/v1/project/tag/{PRODUCT_TAG_IN_DEPENDENCY_TRACK}'
    h = {
        'X-Api-Key': f'{DEPENDENCY_TRACK_API_KEY}',
    }

    req = requests.get(
        u,
        headers=h,
        verify=False,
    )

    resp = req.json()
    temp = {

    }
    for p in resp:
        temp[p['uuid']] = p['name']

    return temp


def check_integration_properties_on_project_in_dependency_track_if_exists(
        project_uuid: str,
        project_e_id: int,  # defect dojo e_id
):
    """
    if return param is 'ok', no change is needed'
    if return param is '
    :return:
    """

    u = DEPENDENCY_TRACK_URL + f'/api/v1/project/{project_uuid}/property'
    h = {
        'X-Api-Key': f'{DEPENDENCY_TRACK_API_KEY}',
    }

    req = requests.get(
        u,
        headers=h,
        verify=False,
    )
    resp = req.json()
    for prop in resp:
        if prop['propertyName'] == 'defectdojo.engagementId':
            if prop['propertyValue'] == str(project_e_id):  # no change is needed
                return

    delete_integration_properties_on_project_in_dependency_track(
        project_uuid
    )
    set_integration_properties_on_project_in_dependency_track(
        project_uuid,
        project_e_id
    )


def set_integration_properties_on_project_in_dependency_track(
        project_uuid: str,
        engagement_id: int,
):
    u = DEPENDENCY_TRACK_URL + f'/api/v1/project/{project_uuid}/property'
    h = {
        'X-Api-Key': f'{DEPENDENCY_TRACK_API_KEY}',
    }

    d = {
        "groupName": "integrations",
        "propertyName": "defectdojo.engagementId",
        "propertyValue": str(engagement_id),
        "propertyType": "STRING",
        "description": None
    }

    requests.put(
        u,
        headers=h,
        verify=False,
        json=d
    )


def delete_integration_properties_on_project_in_dependency_track(
        project_uuid: str
):
    u = DEPENDENCY_TRACK_URL + f'/api/v1/project/{project_uuid}/property'
    h = {
        'X-Api-Key': f'{DEPENDENCY_TRACK_API_KEY}',
    }

    requests.delete(
        u,
        headers=h,
        verify=False,
    )


dp_track_projects = get_projects_by_tag_from_dependency_track()
dp_track_projects_with_defect_dojo_eng_id = {}
for p in dp_track_projects.keys():
    e_id = get_project_engagement_id_from_defect_dojo_if_exists(dp_track_projects[p])
    if e_id == -1:
        e_id = create_engagement_in_defect_dojo(project_name=dp_track_projects[p])

    dp_track_projects_with_defect_dojo_eng_id[p] = e_id

for p_uuid in dp_track_projects_with_defect_dojo_eng_id.keys():
    check_integration_properties_on_project_in_dependency_track_if_exists(
        p_uuid,
        dp_track_projects_with_defect_dojo_eng_id[p_uuid]
    )
    print(f'Project {dp_track_projects[p_uuid]} --E ID-> {dp_track_projects_with_defect_dojo_eng_id[p_uuid]} Done.')
