function validateOrder() {
    // Variables for the form fields

    var pizza = document.form_order.pizza.value;
    var quantity = document.form_order.quantity.value;

    //Check the email field is empty
    if ((pizza == "") || (pizza == "undefined")) {
      alert("Insert a valide pizza's name.");
      document.form_order.pizza.select();
      return false;
    }
    //Check the password field is empty
    else if ((quantity == "") || (quantity <= 0)) {
      alert("Quantity is required > 0.");
      document.form_order.quantity.focus();
      return false;
    }

    //Send the form
    else {
      document.form_order.action = "/order";
      document.form_order.submit();
    }
  }