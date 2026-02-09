# Project Proposal

## 1. Project Identification
- **Project Title: CPT Program Discord Bot (Student Support Bot)
- **Course: CPT 298 01
- **Term: Spring 2026
- **Student Name(s): Ayden Sturtevant, Ian Broshes, Darian Mongiovi
- **Primary Contact: Discord
- **Proposed Start Date: Pending Approval
- **Proposed End Date: TBD
---

## 2. Project Selection & Motivation
Our group selected to do a CPT program Discord bot. This project is going to be designed to support the CPT program by creating a practical internal
automation tool that would also align with real world IT tasks. The intent of this first project is to apply previously learned skills throughout the CPT
program and apply it to a realistic environment while also contributing to the development and management of the internal CPT network.

Discord is already the primary communication platform for us CPT students. However commonly requested program information (eg. resources, links, contact details, and general help/guidance, etc.) 
is often repeated across channels and different conversations. This creates a very unnecessary overhead for staff and student workers and can also possibly lead to inconsistent responses.

By building an internal Discord bot, our group can have a center point for frequently asked questions and provide students with quick, reliable access to approved sources.
---

## 3. Problem Statement
Currently CPT students rely on manual responses from instructors, staff, or peers to answer routine program related questions.
The current approach: 
* Does not scale well as student participation grows
* Leads to possible duplicated effort
* Can result in outdated or inconsistent information

The CPT program would greatly benefit from a lightweight, maintainable automation tool that can provide standardized responses and act as a single source of truth
for common CPT program information.
---

## 4. Proposed Solution Overview
To address this problem, our group proposes building an internal Discord bot that runs within the CPT internal environemnt and provides automated responses to 
common CPT program questions.

This bot will use a command based interface to deliver approved CPT information such as helpful resources, links, answers to FAQs, and general guidance. All data returned by the bot will be stored
in a centralized and maintainable format (database or structured config files), which would allow updates without modifying core bot logic.

The bot will be deployed on a CPT internal Linux vm and designed with clear doccumentation so future students would be able to maintain or extend it. By automating common info requestsm the bot will reduce
repetitive workload, increase the consistency of responses, and provide students with faster access to reliable CPT resources.
---

## 5. Technical Stack & Tools

- **Operating System(s): Linux (CPT Internal VM)
- **Programming Language(s): Python 3
- **Frameworks / Libraries: Discord.py
- **Databases / Storage: PostgreSQL, or possible alternative of structured local files
- **Infrastructure (VMs, containers, etc.): The bot will be deployed on a CPT internal Linux vm and run as a managed background service. Containerization (Docker) would be 
considred only if approved and appropriate for long term use.
- **Tools (Git, CI, monitoring, APIs, etc.): Git and GitHub for version control and team colaboration, environment variables for secure config and secrets management, basic logging
for monitoring and troubleshooting, and the discord API for bot communication.
---

## 6. Prerequisite Knowledge & Skills
This project builds upon previous skills I have learned throughout the CPT program. I have prior experience with Python scripting, Git/GitHub, and working within Linux environments, as well as 
direct experience creating a Discord bot for a previous Python class project. Additional skills that may need to be learned include production style deployment, service management, and 
secure config practices within the CPT internal network. -Ayden

Working with discord bots in the past I have experience with automating responses for user inputs, and writing functions that take user input. SQL is a interest of mine as I innitially started IT studies with data analytics programs. Designing creative database schemas that can provide students with relevant reasources based on simple inputs is a motivating challenge. I have experience writting DDL code to define a database, and DQL code for the bot to use for queries. -Darian
---

## 7. Project Scope & Deliverables
The scope of the project is going to mainly limited to designing, implementing, and deploying a functional Discord bot within the CPT internal environment. The bot will provide 
command based informational responses using a centralized and maintainable data source. Development will mainly focus on reliabilitym clarity, and documentation rather than advanced or 
experimental features. Though if time permits, more features are subject to be added.

Deliverables for this project include a GitHub repository containing the completed proposal, all source code, config files, and the documentation required to understand, deploy, and maintain the bot.
A final presentation will also be completed with each group member participatiing as required.
---

## 8. Milestones & Timeline
Phase 1: Planning and Setup
Finalize project requirements and scope
Fork and complete the project proposal
Set up development environment and version control

Phase 2: Core Development
Implement core functionality
Develop command based responses
Integrate the chosen data storage method

Phase 3: Deployment and Testing
Deplot the bot to the CPT internal environment
Test functionality, permissions, and reliability
Address possible bugs and stability issues

Phase 4: Documentation and Presentation
Finish project documentation and setup guides
Prepare final demonstration and presentation
Then finally participate in scheduled presentation
---

## 9. Risks, Constraints & Dependencies
Risks:
Possible delays relating to access or approval for CPT internal infastructure
Misconfiguration of Discord permissions or bot credentials
Limited Time

Contraints:
Deployment must remain within the CPT internal environment
Project must follow the approved scope and proposal
No handling of sensitive or personal student data

Dependencies:
Approval of the project proposal
Access to a CPT internal vm
Creation and approval of a Discord app and bot token
---

## 10. Security, Ethics & Safety Considerations
Authentication and Authorization:
The bot will authenticate using a Discord bot token and operate under the principle of least privlage. No user authentication beyond standard Discord permissions will be implemented.

Data Sensitivity:
The bot will not store, process, or access sesitive or personal student data. All information provided will be purely informational.

Network Exposure:
The bot will be deployed within the CPT internal environment and will not expose any additional network services or open ports beyond that of which is required for Doscord communication.

Logging, Monitoring, or Automation Impact:
Basic logging will be implemented for troubleshooting, and operational awareness. There will be no automated actions that could negativly impact users.

Ethical Considerations:
The bot will provide answers and guidance only and will not ever act as a moderator or replace offical CPT communications. Its functionality will be limited in scope and designed to avoid 
misuse.
---

## 11. Team Structure (If Applicable)
If working in a group, describe:
- Roles are very equal, we all hold resposability for working on code and making suggestions on overall structure.
- Currently we are using discord to communicate about initial structures. A github repository will be set up to handle code revisions.
- Simple voting to resolve any ambiguity issues. Goals are very cleared and structured. We will stick to a set of packages and tools to avoid technical conflicts.
- The project can be parsed out into different functions needed so members can focus on strong suits weather it be sql, or web apis.

---

## 12. Documentation & Knowledge Transfer Plan
The project documentation will be maintained within the GitHub repository and include setup instructions, config details, and some basic troubleshooting guidance. The 
documentation will be written so that future CPT students can deploy, maintain, and extend the bot without needing direct assistance from the original development team.
And required internal knowledgebase documentation will also be completed as specidfied.
---

## 13. Faculty/cpt.internal Resources Requested
Access to a CPT internal Linux vm

Permission to create and configure a Discord app and bot token

Access to an internal PostgreSQL database, if approved and available

And any other permissions required in order to properly deploy our bit wihtin the CPT internal network

---

## 14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:
- This is a self-directed technical project
- I am responsible for research and troubleshooting
- Evaluation will consider process, documentation, and professionalism

**Signature (Name & Date):**

Student 1:  __Ayden Sturtevant__________________________ Date: _02/07/2026______________
Student 2:  __Darian Mongiovi___________________________ Date: _02/07/2026______________
Student 3:  ____________________________ Date: _______________
Student 4:  ____________________________ Date: _______________

Instructor: ____________________________ Date: _______________
