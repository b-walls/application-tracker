const table = document.getElementById("table");

const badgeForStatus = s => {
          const map = { APPLIED: "primary", INTERVIEW: "warning", OFFER: "success", ACCEPTED: "success", REJECTED: "danger" };
          return map[s?.toUpperCase?.()] || "secondary";
        };


document.addEventListener("DOMContentLoaded", () => {
  axios.get("/api/applications")
    .then(response => {
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
          <tr onclick="window.open('/applications/${id}', '_blank')" style="cursor: pointer;">
            <th scope="row">${i}</th>
            <td>${company}</td>
            <td>${jobTitle}</td>
            <td>${location}</td>
            <td><span class="badge text-bg-${badgeForStatus(app.status)}">${app.status ?? "UNKNOWN"}</span></td>
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