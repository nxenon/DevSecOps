[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps)
# [Guide to Software Composition Analysis on Snyk](https://snyk.io/series/open-source-security/software-composition-analysis-sca/)
- 📝 Taken notes from "Guide to Software Composition Analysis" by Snyk

Software composition analysis is your best bet for finding vulnerabilities 
in open source packages and learning how to fix them,
empowering you to secure your code and the health of your applications.

## What Is Software Composition Analysis (SCA)
- Software Composition Analysis (SCA) is an application security methodology for managing open source components
- Using SCA, development teams can `quickly` track and analyze any open-source component into a project
- SCA tools can discover:
  - related components
  - their supporting libraries
  - direct and indirect dependencies
- SCA tools can also detect:
  - software licenses
  - deprecated dependencies
  - vulnerabilities and potential exploits
- The scanning process generates a Bill of Material (BOM), providing a complete inventory of a project's software assets
- SCA requires to be `developer first`

## Why Use a Software Composition Analysis Tool?
Open source components are becoming major building blocks in software across practically every vertical.
SCA tools help keeping track of open source components used by your applications,
which is critical both from a productivity and a security standpoint.

## Why is Software Composition Analysis (SCA) important?
- More and more applications are using `open source`
- It has been estimated that open source code makes up 90 percent of the code composition of application
- securing applications assembled from different building blocks is a challenge for organizations that want to secure their code base

## Modern Software Supply Chains
- Open source is just one piece of the puzzle
- A security issues in one piece of a puzzle, can damage other components as well
- The recent SolarWinds attack, this time targeting proprietary software, further demonstrates the growing risk the modern software supply chain poses for organizations

## Open Does not Mean Secure
- Open source projects are considered to be safer to use
- After all, when entire community is involved in maintaining and developing a project, (security) issues are identified and fixed more quickly
- Open source projects are public and visible to all malicious actors
- Each vulnerability discovered and fixed in them, is exposed for attackers to find
- The more popular the package is, more interest have the attackers to find and exploit it

## 5 Software Composition Analysis (SCA) Challenges
Challenges:

### 1. Obscured visibility
- Developer knows what packages installs, but those packages are `dependant to other open source` libraries and packages which are not visible directly/necessarily by developer
- Vast majority of vulnerabilities which are exposed, are vulnerabilities in libraries `that developers were not aware that they were in use`

### 2. Understanding the dependency logic
- To identify the dependencies an application is using, you need to understand of how each ecosystem
- It is important that SCA solution understand the logic to avoid false-positives

### 3. Drowning in vulnerabilities
- Large number of vulnerabilities are discovering and organizations can not pay attention to all of them
- Prioritization is important, because you cannot track all issues
- CVSS-based severities is the common method for assessing risk and prioritizing

### 4. Find me a vulnerability database
- The National Vulnerability Database (NVD) is commonly used for receiving updates on vulnerabilities
- A substantial amount of security intelligence on vulnerabilities that is available in other sources such as `issue trackers`, `online forums`, `security newsletters`, and more
- NVD might also not add vulnerabilities in a timely enough fashion
- 92% of the JavaScript vulnerabilities in NVD, for example, were added to Snyk beforehand

### 5. The need for speed
- Develop speed is so fast and in other hand, security issues and vulnerabilities can be discovered more
- This has given rise to the notion of DevSecOps and Shifting Left in the security model—moving responsibility for security into the development teams to ensure minimum disruption to development workflows while also ensuring security

## How to choose a Software Composition Analysis tool
![How to choose a Software Composition Analysis tool](https://github.com/nxenon/DevSecOps/assets/61124903/2176a966-f62c-4e00-82d8-1d9533a3c9e1)

- Developer-focused
- Ecosystem support & Integrations
- Dependency Analysis
- Accurate & actionable vulnerability detection
- Prioritization
- Remediation
- Governance & Control
- Reporting
- Automation & Extensibility
- Cloud native applications

## Six Software Composition Analysis (SCA) best practices
- find a developer-friendly tool
  - show developers how it helps them
- Understand dependencies
- Automate scans and identify actionable fixes
- Integrate SCA into your CI/CD pipeline
- Consider the power of reports and SBoM capabilities
- Strengthen security policies and improve license compliance
