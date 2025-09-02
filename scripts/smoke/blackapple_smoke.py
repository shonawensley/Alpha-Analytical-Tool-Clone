from modules.blackapple import analyze_blackapple, ba_status_label

DRAWS = ["162","407","538","924","153","874","260","317","482","795"]
ba = analyze_blackapple(DRAWS)
print("BA Score:", ba.get("score"))
print("Status:", ba_status_label(ba.get("score", 0)))
print("Triggers:", ba.get("triggers"))
print("Top 3:", ba.get("candidates", [])[:3])
