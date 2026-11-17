"""Gera as páginas do site a partir de um molde comum (topo, rodapé, contato).
Rodar com: python3 scripts/gerar.py  (na raiz do repositório). As páginas geradas são as que vão para o ar."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
V = "20261115"

CONTATO = {
    "whatsapp": "5561982152262",
    "whatsapp_txt": "(61) 98215-2262",
    "telefone": "556135321072",
    "telefone_txt": "(61) 3532-1072",
    "email": "contato@ipaq.tec.br",
    "horario": "Segunda a sexta, das 9h às 19h",
    "endereco": "SHIN QI 13, Conjunto 1, Casa 6, Lago Norte, Brasília/DF, CEP 71535-010",
}

MENU = [("", "Início"), ("institutos/", "Institutos"), ("pericia/", "Perícia"), ("solucoes/", "Soluções")]

ICONES = {
    "radar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 12l6-6"/></svg>',
    "escudo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "alerta": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 3l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
    "olho": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "lupa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></svg>',
    "antena": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 13v8"/><circle cx="12" cy="11" r="2"/><path d="M7.8 6.8a6 6 0 000 8.4M16.2 6.8a6 6 0 010 8.4M5 4a10 10 0 000 14M19 4a10 10 0 010 14"/></svg>',
}


def zap(msg):
    from urllib.parse import quote
    return f"https://wa.me/{CONTATO['whatsapp']}?text={quote(msg)}"


def pagina(caminho, titulo, descricao, corpo, atual):
    nivel = caminho.count("/")
    pre = "../" * nivel
    menu = "".join(
        f'<a href="{pre}{href}"{" aria-current=\"page\"" if href == atual else ""}>{nome}</a>' for href, nome in MENU
    )
    corpo = corpo.replace("{pre}", pre)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="facebook-domain-verification" content="303kphftldqxe6akpcox22kbzmjh5s">
  <title>{titulo}</title>
  <meta name="description" content="{descricao}">
  <meta property="og:title" content="{titulo}">
  <meta property="og:description" content="{descricao}">
  <meta property="og:type" content="website">
  <link rel="icon" href="{pre}assets/logo.png">
  <link rel="stylesheet" href="{pre}assets/estilo.css?v={V}">
  <script src="{pre}assets/site.js?v={V}" defer></script>
</head>
<body>

<header class="topo">
  <div class="container">
    <a class="marca" href="{pre or './'}">
      <img src="{pre}assets/logo.png" alt="">
      <span><strong>Quintiliano Tecnologia</strong><small>INQ · Instituto de Inteligência Cibernética Quintiliano</small></span>
    </a>
    <button class="menu-botao" type="button" aria-expanded="false" aria-label="Abrir menu">Menu</button>
    <nav class="menu" aria-label="Principal">{menu}<a class="botao" href="#contato">Fale conosco</a></nav>
  </div>
</header>

{corpo}

<section class="secao alt" id="contato">
  <div class="container contato">
    <div>
      <span class="rotulo">Contato</span>
      <h2>Fale com a nossa equipe</h2>
      <p class="intro">Projetos estratégicos, incidentes críticos ou demandas periciais. Conte o cenário e a urgência, e retornamos com a orientação adequada. Todas as conversas são tratadas com sigilo.</p>
      <div class="botoes">
        <a class="botao" href="{zap("Olá! Vim pelo site da Quintiliano Tecnologia e gostaria de falar sobre uma demanda.")}" target="_blank" rel="noopener">Falar no WhatsApp</a>
        <a class="botao contorno" href="mailto:{CONTATO['email']}">Enviar e-mail</a>
      </div>
    </div>
    <div class="dados">
      <div><span>WhatsApp</span><a href="{zap("Olá! Vim pelo site da Quintiliano Tecnologia.")}" target="_blank" rel="noopener">{CONTATO['whatsapp_txt']}</a></div>
      <div><span>Telefone</span><a href="tel:+{CONTATO['telefone']}">{CONTATO['telefone_txt']}</a></div>
      <div><span>E-mail</span><a href="mailto:{CONTATO['email']}">{CONTATO['email']}</a></div>
      <div><span>Horário</span><strong>{CONTATO['horario']}</strong></div>
      <div><span>Sede</span><strong>{CONTATO['endereco']}</strong></div>
    </div>
  </div>
</section>

<footer class="rodape">
  <div class="container">
    <div><strong style="color:#fff">Quintiliano Tecnologia</strong><br>INQ · Instituto de Inteligência Cibernética Quintiliano Ltda · Brasília/DF</div>
    <div>{" · ".join(f'<a href="{pre}{h}">{n}</a>' for h, n in MENU)}</div>
  </div>
</footer>

</body>
</html>
"""


