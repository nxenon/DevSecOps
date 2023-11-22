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
77. Use only trusted system objects, e.g. server side session objects, for making access authorization decisions
78. Use a single site-wide component to check access authorization. This includes libraries that call external authorization services
79. Access controls should fail securely
80. Deny all access if the application cannot access its security configuration information
81. Enforce authorization controls on every request, including those made by server side scripts, "includes" and requests from rich client-side technologies like AJAX and Flash
82. Separate privileged logic from other application code
83. Restrict access to `files` or `other resources`, including those `outside` the application's direct control, to only authorized users
84. Restrict access to `protected URLs` to only authorized users
85. Restrict access to `protected functions` to only authorized users
86. Restrict `direct object references` to only authorized users
87. Restrict access to `services` to only authorized users
88. Restrict access to `application data` to only authorized users
89. Restrict access to `user and data attributes` and `policy information` used by access controls
90. Restrict access security-relevant configuration information to only authorized users
91. Server side implementation and presentation layer representations of access control rules must match
92. If state data must be stored on the client, use `encryption` and `integrity` checking on it
93. Enforce application login flows to comply with business rules 
94. Limit the number of transactions a single user or device can perform in a given period of time
95. Use the "referer" header as a `supplemental check` only, it should never be the sole authorization check, as it can be spoofed
96. If long authenticated sessions are allowed, periodically re-validate a user’s authorization to ensure that `their privileges have not changed` and if they have, log the user out and force them to re-authenticate
97. Implement account auditing and enforce disable of unused accounts
    - e.g. After no more than 30 days from the expiration of an account’s password
98. the application must support disabling of accounts and terminating sessions when authorization ceases
99. Service accounts or accounts supporting connections to or from external systems should have the least privilege possible
100. Create an Access Control Policy to document an application's business rules, data types and access authorization criteria and/or processes so that access can be properly provisioned and controlled. This includes identifying access requirements for both the data and system resources

### Cryptographic Practices
101. All cryptographic functions must be implemented on a trusted e.g. `server`
102. Protect master secrets from unauthorized access
103. Cryptographic modules should fail securely
104. All random numbers, random file names, random GUIDs, and random string should be generated using the cryptographic module's approved random number generator when these random values are intended to be un-guessable
105. Cryptographic modules used by the application should be compliant to `FIPS 140-2` or an equivalent standard
106. Establish and utilize a policy and process for how cryptographic keys will be managed

### Error Handling & Logging
107. Do not disclose information in error messages, including system details, session identifiers or account information
108. Use error handlers that do not display debugging or stack trace information
109. Implement generic error messages and use custom error pages
110. The application should handle application errors and not rely on server configuration
111. Properly free allocated memory, when error conditions error
112. Error handling logic associated with security controls should `deny access by default`
113. All logging controls should be implemented on a trusted system e.g. `server`
114. Logging controls should support both success and failure of specified security events
115. Ensure logs contain important `log event data`
116. Ensure log entries that include un-trusted data will not execute as code in the intended log viewing interface or software
117. Restrict access to logs to only authorized individuals
118. Utilize a master routine for all logging operations
119. Do not store sensitive information in logs, including `unnecessary system details`, `session IDs` or `passwords`
120. Ensure that a mechanism exists to conduct log analysis
121. Log all `input validation failures`
122. Log all **authentication attempts**, `especially failures`
123. Log all `access control failures`
124. Log all `tempering events`, including unexpected changes to state data
125. Log attempts to connect with `invalid` or `expired` session tokens
126. Log all `system exceptions`
127. Log all `administrative functions`, including changes to the security configuration settings 
128. Log all `backend TLS connection failures`
129. Log `cryptographic module failures`
130. Use a cryptographic hash function to validate log entry integrity

### Data Protection
131. implement [least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)
     - user must only access to things that really needs
