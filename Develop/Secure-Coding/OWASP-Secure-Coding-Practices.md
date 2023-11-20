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
17. all encoding on a trusted system e.g., `the Server`
18. Utilize a standard method for each type of output encoding
19. Encode output `based on the context` it will be in.
20. Encode all characters unless they are known to be safe for the intended interpreter
21. Sanitize output of un-trusted data to queries based on `context` e.g. SQL, XML, LDAP
22. Sanitize output of un-trusted data to `OS Commands`

### Authentication & Password Management
23. Require Authentication for `all routes & resources`, except for those which intented to be public
24. All authentication controls must be enforced on a trusted system e.g. `Server`
25. Use and implement standard, tested auth services
26. Use a `centralized implementation` for all auth controls, including libraries that call external auth services
27. `Separate` authentication logic and the resource being requested and use redirection to and from centralized auth control
28. All authentication controls should fail securely
29. All administrative and account management functions must be at least as secure as the primary auth mechanism
30. If application stores credential
    - Ensure using only `cryptographically strong one-way salted` hashes of password
    - Password table and keys are `write-able` only by application
    - `Do not use MD5`
31. Password hashing must be implemented on a trusted system, e.g. `Server`
32. Validate authentication data only on completion of all data input
    - Especially when the authentication mechanism is sequential (steps by steps, and order is important)
33. Authentication failure process should not show which part was incorrect.
    - Instead of 'invalid username' or 'invalid password', just show `Invalid username and/or password`
    - Errors must be identically in both `display and source code`
34. Use authentication when using external systems, if they involve sensitive information
35. Authentication credentials for accessing services should be stored in a protected location on a trusted system (e.g. `Server`)
    - Source code is not a secure location
36. Use only HTTP POST Request to transit authentication credentials
37. Only send non-temporary passwords over an encrypted connection or as encrypted data, such as in an encrypted email. Temporary passwords associated with email resets may be an exception
38. Enforce password complexity requirements based on policy or regulations.
39. Enforce password length requirements based on policy or regulations.
40. Password entry should be hidden on the user's system
41. Enforce account disabling after an established number of invalid login attempts
    - account must be locked temporary
    - but not so long to allow Denial of Service attack
42. Password reset and changing operations require the same level of controls as account creation and authentication.
43. Password reset questions should support sufficiently random answers. (e.g., "favorite book" is a bad question because “The Bible” is a very common answer)
44. If using email based resets, only send email to a pre-registered address with a temporary link/password
45. Temporary links and password should have short expiration time
46. Enforce the changing of temporary passwords on the next use
47. `Notify users when a password reset occurs`
48. Prevent password `re-use`
49. Passwords should be at least one day old before they can be changed, to prevent attacks on password re-use
50. Enforce password changes based on requirements in a policy or regulations.
    - Critical systems may require more frequent changes
51. Disable `remember me` functionality for password fields
52. The last successful or unsuccessful of a user account should be reported to the user at the next successful login
53. implement monitoring to identify attacks against multiple user accounts, using same password.
54. Change all vendor-supplied default passwords and user IDs or disable associated accounts
55. Re-authenticate users prior to performing critical operations
    - e.g. get password before changing e-mail, password &...
56. Use Multi-Factor Authentication for highly sensitive accounts
57. If using third party code for authentication, inspect the code carefully to ensure it is not affected by any malicious code

### Session Management
58. Use the server or framework's session management controls.
59. Session identifier creation must always be done on a trusted system e.g. `Server`
60. Session management controls should use well vetted algorithms that ensure sufficiently random session identifiers
61. Set the `domain` and `path` for cookies containing authenticated session identifiers to an appropriately restricted value for the site
62. Logout functionality should `fully` terminate the associated session or connection
63. Logout functionality should be available from `all pages protected by authorization`
64. Establish a session inactivity timeout that is a short as possible
    - Balance `Risk` & `Business Functional` requirement\
    - In most cases, it should be `no more than several hours`
65. Disallow persistent logins and enforce periodic session terminations, even when the session is active
    - user should receive notification to mitigate negative impact
66. If a session was established before login:
    - close the session first
    - then establish a new session
67. Generate a new session ID on any re-authentication
68. Do not allow concurrent logins with the same user ID
69. Do not expose session IDs in `URLs`, `error messages` or `logs`
    - session IDs should only be located in HTTP Cookie header.
    - Do not pass it as a GET parameter
70. Protect server side session data from unauthorized access: `appropriate access control on server`
71. Generate a new session ID and deactivate the old ones periodically: `avoid session hijacking`
72. generate new session ID if the connection changes from HTTP to HTTPS
73. Supplement standard session management for sensitive server-side operations, like account management, by utilizing per-session strong random tokens or parameters. This method can be used to prevent Cross Site Request Forgery attacks
74. Supplement standard session management for highly sensitive or critical operations by utilizing per-request, as opposed to per-session, strong random tokens or parameters
75. Set the `secure` attribute for cookies transmitted ofr HTTPS
76. Set cookies with the `HttpOnly` attribute, unless you specifically require client-side access to cookie

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
