# ♾️ DevSecOps
DevSecOps **Taken Notes** from articles `in addition to` resources for DevSecOps.

# 📝 Notes & Resources
Some links are resources and some links are notes which have been manually taken.

## 🪜 Design / Plan
In **Design** / **Plan** Phase:
- `Threat Models` & `Security Requirements` should be designed and defined
- `Risks` & `Plans` for preventing threats from happening should be identified


### Development Lifecycle
- [SDL (Security Development Lifecycle) by Microsoft](./Design/Development-Lifecycle/SDL-by-Microsoft.md)
- [How to Ensure Security at the Speed of DevSecOps by Gitlab](./Design/Development-Lifecycle/How-to-Ensure-Security-at-the-Speed-of-DevOps-by-Gitlab.md)
### Threat Model
- [Threat Modeling by OWASP](./Design/Threat-Model/Threat-Modeling-by-OWASP.md)
- [Structured Threat Modeling Process by OWASP](./Design/Threat-Model/Threat-Modeling-Process-By-OWASP.md)

## 🧑‍💻 Develop
In **Develop** Phase:
- `Secure Coding` should be determined
- `Static Analysis Security Testing (SAST)` can be integrated into developers environment
  - when developer is actively coding (e.g. a SAST IDE Plugin)


### Secure Coding
- [OWASP Secure Coding Practices](./Develop/Secure-Coding/OWASP-Secure-Coding-Practices.md)
### SAST in Developer's Environment
- [SonarLint](https://www.sonarsource.com/products/sonarlint/)
- [Semgrep](https://semgrep.dev/)
- [Snyk](https://snyk.io/)

# ⚒️ Build
In **Build** Phase:
  - `Static Application Security Testing (SAST)` should be used to find security issues in code
  - `Software Composition Analysis (SCA)` & `Software Bill of Material (SBOM)` should be done to find components and compare them against a database like National Vulnerability Database
  - `Secret Management` should be implemented to find **Secrets** in code
  - `Interactive Application Security Testing (IAST)` should be performed to test in an automated way and find vulnerabilities faster in run-time


### Static Application Security Testing (SAST)
- TODO
### Software Composition Analysis (SCA)
- TODO
### Secret Management
- TODO
### Interactive Application Security Testing (IAST)
- TODO

# ⛏️ DevSecOps Tools
Useful tools in DevSecOps + Notes

## Vulnerability Management
### DefectDojo
- [DefectDojo Installation & Setup Notes](./Tools/DefectDojo/Install-Setup.md)

# 🔃 Reference
- [DevSecOps Roadmap](https://github.com/hahwul/DevSecOps)
