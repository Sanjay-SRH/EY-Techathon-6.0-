from flask import Flask, jsonify, request, render_template
import time
from datetime import datetime

from mock_data import (
    MOCK_SUCCESS_DATA, MOCK_FAILURE_DATA, MOCK_CLINICAL_FAILURE, MOCK_COMMERCIAL_FAILURE, 
    MOCK_SUPPLY_FAILURE, MOCK_CONDITIONAL_SUCCESS, MOCK_REPURPOSING_SUCCESS
)

app = Flask(__name__)
# MASTER AGENT SIMULATION LOGIC
@app.route('/vetting-process', methods=['POST'])
def run_vetting_simulation():
    """Selects one of the seven mock scenarios based on the Molecule ID input."""
    data = request.get_json()
    molecule = data.get('molecule', 'N/A').strip().lower()

    simulation_duration = 3
    output_data = MOCK_SUCCESS_DATA.copy()
    #Conditional Logic to Select Mock Data (Case-Insensitive Check)
    if molecule == 'sertraline':
        output_data = MOCK_SUCCESS_DATA.copy()
    elif molecule == 'toxin-z' :
        output_data = MOCK_CONDITIONAL_SUCCESS.copy()
    elif molecule == 'celecoxib':
        simulation_duration = 1
        output_data = MOCK_FAILURE_DATA.copy()
    elif molecule == 'rofecoxib':
        output_data = MOCK_CLINICAL_FAILURE.copy()
    elif molecule == 'pilocarpine':
        output_data = MOCK_COMMERCIAL_FAILURE.copy()
    elif molecule == 'albendazole':
        output_data = MOCK_SUPPLY_FAILURE.copy()
    elif molecule == 'metformin':
        output_data = MOCK_REPURPOSING_SUCCESS.copy()
    

    time.sleep(simulation_duration)

    output_data["molecule_id"] = data.get('molecule', 'N/A').strip()
    output_data["target_area"] = data.get('target', 'N/A')

    return jsonify(output_data)

# FRONTEND ENDPOINTS

@app.route('/')
def index():
    """Renders the main input page."""
    return render_template('index.html')

@app.route('/pitch-deck-mock')
def pitch_deck_mock():
    """Renders the mock report. Uses the success data as a default."""
    molecule_name = request.args.get('molecule', 'sertraline').strip().lower()
    target_area = request.args.get('target', 'General Research')

    if molecule_name == 'sertraline':
        report_data = MOCK_SUCCESS_DATA.copy()
    elif molecule_name == 'toxin-z' :
        report_data = MOCK_CONDITIONAL_SUCCESS.copy()
    elif molecule_name == 'celecoxib':
        simulation_duration = 1
        report_data = MOCK_FAILURE_DATA.copy()
    elif molecule_name == 'rofecoxib':
        report_data = MOCK_CLINICAL_FAILURE.copy()
    elif molecule_name == 'pilocarpine':
        report_data = MOCK_COMMERCIAL_FAILURE.copy()
    elif molecule_name == 'albendazole':
        report_data = MOCK_SUPPLY_FAILURE.copy()
    elif molecule_name == 'metformin':
        report_data = MOCK_REPURPOSING_SUCCESS.copy()

    report_data["molecule_id"] = molecule_name.capitalize()
    report_data["target_area"] = target_area
    now = datetime.now().strftime("%B %d, %Y | %I:%M %p")
    return render_template('pitch_deck_mock.html', data=report_data, current_time = now)

@app.route('/pitch-deck-mock-fail')
def pitch_deck_mock_fail():
    """Renders the mock report for a failure scenario."""
    return render_template('pitch_deck_mock.html', data=MOCK_FAILURE_DATA)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)