<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp; 
# ♾️ DevSecOps
DevSecOps **Taken Notes** from articles `in addition to` resources for DevSecOps.

# 📝 Notes & Resources
Some links are resources and some links are notes which have been manually taken. Names which have `+` at the beginning, are taken notes.

## 🪜 Design / Plan
In **Design** / **Plan** Phase:
- `Threat Models` & `Security Requirements` should be designed and defined
- `Risks` & `Plans` for preventing threats from happening should be identified


### Development Lifecycle
- [+ SDL (Security Development Lifecycle) by Microsoft](./Design/Development-Lifecycle/SDL-by-Microsoft.md)
- [+ How to Ensure Security at the Speed of DevSecOps by Gitlab](./Design/Development-Lifecycle/How-to-Ensure-Security-at-the-Speed-of-DevOps-by-Gitlab.md)
### Threat Model
- [+ Threat Modeling by OWASP](./Design/Threat-Model/Threat-Modeling-by-OWASP.md)
- [+ Structured Threat Modeling Process by OWASP](./Design/Threat-Model/Threat-Modeling-Process-By-OWASP.md)

## 🧑‍💻 Develop
In **Develop** Phase:
- `Secure Coding` should be determined
- `Static Analysis Security Testing (SAST)` can be integrated into developers environment
  - when developer is actively coding (e.g. a SAST IDE Plugin)


### Secure Coding
- [+ OWASP Secure Coding Practices](./Develop/Secure-Coding/OWASP-Secure-Coding-Practices.md)
### SAST in Developer's Environment
- [SonarLint](https://www.sonarsource.com/products/sonarlint/)
  - [Using SonarLint with SonarQube in Intellij IDE](https://medium.com/@tarunchhabra/using-sonarlint-with-sonarqube-in-intellij-ide-5128111d1b8d)
  - [Real-time Code Quality Scan with SonarLint in Visual Studio Code](https://medium.com/@dijin123/real-time-code-quality-scan-with-sonarlint-in-visual-studio-code-64c3c7b34131)
- [Semgrep](https://semgrep.dev/)
  - [Semgrep on Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=Semgrep.semgrep)
  - [Semgrep Plugin Page on Jetbrains](https://plugins.jetbrains.com/plugin/22622-semgrep)
- [Snyk](https://snyk.io/)
  - [Snyk Plugin in Visual Studio Code](https://docs.snyk.io/integrate-with-snyk/use-snyk-in-your-ide/visual-studio-code-extension)
    - [Snyk VS Code Plugin Configuration](https://docs.snyk.io/integrate-with-snyk/use-snyk-in-your-ide/visual-studio-code-extension/visual-studio-code-extension-configuration)
  - [Snyk Plugin in Jetbrains](https://docs.snyk.io/integrate-with-snyk/use-snyk-in-your-ide/jetbrains-plugins)
    - [Snyk Jetbrains Plugin Configuration](https://docs.snyk.io/integrate-with-snyk/use-snyk-in-your-ide/jetbrains-plugins/configuration-environment-variables-and-proxy-for-the-jetbrains-plugins)

# ⚒️ Build
In **Build** Phase:
  - `Static Application Security Testing (SAST)` should be used to find security issues in code
  - `Software Composition Analysis (SCA)` & `Software Bill of Material (SBOM)` should be done to find components and compare them against a database like National Vulnerability Database
  - `Secret Management` should be implemented to find **Secrets** in code
  - `Interactive Application Security Testing (IAST)` should be performed to test in an automated way and find vulnerabilities faster in run-time


### Static Application Security Testing (SAST)
- [+ What Is SAST on Synopsys](./Build/What-Is-SAST-by-Synopsys.md)
- [Beginners Guide to SAST Using SonarQube by Packt.com](https://security.packt.com/beginners-guide-to-static-application-security-testing-sast-using-sonarqube/)
- [SAST Using Snyk and SonarQube by OpenSourceforu.com](https://www.opensourceforu.com/2021/02/devsecops-static-application-security-testing-using-snyk-and-sonarqube/)
### Software Composition Analysis (SCA)
- [+ What is Software Composition Analysis (SCA) on Synopsys](./Build/What-Is-Software-Composition-Analysis-by-Synopsys.md)
### Secret Management
- TODO
### Interactive Application Security Testing (IAST)
- TODO

# 🔗 Other Resources
- [Open Source Security Report by Snyk](https://snyk.io/reports/open-source-security/)

# ⛏️ DevSecOps Tools
Useful tools in DevSecOps + Notes

## Vulnerability Management
### DefectDojo
- [+ DefectDojo Installation & Setup Notes](./Tools/DefectDojo/Install-Setup.md)

# 🔃 Reference
- [DevSecOps Roadmap](https://github.com/hahwul/DevSecOps)
