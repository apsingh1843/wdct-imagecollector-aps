const usernamefield = document.querySelector("#usernamefield");
const usernamearea = document.querySelector(".username-feedback");
const emailfield = document.querySelector("#emailfield");
const emailarea = document.querySelector(".email-feedback");
const passwordfield= document.querySelector("#passwordfield");
const showpassword = document.querySelector("#showpassword");
const SubmitBtn = document.querySelector(".submit_btn");

const PasswordToggle = (e) => {
if (showpassword.textContent === "Show") {
  showpassword.textContent = "Hide";
  passwordfield.setAttribute("type", "text");
}
else {
  showpassword.textContent = "Show";
  passwordfield.setAttribute("type", "password");
}
};

showpassword.addEventListener("click", PasswordToggle);


emailfield.addEventListener("keyup", (e) => {
  const emailval = e.target.value;

  emailfield.classList.remove("is-invalid");
  emailarea.style.display = "none";
  SubmitBtn.removeAttribute("disabled");

  if (emailval.length > 0) {
    fetch("/authentication/validate-email", {
       body: JSON.stringify({ email: emailval }),
       method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.email_error) {
          SubmitBtn.setAttribute("disabled","");
          emailfield.classList.add("is-invalid");
          emailarea.style.display = "block";
          emailarea.innerHTML = `<p>${data.email_error}</p>`;
        }
      });
  }
});

usernamefield.addEventListener("keyup", (e) => {
  console.log("555", 555);
  const usernameval = e.target.value;

  usernamefield.classList.remove("is-invalid");
  usernamearea.style.display = "none";
  SubmitBtn.removeAttribute("disabled");


  if (usernameval.length > 0) {
    fetch("/authentication/validate-username", {
       body: JSON.stringify({ username: usernameval }),
       method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.username_error) {
          SubmitBtn.setAttribute("disabled","");
          usernamefield.classList.add("is-invalid");
          usernamearea.style.display = "block";
          usernamearea.innerHTML = `<p>${data.username_error}</p>`;
        }
      });
  }
});
