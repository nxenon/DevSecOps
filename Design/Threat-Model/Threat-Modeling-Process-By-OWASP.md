[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps)
# [Threat Modeling Process by OWASP](https://owasp.org/www-community/Threat_Modeling_Process)

## Introduction
- These document enables you `identify`, `quantify`, and `address` the security risks associated with application.
- Threat modeling looks at a system from a potential `attacker’s perspective`, as opposed to a defender’s viewpoint
- Threat modeling process can break down into 3 parts:
  - Decompose the Application
  - Determine and Rank Threats
  - Determine Countermeasures and Mitigation

## Decompose the Application
- basic understanding of the application
- how it interacts with external entities
  - Creating use cases to understand how the application is used
  - Identifying entry points to see where a potential attacker could interact with the application
  - Identifying assets, i.e. items or areas that the attacker would be interested in
  - Identifying trust levels that represent the access rights that the application will grant to external entities

## Determine and Rank Threats
Using a threat categorization is critical, such as:
 - [STRIDE](https://en.wikipedia.org/wiki/STRIDE_%28security%29)
 - [Application Security Frame](https://pathlock.com/learn/what-are-application-security-frameworks/)
 - These provide threat categories like:
   - Auditing & Logging
   - Authentication
   - Authorization
   - Configuration Management
   - Data Protection in Storage and Transit
   - Data Validation
   - Exception Management
- The Goal of the threat categorization is to help:
  - Identify threats from `attacker` perspective: [STRIDE](https://en.wikipedia.org/wiki/STRIDE_%28security%29)
  - Identify threats from `defensive` perspective:  [Application Security Frame](https://pathlock.com/learn/what-are-application-security-frameworks/)
  - [DFDs](https://en.wikipedia.org/wiki/Data-flow_diagram) help identify potential threats from attacker's perspective such as:
    - Data Sources
    - Processes
    - Data Flows
    - Interactions with Users

## Determine Countermeasures and Mitigation
vulnerability may be mitigated with implementation of a countermeasure. The risk mitigation strategy might involve evaluating these threats from the business impact they pose. Once the possible impact is identified, options for addressing the risk include:
- `Accept`: decide that the business impact is acceptable
- `Eliminate`: remove components that make the vulnerability possible
- `Mitigate`: add checks or controls that reduce the risk impact, or the chances of its occurrence
