# Categorize Action Types 
jump_shots = ["Jump Shot", "Running Jump Shot", "Pullup Jump shot", "Step Back Jump shot",
              "Floating Jump shot", "Turnaround Jump Shot", "Running Pull-Up Jump Shot",
              "Turnaround Fadeaway Bank Jump Shot", "Driving Jump shot", "Turnaround Fadeaway shot",
              "Fadeaway Jump Shot", "Driving Floating Jump Shot", "Turnaround Fadeaway Bank Jump Shot"]

bank_shots = ["Jump Bank Shot", "Turnaround Bank shot", "Driving Floating Bank Jump Shot",
              "Step Back Bank Jump Shot", "Fadeaway Bank shot", "Hook Bank Shot", "Driving Bank shot",
             "Pullup Bank shot"]

layup_shots = ["Layup Shot", "Driving Layup Shot", "Running Layup Shot", "Cutting Layup Shot",
          "Finger Roll Layup Shot", "Putback Layup Shot", "Alley Oop Layup shot",
          "Driving Reverse Layup Shot", "Running Finger Roll Layup Shot", "Running Alley Oop Layup Shot",
          "Running Reverse Layup Shot", "Reverse Layup Shot", "Driving Finger Roll Layup Shot",
          "Tip Layup Shot", "Cutting Finger Roll Layup Shot"]

dunk_shots = ["Dunk Shot", "Driving Dunk Shot", "Putback Dunk Shot", "Alley Oop Dunk Shot",
         "Running Dunk Shot", "Reverse Dunk Shot", "Tip Dunk Shot", "Running Alley Oop Dunk Shot",
         "Running Reverse Dunk Shot", "Cutting Dunk Shot", "Driving Reverse Dunk Shot"]

hook_shots = ["Driving Hook Shot", "Turnaround Hook Shot", "Turnaround Bank Hook Shot", "Driving Bank Hook Shot",
         "Running Hook Shot", "Hook Shot", "Hook Bank Shot"]

# Map function
def categorize_shot(action):
    if action in jump_shots:
        return "Jump Shot"
    elif action in bank_shots:
        return "Bank Shot"
    elif action in layup_shots:
        return "Layup Shot"
    elif action in dunk_shots:
        return "Dunk Shot"
    elif action in hook_shots:
        return "Hook Shot"
    else:
        return "Other"