def cartao(icone, titulo, texto):
    return f'<div class="cartao"><div class="icone">{ICONES[icone]}</div><h3>{titulo}</h3><p>{texto}</p></div>'


INICIO = f"""
<section class="abertura">
  <svg class="rede" aria-hidden="true"></svg>
  <div class="container">
    <span class="rotulo">Tecnologia · Inteligência · Segurança cibernética</span>
    <h1>Tecnologia, inteligência e segurança cibernética em nível estratégico</h1>
    <p class="lead">Soluções avançadas para organizações privadas, públicas e para o sistema de justiça, em contextos de alta complexidade.</p>
    <div class="botoes">
      <a class="botao" href="#contato">Falar com a equipe</a>
      <a class="botao contorno" href="{{pre}}solucoes/">Ver modelos de contratação</a>
    </div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="cabeca">
      <span class="rotulo">Áreas de atuação</span>
      <h2>Da prevenção à prova técnica</h2>
      <p class="intro">Atuamos na concepção e implementação de soluções em tecnologia da informação, segurança cibernética, inteligência digital, contraespionagem eletrônica, inteligência e contrainteligência cibernéticas e perícia de informática, com foco na proteção de ativos, na produção de conhecimento especializado e no suporte a decisões críticas.</p>
    </div>
    <div class="grade g3">
      {cartao("radar", "Inteligência cibernética", "Monitoramento avançado e análise de ameaças, para antecipar riscos e apoiar decisões.")}
      {cartao("escudo", "Segurança cibernética", "Proteção de ambientes, avaliação de maturidade e gestão de riscos de segurança da informação.")}
      {cartao("alerta", "Resposta a incidentes", "Contenção de ataques, recuperação das operações e redução de impactos técnicos, financeiros e reputacionais.")}
      {cartao("olho", "Contrainteligência cibernética", "Detecção e neutralização de ameaças digitais avançadas e de ações de infiltração.")}
      {cartao("lupa", "Perícia técnica", "Análises forenses com cadeia de custódia preservada e laudos para processos administrativos e judiciais.")}
      {cartao("antena", "Contraespionagem eletrônica", "Identificação e bloqueio de atividades de espionagem tecnológica em ambientes físicos e digitais.")}
    </div>
  </div>
</section>

<section class="secao alt">
  <div class="container grade g2" style="align-items:center;gap:48px">
    <div>
      <span class="rotulo">Como atuamos</span>
      <h2>Tecnologia, estratégia e contexto jurídico, juntos</h2>
      <p class="intro">A atuação integrada entre essas três frentes garante respostas tecnicamente robustas e juridicamente sustentáveis, do primeiro diagnóstico ao laudo final.</p>
      <div class="publicos"><span>Organizações privadas</span><span>Órgãos públicos</span><span>Sistema de justiça</span><span>Instituições financeiras</span></div>
    </div>
    <ol class="etapas" style="grid-template-columns:1fr 1fr">
      <li><strong>Diagnóstico</strong><span>Entendimento do cenário, dos ativos e das ameaças.</span></li>
      <li><strong>Estratégia</strong><span>Definição de políticas, controles e prioridades.</span></li>
      <li><strong>Execução</strong><span>Implementação, monitoramento e resposta.</span></li>
      <li><strong>Prova técnica</strong><span>Relatórios e laudos com valor jurídico.</span></li>
    </ol>
  </div>
</section>
"""

