<template>
  <div class="container">
    <p class="heading">Регистрация</p>
    <div class="box">

      <div><input type="text" autocomplete="off" v-model="email" placeholder="Введите email"></div>
    </div> <div class="box">

      <div><input type="text" autocomplete="off" v-model="username" placeholder="Введите имя"></div>
    </div>
    <div class="box">

      <div><input type="text" autocomplete="off" v-model="password" placeholder="Введите пароль"></div>
    </div> <div class="box">

      <div><input type="text" autocomplete="off" v-model="password_confirmation" placeholder="Повторите пароль"></div>
    </div>
    <button class="loginBtn" @click="register">Зарегистрироваться</button>
    <p class="text">Уже зарегистрированы? <a @click="$router.push('/login')">Войти</a></p>
  </div>
</template>

<script>
export default {
  name: "register",
  data(){
    return {
      username : "",
      email : "",
      password : "",
      password_confirmation : "",
    }
  },
  methods: {
    register: function () {
      let data = {
        email: this.email,
        username: this.username,
        password: this.password,

      }
      console.log(data)
      this.$store.dispatch('register', data)
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
