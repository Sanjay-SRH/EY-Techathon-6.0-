-----
💊 EY Innovation Orchestrator: Autonomous Molecule Vetting
*Accelerating Time-to-Concept through Agentic AI Orchestration*
📖 Project Overview
The EY Innovation Orchestrator is a functional technology prototype designed to automate the manual, 3-6 month pharmaceutical vetting process for drug repurposing. By utilizing an agentic multi-agent framework, the system collapses the research cycle into a simulated **48-hour window**, delivering an **80% reduction in Time-to-Concept**.
Key Innovation: The IP Kill-Switch
Our solution features an integrated **IP Kill-Switch**. If the Patent Agent identifies an active conflict or legal blocker, the Master Orchestrator immediately halts all research threads to prevent wasted R\&D spend.
-----
📐 System Architecture
The solution follows a modular 3-tier architecture:
1.  Presentation Layer: A Flask-based web dashboard (HTML5/CSS3) for scientist input and real-time agent tracking.
2.  Orchestration Layer: A Python Master Agent that manages parallel task delegation and final data synthesis.
3.  Execution Layer (Specialized Agents):** Five worker agents operating in parallel:
      * Patent Agent: Scans for IP clearance and expiry dates.
      * Clinical Agent: Reviews historical safety and Phase III success.
      * IQVIA Market Agent: Calculates commercial ratings and market sizing.
      * Web Agent: Reviews scientific literature and trend evidence.
      * EXIM Data Agent: Checks API supply chain viability and costing.
----
🛠️ Installation & Setup
1\. Prerequisites
* **Python 3.8+** installed.
* A web browser (Chrome or Edge recommended).

2\. Install Dependencies
Run this in your terminal to install the core framework:
```
pip install flask flask-cors reportlab
```
3\. Start the Backend Server
Navigate to the project folder and run:
```
python app.py
```
*Note: The terminal must stay open for the frontend to communicate with the agents.*
4\. Launch the Dashboard

Open `(http://127.0.0.1:5000)` in your browser to interact with the system.

-----
🚀 Testing the Demo

|       Scenario       | Input Molecule |       Expected Outcome        |          Result Metrics          |
| -------------------- | -------------- | ----------------------------- | -------------------------------- |
| **Success Case**     | `Sertraline`   | Full vetting cycle completes. | **4.7/5 Rating**, ₹43k Cr Market |
| **Kill-Switch Case** | `Celecoxib`    | **IP Kill-Switch** triggers.  | Cycle stops; Status: **HALTED**  |

-----
📊 Outputs
The system produces an automated **Product Pitch Deck (PDF)**. This report synthesizes:
  * A final **GO/NO-GO** recommendation.
  * Quantitative commercial potential scores.
  * Validated time-savings metrics (80% reduction).

-----
Since it is a Prototype i have given 7 Molecule names in the mock_data.py You can use them for testing the prototype.
I am also providing the molecule_id and the Target Therapeutic Area

| Molecule ID|         Target Therapeutic        |
|------------|-----------------------------------|
|Sertraline  |Obsessive-Complusive Disorder (OCD)|
|Celecoxib   |Novel Anti-inflammatory            |
|Rofecoxib   |Advance Pain Relief                |
|Pilocarpine |Alzheimer's Disease                |
|Albendazole |Tropical Parasite                  |
|Metformin   |Anti-Aging/Longevity               |
|Toxin-Z     |Autoimmune Disorder                |

After running any of these names you have to click the "Initiate Autonomous Vetting Cycle" then the process will start and give you details of the vetting cycle and the after that if you scroll down you will find a button "Download Final Product Pitch Deck"
if you click that you will be redirected to the new tab in your browser and you will be able to see a dropdown asking to download you can dowload it as a PDF and save the information.



NOTE:-
1. Dear sir/mam i am sorry for not submitting the video. The reason is i have not been notified for the detailed submission as soon as i was selected. I was notified 5 days prior to the submission deadline.
2. due to that there are few things missing, photos of me and my teammate and the recorded video.
3. Please consider this since we worked so hard in this 5 days of time,
   hope you like our prototype and shortlist us to the next stage of the compitition.