132. Protect all `cached` or `temporary` copies of sensitive data stored on the server from unauthorized access and purge those temporary working files as soon as they are no longer required
133. Encrypt highly `sensitive stored information`, like authentication verification data, even on the server side. Always use well vetted algorithms, see "Cryptographic Practices" for additional guidance
134. Protect server-side source code from being downloaded by a user
135. Do not store `passwords`, `connection strings` or other `sensitive information` in **clear text** or in any non-cryptographically secure manner on the client side
136. Remove `comments` in user accessible production code that may reveal backend or other sensitive information
137. Remove unnecessary application and system documentation as this can reveal useful information to attackers
138. Do not include sensitive information in `HTTP GET` request parameters
139. Disable `auto complete features` on forms expected to contain sensitive information
140. Disable `client side caching` on pages containing sensitive information. `Cache-Control: no-store`, may be used in conjunction with the HTTP header control `Pragma: no-cache`, which is less effective, but is HTTP/1.0 backward compatible
141. The application should `support the removal of sensitive data` when that data is no longer required
142. Implement appropriate access controls for sensitive data stored on the server. This includes cached data, temporary files and data that should be accessible only by specific system users

### Communication Security
143. Implement encryption for the `transmission` of all sensitive information
144. TLS certificates should be `valid` and have the `correct domain name`, `not be expired`, and be `installed with intermediate certificates` when required
145. Failed TLS connections `should not fall back` to an insecure connection
146. Utilize TLS connections for all content requiring authenticated access and for all other sensitive information
147. Utilize TLS for connections to external systems that involve sensitive information or functions
148. Utilize a single standard TLS implementation that is configured appropriately 
149. Specify character encodings for all connections 
150. Filter parameters containing sensitive information from the `HTTP referer`, when linking to external sites

### System Configuration
151. Ensure servers, frameworks and system components are `running the latest version`
152. Ensure servers, frameworks and system components have `all patches issued` for the version in use
153. Turn off `directory listings`
154. Restrict the web server, **process and service accounts** to the `least privileges possible`
155. When <u>exceptions occur</u>, fail securely
156. Remove all unnecessary functionality and files
157. Remove <u>test code</u> or any functionality `not intended for production`, prior to deployment
158. Prevent <u>disclosure of your directory structure</u> in the `robots.txt` file by placing directories not intended for public indexing into an isolated parent directory. Then "Disallow" that entire parent directory in the robots.txt file rather than Disallowing each individual directory
159. `Define which HTTP methods`, GET or POST, the application will support and whether it will be handled differently in different pages in the application
160. <u>Disable unnecessary HTTP methods</u>, such as `WebDAV extensions`. If an extended HTTP method that supports file handling is required, utilize a well-vetted authentication mechanism
161. if the web server **handles both** `HTTP 1.0` and `1.1`, ensure that both are configured in a similar way or ensure that you understand any difference that may exist (e.g. handling of extended HTTP methods)
162. Remove unnecessary information from HTTP response `headers` related to the `OS`, `web-server version` and `application frameworks`
163. The security configuration store for the application should be able to be output in `human-readable` form to support auditing
164. Implement an `asset management` system and register <u>system components and software</u> in it
165. Isolate Production environment and Development environment (network)
     - test or Development environments are often less secure
     - test environment must be access only by authorized test groups
166. Implement a `software change control system` to manage and record changes to the code both in development and production

### Database Security
167. Use strongly `typed parameterized queries`
168. Utilize `input validation` and `output encoding` and be sure to address meta characters. <u>If these fail, do not run the database command</u>
169. Ensure that variables are `strongly typed`
170. The application should use the `lowest` possible <u>level of privilege</u> when accessing the database
171. Use secure credentials for database access
172. <u>Connection strings</u> `should not be hard coded within the application`. Connection strings should be stored in a **separate configuration file** on a trusted system, and they should be `encrypted`.
173. Use stored procedures to abstract `data access` and allow for the removal of permissions to the base tables in the database
174. `Close the connection` <u>as soon as possible</u>
175. Remove or change all `default database administrative passwords`. Utilize strong passwords/phrases or implement `multi-factor authentication`
176. <u>Turn off</u> all `unnecessary database functionality` 
     - (e.g., unnecessary stored procedures or services, utility packages, install only the minimum set of features and options required (surface area reduction))
177. <u>Remove</u> unnecessary `default vendor content` (e.g., sample schemas)
178. <u>Disable</u> any `default accounts` that are not required to support business requirements
179. The application should connect to the database with `different credentials` for every trust distinction (e.g., user, read-only user, guest, administrators)

### File Management


### Memory Management


### General Coding Practices


## Glossary
- [See OWASP Secure Coding Practices Glossary Section](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
