# [What Is Static Application Security Testing](https://www.synopsys.com/glossary/what-is-sast.html)
- 📝 Taken notes from "What Is Static Application Security Testing" BY Synopsys  

Static application security testing (SAST), or static analysis,
is a testing methodology that analyzes source code to find security vulnerabilities
that make your organization’s applications susceptible to attack.
SAST scans an application before the code is compiled. It’s also known as white box testing.

## 🛠️ What Problems Does SAST Solve?
- SAST is in very early place in the SDLC
- SAST works without code getting executed
- Developers can find vulnerability faster, fix them faster `before` taking place in the production
- SAST tools can give feedback do developers `when they are actively coding`
- SAST tools can provide graphical representation of the issues found, from `source` to `sink`
- SAST tools can also provide guidance for solving the security issues
- SAST tools must be run on the application on a regular basis
  - during daily/monthly builds

## ❗ Why Is SAST an Important Security Activity
- Developers dramatically are more than security staff
- A key strength of SAST tools is the ability to analyze 100% of the codebase.
- It is faster than manual code reviews done by humans
- They can scan millions of lines of code in a matter of minutes
- They automatically find vulnerabilities such as:
  - buffer overflows
  - SQL injection
  - cross site scripting (XSS)
  - and...

## 🗝️ What Are the Key Steps to Run SAST Effectively?
- Finalize the Tool
  - select the SAST tool based on the programming language you are using
  - it should be able to scan your underlying framework too
- Create the Scanning Infrastructure & Deploy the Tool
  - provide access
  - licensing
  - database
  - server
- Customize the Tool
  - write new rules
  - updating existing rules based on your needs
  - create dashboards
  - tracking scan results
  - build custom reports
- Prioritize & Onboard Applications
  - Scan high priority applications first
- Analyse Scan Results
  - remove false positives
  - after issued finalized, they must be provided to the development teams
- Provide Governance & Training
  - You should ensure that the development team is using the SAST tools effectively
  - regular training can be highly effective
