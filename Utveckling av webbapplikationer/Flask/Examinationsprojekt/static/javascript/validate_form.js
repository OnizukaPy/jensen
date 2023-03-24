function validateForm() {
    // Variables for the form fields

    var email = document.form_login.email.value;
    var password = document.form_login.password.value;

    // Espressione regolare dell'email
    var email_reg_exp = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-]{2,})+.)+([a-zA-Z0-9]{2,})+$/;

    //Check the email field is empty
    if (!email_reg_exp.test(email) || (email == "") || (email == "undefined")) {
      alert("Insert a valide email adress.");
      document.form_login.email.select();
      return false;
    }
    //Check the password field is empty
    else if ((password == "") || (password == "undefined")) {
      alert("The password field is required.");
      document.form_login.password.focus();
      return false;
    }

    //Send the form
    else {
      document.form_login.action = "/login";
      document.form_login.submit();
    }
  }