[<img src="https://github.com/nxenon/DevSecOps/assets/61124903/07f55353-3a61-4340-844b-af61ec1fe1f5" width="75%" valign="middle" alt="DevSecOps" />&nbsp;&nbsp;](https://github.com/nxenon/DevSecOps)
# [What Is Software Composition Analysis](https://www.synopsys.com/glossary/what-is-software-composition-analysis.html)
- 📝 Taken notes from "What Is Software Composition Analysis" BY Synopsys  



Software composition analysis (SCA) is an automated process that `identifies the open source software in a codebase`.
This analysis is performed to `evaluate security`, `license compliance`, and `code quality`.

Companies need to be aware of `open source license limitations and obligations`. 
Tracking these obligations manually became too arduous of a task,
and it often overlooked code and its accompanying vulnerabilities.
An automated solution, SCA, was developed, and from this initial use case,
it expanded to analyze code security and quality. 

In a modern DevOps or DevSecOps environment, SCA has galvanized the `“shift left”` paradigm.
Earlier and continuous SCA testing has enabled developers 
and security teams to drive productivity without compromising security and quality. 

## 🛠️ How Does Software Composition Analysis Work?
- SCA tools inspect:
  - package managers
  - manifest files
  - source code
  - binary files
  - container images
  - &...
- Software is compiled `Bill of Materials (BOM)` to be compared against a variety of databases, including `NVD`
- SCA tools can also compare BOMs against other (usually commercial) databases to discover licenses associated with the code and analyze overall code quality
  - History of contribution
  - version control
- By comparing BOM against a database, security team can find security issues and act quickly to fix them

## ❗ Why Is Software Composition Analysis Important?
- SCA offers `security`, `speed`, and `reliablility`.
- Manual tracking of open source code is no longer sufficient
- The increasing prevalence of cloud-native applications and more-complex applications make robust and dependable SCA tools a necessity