INSTITUTOS = f"""
<section class="abertura pequena">
  <svg class="rede" aria-hidden="true"></svg>
  <div class="container">
    <span class="rotulo">Institutos</span>
    <h1>Ecossistema de soluções tecnológicas</h1>
    <p class="lead">Institutos integrados em tecnologia, inteligência e segurança cibernética.</p>
  </div>
</section>

<section class="secao">
  <div class="container estreito">
    <span class="rotulo">Institutos de excelência digital</span>
    <h2>Todo o ciclo de tecnologia, inteligência e segurança</h2>
    <p class="intro">Nosso ecossistema é formado por institutos complementares que atuam em todo o ciclo de tecnologia, inteligência e segurança cibernética. Reunimos especialistas em investigação digital, gestão de risco, proteção de infraestruturas críticas, desenvolvimento de ferramentas tecnológicas e produção de conhecimento aplicado.</p>
    <p class="intro">A atuação combina prática de campo, pesquisa avançada e domínio jurídico, com respostas técnicas a órgãos governamentais, grandes empresas e operadores do Direito no Brasil e no exterior. A integração entre os institutos permite enxergar ameaças de forma sistêmica e propor soluções estratégicas, auditáveis e alinhadas às melhores práticas internacionais.</p>
  </div>
</section>

<section class="secao alt">
  <div class="container">
    <div class="cabeca"><span class="rotulo">Conheça os institutos</span><h2>Quem faz parte</h2></div>
    <div class="grade g2">
      <div class="cartao">
        <div class="icone">{ICONES["radar"]}</div>
        <h3>INQ · Instituto de Inteligência Cibernética Quintiliano</h3>
        <p>Inteligência e contrainteligência cibernéticas, segurança da informação, resposta a incidentes e contraespionagem eletrônica para organizações públicas e privadas.</p>
      </div>
      <div class="cartao">
        <div class="icone">{ICONES["lupa"]}</div>
        <h3>IPAQ · Instituto de Perícias e Alta Tecnologia Quintiliano</h3>
        <p>Produção de provas técnicas, perícias complexas, auditorias especializadas e cadeia de custódia de dados, com atuação judicial e extrajudicial.</p>
        <a class="botao contorno" href="https://ipaq.tec.br/" target="_blank" rel="noopener">Visitar o site do IPAQ</a>
      </div>
    </div>
  </div>
</section>

<section class="secao">
  <div class="container grade g2" style="gap:24px">
    <div class="cartao">
      <span class="rotulo">Consultoria</span>
      <h3>Estratégia e conformidade</h3>
      <p>Consultoria estratégica em segurança da informação, avaliação de maturidade cibernética, desenho de arquiteturas seguras e programas de conformidade com normas nacionais e internacionais. Do diagnóstico técnico e de governança à definição de políticas, processos e tecnologias, além de capacitação executiva e técnica das equipes.</p>
    </div>
    <div class="cartao">
      <span class="rotulo">Resposta e perícia</span>
      <h3>Prontidão para incidentes</h3>
      <p>Atuação em regime de prontidão para conter ataques, restaurar operações e reduzir impactos. Perícia digital e inteligência com laudos fundamentados e aderentes às exigências legais, além de exercícios de simulação, testes de invasão e programas continuados de treinamento.</p>
    </div>
  </div>
</section>
"""

PERICIA = f"""
<section class="abertura pequena">
  <svg class="rede" aria-hidden="true"></svg>
  <div class="container">
    <span class="rotulo">Perícia digital para o Direito</span>
    <h1>Perícia digital, inteligência e segurança cibernética para casos complexos</h1>
    <p class="lead">Metodologia pericial reconhecida, cadeia de custódia rastreável e laudos robustos e defensáveis. Apoiamos advogados, Ministério Público e magistrados em todas as fases do processo, do incidente digital à sentença.</p>
    <div class="botoes"><a class="botao" href="#contato">Consultar uma demanda pericial</a><a class="botao contorno" href="#metodologia">Ver metodologia</a></div>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="cabeca">
      <span class="rotulo">Perícias digitais</span>
      <h2>Portfólio completo</h2>
      <p class="intro">Analisamos computadores, servidores e ambientes em nuvem para identificar fraudes, vazamentos e adulterações de dados e rastrear ações em ambientes corporativos e governamentais. Cada laudo é escrito em linguagem clara, para facilitar a compreensão jurídica e a apresentação em juízo.</p>
    </div>
    <div class="grade g2">
      {cartao("lupa", "Perícia computacional", "Análise de computadores, servidores e mídias de armazenamento.")}
      {cartao("antena", "Dispositivos móveis", "Smartphones, tablets e wearables, com extração e análise de dados.")}
      {cartao("radar", "Forense em redes", "Tráfego, registros de acesso, incidentes de intrusão e vazamento de dados.")}
      {cartao("escudo", "Due diligence digital", "Mapeamento de riscos cibernéticos, validação de evidências online e histórico digital de pessoas e empresas.")}
    </div>
  </div>
</section>

<section class="secao alt" id="metodologia">
  <div class="container">
    <div class="cabeca"><span class="rotulo">Metodologia</span><h2>Rigor técnico em cada etapa</h2></div>
    <ol class="etapas">
      <li><strong>Preservação</strong><span>Identificação e isolamento das fontes de evidência, antes de qualquer alteração.</span></li>
      <li><strong>Aquisição forense</strong><span>Cópia bit a bit, com registro de integridade e documentação da cadeia de custódia.</span></li>
      <li><strong>Análise</strong><span>Exame técnico com ferramentas e procedimentos reconhecidos e reprodutíveis.</span></li>
      <li><strong>Laudo</strong><span>Conclusões fundamentadas, em linguagem clara, prontas para o processo.</span></li>
    </ol>
  </div>
</section>
"""

