<template>
  <div class="container">
    <p class="heading">Вход</p>
    <div class="box">
      <p>Email</p>
      <div><input type="text" autocomplete="off" placeholder="Введите email"></div>
    </div>
    <div class="box">
      <p>Пароль</p>
      <div><input type="text" autocomplete="off" placeholder="Введите пароль"></div>
    </div>
    <button class="loginBtn">Войти</button>
    <p class="text">Нет аккаунта? <a @click="$router.push('/register')">Зарегистрироваться</a></p>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login: function () {
      let email = this.email
      let password = this.password
      this.$store.dispatch('login', {email, password})
        .then(() => this.$router.push('/'))
        .catch(err => console.log(err))
    }
  }
}
</script>

<style scoped>


body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: white;
}

.container {
  background: white;
  width: 350px;
  height: 350px;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  color: #007cff;
  padding: 2em
}

.heading {
  font-size: 2em;
  margin-bottom: 0.5em
}

.box {
  margin: 0.2em 0
}

.container
.box p {
  color: black;
}

.container .box div {
  position: relative;
  width: 100%;
  height: 40px;
  margin: 0.2em 0
}

.container .box input {
  position: absolute;
  width: 100%;
  height: 100%;
  background: white;
  color: black;
  border: none;
  outline: none;
  padding-left: 0.8em;
  border-radius: 10px;
  transition: all 0.5s
}

.container .box input:focus::placeholder {
  color: black
}

.container .box div::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 102%;
  height: 105%;
  border-radius: 10px;
  background: #007cff
}

.loginBtn {
  width: 102%;
  height: 40px;
  border-radius: 10px;
  margin: 0.2em 0;
  transform: translate(-1%);
  cursor: pointer;
  color: black;
  background: #007cff;
  transition: all 0.5s
}

.loginBtn:hover {
  transform: translate(-1%, 5%);
  box-shadow: 0 0 10px #007cff
}

.text {
  font-size: 0.8em;
  margin-top: 0.5em;
  text-align: center;
  color: black;
}

.text a {
  color: #007cff;
}
</style>
