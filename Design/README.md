# Design

## Development Lifecycle

### [SDL (Secure Development Lifecycle) by Microsoft](https://www.microsoft.com/en-us/securityengineering/sdl/practices)

- Provide Training:
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
- Define Security Requirements
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
- Define Metrics and Compliance Reporting 
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
- Perform Threat Modeling
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
- Establish Design Requirements
  - engineers typically rely on cryptography, authentication, logging, and others
  - `But` in many cases **Design** or **implementation** result in security vulnerabilities
- Define and Use Cryptography Standards
  - Data must be encrypted when transmitted or stored
  - Incorrect choice of cryptography can be catastrophic
  - It is best to have or develop a encryption standards
  - Encryption libraries must be implemented in a way that can be replaced easily when needed
- Manage the Security Risk of Using Third-Party Components
  - Vulnerabilities in third-party components can cause vulnerabilities in a bigger system they have integrated to
  - To Mitigate Risks:
    - have an accurate inventory of third-party components
    - have a plan to response when new vulnerabilities are discovered
    - additional validation based on organization risk level (based on type of component and potential vulnerabilities)
- Use Approved Tools
  - Define and publish a list of approved tools and their associated security checks
  - These tools must be updated
- Perform Static Analysis Security Testing (SAST)
  - Analyzing source code before compilation:
    - is a highly scalable method of security code review
    - helps ensure secure coding policies are being followed
  - SAST is typically integrated into the `commit pipeline`
  - SAST can be also be in used when the developer `is` coding (IDE Plugins)
- Perform Penetration Testing
  - simulating actions of a real hacker by skilled security professionals
  - Penetration Testing Helps Uncover Vulnerabilities Resulting From:
    - Coding errors
    - System configuration faults
    - Or other operational deployment weaknesses
  - Penetration tests are often performed `in conjunction with` automated and manual code reviews
- Establish a Standard Incident Response Process 
  - Preparing an Incident Response (IR) Plan is essential to solve new threats
  - IR Plan should be created `in coordination with` Product Security Incident Response Team (PSIRT) team
  - IR Plan should be tested before it is needed !

### [How to ensure security at the speed of DevOps by Gitlab](https://about.gitlab.com/blog/2019/10/31/speed-security-devops/)

#### Overview:
Choosing between security and speed is sometimes hard. Teams often do not have security in their pipelines and deployments, because security checks are manual. But you can make have security in the beginning of SDLC.

1. Make Small, Frequent Changes
   - run automated tests on small chunks of code to identify security issues faster
   - developers can fix these small chunks of code easier than a fixing a big change
2. Educate Developers and Security Teams
   -  Create or adopt educational program with these goals:
      - teach developers to recognize common vulnerabilities and remediate on their own
      - security professionals should understand development technology
3. Fail Fast, Fix Fast
   - If automated scan find security vulnerabilities, developers should respond fast
4. Prioritize Risks
   - Risks have different level of priorities
   - DevOps and Security team must define security guidelines that allows team to prioritize risks
   - Risks with high priority must be fixed in the short term
5. Automate as Much as Possible
   - Manual security tests cannot keep up
   - There are many tasks (technologies, deployments &...), so that security teams cannot perform these tasks manually
   - Tests must be pre-written
   - Policies must be pre-defined
6. More Is Better
   - Testing more frequently is better
   - In rapid development, teams have small changes, and small fixes
   - Vulnerabilities can be found in these small changes easier

#### Conclusion -> Like Always, Communication is the Key
- Security and DevOps teams must co-operate and be on the same page
- Leaders must push the members to work together and understand each team goals
- Every business should focus on building a security-first mindset
- Make it easy with integrated or single tools

## Threat Model

### [Threat Modeling by OWASP](https://owasp.org/www-community/Threat_Modeling)

#### Overview

- Threat modeling works to `identify`, `communicate` and `understand` threats and mitigations.
- A threat model is a structured representation of all the information that has effect on security of an application.
- It is a view of application from lens of security
- Threat modeling can be applied on:
  - software
  - applications
  - systems
  - networks
  - distributed systems
  - Internet of Things (IOT) devices
  - business processes
- A threat model typically includes:
  - Description of the subject to be modeled
  - Assumptions that can be checked or challenged in the future as the threat landscape changes
  - Potential threats of the system
  - Actions that can be taken to mitigate each threat
  - A way of validating the model and threats, and verification of success of actions taken
- Threat modeling is a process for `capturing`, `organizing`, and `analyzing` all of this information.
- In addition, threat modeling efforts, produces a prioritized list of security improvements to these elements of an application:
  - concept
  - requirements
  - design
  - implementation

#### Objectives of Threat Modeling

- Identify Threats
- Defining countermeasures to prevent or mitigate the effects of threats to the system
- A threat is a potential or actual undesirable event that may be malicious such as:
  - DOS Attack
  - Failure of Storage Device
- Threat modeling is a planned activity for identifying and assessing application threats and vulnerabilities

#### Threat Modeling Across the Lifecycle

- Threat modeling is **best** applied  `continuously` throughout a software development.
- Ideally, a high-level threat model should be defined early on in the concept of planing phase
- Threat model should be refind throughout the lifecycle
- `More` details added to the system, `More` attack vectors appear
- The ongoing threat modeling process should `examine`, `diagnose`, and `address` these threats
- Updating threat model is advisable after events such as:
  - A new feature is released
  - Security incidents occurs
  - Architectural or infrastructure changes

#### Threat Modeling: Four Question Framework

Following questions can help to organize threat modeling:
- What are we working on ?
- What can go wrong ?
- What are we going to do about it ?
- Did we do a good job ?

Refine The Search Space:
- Assess Scope (What are we working on ?)
  - can be small as a sprint
  - can be large as a whole system
- Identify What Can Go Wrong
  - This can be:
    - simple as a brainstorm
    - kill chains
    - attack trees
- Identify Countermeasures or Manage Risk
  - What to do with each threat ?
  - this might be:
    - implement a mitigation
    - apply: accept/transfer/eliminate approaches of risk management
- Asses Your Work
  - Did you do good enough ?

#### Structured Threat Modeling Process

[See this](#structured-threat-modeling-process-by-owasp)


### [Structured Threat Modeling Process by OWASP](https://owasp.org/www-community/Threat_Modeling_Process)

- TODO
