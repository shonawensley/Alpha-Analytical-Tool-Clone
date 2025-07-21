for _, row in df.iterrows():
        # -------- normalise & sanity‑clean -------------------------
        set_name  = str(row.get("Set",  "") or "").strip()
        draw_name = str(row.get("Draw", "") or "").strip()
        row_type  = str(row.get("RowType", "") or "").strip().upper()
        if not (set_name and draw_name and row_type):
            continue

        # Accept mixed‑case / dashes
        if row_type in {"DRAW_DATA", "DRAW"}:
            row_type = "DRAW_DATA"
        elif row_type.replace("-", "") == "R2":
            row_type = "R2"

        col_values = {str(c): str(row.get(str(c), "")).strip()
                      for c in ["7","6","5","4","3","2","1"]}
        # -----------------------------------------------------------

        draw_node = (
            sect_node["sets"]
            .setdefault(set_name, {})
            .setdefault("draws", {})
            .setdefault(draw_name, {"pattern_variations": {}, "draw_data": {}})
        )

        if row_type == "DRAW_DATA":
            draw_node["draw_data"] = col_values
        else:            # R2, R3, …
            draw_node["pattern_variations"].setdefault(row_type, col_values) 