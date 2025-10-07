import sys
from pathlib import Path
root = Path(__file__).resolve().parent
src = root / "src"
if str(src) not in sys.path:
    sys.path.insert(0, str(src))
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

import os
import importlib.util as _iu

from _import_hygiene import project_modules_first as _pmf

w_state2 = "Connecticut4"
mid_win = "894"
eve_win = "059"

try:
    with _pmf():
        try:
            sys.modules.pop("modules")
            sys.modules.pop("modules.winner_report_full")
        except KeyError:
            pass
        try:
            from modules.winner_report_full import write_winner_full_report
        except Exception as _ie:
            _wr_path = os.path.join(str(root), 'modules', 'winner_report_full.py')
            print('fallback path', _wr_path)
            if os.path.exists(_wr_path):
                _spec = _iu.spec_from_file_location('modules.winner_report_full_fallback', _wr_path)
                if _spec and _spec.loader:
                    _mod = _iu.module_from_spec(_spec)
                    _spec.loader.exec_module(_mod)
                    write_winner_full_report = getattr(_mod, 'write_winner_full_report', None)
            if not callable(locals().get('write_winner_full_report', None)):
                raise
    generated = []
    if len(mid_win) == 3 and mid_win.isdigit():
        p_mid = write_winner_full_report(w_state2, mid_win)
        generated.append(("Midday", p_mid))
    if len(eve_win) == 3 and eve_win.isdigit():
        p_eve = write_winner_full_report(w_state2, eve_win)
        generated.append(("Evening", p_eve))
    for label, path_out in generated:
        print(label, path_out, os.path.relpath(path_out))
except Exception as e:
    import traceback
    traceback.print_exc()
    print('error:', e)
