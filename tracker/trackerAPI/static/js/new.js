const check = document.getElementById("newCompany");
const extra = document.getElementById("extraFields");
const selectCompany = document.getElementById("company");
const footer = document.getElementById("footer");

check.addEventListener("change", () => {
  if (check.checked) {
    extra.classList.add("show");
    extra.querySelectorAll("input, textarea").forEach(el => el.disabled = false);
    selectCompany.disabled = true;
  } else {
    extra.classList.remove("show");
    extra.querySelectorAll("input, textarea").forEach(el => el.disabled = true);
    selectCompany.disabled = false;
  }
});

extra.querySelectorAll("input, textarea").forEach(el => el.disabled = true);

document.addEventListener("DOMContentLoaded", () => {
  axios.get('/api/company')
  .then(response => {
    const companies = response.data;
    selectCompany.innerHTML = "<option selected></option>";
    companies.forEach((company, i) => {
      const option = `<option value=${i}>${company.name}</option>`;
      selectCompany.innerHTML += option;
    })
  })
  .catch(error => {
    console.log(error);
  })
});