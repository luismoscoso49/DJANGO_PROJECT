customers = [];

function getCustomers() {
  // Petición HTTP
  fetch('https://minticequipo14.herokuapp.com/team14/getAllPacientes/')
    .then(response => {
      console.log(response);
      if (response.ok)
        return response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      customers = JSON.parse(data);
      handleCustomers();
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handleCustomers() {
  const divs = [];
  customers.forEach((cust) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3> id_paciente: $(cust.id_paciente} </h3>
      <h3> nombre: $(cust.nombre} </h3>	      
      <h3> direccion: $(cust.direccion} </h3>	 
      <h3> telefono: $(cust.telefono} </h3>	  
      `;
    divs.push(div);
  });
  document.getElementById("cargando").remove();
  const info = document.getElementById("info-customers");
  divs.forEach(div => info.appendChild(div));
}

function handleError() {
  document.getElementById("cargando").remove();
  const message = document.createElement("p");
  message.innerText = "No se pudo cargar la información. Intente más tarde.";
  const info = document.getElementById("info-customers");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getCustomers);