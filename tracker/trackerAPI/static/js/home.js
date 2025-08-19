const table = document.getElementById("table");

document.addEventListener("DOMContentLoaded", () => {
  axios.get("/api/applications")
    .then(response => {
      console.log(response.data);
      const applications = response.data;

      table.innerHTML = "";
      let i = 1;
      applications.forEach(app => {
        const company = app.posting_details.company_details.name;
        const location = app.posting_details.location;
        const status = app.status;
        const jobTitle = app.job_title;
        const id = app.id;

        const row =  `
          <tr onclick="window.open('/api/applications/${id}', '_blank')" style="cursor: pointer;">
            <th scope="row">${i}</th>
            <td>${company}</td>
            <td>${jobTitle}</td>
            <td>${location}</td>
            <td>${status}</td>
          </tr>
        `;
        table.innerHTML += row
        i++;
      });
    })
    .catch(error => {
      console.error("Error fetching:", error);
    });
})