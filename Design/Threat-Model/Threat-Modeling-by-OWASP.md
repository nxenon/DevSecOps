[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps)
# [Threat Modeling by OWASP](https://owasp.org/www-community/Threat_Modeling)

## Overview

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

## Objectives of Threat Modeling

- Identify Threats
- Defining countermeasures to prevent or mitigate the effects of threats to the system
- A threat is a potential or actual undesirable event that may be malicious such as:
  - DOS Attack
  - Failure of Storage Device
- Threat modeling is a planned activity for identifying and assessing application threats and vulnerabilities

## Threat Modeling Across the Lifecycle

- Threat modeling is **best** applied  `continuously` throughout a software development.
- Ideally, a high-level threat model should be defined early on in the concept of planing phase
- Threat model should be refind throughout the lifecycle
- `More` details added to the system, `More` attack vectors appear
- The ongoing threat modeling process should `examine`, `diagnose`, and `address` these threats
- Updating threat model is advisable after events such as:
  - A new feature is released
  - Security incidents occurs
  - Architectural or infrastructure changes

## Threat Modeling: Four Question Framework

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

## Structured Threat Modeling Process

[See this](Threat-Modeling-Process-By-OWASP.md)
