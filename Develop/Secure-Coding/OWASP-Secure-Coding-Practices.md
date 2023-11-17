# [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
Check list format that can be integrated into the software development lifecycle.

## Introduction
- Generally it is much cheaper to build secure software than fixing security issues.
- Security breaches can have much cost themselves (coding secure, is much better)
- From SANS 2009 Study:
  - More than 60% of attacks on internet, are against web application `(application layer)`
- Developers team should assess their level of secure coding knowledge

## Software Security and Risk Principles Overview
- The goal of software security is to maintain the `confidentiality`, `integrity`, and `availability` of information resources
- Primary focus of this document is web application
- `Risk` is a **combination of factors that threaten the success** of the business
- This can be described conceptually as follows: a `threat agent` interacts with a `system`, which may have a `vulnerability` that can be `exploited` in order to cause an `impact`.
- Client-side controls are good, but not enough!
  - Attackers can bypass client-side controls easily by proxies like Burp
  - The security controls must be implemented in server-side
- Software vulnerabilities can have a scope beyond the software itself:
  - Software and its information
  - Operating System
  - Backend Database
  - Other APPs in a shared environment
  - User's System
  - Other Software that the user interacts with

## Secure Coding Practices Checklist

### Input Validation
1. Perform Data Validation on `Server`
2. Classify data sources into `trusted` or `untrusted`:
   - validate the untrusted data sources
3. There should be a centralized input validation routine for the app
4. Specify proper character sets, such as UTF-8 for all sources
5. Encode data to a common character set before validating
6. All validation failure should result in input rejection
7. Determine if the system supports UTF-8 and if so, validate after UTF-8 decoding is completed
8. Validate client data before processing
   - all parameters
   - headers
   - cookies
   - values
9. Verify that header values in both request and responses contain only ASCII characters
10. Validate data before redirection
11. Validate for expected data types
12. Validate data range
13. Validate data length
14. Validate all input against a `white` list of allowed characters, whenever possible
15. If any `dangerous (Hazardous) character` must be allowed, extra controls like output encoding should be implemented. Examples of hazardous include:
    - `<`, `>`
    - `"`, `'`
    - `%`
    - `(`, `)`
    - `&`
    - `\ `, `\'`, `\"`
16. Extra checks:
    - Null bytes: `%00`
    - New Line Characters: `%0d`, `%0a`, `\r`, `\n`
    - Check for "dot-dot-slash" (`../` or `..\ `)
    - If UTF-8 extended character set encoding is supported:
      - address alternate representation like: `%c0%ae%c0%ae/`

### Output Encoding


### Authentication & Password Management


### Session Management


### Access Control


### Cryptographic Practices


### Error Handling & Logging


### Data Protection


### Communication Security


### System Configuration


### Database Security


### File Management


### Memory Management


### General Coding Practices


## Glossary
- [See OWASP Secure Coding Practices Glossary Section](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
