import time

import streamlit as st

from expediciones import EXPEDICIONES
from utils import render_message, fake_timestamp

st.set_page_config(
    page_title="La Expedición del Docente",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

TEXT_ON_COLOR = {1: "#FFFFFF", 2: "#FFFFFF", 3: "#FFFFFF", 4: "#FFFFFF", 5: "#15321F"}
TINT = {1: "#FFE9FD", 2: "#F2E3FF", 3: "#DEF5F8", 4: "#FFE9D9", 5: "#DCFCE9"}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

:root {
    --bg-app: #F4F6FB;
    --text-dark: #1B2340;
    --text-muted: #767A8C;
    --border: #E7EAF3;
    --primary: #35BFFF;
    --tip-bg: #FFFBEA;
    --tip-border: #E8C90A;
}

.stApp { background: var(--bg-app); }
.block-container { padding-top: 0 !important; padding-bottom: 2rem; }
h1,h2,h3,h4 { font-family:'Space Grotesk',sans-serif !important; color:var(--text-dark) !important; }
p,li,span,div { font-family:'Inter',sans-serif !important; }
#MainMenu,footer { visibility:hidden; }

/* Header stays in the DOM (it holds the "reopen sidebar" arrow when the
   sidebar is collapsed) but is made invisible/click-through except for
   that one control, which must stay usable. */
header[data-testid="stHeader"] {
    background:transparent !important;
    box-shadow:none !important;
    pointer-events:none;
}
header[data-testid="stHeader"] [data-testid="stAppDeployButton"],
header[data-testid="stHeader"] [data-testid="stMainMenu"] {
    visibility:hidden;
}
/* stToolbarActions (the native "running" spinner) stays visible and
   click-through, themed by .streamlit/config.toml instead of overridden here. */
header[data-testid="stHeader"] [data-testid="stToolbarActions"] {
    visibility:visible;
    pointer-events:none;
}
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"] {
    visibility:visible;
    pointer-events:auto;
    background:#EEF8FF;
    border-radius:8px;
    margin:6px;
}
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"]:hover {
    background:#D9F1FF;
}
/* Restore the Material Symbols icon font (the global `span` rule above
   otherwise turns icon ligatures into literal text like
   "keyboard_double_arrow_right"), and color the arrow so it reads as a button. */
[data-testid="stIconMaterial"] {
    font-family:"Material Symbols Rounded" !important;
}
header[data-testid="stHeader"] [data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"] {
    color:var(--primary) !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background:#FFFFFF;
    border-right:1px solid var(--border);
}
section[data-testid="stSidebar"] .block-container { padding:0 !important; }

.sb-header {
    padding:18px 16px 14px;
    border-bottom:1px solid var(--border);
    text-align:center;
}
.sb-logo { font-size:1.5rem; margin-bottom:3px; }
.sb-title { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:0.88rem; color:var(--text-dark); }
.sb-sub { font-size:0.63rem; color:var(--text-muted); margin-top:1px; }

.sb-course {
    padding:12px 16px 11px;
    border-bottom:1px solid var(--border);
}
.sb-course-row { display:flex; justify-content:space-between; align-items:baseline; margin-bottom:5px; }
.sb-course-label { font-size:0.65rem; font-weight:700; text-transform:uppercase; letter-spacing:0.4px; color:var(--text-dark); }
.sb-course-val { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:0.74rem; color:var(--primary); }

.progress-track { background:var(--border); border-radius:99px; height:5px; overflow:hidden; }
.progress-fill  { height:100%; border-radius:99px; transition:width .4s ease; }

.sb-list-label {
    padding:10px 16px 3px;
    font-size:0.59rem; font-weight:700; letter-spacing:1px; text-transform:uppercase;
    color:var(--text-muted);
}

