"""Gera os SVGs do README do perfil (versões clara e escura)."""
from pathlib import Path
from html import escape

RAIZ = Path(__file__).resolve().parent.parent / "assets"

TEMAS = {
    "light": dict(bone="#1F2328", muted="#6E7781", rule="#D0D7DE", accent="#0969DA", card="#F6F8FA"),
    "dark": dict(bone="#E6EDF3", muted="#8B949E", rule="#30363D", accent="#58A6FF", card="#161B22"),
}

MONO = 'ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,"Liberation Mono",monospace'


def base(w, h, label, corpo, t):
    return f"""<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(label)}">
  <style>
    .mono {{ font-family: {MONO}; }}
    .rise {{ opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }}
    @keyframes rise {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}
    .draw {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.4s cubic-bezier(.6,0,.2,1) forwards; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    .blink {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    .a1{{animation-delay:.1s}} .a2{{animation-delay:.25s}} .a3{{animation-delay:.4s}} .a4{{animation-delay:.55s}} .a5{{animation-delay:.7s}} .a6{{animation-delay:.85s}} .a7{{animation-delay:1s}} .a8{{animation-delay:1.15s}}
    @media (prefers-reduced-motion: reduce) {{ .rise,.draw,.blink {{ animation: none; opacity: 1; stroke-dashoffset: 0; }} }}
  </style>
{corpo}
</svg>
"""


def txt(x, y, s, t, size=15, cor="bone", cls="", extra=""):
    return f'  <text class="mono {cls}" x="{x}" y="{y}" font-size="{size}" fill="{t[cor]}" {extra}>{escape(s)}</text>'


def header(t):
    c = [
        f'  <line class="draw" x1="48" y1="58" x2="952" y2="58" stroke="{t["rule"]}" stroke-width="1"/>',
        txt(48, 44, "PROFILE — INDEX Nº 001", t, 11, "muted", "rise a1", 'letter-spacing="3.5"'),
        txt(952, 44, "JOINVILLE, SC — 26.30° S", t, 11, "muted", "rise a1", 'letter-spacing="3.5" text-anchor="end"'),
        txt(46, 160, "Caio Miranda Coelho", t, 64, "bone", "rise a2", 'letter-spacing="-2"'),
        txt(48, 202, "Software Engineer @ TOTVS — AI & Software Architecture.", t, 19, "muted", "rise a3"),
        f'  <text class="mono rise a4" x="48" y="262" font-size="16" fill="{t["accent"]}">$ whoami --focus<tspan fill="{t["bone"]}"> ai-agents · clean-architecture · ddd · cloud</tspan><tspan class="blink" fill="{t["accent"]}"> ▌</tspan></text>',
        f'  <line class="draw a5" x1="48" y1="300" x2="952" y2="300" stroke="{t["rule"]}" stroke-width="1"/>',
        txt(48, 326, "“Focusing on the process and trusting in the hard work when it matters most.”", t, 13, "muted", "rise a6", 'font-style="italic"'),
    ]
    return base(1000, 350, "Caio Miranda Coelho — Software Engineer at TOTVS", "\n".join(c), t)


def secao(num, nome, t):
    c = [
        txt(48, 30, f"{num:02d}", t, 12, "accent", "rise a1", 'letter-spacing="2"'),
        txt(84, 30, nome.upper(), t, 12, "bone", "rise a1", 'letter-spacing="3" font-weight="700"'),
        f'  <line class="draw a2" x1="{100 + len(nome) * 11}" y1="26" x2="952" y2="26" stroke="{t["rule"]}" stroke-width="1"/>',
    ]
    return base(1000, 48, f"{num:02d} — {nome}", "\n".join(c), t)


def linhas_rotuladas(itens, t, label, top=32, passo=34):
    c = [f'  <line x1="160" y1="8" x2="160" y2="{top + passo * (len(itens) - 1) + 12}" stroke="{t["rule"]}" stroke-width="1"/>']
    for i, (rot, val, cor) in enumerate(itens):
        y = top + passo * i
        a = f"a{min(i + 1, 8)}"
        c.append(txt(48, y, rot, t, 11, "muted", f"rise {a}", 'letter-spacing="2.5"'))
        c.append(txt(178, y, val, t, 15, cor, f"rise {a}"))
    return base(1000, top + passo * (len(itens) - 1) + 24, label, "\n".join(c), t)


WHOAMI = [
    ("ROLE", "Software Engineer at TOTVS — Brazil", "bone"),
    ("FOCUS", "AI agents · LLM tooling · Clean Architecture · DDD", "bone"),
    ("BUILDING", "local coding agents: sandboxed, observable, human-in-the-loop", "accent"),
    ("LOVES", "techniques, patterns and software architecture", "bone"),
    ("BASE", "Joinville, Santa Catarina — BR", "muted"),
]

