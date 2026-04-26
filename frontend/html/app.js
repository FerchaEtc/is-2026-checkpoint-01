// Atrapa el <tbody> donde van a ir las filas y el <div> del indicador
const tableBody = document.getElementById('team-table-body');
const statusContainer = document.getElementById('backend-status');
const statusText = document.getElementById('status-text');


async function fetchTeamData() {
    try {
        // Da un feedback visual mientras se espera al back
        statusContainer.className = 'status-container connecting';
        statusText.textContent = "Conectando al backend...";
        
        // Hace la petición GET al endpoint
        const response = await fetch('http://localhost:5000/api/team');

        // Si el backend no anda, corta aca
        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        // Parsea el cuerpo de la respuesta a un array de objetos
        const teamMembers = await response.json();

        // Estado exitoso -> pasa a online y modifica el texto
        statusContainer.className = 'status-container online';
        statusText.textContent = "Backend Online";
        // Limpia la tabla
        tableBody.innerHTML = '';

        // Itera sobre el array
        teamMembers.forEach(member => {
            // Crea un elemento <tr> en memoria
            const row = document.createElement('tr');
           
            // Inyecta las columnas en la tabla (<td>)
            row.innerHTML = `
                <td>${member.nombre} ${member.apellido}</td>
                <td>${member.legajo}</td>
                <td>${member.feature}</td>
                <td>${member.servicio}</td>
                <td>${member.estado}</td>
            `;
           
            // Mete la fila terminada adentro del <tbody>
            tableBody.appendChild(row);
        });


    } catch (error) {
        // Error, informa visualmente -> pasa a offline y modifica el texto
        console.error("Falló la conexión con el backend:", error);
        statusContainer.className = 'status-container offline';
        statusText.textContent = "Backend Offline";
        tableBody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: #e74c3c;">No se pudieron cargar los datos.</td></tr>`;
    }
}


// Ejecuta la funcion
fetchTeamData();
