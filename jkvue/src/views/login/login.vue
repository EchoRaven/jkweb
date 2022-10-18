<template>
    <div class="login_board">
        <h2 class="login_table">Login</h2>
        <form>
            <p v-show="showTishi">{{tishi}}</p>
            <input class="input" type="text" id="username" placeholder="username" v-model="username">
            <input class="input" type="password" id="password" placeholder="password" v-model="password">
            <button class="loginbutton" v-on:click="login">登录</button>
            <span class="c_t_r" v-on:click="ToRegister">go to register page</span>
        </form>
    </div>
</template>

<script>
import { setCookie, getCookie } from '../../assets/js/cookie.js'
export default {
    data() {
        return {
            username: "",
            password: "",
            showTishi: false,
            tishi: "",
        }
    },
    methods: {
        login() {
            if (this.username == "" || this.password == "") {
                alert("please input username and password")
                console.log('empty cin')
            } else {
                // URLSearchParams对象是为了让参数以form data形式
                let params = new URLSearchParams();
                params.append('username', this.username);
                params.append('password', this.password);
                this.axios.post("http://127.0.0.1:5000/user/login", params).then((res) => {
                    console.log(res.data)
                    console.log(typeof res.data)
                    if (res.data == 405) {
                        this.tishi = "user does not exist"
                        console.log(res.data)
                        this.showTishi = true
                    } else if (res.data == 404) {
                        this.tishi = "false password"
                        this.showTishi = true
                        console.log(res.data)
                    } else if (res.data == 403) {
                        this.tishi = "false form"
                        this.showTishi = true
                        console.log(res.data)
                    } else if (res.data == "admin") {
                        this.$router.push("/home")
                        console.log(res.data)
                    } else if (res.data == 402) {
                        console.log('successful login')
                        this.tishi = "successful login"
                        this.showTishi = true
                        console.log(res.data)
                        setCookie("username", this.username, 1000 * 60)
                        setTimeout(function () {
                            this.$router.push("/home")
                        }.bind(this), 1000)
                    }
                })
            }
        },
        ToRegister() {
            this.$router.push("/register")
        }
    }
}
</script>