SOLUCOES = f"""
<section class="abertura pequena">
  <svg class="rede" aria-hidden="true"></svg>
  <div class="container">
    <span class="rotulo">Tecnologia, inteligência e defesa digital</span>
    <h1>Modelos de contratação em segurança cibernética</h1>
    <p class="lead">Projetos sob medida para governo, empresas e área jurídica, combinando segurança cibernética, inteligência, perícia digital e resposta a incidentes.</p>
  </div>
</section>

<section class="secao">
  <div class="container">
    <div class="cabeca"><span class="rotulo">Engajamentos</span><h2>Escolha o formato do seu projeto</h2></div>
    <div class="grade g3">
      <div class="cartao">
        <h3>Projetos pontuais</h3>
        <p>Projetos estratégicos sob medida, com investimento definido por escopo, complexidade técnica e nível de confidencialidade.</p>
        <ul><li>Diagnóstico de riscos</li><li>Relatórios gerenciais</li><li>Implementação de controles-chave</li><li>Treinamentos</li></ul>
        <a class="botao" href="{zap("Olá! Tenho interesse em um projeto pontual da Quintiliano Tecnologia.")}" target="_blank" rel="noopener">Solicitar proposta</a>
      </div>
      <div class="cartao">
        <h3>Retainer estratégico</h3>
        <p>Retenção e suporte contínuo, com mensalidade conforme o volume de demandas, os níveis de serviço e a necessidade de resposta a incidentes.</p>
        <ul><li>Monitoramento 24×7</li><li>Gestão de incidentes</li><li>Equipe multidisciplinar dedicada</li><li>Atendimento prioritário</li></ul>
        <a class="botao" href="{zap("Olá! Quero agendar uma conversa sobre o retainer estratégico da Quintiliano Tecnologia.")}" target="_blank" rel="noopener">Agendar conversa</a>
      </div>
      <div class="cartao">
        <h3>Briefing</h3>
        <p>Envie o seu cenário, a urgência e os objetivos, e receba uma proposta técnica personalizada da nossa equipe.</p>
        <ul><li>Resposta com orientação inicial</li><li>Proposta técnica sob medida</li><li>Tratamento sigiloso</li></ul>
        <a class="botao" href="mailto:{CONTATO['email']}?subject=Briefing%20-%20Quintiliano%20Tecnologia">Enviar briefing</a>
      </div>
    </div>
  </div>
</section>
"""

PAGINAS = [
    ("index.html", "", "Quintiliano Tecnologia · Inteligência e segurança cibernética", "Tecnologia, inteligência e segurança cibernética em nível estratégico para organizações privadas, públicas e para o sistema de justiça.", INICIO, ""),
    ("institutos/index.html", "institutos/", "Institutos · Quintiliano Tecnologia", "Institutos integrados em tecnologia, inteligência e segurança cibernética: INQ e IPAQ.", INSTITUTOS, "institutos/"),
    ("pericia/index.html", "pericia/", "Perícia digital · Quintiliano Tecnologia", "Perícia digital com metodologia reconhecida e cadeia de custódia rastreável, para advogados, Ministério Público e magistrados.", PERICIA, "pericia/"),
    ("solucoes/index.html", "solucoes/", "Soluções · Quintiliano Tecnologia", "Projetos pontuais, retainer estratégico e briefing para propostas em segurança cibernética, inteligência e perícia digital.", SOLUCOES, "solucoes/"),
]

for arquivo, caminho, titulo, desc, corpo, atual in PAGINAS:
    destino = RAIZ / arquivo
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(pagina(caminho, titulo, desc, corpo, atual), encoding="utf-8")
    print("ok", arquivo)

# A página Insights estava vazia no site antigo: o endereço leva para o início.
(RAIZ / "insights-2" / "index.html").write_text(
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="robots" content="noindex">'
    '<meta http-equiv="refresh" content="0; url=../"><link rel="canonical" href="../"><title>Quintiliano Tecnologia</title>'
    '</head><body><a href="../">Ir para o início</a></body></html>', encoding="utf-8")
print("ok insights-2/index.html")
