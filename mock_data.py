#--- MOCK DATA FOR THE AGENTIC INNOVATION ORCHESTRATOR PROTOTYPR ---
#Contains seven distinct demonstration scenarios (GO, NO-GO, and Conditional)

#==========================================================================
#1. POSITIVE PATH: Sertraline for OCD (GO DECISION)
#==========================================================================

MOCK_SUCCESS_DATA = {
    "molecule_id" : "Sertraline",
    "target_area" : "Obsessive-Complusive Disorder (OCD)",
    "status" : "COMPLETED",
    "time_reduction_percentage" : "80%",
    "time_to_concept" : "48 Hours",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "primary_patent_expiry" : "Expired (1997-07-06)",
            "risk_summary" : "IP is clear for repurposing, eliminating a major financial risk."
        },
        "Clinical_Data" : {
            "existing_indications" : "Depression, Panic Disorder, OCD",
            "technical_risk" : "LOW (Robust historical data)",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 43,000 Crore",
            "commercial_rating" : "4.7 / 5 (Strong Buy)",
        },
        "EXIM_Data" : {
            "api_source_country" : "India, China",
            "avg_api_cost_inr" : "₹ 1,25,000 per kg",
        }
    },
    "final_synthesis" : {
        "project_name" : " Generic Sertraline for OCD Repurposing",
        "key_decision" : "GO: IP cleared and high commercial viability.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#2. NEGATIVE PATH 1: Celecoxib (IP KILL-SWITCH)
#==========================================================================

MOCK_FAILURE_DATA = {
    "molecule_id" : "Celecoxib",
    "target_area" : "Novel Anti-inflammatory",
    "status" : "HALATED - IP CONFLICT",
    "time_reduction_percentage" : "100%",
    "time_to_concept" : "2 Hours (Halated)",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "HIGH RISK - CONFLICT",
            "primary_patent_expiry" : "Active (2035-10-20)",
            "risk_summary" : "CRITICAL: Primary synthesis patent is active. **IP Kill-Switch activated.**"
        },
        "Clinical_Data" : {
            "existing_indications" : "MEDIUM",
            "technical_risk" : "None",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 55,000 Crore",
            "commercial_rating" : "3.5 / 5 (Strong Buy)",
        },
        "EXIM_Data" : {
            "avg_api_cost_inr" : "₹ 3,50,000 per kg",
        }
    },
    "final_synthesis" : {
        "project_name" : " Project Celecoxib Repurposing: IP Halated",
        "key_decision" : "NO GO: Kill-Switch activated. Zero resources wasted on futile research.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#3. NEGATIVE PATH 2: Rofecoxib (CLINICAL KILL-SWITCH)
#==========================================================================

MOCK_CLINICAL_FAILURE = {
    "molecule_id" : "Rofecoxib",
    "target_area" : "Advance Pain Relief",
    "status" : "HALATED - CLINICAL RISK",
    "time_reduction_percentage" : "95%",
    "time_to_concept" : "48 Hours (Technical Hault)",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "risk_summary" : "IP is clear."
        },
        "Clinical_Data" : {
            "existing_indications" : "Legacy Anti-inflammatory",
            "technical_risk" : "HIGH (Repeated instances of Severe Adverse Events-SAE in trails)",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 70,000 Crore",
            "commercial_rating" : "5.0 / 5 (Market is huge, but product is unsafe)",
        },
        "EXIM_Data" : {
            "avg_api_cost_inr" : "₹ 2,00,000 per kg",
        }
    },
    "final_synthesis" : {
        "project_name" : " Project Rofecoxib: Clinical Risk Halated",
        "key_decision" : "NO-GO: Technical Kill-Switch activated. High risk of patient harm and FDA failure.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#4. NEGATIVE PATH 3: Pilocarpine (COMMERCIAL KILL-SWITCH)
#==========================================================================

MOCK_COMMERCIAL_FAILURE = {
    "molecule_id" : "Pilocarpine",
    "target_area" : "Alzheimer's Disease",
    "status" : "HALATED - COMMERCIAL RISK",
    "time_reduction_percentage" : "85%",
    "time_to_concept" : "48 Hours (Market Hault)",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "risk_summary" : "IP is clear."
        },
        "Clinical_Data" : {
            "existing_indications" : "MEDIUM",
            "technical_risk" : "MINOR",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 1,50,000 Crore",
            "commercial_rating" : "2.1 / 5 (Strong Competition)",
        },
        "EXIM_Data" : {
            "avg_api_cost_inr" : "₹ 4,00,000 per kg",
        }
    },
    "final_synthesis" : {
        "project_name" : "Project Pilocarpine Repurposing: Market Halated",
        "key_decision" : "NO-GO: High API cost and extreme market competition make ROI unfeasible.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#5. NEGATIVE PATH 4: Albendazole (SUPPLY CHAIN KILL-SWITCH)
#==========================================================================

MOCK_SUPPLY_FAILURE = {
    "molecule_id" : "Albendazole",
    "target_area" : "Tropical Parasite",
    "status" : "HALATED - SUPPLY CHAIN RISK",
    "time_reduction_percentage" : "85%",
    "time_to_concept" : "48 Hours (Supply Halt)",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "risk_summary" : "IP is clear."
        },
        "Clinical_Data" : {
            "technical_risk" : "LOW (Efficiency proven in small trails.)",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 1,200 Crore",
            "commercial_rating" : "4.5 / 5 (Niche Market)",
        },
        "EXIM_Data" : {
            "api_source_country" : "One Country (Unstable Region)",
            "supply_chain_viability": "CRITICAL RISK (Sole supplier in unstable region,high political risk)",
        }
    },
    "final_synthesis" : {
        "project_name" : "Project Albendazole: Supply Risk Halated",
        "key_decision" : "NO-GO: HIgh dependency on a sole, high-risk supplier is a strategic failure point.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#6. REPURPOSING SUCCESS PATH: Metformin (NEW INDICATION GO)
#==========================================================================

MOCK_REPURPOSING_SUCCESS = {
    "molecule_id" : "Metformin",
    "target_area" : "Anti-Aging/Longevity",
    "status" : "COMPLETED",
    "time_reduction_percentage" : "90%",
    "time_to_concept" : "48 Hours",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "primary_patent_expiry" : "Expired (1970s)",
        },
        "Clinical_Data" : {
            "existing_indications" : "Diabetes, PCOS",
            "technical_risk" : "LOW (Extremely large safety profile)",
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 2,00,000 Crore (Forecasted)",
            "commercial_rating" : "5.0 / 5 (Massive, emerging market)",
        },
        "EXIM_Data" : {
            "api_source_country" : "Global",
            "avg_api_cost_inr" : "₹ 15,000 per kg (Very Cheap)",
        }
    },
    "final_synthesis" : {
        "project_name" : " Generic Metformin for Longevity",
        "key_decision" : "GO: Zero IP risk, high market viability, and established safety. Launch immediately.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}

#==========================================================================
#7. CONDITIONAL GO PATH: Toxin-Z (REGULATORY WARNING)
#==========================================================================

MOCK_CONDITIONAL_SUCCESS = {
    "molecule_id" : "Toxin-Z",
    "target_area" : "Autoimmune Disorder",
    "status" : "COMPLETED - WARNING",
    "time_reduction_percentage" : "70%",
    "time_to_concept" : "48 Hours",
    "results" : {
        "Patent_Landscape" : {
            "ip_conflict_status" : "LOW RISK",
            "risk_summary" : "IP is clear."
        },
        "Clinical_Data" : {
            "technical_risk" : "HIGH - REGULATORY PENDING",
            "safety_note" : "Regulatory agent flags pending 'Black Box' warning from FDA based on recent phase IV trial data."
        },
        "IQVIA_Market_Insights" : {
            "current_market_size_inr" : "₹ 60,000 Crore",
            "commercial_rating" : "4.0 / 5",
        },
        "EXIM_Data" : {
            "avg_api_cost_inr" : "₹ 2,50,000 per kg",
        }
    },
    "final_synthesis" : {
        "project_name" : "Project Toxin-Z: Conditional Go",
        "key_decision" : "HOLD: Conditional GO. Requires immediate Human Regulatory Review (HRR) on pending FDA warning.",
        "pitch_deck_link" : "/pitch-deck-mock"
    }
}
