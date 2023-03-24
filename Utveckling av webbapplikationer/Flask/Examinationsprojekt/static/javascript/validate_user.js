function validateUserForm() {
    // Variables for the form fields

    var name = document.form_user.name.value;
    var email = document.form_user.email.value;
    var password = document.form_user.password.value;

    // Espressione regolare dell'email
    var email_reg_exp = /^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-]{2,})+.)+([a-zA-Z0-9]{2,})+$/;

    //Check the email field is empty
    if (!email_reg_exp.test(email) || (email == "") || (email == "undefined")) {
      alert("Insert a valide email adress.");
      document.form_user.email.select();
      return false;
    }
    //Check the name field is empty
    else if ((name == "") || (name == "undefined")) {
        alert("The password field is required.");
        document.form_user.password.focus();
        return false;
        }
    //Check the password field is empty
    else if ((password == "") || (password == "undefined")) {
      alert("The password field is required.");
      document.form_user.password.focus();
      return false;
    }

    //Send the form
    else {
      document.form_user.action = "/add_user";
      document.form_user.submit();
    }
  }