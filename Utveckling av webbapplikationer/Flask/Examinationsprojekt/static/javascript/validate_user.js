function validateUser() {
  // Variables for the form fields

  var name = document.form_register.name.value;
  var email = document.form_register.email.value;
  var password = document.form_register.password.value;
  var password_confirm = document.form_register.password_confirm.value;

  // Espressione regolare dell'email
  var email_reg_exp = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-]{2,})+.)+([a-zA-Z0-9]{2,})+$/;

  //Check the name field is empty
  if ((name == "") || (name == "undefined")) {
    alert("The name field is required.");
    document.form_register.name.focus();
    return false;
  }

  //Check the email field is empty
  if (!email_reg_exp.test(email) || (email == "") || (email == "undefined")) {
    alert("Insert a valide email adress.");
    document.form_register.email.select();
    return false;
  }
  //Check the password field is empty
  else if ((password == "") || (password == "undefined")) {
    alert("The password field is required.");
    document.form_register.password.focus();
    return false;
  }

  //Check the password_confirm field is empty
  else if ((password_confirm == "") || (password_confirm == "undefined")) {
    alert("The password confirmation field is required.");
    document.form_register.password_confirm.focus();
    return false;
  }

  //Check the password and password_confirm fields are equal
  else if (password != password_confirm) {
    alert("The password and password confirmation fields must be equal.");
    document.form_register.password.focus();
    return false;
  }

  //Send the form
  else {
    document.form_register.action = "/register";
    document.form_register.submit();
  }
}