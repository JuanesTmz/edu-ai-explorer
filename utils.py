import re
from datetime import datetime, timedelta


def render_message(text: str) -> str:
    """Convierte un subconjunto simple de markdown (negritas, listas, párrafos) a HTML."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    blocks = [b for b in text.split("\n\n") if b.strip() != ""]
    html_blocks = []
    for block in blocks:
        lines = [l for l in block.split("\n") if l.strip() != ""]
        if lines and all(l.strip().startswith("- ") for l in lines):
            items = "".join(f"<li>{l.strip()[2:].strip()}</li>" for l in lines)
            html_blocks.append(f"<ul class='msg-list'>{items}</ul>")
        else:
            html_blocks.append(f"<p class='msg-p'>{'<br>'.join(lines)}</p>")
    return "".join(html_blocks)


_BASE_TIME = datetime(2024, 1, 1, 8, 0)


def fake_timestamp(index: int) -> str:
    """Genera una hora ficticia incremental para dar sensación de chat real."""
    t = _BASE_TIME + timedelta(minutes=index * 2)
    hour = t.strftime("%I:%M").lstrip("0")
    suffix = "a.m." if t.hour < 12 else "p.m."
    return f"{hour} {suffix}"
