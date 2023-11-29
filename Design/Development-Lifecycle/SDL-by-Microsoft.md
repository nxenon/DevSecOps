[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps)
# [SDL (Security Development Lifecycle) by Microsoft](https://www.microsoft.com/en-us/securityengineering/sdl/practices)

## Provide Training:
  - Developers, engineers and even managers must understand security basics
  - They must know how to build security into software and services
  - effective training will help:
    - Security Policies
    - SDL Practices
    - Standards
    - Requirements of Software Security
  - Everyone:
    - `does not have to` be a hacker or security expert
    - `must` understand attacker's perspective and its goal
## Define Security Requirements
  - `Security & Privacy` is a fundamental aspect of developing highly secure applications & systems
  - Security requirements must be `continually` updated
  - Changes must be identified and threat landscape must be updated based on changes
  - Best Time to Define Security Requirements:
    - Initial Design
    - Planing Stages
  - Factors That Influence Security Requirements
    - Legal Requirements
    - Industry Requirements
    - Internal Standards
    - Coding Practices
    - Review of Previous Incidents
    - Review of Known Threats
  - Security Requirements must be tracked by:
    - Either work-tracking system
    - Or telemetry derived from engineering pipeline
## Define Metrics and Compliance Reporting 
  - Define `minimum` acceptable level
  - Hold teams accountable to meeting that criteria
  - Define Minimum Level Helps:
    - Teams understand risks associated with security issues
    - Identify and fix security issues during development (faster response time)
    - Apply the standards throughout the entire project
  - Set a Bug Bar (Bug Level or Severity) Helps:
    - Identify critical and important severity bugs
    - All bug levels must fix in a specified time (based on severity)
  - In order to Track KPI and Ensure Security Tasks Are Done:
    - Use bug tracking mechanism
    - Or use work tracking mechanism
    - For example: Azure DevOps
    - All security works must be labeled and tracked
## Perform Threat Modeling
  - should be used in environments where there is meaningful security risk
  - Threat Modeling Can Be Applied at:
    - Component
    - Application
    - System Level
  - Threat Modeling is a Practice That Allows Development Team:
    - `Consider` / `Document` / `Discuss` security implications
  - Applying a structured approach helps a team:
    - Identify Security Vulnerabilities from threats:
      - more effectively
      - lese expensively
## Establish Design Requirements
  - engineers typically rely on cryptography, authentication, logging, and others
  - `But` in many cases **Design** or **implementation** result in security vulnerabilities
## Define and Use Cryptography Standards
  - Data must be encrypted when transmitted or stored
  - Incorrect choice of cryptography can be catastrophic
  - It is best to have or develop a encryption standards
  - Encryption libraries must be implemented in a way that can be replaced easily when needed
## - Manage the Security Risk of Using Third-Party Components
  - Vulnerabilities in third-party components can cause vulnerabilities in a bigger system they have integrated to
  - To Mitigate Risks:
    - have an accurate inventory of third-party components
    - have a plan to response when new vulnerabilities are discovered
    - additional validation based on organization risk level (based on type of component and potential vulnerabilities)
## - Use Approved Tools
  - Define and publish a list of approved tools and their associated security checks
  - These tools must be updated
## - Perform Static Analysis Security Testing (SAST)
  - Analyzing source code before compilation:
    - is a highly scalable method of security code review
    - helps ensure secure coding policies are being followed
  - SAST is typically integrated into the `commit pipeline`
  - SAST can be also be in used when the developer `is` coding (IDE Plugins)
## - Perform Penetration Testing
  - simulating actions of a real hacker by skilled security professionals
  - Penetration Testing Helps Uncover Vulnerabilities Resulting From:
    - Coding errors
    - System configuration faults
    - Or other operational deployment weaknesses
  - Penetration tests are often performed `in conjunction with` automated and manual code reviews
## - Establish a Standard Incident Response Process 
  - Preparing an Incident Response (IR) Plan is essential to solve new threats
  - IR Plan should be created `in coordination with` Product Security Incident Response Team (PSIRT) team
  - IR Plan should be tested before it is needed !
