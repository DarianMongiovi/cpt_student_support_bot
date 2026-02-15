# Project Proposal

## 1. Project Identification
- **Project Title: CMCC Academic & Athletics Calender Data Integration
- **Course: CPT 298 01
- **Term: Spring 2026
- **Student Name(s): Ayden Sturtevant, Ian Broshes, Darian Mongiovi, Daniel Lukonda
- **Primary Contact: Discord
- **Proposed Start Date: Pending Approval
- **Proposed End Date: TBD
---

## 2. Project Selection & Motivation
Our group selected this project as it directly supports the CPT program while also applying practical skills in data integration, database management, and automation. 
Academic calender data, O365 events, and athletic schedules currently exist in seperate systems and formats (PFD, JSON, or Excel), which can make it difficult to manage consistently.

By automating the extraction and integration of these sources into a centralized PostgreSQL database, we create a unified and most importantly a maintainable warehouse. This project 
reflects real world IT practices such as APU integration, file parsing, schema design, and automated data processing while directly contributing to CPT infrastructure.
---

## 3. Problem Statement
Academic calender data, O365 events, and athletic schedules are stored across multiple platforms and formats which includes PDF, JSON, .ics, and Excel. Because these sources are 
seperate and structured differently. there is no centralized or automated method to manage this data.

This lack of integration limits consistency, query capability, and long term maintainability. An automated process is needed to consolidate these sources into a structured
PostgreSQL database.
---

## 4. Proposed Solution Overview
To address this problem, our group proposes developing a ETL (Extract, Transform, Load) pipeline that collects calender data from multiple sources and integrates it into
a centralized PostgreSQL database within the CPT internal environment.

The process will extract data from the academic calender JSON output, O365 events, and athletic schedules (.ics or other structured formats), normalize the data into a consistent
schema, and then load it into the database. This solution creates a unified and maintainable warehouse that supports reliable storage, quering, and future automation.
---

## 5. Technical Stack & Tools

- **Operating System(s): Linux (CPT Internal VM)
- **Programming Language(s): Python 3
- **Frameworks / Libraries: O365, ics and or icalender, pandas, psycopg
- **Databases / Storage: PostgreSQL, or possible alternative of structured local files
- **Infrastructure (VMs, containers, etc.): The ETL process will run on a CPT internal Linux machine and may be executed manually or scheduled as an automated task depending on 
approval and scope.
- **Tools (Git, CI, monitoring, APIs, etc.): Git and GitHub for version control and team colaboration, environment variables for secure config and secrets management, basic logging
for monitoring and troubleshooting, and external APIs required for O365 integration.
---

## 6. Prerequisite Knowledge & Skills
This project builds on skills developed throughout the CPT program, including Python scripting, database fundamentals, and working within Linux environments. I have prior experience with Python development, structured data processing, and SQL, as well as using Git/GitHub for version control.. working with external APIs (O365), parsing .ics calendar files, refining database schema design, and implementing automated ETL processes within the CPT internal environment. - Ayden

Working with discord bots in the past I have experience with automating responses for user inputs, and writing functions that take user input. SQL is a interest of mine as I innitially started IT studies with data analytics programs. Designing creative database schemas that can provide students with relevant reasources based on simple inputs is a motivating challenge. I have experience writting DDL code to define a database, and DQL code for the bot to use for queries. -Darian
---

## 7. Project Scope & Deliverables
The scope of this project will be mainly limited to designing, implementing, and deploying an automated ETL pipeline that will aggregate academic and athletic calender data into a PostgreSQL
database within the CPT internal environment. Development will mainly focus on reliable data extraction, normalization into consistent schema, and accurate database integration.

Deliverables for this project include a GitHub repository containing the completed proposal, all source code, database schema definitions, config files, and the documentation required to deploy and maintain the integration process. A final live demonstration of the working pipeline will also be completed with each group member participating as required.
---

## 8. Milestones & Timeline
Phase 1: Planning & Design
Finalize project requirements and data sources
Design PostgreSQL database schema
Set up development environment and repository