/* expedition card */
.exp-sc {
    margin:3px 10px;
    padding:9px 11px;
    border-radius:10px;
    border:1.5px solid var(--border);
    background:#FAFBFD;
}
.exp-sc.sc-active   { border-color:var(--exp-color,var(--primary)); background:#FFF; box-shadow:0 2px 10px rgba(0,0,0,.06); }
.exp-sc.sc-done     { border-color:#E8C90A; background:#FFFCF0; }
.exp-sc.sc-locked   { opacity:.38; pointer-events:none; }

.sc-top { display:flex; align-items:center; gap:8px; }
.sc-icon { font-size:1rem; flex-shrink:0; }
.sc-info { flex:1; min-width:0; }
.sc-num  { font-size:0.58rem; font-weight:700; text-transform:uppercase; letter-spacing:.4px; color:var(--text-muted); }
.sc-name { font-family:'Space Grotesk',sans-serif; font-size:0.79rem; font-weight:600; color:var(--text-dark); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.sc-chip { flex-shrink:0; font-size:0.57rem; font-weight:700; padding:2px 6px; border-radius:99px; text-transform:uppercase; white-space:nowrap; }
.chip-done   { background:#FFF3CC; color:#8A6D00; }
.chip-active { background:#EEF8FF; color:#0A6A96; }
.chip-open   { background:#F0F2FA; color:#555A70; }
.chip-lock   { background:#F0F2FA; color:#A0A4B4; }

.sc-prog-row { display:flex; align-items:center; gap:5px; margin-top:6px; }
.sc-pct { font-size:0.59rem; color:var(--text-muted); flex-shrink:0; width:26px; text-align:right; }

section[data-testid="stSidebar"] .stButton { margin:2px 10px 3px 10px; }
section[data-testid="stSidebar"] .stButton > button {
    width:100% !important; background:#EEF8FF !important; color:#0A6A96 !important;
    border:1.5px solid #B3E4FF !important; border-radius:8px !important;
    padding:6px 10px !important; font-size:0.76rem !important; font-weight:600 !important;
    box-shadow:none !important; text-align:center !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background:#D9F1FF !important; border-color:#35BFFF !important;
}

.sb-badge-row { display:flex; align-items:center; gap:7px; padding:5px 16px; }
.sb-badge-icon { font-size:.95rem; }
.sb-badge-name { font-size:.74rem; color:var(--text-dark); }

/* ── CHAT SHELL ──────────────────────────────────────────────────────────
   Real chat layout: header and response options stay in place; only the
   messages in the middle scroll. `chat_scroll_region` is a native
   Streamlit fixed-height container (height=… in Python), which already
   handles internal scrolling — this just strips its default box so it
   reads as a seamless continuation of the header/footer panels. */
.st-key-chat_scroll_region {
    background:#FFFFFF;
    padding:0 !important;
    border-radius:0 !important;
}
.st-key-chat_scroll_region > div { gap:0 !important; }

/* ── CHAT HEADER (fixed) ── */
.chat-header {
    width:100%;
    background:#FFFFFF;
    border:1px solid var(--border);
    border-radius:20px 20px 0 0;
    border-bottom:2px solid var(--border);
    padding:13px 24px 12px;
    box-shadow:0 6px 24px rgba(27,35,64,.10);
    display:flex;
    align-items:center;
    gap:13px;
}
.ch-av {
    width:40px; height:40px; border-radius:50%; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:.82rem;
}
.ch-info { flex:1; min-width:0; }
.ch-name {
    font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:.94rem;
    color:var(--text-dark); display:flex; align-items:center; gap:6px; flex-wrap:wrap;
}
.ch-exp-tag { font-size:.6rem; font-weight:600; padding:2px 7px; border-radius:99px; white-space:nowrap; }
.ch-status { font-size:.7rem; color:var(--text-muted); display:flex; align-items:center; gap:5px; margin-top:2px; }
.ch-dot { width:7px; height:7px; border-radius:50%; background:#2ECC71; display:inline-block; flex-shrink:0; }

/* ── CHAT BODY ── */
.chat-body {
    width:100%;
    background:#FFFFFF;
    border-left:1px solid var(--border);
    border-right:1px solid var(--border);
    padding:14px 28px 10px;
}
.chat-cap {
    width:100%;
    height:6px; background:#FFFFFF;
    border:1px solid var(--border); border-top:none;
    box-shadow:0 4px 14px rgba(27,35,64,.04);
}

/* ── OPTIONS ZONE (fixed footer) ── */
.opts-zone {
    width:100%;
    background:#F8F9FC;
    border:1px solid var(--border); border-top:2px solid var(--border);
    border-radius:0 0 20px 20px;
    padding:10px 28px 16px;
    box-shadow:0 -4px 14px rgba(27,35,64,.04);
}
.opts-label { font-size:.67rem; font-weight:700; text-transform:uppercase; letter-spacing:.5px; color:var(--text-muted); margin-bottom:8px; }

/* ── MESSAGE BUBBLES ── */
.msg-row { display:flex; align-items:flex-end; gap:9px; margin:14px 0 2px; }
.msg-row.user-row { justify-content:flex-end; }
.msg-col { display:flex; flex-direction:column; max-width:76%; }
.msg-col.user-col { align-items:flex-end; }
.avatar { width:30px; height:30px; border-radius:50%; flex-shrink:0; display:flex; align-items:center; justify-content:center; font-size:.62rem; font-family:'Space Grotesk',sans-serif; font-weight:700; }
.avatar.agent-av { color:#fff; }
.avatar.user-av  { background:#EDF0F8; font-size:1rem; }
.bubble { padding:11px 15px; line-height:1.55; font-size:.91rem; color:var(--text-dark); }
.bubble.agent-bubble { background:#fff; border:1px solid var(--border); border-radius:4px 16px 16px 16px; box-shadow:0 2px 8px rgba(27,35,64,.04); }
.bubble.user-bubble  { border-radius:16px 4px 16px 16px; font-weight:500; }
.bubble .msg-p { margin:0 0 8px; }
.bubble .msg-p:last-child { margin-bottom:0; }
.bubble .msg-list { margin:4px 0 8px 18px; padding:0; }
.bubble .msg-list:last-child { margin-bottom:0; }
.bubble strong { font-weight:700; }
.msg-time { font-size:.65rem; color:var(--text-muted); margin:3px 2px 0; }

/* ── TYPING ── */
.typing-row { display:flex; align-items:flex-end; gap:9px; margin:10px 0; }
.typing-bubble { background:#fff; border:1px solid var(--border); border-radius:4px 16px 16px 16px; padding:13px 16px; display:flex; gap:5px; }
.typing-bubble .dot { width:7px; height:7px; border-radius:50%; background:#B7BCD0; animation:tb 1.2s ease-in-out infinite; }
.typing-bubble .dot:nth-child(2) { animation-delay:.15s; }
.typing-bubble .dot:nth-child(3) { animation-delay:.3s; }
@keyframes tb { 0%,60%,100%{transform:translateY(0);opacity:.5;} 30%{transform:translateY(-5px);opacity:1;} }

/* ── LAYER DIVIDER ── */
.layer-divider { text-align:center; margin:20px 0 14px; }
.layer-pill { display:inline-block; padding:5px 15px; border-radius:20px; font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:.67rem; letter-spacing:1.4px; text-transform:uppercase; }

/* ── TIP ── */
.tip-card { background:var(--tip-bg); border:1.5px dashed var(--tip-border); border-radius:12px; padding:12px 14px; margin:12px 0; display:flex; gap:9px; }
.tip-icon { font-size:1rem; flex-shrink:0; }
.tip-label { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:.69rem; color:#8A6D00; text-transform:uppercase; letter-spacing:.8px; margin-bottom:3px; }
.tip-text { font-size:.81rem; color:#5C4A00; line-height:1.5; }

/* ── BADGE CARD ── */
.badge-card { background:linear-gradient(135deg,#FFF8E1,#FFEFC2); border:2px solid #F4C430; border-radius:18px; padding:24px; margin:14px auto; max-width:720px; text-align:center; box-shadow:0 6px 20px rgba(244,196,48,.18); }
.badge-card h3 { color:#8A6D00 !important; margin:4px 0 2px; }
.badge-card .badge-emoji { font-size:2.5rem; display:block; margin-bottom:4px; }
.badge-card .badge-name { font-size:.98rem; color:var(--text-dark); font-weight:600; }
.badge-card .badge-sub  { font-size:.77rem; color:var(--text-muted); margin-top:5px; }

/* ── MAIN BUTTONS ── */
.stButton > button {
    background:#FFFFFF !important; color:var(--text-dark) !important;
    border:1.5px solid var(--border) !important; border-radius:14px !important;
    padding:10px 16px !important; font-family:'Inter',sans-serif !important;
    font-size:.86rem !important; text-align:left !important;
    white-space:normal !important; height:auto !important;
    line-height:1.4 !important; box-shadow:none !important; transition:all .2s !important;
}
.stButton > button:hover { border-color:var(--primary) !important; background:#F3FBFF !important; }

/* ── HERO ── */
.hero-shell { max-width:900px; margin:28px auto 0; }
.hero-panel {
    background:radial-gradient(circle at top left,rgba(53,191,255,.18),transparent 35%),
               radial-gradient(circle at bottom right,rgba(159,29,237,.16),transparent 30%),
               linear-gradient(135deg,#FFFFFF,#F9FBFF);
    border:1px solid var(--border); border-radius:24px;
    box-shadow:0 16px 48px rgba(27,35,64,.08); padding:32px;
}
.hero-kicker { display:inline-flex; align-items:center; gap:7px; padding:6px 12px; border-radius:999px; background:#EEF8FF; color:#146A92; font-size:.72rem; font-weight:700; letter-spacing:.8px; text-transform:uppercase; }
.hero-title { font-family:'Space Grotesk',sans-serif !important; font-size:clamp(1.8rem,3.5vw,3rem); line-height:1.08; margin:14px 0 12px; color:var(--text-dark); }
.hero-title .accent { background:linear-gradient(135deg,#35BFFF,#9F1DED); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.hero-copy { max-width:68ch; color:var(--text-muted); font-size:.94rem; line-height:1.7; }
.hero-grid { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:12px; margin-top:22px; }
.hero-card { background:rgba(255,255,255,.85); border:1px solid var(--border); border-radius:16px; padding:15px 15px 17px; }
.hero-card .eyebrow { font-size:.68rem; font-weight:700; letter-spacing:.8px; text-transform:uppercase; color:#8A6D00; margin-bottom:7px; }
.hero-card p { margin:0; color:var(--text-dark); line-height:1.55; font-size:.87rem; }
.hero-footer { margin-top:18px; display:flex; flex-wrap:wrap; gap:8px; }
.hero-footer span { background:#FFFFFF; border:1px solid var(--border); border-radius:999px; padding:6px 11px; font-size:.81rem; color:var(--text-muted); }

/* ── 5 DIMENSIONS (start screen) ── */
.dim-panel { background:#FFFFFF; border:1px solid var(--border); border-radius:24px; padding:28px 32px; margin-top:16px; }
.dim-header p { margin:10px 0 0; max-width:68ch; color:var(--text-muted); font-size:.9rem; line-height:1.6; }
.dim-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:12px; margin-top:20px; }
.dim-card { border:1px solid var(--border); border-radius:16px; padding:14px 15px; background:#FAFBFD; }
.dim-num { font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:1.3rem; }
.dim-name { font-family:'Space Grotesk',sans-serif; font-weight:600; font-size:.85rem; color:var(--text-dark); margin:4px 0 6px; }
.dim-desc { font-size:.79rem; color:var(--text-muted); line-height:1.5; }
.unesco-link { display:inline-block; margin-top:20px; font-size:.85rem; font-weight:600; color:var(--primary); text-decoration:none; }
.unesco-link:hover { text-decoration:underline; }

/* ── READONLY SCROLL (completados en modo vista) ── */
.st-key-chat_scroll_readonly {
    background:#FFFFFF;
    padding:0 !important;
    border-radius:0 !important;
}
.st-key-chat_scroll_readonly > div { gap:0 !important; }

/* ── BANNER MODO VISTA ── */
.readonly-banner {
    display:flex; align-items:center; gap:9px;
    background:#FFFBEA; border:1.5px solid #E8C90A;
    border-radius:10px; padding:9px 15px; margin-bottom:10px;
    font-size:.76rem; color:#5C4A00; font-weight:500;
}
.readonly-banner .rb-icon { font-size:.95rem; flex-shrink:0; }

/* ── SIDEBAR BACK BUTTON ── */
.st-key-go_menu > button {
    background:#F4F6FB !important;
    color:var(--text-muted) !important;
    border:1px dashed var(--border) !important;
}
.st-key-go_menu > button:hover {
    background:#EEF8FF !important;
    color:#0A6A96 !important;
    border-color:#35BFFF !important;
}

/* ── REFLECTION (end screen) ── */
.reflect-shell { max-width:760px; margin:24px auto 0; }
.reflect-panel { background:linear-gradient(135deg,#FFFFFF,#F9FBFF); border:1px solid var(--border); border-radius:24px; box-shadow:0 16px 48px rgba(27,35,64,.08); padding:32px; }
.reflect-copy { color:var(--text-dark); font-size:.95rem; line-height:1.75; }
.reflect-copy p { margin:0 0 14px; }
.reflect-copy p:last-child { margin-bottom:0; }
.reflect-list { margin:18px 0; padding:0; list-style:none; }
.reflect-list li { display:flex; gap:10px; padding:9px 0; border-top:1px solid var(--border); font-size:.86rem; color:var(--text-dark); }
.reflect-list li:first-child { border-top:none; }
.reflect-list .dot { flex-shrink:0; width:8px; height:8px; border-radius:50%; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
defaults = {
    "completed": set(),
    "current_exp": None,
    "history": [],
    "current_node": None,
    "shown_layers": set(),
    "just_completed": False,
    "pending_next": None,
    "viewing_exp": None,
    "exp_snapshots": {},
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── Helpers ────────────────────────────────────────────────────────────────────
def is_unlocked(n: int) -> bool:
    return n == 1 or (n - 1) in st.session_state.completed


def get_status(n: int) -> str:
    if n in st.session_state.completed:
        return "completed"
    if n == st.session_state.current_exp:
        return "active"
    if is_unlocked(n):
        return "unlocked"
    return "locked"


def current_progress(n: int) -> float:
    if n in st.session_state.completed:
        return 1.0
    if n != st.session_state.current_exp:
        return 0.0
    keys = list(EXPEDICIONES[n]["conversacion"].keys())
    node = st.session_state.current_node
    return (keys.index(node) + 1) / len(keys) if node in keys else 0.0


def push_node(node: dict):
    st.session_state.history.append({"type": "agent", "content": node["agente"]})


def build_meta_tip(node: dict) -> str:
    c = node.get("capa", 0)
    if c == 1:
        return "K-7 se dio cuenta de que todavía está en piloto automático. Empújalo a salir del libreto y a mirar la realidad del grupo."
    if c == 2:
        return "K-7 ya notó que hay algo delicado en juego. Haz que nombre qué deja fuera y quién podría quedar expuesto."
    return "K-7 entendió que tocaba rediseñar. Pídele una versión más justa, más situada y menos genérica."


def maybe_tip(node: dict):
    if node.get("tip"):
        st.toast(build_meta_tip(node), icon="💬")


def save_active_snapshot():
    """Guarda el estado de la expedición activa para poder retomarla después."""
    n = st.session_state.current_exp
    if n is None:
        return
    st.session_state.exp_snapshots[n] = {
        "history": list(st.session_state.history),
        "current_node": st.session_state.current_node,
        "shown_layers": set(st.session_state.shown_layers),
        "just_completed": st.session_state.just_completed,
        "pending_next": st.session_state.pending_next,
    }


def go_to_menu():
    save_active_snapshot()
    st.session_state.viewing_exp = None


def view_expedition(n: int):
    """Muestra la expedición n. Si es la activa, retoma donde se quedó;
    si es otra (ya completada), guarda la activa y la abre en modo lectura."""
    if n != st.session_state.current_exp:
        save_active_snapshot()
    st.session_state.viewing_exp = n


def start_expedition(n: int):
    save_active_snapshot()
    st.session_state.current_exp = n
    st.session_state.viewing_exp = n
    st.session_state.current_node = "inicio"
    st.session_state.history = []
    st.session_state.shown_layers = set()
    st.session_state.just_completed = False
    st.session_state.pending_next = None
    conv = EXPEDICIONES[n]["conversacion"]
    push_node(conv["inicio"])
    maybe_tip(conv["inicio"])


def select_option(idx: int):
    n = st.session_state.current_exp
    node = EXPEDICIONES[n]["conversacion"][st.session_state.current_node]
    opt = node["opciones"][idx]
    st.session_state.history.append({"type": "user", "content": opt["texto"]})
    st.session_state.pending_next = opt["siguiente"]


def resolve_pending():
    n = st.session_state.current_exp
    conv = EXPEDICIONES[n]["conversacion"]
    nid = st.session_state.pending_next
    nnode = conv[nid]
    push_node(nnode)
    maybe_tip(nnode)
    st.session_state.current_node = nid
    if nnode.get("es_final"):
        st.session_state.completed.add(n)
        st.session_state.just_completed = True
    st.session_state.pending_next = None


# ── HTML builders ──────────────────────────────────────────────────────────────
def agent_bubble_html(n: int, content: str, idx: int) -> str:
    color = EXPEDICIONES[n]["color"]
    return f"""
<div class="msg-row">
  <div class="avatar agent-av" style="background:{color};">K7</div>
  <div class="msg-col">
    <div class="bubble agent-bubble">{render_message(content)}</div>
    <div class="msg-time">K-7 · {fake_timestamp(idx)}</div>
  </div>
</div>"""


def user_bubble_html(n: int, content: str, idx: int) -> str:
    color = EXPEDICIONES[n]["color"]
    ton = TEXT_ON_COLOR[n]
    return f"""
<div class="msg-row user-row">
  <div class="msg-col user-col">
    <div class="bubble user-bubble" style="background:{color};color:{ton};">{content}</div>
    <div class="msg-time">Tú · {fake_timestamp(idx)}</div>
  </div>
  <div class="avatar user-av">🧑‍🏫</div>
</div>"""


def typing_html(n: int) -> str:
    color = EXPEDICIONES[n]["color"]
    return f"""
<div class="typing-row">
  <div class="avatar agent-av" style="background:{color};">K7</div>
  <div class="typing-bubble">
    <div class="dot"></div><div class="dot"></div><div class="dot"></div>
  </div>
</div>"""


def render_chat_header(n: int):
    exp = EXPEDICIONES[n]
    color = exp["color"]
    tint = TINT[n]
    ton = TEXT_ON_COLOR[n]
    st.markdown(f"""
<div class="chat-header">
  <div class="ch-av" style="background:{color};color:{ton};">K7</div>
  <div class="ch-info">
    <div class="ch-name">
      K-7
      <span class="ch-exp-tag" style="background:{tint};color:{color};">
        Exp. {n}: {exp['titulo']}
      </span>
    </div>
    <div class="ch-status"><span class="ch-dot"></span>Inteligencia visitante · en línea</div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_completed_expedition_view(n: int):
    """Vista de solo lectura: muestra la conversación completa ya tenida en una expedición."""
    exp = EXPEDICIONES[n]
    snap = st.session_state.exp_snapshots.get(n, {})
    history = snap.get("history", [])

    st.markdown("""
<div class="readonly-banner">
  <span class="rb-icon">📖</span>
  <span>Estás revisando una conversación ya completada. Usa el menú lateral para navegar a otra expedición.</span>
</div>
""", unsafe_allow_html=True)

    render_chat_header(n)

    with st.container(key="chat_scroll_readonly", height=420, border=False, autoscroll=False):
        parts = []
        for i, msg in enumerate(history):
            if msg["type"] == "agent":
                parts.append(agent_bubble_html(n, msg["content"], i))
            elif msg["type"] == "user":
                parts.append(user_bubble_html(n, msg["content"], i))
        st.markdown(f'<div class="chat-body">{"".join(parts)}</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-cap"></div>', unsafe_allow_html=True)

    badge = exp["badge"]
    st.markdown(f"""
<div class="badge-card">
  <span class="badge-emoji">{badge['icono']}</span>
  <h3>Insignia obtenida</h3>
  <div class="badge-name">{badge['nombre']}</div>
  <div class="badge-sub">Expedición {n} completada</div>
</div>
""", unsafe_allow_html=True)


def render_tip(content: str):
    st.markdown(f"""
<div class="tip-card">
  <span class="tip-icon">💡</span>
  <div>
    <div class="tip-label">Cómo funciona esto</div>
    <div class="tip-text">{content}</div>
  </div>
</div>""", unsafe_allow_html=True)


def render_layer_divider(n: int, content: str):
    tint = TINT[n]
    color = EXPEDICIONES[n]["color"]
    capa_map = {"El Encuentro": 1, "La Conversación": 2, "La Creación": 3}
    num = capa_map.get(content, "")
    st.markdown(f"""
<div class="layer-divider">
  <span class="layer-pill" style="background:{tint};color:{color};">
    Capa {num} · {content}
  </span>
</div>""", unsafe_allow_html=True)


DIMENSION_BLURBS = {
    1: "La IA solo es útil si el docente aporta primero su conocimiento del territorio humano.",
    2: "Detectar el daño que un agente puede causar sin mala intención, solo por ignorar un contexto.",
    3: "Entender por qué y cómo falla un modelo: qué datos tiene, qué sesgos arrastra, cuándo inventa.",
    4: "La creatividad pedagógica del docente es lo que convierte una plantilla en una experiencia real.",
    5: "El conocimiento que un docente acumula en el aula es el que ningún agente puede generar solo.",
}


def render_start_screen():
    st.markdown("""
<div class="hero-shell">
  <div class="hero-panel">
    <div class="hero-kicker">Simulación narrativa para docentes</div>
    <div class="hero-title">Una inteligencia poderosa entra al aula, pero <span class="accent">todavía no entiende lo humano</span>.</div>
    <div class="hero-copy">
      La experiencia te pone frente a un agente que sabe producir respuestas, pero no sabe leer contextos, límites ni matices escolares.
      Tu trabajo no es repetir un guion: es entrenarlo con criterio docente, empujarlo cuando se quede corto y mostrarle por qué una clase buena no se parece a una plantilla.
    </div>
    <div class="hero-grid">
      <div class="hero-card"><div class="eyebrow">Tu papel</div><p>Actúas como la voz experta que corrige el rumbo de K-7 cuando la propuesta parece correcta, pero todavía no encaja con un aula real.</p></div>
      <div class="hero-card"><div class="eyebrow">La dinámica</div><p>Cada expedición abre un dilema distinto. Respondes, el agente reacciona y la historia se mueve con tus decisiones.</p></div>
      <div class="hero-card"><div class="eyebrow">Lo que te llevas</div><p>Insignias, progreso y una lectura más fina sobre cómo la IA cambia cuando alguien con experiencia real la guía.</p></div>
    </div>
    <div class="hero-footer">
      <span>5 expediciones</span>
      <span>Un agente que aprende contigo</span>
      <span>Decisiones con consecuencias</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

    dim_cards = "".join(
        f"""<div class="dim-card">
  <div class="dim-num" style="color:{EXPEDICIONES[n]['color']};">{n}</div>
  <div class="dim-name">{EXPEDICIONES[n]['dimension_unesco']}</div>
  <div class="dim-desc">{DIMENSION_BLURBS[n]}</div>
</div>"""
        for n in range(1, 6)
    )
    st.markdown(f"""
<div class="hero-shell">
  <div class="dim-panel">
    <div class="dim-header">
      <div class="hero-kicker">Marco de competencias UNESCO 2024</div>
      <p>Cada expedición corresponde a una de las cinco dimensiones del Marco de competencias en materia de IA para docentes de la UNESCO. No las vas a memorizar: las vas a ejercer.</p>
    </div>
    <div class="dim-grid">{dim_cards}</div>
    <a class="unesco-link" href="https://www.unesco.org/es/articles/que-debe-saber-acerca-de-los-nuevos-marcos-de-competencias-en-materia-de-ia-de-la-unesco-para?hub=195885" target="_blank">
      Leer el artículo oficial de la UNESCO ↗
    </a>
  </div>
</div>
""", unsafe_allow_html=True)


ALREADY_DOING = {
    1: "Ya leías a tus estudiantes antes de planear una clase. Hoy se lo tuviste que enseñar a una IA.",
    2: "Ya cuidabas no exponer a un estudiante sin querer. Hoy convertiste ese cuidado en un criterio explícito.",
    3: "Ya dudabas de fuentes poco claras. Hoy aprendiste a dudar también de una máquina segura de sí misma.",
    4: "Ya sabías que una buena clase nace de tu visión, no de un formato. Hoy se la prestaste a un agente que solo sabía producir formato.",
    5: "Ya guardabas años de decisiones que nadie te pidió escribir. Hoy empezaste a ponerlas en palabras.",
}


def render_reflection_screen():
    items = "".join(
        f"""<li><span class="dot" style="background:{EXPEDICIONES[n]['color']};"></span>
  <span><strong>{EXPEDICIONES[n]['dimension_unesco']}.</strong> {ALREADY_DOING[n]}</span></li>"""
        for n in range(1, 6)
    )
    st.markdown(f"""
<div class="reflect-shell">
  <div class="reflect-panel">
    <div class="hero-kicker">Antes de cerrar</div>
    <div class="hero-title" style="font-size:1.6rem;margin:14px 0 12px;">Las cinco competencias no eran nuevas para ti</div>
    <div class="reflect-copy">
      <p>Durante cinco expediciones, K-7 te hizo muchas preguntas. Pero si lo piensas bien, ninguna te enseñó algo que no supieras ya.</p>
    </div>
    <ul class="reflect-list">{items}</ul>
    <div class="reflect-copy">
      <p>Lo único nuevo no fue el conocimiento. Fue el lugar donde tuviste que ponerlo en palabras: un agente que, sin ti, solo sabe producir lenguaje.</p>
      <p>Con ese mismo criterio que ya traías del aula puedes guiar cualquier IA que llegue a tu salón, esta o la que venga después.</p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div class="sb-header">
  <div class="sb-logo">🧭</div>
  <div class="sb-title">La Expedición del Docente</div>
  <div class="sb-sub">Marco UNESCO de competencias IA 2024</div>
</div>
""", unsafe_allow_html=True)

    done_count = len(st.session_state.completed)
    course_pct = int(done_count / 5 * 100)
    st.markdown(f"""
<div class="sb-course">
  <div class="sb-course-row">
    <span class="sb-course-label">Progreso del curso</span>
    <span class="sb-course-val">{done_count}/5</span>
  </div>
  <div class="progress-track">
    <div class="progress-fill" style="width:{course_pct}%;background:linear-gradient(90deg,#35BFFF,#9F1DED);"></div>
  </div>
</div>
<div class="sb-list-label">Expediciones</div>
""", unsafe_allow_html=True)

    if st.session_state.viewing_exp is not None:
        if st.button("← Menú principal", key="go_menu"):
            go_to_menu()
            st.rerun()

    for num in range(1, 6):
        exp = EXPEDICIONES[num]
        status = get_status(num)
        badge = exp["badge"]
        prog_pct = int(current_progress(num) * 100)
        is_viewing = st.session_state.viewing_exp == num

        if status == "completed":
            icon = badge["icono"]
            chip = '<span class="sc-chip chip-done">✓ Hecha</span>'
            card_cls = "exp-sc sc-done"
            prog_color = "#E8C90A"
        elif status == "active":
            icon = exp["icono"]
            chip = '<span class="sc-chip chip-active">En curso</span>'
            card_cls = "exp-sc sc-active"
            prog_color = exp["color"]
        elif status == "unlocked":
            icon = exp["icono"]
            chip = '<span class="sc-chip chip-open">Disponible</span>'
            card_cls = "exp-sc"
            prog_color = exp["color"]
        else:
            icon = "🔒"
            chip = '<span class="sc-chip chip-lock">Bloqueada</span>'
            card_cls = "exp-sc sc-locked"
            prog_color = "#B7BCD0"

        exp_color_var = f"--exp-color:{exp['color']};" if status == "active" else ""
        show_prog = status in ("active", "completed")
        prog_html = f"""
<div class="sc-prog-row">
  <div class="progress-track" style="flex:1;">
    <div class="progress-fill" style="width:{prog_pct}%;background:{prog_color};"></div>
  </div>
  <span class="sc-pct">{prog_pct}%</span>
</div>""" if show_prog else ""

        st.markdown(f"""
<div class="{card_cls}" style="{exp_color_var}">
  <div class="sc-top">
    <span class="sc-icon">{icon}</span>
    <div class="sc-info">
      <div class="sc-num">Expedición {num}</div>
      <div class="sc-name">{exp['titulo']}</div>
    </div>
    {chip}
  </div>
  {prog_html}
</div>
""", unsafe_allow_html=True)

        if status == "completed" and not is_viewing:
            if st.button(f"↩ Ver expedición {num}", key=f"view_{num}"):
                view_expedition(num)
                st.rerun()
        elif status == "active" and not is_viewing:
            if st.button(f"▶ Continuar expedición {num}", key=f"cont_{num}"):
                view_expedition(num)
                st.rerun()
        elif status == "unlocked":
            if st.button(f"▶ Iniciar expedición {num}", key=f"start_{num}"):
                start_expedition(num)
                st.rerun()

    earned = [EXPEDICIONES[n]["badge"] for n in sorted(st.session_state.completed)]
    if earned:
        st.markdown("---")
        st.markdown('<div class="sb-list-label">Insignias obtenidas</div>', unsafe_allow_html=True)
        for b in earned:
            st.markdown(f"""
<div class="sb-badge-row">
  <span class="sb-badge-icon">{b['icono']}</span>
  <span class="sb-badge-name">{b['nombre']}</span>
</div>""", unsafe_allow_html=True)


# ── MAIN AREA ──────────────────────────────────────────────────────────────────
if st.session_state.viewing_exp is None:
    render_start_screen()
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        cur = st.session_state.current_exp
        if cur is None:
            if st.button("Comenzar la expedición", key="begin", use_container_width=True):
                start_expedition(1)
                st.rerun()
        else:
            exp_label = EXPEDICIONES[cur]["titulo"]
            if st.button(f"Continuar → Expedición {cur}: {exp_label}", key="continue_from_menu", use_container_width=True):
                view_expedition(cur)
                st.rerun()

elif st.session_state.viewing_exp != st.session_state.current_exp:
    render_completed_expedition_view(st.session_state.viewing_exp)

else:
    n = st.session_state.current_exp
    exp = EXPEDICIONES[n]
    conv = exp["conversacion"]
    node = conv[st.session_state.current_node]

    # The options panel takes over closing the chat-body's bottom corners;
    # everywhere else (badge screen, transient states) needs the plain cap.
    show_opts = (
        not st.session_state.just_completed
        and node.get("opciones")
        and not st.session_state.pending_next
    )

    render_chat_header(n)

    with st.container(key="chat_scroll_region", height=420, border=False, autoscroll=True):
        # Build all messages as one HTML block
        parts = []
        for i, msg in enumerate(st.session_state.history):
            if msg["type"] == "agent":
                parts.append(agent_bubble_html(n, msg["content"], i))
            elif msg["type"] == "user":
                parts.append(user_bubble_html(n, msg["content"], i))

        st.markdown(f'<div class="chat-body">{"".join(parts)}</div>', unsafe_allow_html=True)

        # Typing indicator then resolve
        if st.session_state.pending_next:
            ph = st.empty()
            with ph.container():
                st.markdown(
                    f'<div class="chat-body" style="padding-top:6px;padding-bottom:12px;border-top:none;">'
                    f'{typing_html(n)}</div>',
                    unsafe_allow_html=True,
                )
            time.sleep(1.1)
            resolve_pending()
            ph.empty()
            st.rerun()

        if not show_opts:
            st.markdown('<div class="chat-cap"></div>', unsafe_allow_html=True)

    with st.container(key="chat_footer_region"):
        # Badge award
        if st.session_state.just_completed:
            badge = exp["badge"]
            st.markdown(f"""
<div class="badge-card">
  <span class="badge-emoji">{badge['icono']}</span>
  <h3>Insignia obtenida</h3>
  <div class="badge-name">{badge['nombre']}</div>
  <div class="badge-sub">Expedición {n} completada</div>
</div>
""", unsafe_allow_html=True)
            c1, c2, c3 = st.columns([1, 2, 1])
            with c2:
                next_n = n + 1
                if next_n <= 5:
                    if st.button(
                        f"Continuar → Expedición {next_n}: {EXPEDICIONES[next_n]['titulo']}",
                        key="next_exp", use_container_width=True,
                    ):
                        start_expedition(next_n)
                        st.rerun()
                else:
                    render_reflection_screen()
                    if st.button("Volver al inicio", key="restart", use_container_width=True):
                        st.session_state.current_exp = None
                        st.session_state.viewing_exp = None
                        st.rerun()

        # Response options
        elif show_opts:
            st.markdown('<div class="opts-zone"><div class="opts-label">Elige tu respuesta</div></div>',
                        unsafe_allow_html=True)
            c_l, c_m, c_r = st.columns([1, 10, 1])
            with c_m:
                for i, opt in enumerate(node["opciones"]):
                    if st.button(opt["texto"],
                                 key=f"opt_{st.session_state.current_node}_{i}",
                                 use_container_width=True):
                        select_option(i)
                        st.rerun()
