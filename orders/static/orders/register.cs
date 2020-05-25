/* Mobile First */
#register_container {
  margin: 20px 20px 0px 20px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
#register_container #register_form {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
#register_container #register_form input {
  width: 100%;
  border-radius: 0px;
  padding: 8px 6px;
}
#register_container #register_form .register_input {
  margin-top: 20px;
}

/* Desktops and laptops */
@media screen and (min-width: 1200px) {
  #login_container {
    width: 50%;
    margin: 0 auto;
    padding-top: 50px;
  }
  #login_container #login_form {
    border: 1px solid forestgreen;
  }
  #login_container #login_form .login_input {
    width: 80%;
  }
  #login_container #login_form .button_big {
    width: 60%;
  }
  #login_container .login_register {
    margin-top: 50px;
  }
}

/*# sourceMappingURL=register.cs.map */