Phase 2: Data Extraction
Implement data ingestion from academic calendar JSON
Integrate O365 calendar access
Parse athletics schedules from .ics or other structured formats

Phase 3: Data Transformation & Integration
Normalize data into a consistent schema
Implement database insertion and update logic
Test data accuracy and consistency

Phase 4: Automation & Deployment
Deploy the ETL process to the CPT internal environment
Implement scheduled execution (if approved)
Perform final testing and validation

Phase 5: Documentation & Presentation
Complete documentation and setup guides
Prepare final demonstration
Deliver project presentation
---

## 9. Risks, Constraints & Dependencies
Risks:
Changes or inconsistencies in source data formats (PDF JSON output, O365 API responses, or .ics files)
API authentication or permission issues with O365
Data normalization challenges when combining multiple calendar sources
Limited time within the half semester project window

Constraints:
Deployment must remain within the CPT internal environment
The project must follow the approved scope and proposal
No modification of original source systems, only data ingestion and storage

Dependencies:
Approval of the project proposal
Access to a CPT internal Linux VM
Access to an internal PostgreSQL database
Proper credentials and permissions for O365 and calendar data sources
---

## 10. Security, Ethics & Safety Considerations
Authentication and Authorization:
Access to O365 and the PostgreSQL database will require proper credentials and permissions. API tokens and database credentials will be stored securely using environment variables and will not be hardcoded in the source code.

Data Sensitivity:
The project will process calendar event data only. No sensitive personal or academic records (such as grades or private student information) will be accessed or stored.

Network Exposure:
The ETL process will run within the CPT internal environment and will not expose additional network services or open ports beyond what is required for approved API communication and database access.

Logging, Monitoring, or Automation Impact:
Basic logging will be implemented for troubleshooting and data validation. The process will perform read only extraction from source systems and controlled inserts/updates into the database to prevent unintended system impact.

Ethical Considerations:
The system will aggregate data for organizational purposes only and will not modify original source systems. All access to external services will comply with institutional policies and approved permissions.
---

## 11. Team Structure (If Applicable)
If working in a group, describe:
- Roles are very equal, we all hold resposability for working on code and making suggestions on overall structure.
- Currently we are using discord to communicate about initial structures. A github repository will be set up to handle code revisions.
- Simple voting to resolve any ambiguity issues. Goals are very cleared and structured. We will stick to a set of packages and tools to avoid technical conflicts.
- The project can be parsed out into different functions needed so members can focus on strong suits weather it be sql, python, or web apis.
---

## 12. Documentation & Knowledge Transfer Plan
Project documentation will be maintained within the GitHub repository and will include setup instructions, database schema definitions, configuration requirements, and execution procedures for the ETL process. Documentation will clearly describe data sources, transformation logic, and database structure to ensure future CPT students can maintain or extend the integration pipeline without direct assistance from the original group. Any required internal knowledgebase documentation will also be completed as specified.
---

## 13. Faculty/cpt.internal Resources Requested
Access to a CPT internal Linux virtual machine for development and deployment

Access to an internal PostgreSQL database instance

Appropriate credentials and permissions for O365 calendar access

Access to athletics calendar data (.ics files or approved alternative source)

Any additional permissions required to securely integrate and test data within the CPT internal environment

## 14. Acknowledgement of Expectations
By submitting this proposal, I acknowledge that:
- This is a self-directed technical project
- I am responsible for research and troubleshooting
- Evaluation will consider process, documentation, and professionalism

**Signature (Name & Date):**

Student 1:  __Ayden Sturtevant__________________________ Date: _02/07/2026______________
Student 2:  __Darian Mongiovi___________________________ Date: _02/07/2026______________
Student 3:  __Ian Broshes______________________________ Date: _02/09/2026______________
Student 4:  _______Daniel Lukonda_____________________ Date: _02/09/2026______________

Instructor: ____________________________ Date: _______________
