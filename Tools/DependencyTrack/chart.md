# Dependency Track Reporting Chart Code
[Vulnerability-Chart-Creator.py](vulnerability-chart-creator.py) code creates multiple charts by `product tags` in dependency tracker.

## Requirements

    pip install requests
    pip install matplotlib

## Usage
- Replace `DEPENDENCY_TRACK_URL:PORT` with you dependency tracker url
- Replace --> token = login(user=`"USERNAME"`, `password="PASSWORD"`) in code with your username which has access to see projects and vulnerabilities.
- Replace `PRODUCT_TAG` in ALL_PRODUCTS_TAGS global variable, then script creates chart for that product tags.

## Output Chart

![image](https://github.com/user-attachments/assets/27edeb3e-88d0-453c-ae63-f98163659ad8)
