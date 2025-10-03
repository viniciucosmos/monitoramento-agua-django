async function atualizar() {
  try {
    let resp = await fetch("/monitoramento/leituras/ultima/");
    let data = await resp.json();

    if (!data.message) {
      // Temperatura
      const tempDiv = document.getElementById("temp-card");
      const tempAlert = document.getElementById("temp-alert");
      document.getElementById("temperatura").textContent =
        data.temperatura + " °C";

      if (data.temperatura < 26) {
        tempDiv.classList.add("alerta");
        tempAlert.textContent = "⚠️ Baixa";
      } else if (data.temperatura > 30) {
        tempDiv.classList.add("alerta");
        tempAlert.textContent = "⚠️ Alta";
      } else {
        tempDiv.classList.remove("alerta");
        tempAlert.textContent = "";
      }

      // pH
      const phDiv = document.getElementById("ph-card");
      const phAlert = document.getElementById("ph-alert");
      document.getElementById("ph").textContent = data.ph;

      if (data.ph < 6) {
        phDiv.classList.add("alerta");
        phAlert.textContent = "⚠️ Baixo";
      } else if (data.ph > 8) {
        phDiv.classList.add("alerta");
        phAlert.textContent = "⚠️ Alto";
      } else {
        phDiv.classList.remove("alerta");
        phAlert.textContent = "";
      }

      // TDS
      const tdsDiv = document.getElementById("tds-card");
      const tdsAlert = document.getElementById("tds-alert");
      document.getElementById("tds").textContent = data.tds + " ppm";

     if (data.tds >= 1200) {
        tdsDiv.classList.add("alerta");
        tdsAlert.textContent = "⚠️ Alto";
      } else {
        tdsDiv.classList.remove("alerta");
        tdsAlert.textContent = "";
      }
    }
  } catch (error) {
    console.error("Erro ao buscar dados:", error);
  }
}

setInterval(atualizar, 300000); // 5 min
atualizar();
