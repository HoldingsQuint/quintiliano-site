// Menu do celular e o desenho de rede da abertura (gerado aqui, sem imagem externa).
(function () {
  var botao = document.querySelector(".menu-botao");
  var menu = document.querySelector(".menu");
  if (botao && menu) {
    botao.addEventListener("click", function () {
      var aberto = menu.classList.toggle("aberto");
      botao.setAttribute("aria-expanded", String(aberto));
    });
  }

  var svg = document.querySelector("svg.rede");
  if (!svg) return;
  var L = 1200, A = 600, n = 46, semente = 7;
  function aleatorio() { semente = (semente * 16807) % 2147483647; return semente / 2147483647; }
  var pontos = [];
  for (var i = 0; i < n; i++) pontos.push([aleatorio() * L, aleatorio() * A]);
  var ns = "http://www.w3.org/2000/svg";
  svg.setAttribute("viewBox", "0 0 " + L + " " + A);
  svg.setAttribute("preserveAspectRatio", "xMidYMid slice");
  for (var a = 0; a < n; a++) {
    for (var b = a + 1; b < n; b++) {
      var dx = pontos[a][0] - pontos[b][0], dy = pontos[a][1] - pontos[b][1];
      var d = Math.sqrt(dx * dx + dy * dy);
      if (d < 170) {
        var l = document.createElementNS(ns, "line");
        l.setAttribute("x1", pontos[a][0]); l.setAttribute("y1", pontos[a][1]);
        l.setAttribute("x2", pontos[b][0]); l.setAttribute("y2", pontos[b][1]);
        l.setAttribute("stroke", "#4fd1ff");
        l.setAttribute("stroke-opacity", (0.45 * (1 - d / 170)).toFixed(2));
        l.setAttribute("stroke-width", "1");
        svg.appendChild(l);
      }
    }
  }
  pontos.forEach(function (p, i) {
    var c = document.createElementNS(ns, "circle");
    c.setAttribute("cx", p[0]); c.setAttribute("cy", p[1]);
    c.setAttribute("r", i % 7 === 0 ? 3.2 : 1.8);
    c.setAttribute("fill", i % 7 === 0 ? "#4fd1ff" : "#9fc4ff");
    svg.appendChild(c);
  });
})();
