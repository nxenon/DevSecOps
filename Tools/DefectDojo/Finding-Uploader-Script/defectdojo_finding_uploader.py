import pandas as pd
import requests
import sys
import numpy as np

DEFECT_DOJO_BASE_URL = 'https://defectdojo.example.com/'  # change this
DEFECT_DOJO_API_TOKEN = "API_TOKEN"  # change this
DEFECT_DOJO_TEST_ID = "TEST_ID"  # change this
FINDING_TAGS = ["TAG1", "TAG2"]  # change this
LEAD_ID = "TEST_LEAD_ID"  # change this (User ID of user in DefectDojo who found the bug)

"""
Do *Not* Change Below This Line
"""
DEFECT_DOJO_TEST_ID = int(DEFECT_DOJO_TEST_ID)
LEAD_ID = int(LEAD_ID)
DEFECT_DOJO_AUTH_HEADER = {
    'Authorization': f"token {DEFECT_DOJO_API_TOKEN}"
}


def read_csv_file(file_name=None) -> pd.DataFrame:
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        if file_name is None:
            print("No file name is provided!")
            exit(1)
    try:
        d = pd.read_csv(file_name)
        d = d.replace({np.nan: None})
        return d
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        exit(1)


def process_csv(data: pd.DataFrame) -> list :
    default_finding_body = {
        "test": DEFECT_DOJO_TEST_ID,
        # "threat_id": 0,
        "found_by": [LEAD_ID],
        "tags": FINDING_TAGS,
        "push_to_jira": False,
        # "vulnerability_ids": [
        #     {
        #         "vulnerability_id": "string"
        #     }
        # ],
        "reporter": LEAD_ID,
        "title": "",
        "date": "",
        # "sla_start_date": "YYYY-MM-DD",
        # "sla_expiration_date": "",
        # "cwe": 0,
        # "epss_score": 1,
        # "epss_percentile": 1,
        # "cvssv3": "AV:A",
        "cvssv3_score": 0,
        "severity": "",
        "description": "",
        "mitigation": "",
        "impact": "",
        "steps_to_reproduce": "",
        "severity_justification": "",
        "references": "",
        "active": True,
        "verified": True,
        "false_p": False,
        "duplicate": False,
        "out_of_scope": False,
        "risk_accepted": False,
        "under_review": False,
        "under_defect_review": False,
        "is_mitigated": False,
        "numerical_severity": "None",
        # "line": 2147483647,
        # "file_path": "string",
        "component_name": "",
        "component_version": "",
        # "static_finding": true,
        # "dynamic_finding": true,
        # "unique_id_from_tool": "string",
        # "vuln_id_from_tool": "string",
        # "sast_source_object": "string",
        # "sast_sink_object": "string",
        # "sast_source_line": 2147483647,
        # "sast_source_file_path": "string",
        # "nb_occurences": 2147483647,
        "publish_date": "",
        # "service": "string",
        # "planned_remediation_date": "2025-01-20",
        # "planned_remediation_version": "string",
        # "effort_for_fixing": "string",
        # "review_requested_by": 0,
        # "defect_review_requested_by": 0,
        # "sonarqube_issue": 0,
        # "reviewers": [
        #     0
        # ]
    }
    all_findings = []

    keys_to_check = [
        'Title', 'URL', 'Finding Date', 'Publish Date', 'Severity',
        'Description', 'Mitigation', 'Impact',
        'Steps to Reproduce', 'Severity Justification', 'Endpoints',
        'References', 'CVSSv3 Score', 'Component Name', 'Component Version',
    ]

    for k in keys_to_check:
        if k not in data:
            print(f'Column {k} is not in CSV file!')
            exit(1)

    for index, row in data.iterrows():
        temp_finding = default_finding_body.copy()
        temp_finding['title'] = row['Title']
        temp_finding['date'] = row['Finding Date']
        temp_finding['cvssv3_score'] = row['CVSSv3 Score']
        temp_finding['severity'] = row['Severity']
        temp_finding['description'] = row['Description']
        temp_finding['mitigation'] = row['Mitigation']
        temp_finding['impact'] = row['Impact']
        temp_finding['steps_to_reproduce'] = row['Steps to Reproduce']
        if row['Severity Justification']:
            temp_finding['severity_justification'] = row['Severity Justification']
        temp_finding['references'] = row['References']
        temp_finding['component_name'] = row['Component Name']
        temp_finding['component_version'] = row['Component Version']
        temp_finding['publish_date'] = row['Publish Date']
        temp_finding['title'] = row['Title']
        all_findings.append(temp_finding)

    return all_findings


def upload_findings(findings_list: list):
    d_url = DEFECT_DOJO_BASE_URL + '/api/v2/findings/'
    for finding in findings_list:
        print(finding)
        req = requests.post(url=d_url, json=finding, headers=DEFECT_DOJO_AUTH_HEADER)
        print(req.status_code)
        print(req.content)


csv_rows = read_csv_file()
findings = process_csv(csv_rows)
if findings:
    upload_findings(findings)