STACK = [
    ("LANGUAGES", "Java · TypeScript · Python · SQL · Dart", "bone"),
    ("BACKEND", "Spring Boot · Spring AI · JPA/Hibernate · WebSocket · REST", "bone"),
    ("AI", "Ollama · LLM agents · opencode · tool calling · streaming", "accent"),
    ("FRONTEND", "React · Vite · Angular · Flutter", "bone"),
    ("ARCH", "Clean Architecture · Ports & Adapters · DDD · Microservices", "bone"),
    ("DATA", "PostgreSQL · Supabase · Pandas · Jupyter", "bone"),
    ("CLOUD", "Docker · Kubernetes · AWS (EKS, API Gateway, Lambda, RDS)", "bone"),
    ("DEVOPS", "Terraform · GitHub Actions · Maven · Git", "bone"),
]

PROJETOS = [
    ("alien-code", "AI", "Local coding assistant: disposable Docker sandboxes", "running the opencode agent on Ollama models, live timeline.", "JAVA 21 · SPRING BOOT · REACT · DOCKER · OLLAMA"),
    ("coding-agent", "AI", "Issue in, draft pull request out: an agent working", "inside an isolated container on GitHub Actions.", "JAVA 21 · SPRING AI · OLLAMA · GITHUB ACTIONS"),
    ("poc-websocket-demo", "AI", "Real LLM streaming over raw WebSocket with stop and", "interrupt-and-replace, like production chat harnesses.", "SPRING AI · WEBSOCKET · REACT 18 · VITE"),
    ("gerenciador-oficina-core", "ARCH", "Workshop management API modeled with DDD, deployed", "to AWS EKS with Terraform and CI/CD pipelines.", "JAVA · SPRING BOOT · DDD · K8S · AWS EKS"),
    ("gerenciador-oficina-gateway-fase-3", "ARCH", "AWS API Gateway as code: routing, rate limiting", "and CloudWatch logs provisioned by Terraform.", "TERRAFORM · AWS API GATEWAY · CLOUDWATCH"),
    ("auth-core", "ARCH", "Titan System auth microservice: users, clinics,", "JWT login and refresh tokens for healthcare.", "JAVA · SPRING BOOT · MICROSERVICES · JWT"),
]


def card(nome, tag, l1, l2, meta, t):
    c = [
        f'  <rect class="rise a1" x="1" y="1" width="478" height="148" rx="10" fill="{t["card"]}" stroke="{t["rule"]}"/>',
        txt(24, 38, nome, t, 16, "bone", "rise a2", 'font-weight="700"'),
        f'  <rect class="rise a2" x="{454 - len(tag) * 9 - 14}" y="22" width="{len(tag) * 9 + 14}" height="22" rx="11" stroke="{t["accent"]}"/>',
        txt(454 - (len(tag) * 9 + 14) / 2, 37, tag, t, 11, "accent", "rise a2", 'text-anchor="middle" letter-spacing="1.5"'),
        txt(24, 72, l1, t, 12, "bone", "rise a3"),
        txt(24, 92, l2, t, 12, "bone", "rise a3"),
        txt(24, 126, meta, t, 10, "muted", "rise a4", 'letter-spacing=".8"'),
    ]
    return base(480, 150, f"{nome} — {l1} {l2}", "\n".join(c), t)


def footer(t):
    c = [
        f'  <line class="draw" x1="48" y1="20" x2="952" y2="20" stroke="{t["rule"]}" stroke-width="1"/>',
        f'  <circle class="blink" cx="54" cy="48" r="4" fill="{t["accent"]}"/>',
        txt(70, 53, "status: shipping agents & architectures — open to talk tech", t, 13, "muted", "rise a1"),
        txt(952, 53, "github.com/CaioMC", t, 13, "muted", "rise a1", 'text-anchor="end"'),
    ]
    return base(1000, 72, "Current status", "\n".join(c), t)


def main():
    for tema, t in TEMAS.items():
        d = RAIZ if tema == "light" else RAIZ / "dark"
        (d / "projects").mkdir(parents=True, exist_ok=True)
        arquivos = {
            "header.svg": header(t),
            "whoami.svg": linhas_rotuladas(WHOAMI, t, "whoami"),
            "stack.svg": linhas_rotuladas(STACK, t, "Technical stack"),
            "footer.svg": footer(t),
        }
        for i, nome in enumerate(["whoami", "projects", "stack", "telemetry"], start=1):
            arquivos[f"s0{i}.svg"] = secao(i, nome, t)
        for p in PROJETOS:
            arquivos[f"projects/{p[0]}.svg"] = card(*p, t)
        for nome, svg in arquivos.items():
            (d / nome).write_text(svg, encoding="utf-8")


if __name__ == "__main__":
    main()
