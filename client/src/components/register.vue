<template>
  <div class="container">
    <p class="heading">Регистрация</p>
    <div class="box">
      <p>Email</p>
      <div>
        <input id="email" type="email" name="email" required v-model="email" placeholder="Введите действующий email"></div>
      </div> <div class="box">
    <p>Имя</p>
      <div><input type="text" id="username" name="username" required v-model="username" placeholder="До 16 символов, буквы и цифры"></div>
    </div>
    <div class="box">
      <p>Придумайте надежный пароль</p>
      <div><input type="password" id="password" name="password" required v-model="password" placeholder="Oт 8 до 20 символов"></div>
    </div> <div class="box">
    <p>Повторите пароль</p>
      <div><input type="password" id="password_confirmation" name="password_confirmation" required v-model="password_confirmation" placeholder="Повторите пароль"></div>
    </div>

    <button class="loginBtn" @click="submit">Зарегистрироваться</button>
    <p class="text">Уже зарегистрированы? <a @click="$router.push('/login')">Войти</a></p>
  </div>
</template>

<script>
import { required, between, maxLength, minLength, email, alphaNum, sameAs} from '@vuelidate/validators'
import useVuelidate from '@vuelidate/core'
export default {
  name: "register",
  setup: () => ({ v$: useVuelidate() }),
  data(){
    return {
      username : '',
      email : '',
      password : '',
      password_confirmation : '',
    }
  },
  validations () {
  return {
    username: {
      required,
      maxLengthValue: maxLength(16),
      alphaNum
    },
    email: {
      required,
      email
    },
    password: {
      required,
      sameAsConf: sameAs(this.password_confirmation),
      maxLengthValue: maxLength(20),
      mixLengthValue: minLength(8),
    }
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
        .catch(err => console.log(err), alert(err))
    },
    async submit () {
      const result = await this.v$.$validate()
      if (!result) {
        alert("Неправильно заполнена форма. Проверьте введенные данные и попробуйте еще раз.")
        return
      }
      this.register()
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
  padding: 2em;
  margin-top: 100px;
}

.heading {
  font-size: 2em;
  margin-bottom: 0.5em
}

.box {
  margin: 0.2em 0;
  margin-top: 15px;
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
  position: relative;
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
