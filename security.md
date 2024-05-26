# Security
This section gives a cyber security risk assessment for the company and recommended security controls.

[Risk Assesment](#risk-assessment) | [Security Controls](#security-controls) | [Plan](./plan.md) | [Network Design](./network.md) | [Cloud Services](./cloud.md) | [Reflection](./reflection.md) | [Return to index](./README.md)

## Risk Assessment  
[View risk assessment spreadsheet](./images/risk_assessment_WinstonShoeb.xlsx)    


Based on the template of Week9, I will identify the asset, security threats, and the vulnerability. There are a total of 3 tables to display the cyber security risk assessment of network.  
**asset**   
I Identify the following asset. There are whole 4 asset type: data, hardware, software, network. In addition,there are 4 different data assets considered: customer information, sales data, financial information, employee records.
| Asset Type | Asset                         |
|------------|-------------------------------|
|Data | Customer Information|
|Data| Sales Data |
|Data| Financial Information|
|Data|Employee Records|
|Hardware| Servers|
|Hardware| Computers and Laptops|
|Hardware| Routers and Switches|
|Software| Business Software Systems|
|Software| Restaurant and Business Software|
|Network| Firewalls|

**Threats**   
There are 11 of the 12 information security threats included:   People errors,Software attacks,Information extortion,Espionage and trespass,Theft,Technological obsolescence,Forces of nature,Technical hardware failures or errors,Technical software failures or errors,Changing quality of services,Sabotage and vandalism.  



**Vulnerability**   
Based on the above information and the numbering of vulnerability, asset, and treat, this is overview of the vulnerability .
| AssetType               | Asset                        | Threat                    | Vulnerability                                              |
|-------------------------|------------------------------|---------------------------|------------------------------------------------------------|
| Data                    | Customer Information         | People errors             | Employee accidentally made an error while entering user information         |
| Data                    | Customer Information         | Software attacks          | Software attacks causing consumer data errors                       |
| Data                    | Sales Data                   | Theft                     | Disgruntled employees maliciously destroy and steal sales data to sell to competitors  |
| Data                    | Sales Data                   | Sabotage and vandalism    | Disgruntled employees maliciously destroy and steal sales data to sell to competitors  |
| Data                    | Financial Information         | Software attacks          | Finance information has been subjected to house arrest attacks            |
| Data                    | Financial Information         | Technological obsolescence | Due to backward technology, financial information’s ability to defend against attacks has declined. |
| Data                    | Financial Information         | Information extortion      | Someone uses finance information for ransomware                       |
| Data                    | Financial Information         | Espionage and trespass     | Competitors illegally intrude to obtain financial information                   |
| Data                    | Employee Records              | People errors             | HR accidentally made an error while entering employee information              |
| Hardware                | Servers                      | Forces of nature          | Server damage caused by earthquake, rainstorm, and other force majeure              |
| Hardware                | Computers and Laptops        | Theft                     | Computers, laptops, and other hardware have been stolen                    |
| Hardware                | Computers and Laptops        | Technological obsolescence | Software and hardware failures caused by outdated technology                  |
| Hardware                | Computers and Laptops        | Technical hardware failures or errors | Software and hardware failures caused by incorrect use                  |
| Hardware                | Routers and Switches          | Changing quality of services | The instability of routers causes network fluctuations                     |
| Software                | Business Software Systems     | Software attacks          | Business Software Systems is experiencing network attacks leading to malfunctions          |
| Software                | Restaurant and Business Software | People errors          | New employees are not familiar with Restaurant and Business Software, resulting in errors   |
| Software                | Restaurant and Business Software | Technological obsolescence | The Restaurant and Business Software version is too old, causing some software functions to be unavailable and errors to occur |
| Software                | Restaurant and Business Software | Technical software failures or errors | The Restaurant and Business Software version is too old, causing some software functions to be unavailable and errors to occur |
| Network                | Firewalls                     | Software attacks          | The firewall has been attacked by hackers.                             |
| Network                | Firewalls                     | Information extortion      | The firewall has been attacked by hackers and subjected to ransom and extortion          |




## Security Controls

Based on the previous risk assessment, the data asset with the highest risk is "Financial Information." It faces the following risks:    

**Software attacks:**   (Finance information has been subjected to house arrest attacks)  
**Technological obsolescence:**  (Due to backward technology, financial information’s ability to defend against attacks has declined.)  
**Information extortion:**   (Someone uses finance information for ransomware)  
**Espionage and trespass:**   (Restaurant competitors illegally intrude to obtain financial information)  
To reduce these risks, the following security controls are recommended:

**1.Multi-Factor Authentication (MFA):**  
***How to reduce risk***  
1. Implement high level MFA requirements in the office area to access the financial information. Only allow authenticated employees, such as managers or above to access the financial information and financial server. 
2. Require manager and above to register MFA in the system to ensure that their accounts have an additional authentication to enhance access security.  

***Details***     
1. MFA settings should only be implemented on servers in the office area to keep sure that access to financial information is just through high-level authentication.    
2. Provide training and support to all employees to make sure that they understand the importance of MFA. Choose an MFA solution, such as SMS verification codes.    
3. Network design requires the use of network isolation to separate servers in the office area from other network areas, ensuring that only authenticated individuals can access financial information. Implement MFA for management personnel and above, restricting their access to network segments containing financial information.  

**2.Firewall:**  
***How to reduces risk***  
The firewall has been deployed across the entire network boundary, but it could be strengthened, specifically in office areas and security room network segments (as there are financial server, sale server and so on here). Strengthen firewall to keep sure that only authorized employee can access the financial information and financial serve.

***Details***
1. Add new specific access controls to firewall rules that only allow managers and above can access servers in the office area, and ensure restrict unauthorized access.  
2.Upgrade firewall rules to adapt to new threats and vulnerabilities regularly.
3. Monitor firewall logs regularly. In addition, detect and handle abnormal access and behaviors promptly  

**Disadvantages for Users:**  

***MFA:***  
1. Increase complexity: It results in that when employees view data and informations through MFA, they will find that the MFA process is more complex and time-consuming.  
2. Learning difficulty: Introducing and using MFA will take users some time to learn and adapt to new rules, resulting in potential learning costs    
**Firewalls:**  
1. Impact network speed: Strengthen firewall rules could increase scrutiny of network which could affect network speed and performance.    
2. Remote access issue: Due to the advanced firewall restrictions, managers or stakeholders working remotely could be restricted to access financial data remotely.    
