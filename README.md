[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps) 
# ♾️ DevSecOps
DevSecOps **Taken Notes** from articles `in addition to` resources for DevSecOps.

# 📝 Notes & Resources
Some links are resources and some links are notes which have been manually taken. Names which have `+` at the beginning, are taken notes.

## 🪜 Design / Plan
**Design** / **Plan** Phase Actions:
- `Threat Models` & `Security Requirements` should be designed and defined
- `Risks` & `Plans` for preventing threats from happening should be identified


### Development Lifecycle
- [+ SDL (Security Development Lifecycle) by Microsoft](./Design/Development-Lifecycle/SDL-by-Microsoft.md)
- [+ How to Ensure Security at the Speed of DevSecOps by Gitlab](./Design/Development-Lifecycle/How-to-Ensure-Security-at-the-Speed-of-DevOps-by-Gitlab.md)
### Threat Model
- [+ Threat Modeling by OWASP](./Design/Threat-Model/Threat-Modeling-by-OWASP.md)
- [+ Structured Threat Modeling Process by OWASP](./Design/Threat-Model/Threat-Modeling-Process-By-OWASP.md)

## 🧑‍💻 Develop
**Develop** Phase Actions:
- `Secure Coding`
- `Static Analysis Security Testing (SAST)`: Can be integrated into developers environment (Find security issues in code)
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

## ⚒️ Build
**Build** Phase Actions:
- `Static Application Security Testing (SAST)`: Find security issues in **code**
- `Software Composition Analysis (SCA)` & `Software Bill of Material (SBOM)`: Find components and compare them against a database like National Vulnerability Database
- `Secret Management`: Find **Secrets**
- `Interactive Application Security Testing (IAST)`: Test in an automated way and find vulnerabilities faster in run-time


### Static Application Security Testing (SAST)
- [+ What Is SAST on Synopsys](./Build/What-Is-SAST-by-Synopsys.md)
- [Beginners Guide to SAST Using SonarQube by Packt.com](https://security.packt.com/beginners-guide-to-static-application-security-testing-sast-using-sonarqube/)
- [SAST Using Snyk and SonarQube by OpenSourceforu.com](https://www.opensourceforu.com/2021/02/devsecops-static-application-security-testing-using-snyk-and-sonarqube/)
### Software Composition Analysis (SCA)
- [+ What is Software Composition Analysis (SCA) on Synopsys](./Build/What-Is-Software-Composition-Analysis-by-Synopsys.md)
- [+ Guide to Software Composition Analysis by Snyk](Build/Guide-to-Software-Composition-Analysis-by-Snyk.md)
### Secret Management
- [Secret Management: Tools & Best Practice by Snyk](https://snyk.io/learn/secrets-management/)
- [Secret Management Cheat Sheet by OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
### Interactive Application Security Testing (IAST)
- [Interactive Application Security Testing (IAST) by Snyk](https://snyk.io/learn/application-security/iast-interactive-application-security-testing/)
- [Interactive Application Security Testing by OWASP](https://owasp.org/www-project-devsecops-guideline/latest/02c-Interactive-Application-Security-Testing)

## 🧪 Test
**Test** Phase Actions:
- `Interactive Application Security Testing (IAST)`: Test in an automated way and find vulnerabilities faster in run-time
  - [See IAST Section](#interactive-application-security-testing-iast)
- `Dynamic Application Security Testing (DAST)`: Evaluate application from `outside` automatically
- `Penetration Testing`: Evaluate application `black box` by ethical hackers

### Dynamic Application Security Testing (DAST)
- [Dynamic Application Security Testing with ZAP and GitHub Actions](https://www.zaproxy.org/blog/2020-05-15-dynamic-application-security-testing-with-zap-and-github-actions/)
- [Dynamic Application Security Testing by Gitlab](https://docs.gitlab.com/ee/user/application_security/dast/)
### Penetration Testing
- [Penetration Testing at DevSecOps Speed](https://www.breachlock.com/resources/blog/penetration-testing-at-devsecops-speed/)

## ⚓ Deploy
**Deploy** Phase Actions:
- `Hardening & Secure Configuration`
- `Security Scanning` 

### Hardening & Secure Configuration
- TODO
### Security Scanning
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
