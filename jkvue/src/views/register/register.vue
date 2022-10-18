<template>
    <div class="reg_board">
        <h2 class="reg_table">Register</h2>
        <form>
            <p v-show="showTishi">{{tishi}}</p>
            <input class="input" type="text" id="username" placeholder="username" v-model="username">
            <input class="input" type="text" id="password" placeholder="password" v-model="password">
            <input class="input" type="text" id="email" placeholder="email" v-model="email">
            <button class="veributton" v-on:click="sendvcode">send verificode</button>
            <input class="input" type="text" id="vcode" placeholder="vcode" v-model="vcode">
            <button class="regbutton" v-on:click="register">register</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "",
            password: "",
            email: "",
            vcode: "",
            showTishi: false,
            tishi: "",
        }
    },
    methods: {
        sendvcode() {
            if (this.email == "") {
                alert("please input email")
                console.log('empty email')
            } else {
                let params = new URLSearchParams();
                params.append('email', this.email);
                console.log(this.email)
                this.axios.post("http://127.0.0.1:5000/user/mail", params).then((res) => {
                    console.log(res.data)
                    console.log(typeof res.data)
                    if (res.data == 406) {
                        console.log(res.data)
                        this.tishi = "fail to send mail"
                        this.showTishi = True
                    } else if (res.data == 407) {
                        console.log(res.data)
                    }
                })
            }
        },
        register() {
            if (this.username == "" || this.password == "" || this.email == "" || this.vcode == "") {
                alert("please input infomation")
                console.log('empty cin')
            } else {
                let params = new URLSearchParams();
                params.append('username', this.username);
                params.append('password', this.password);
                params.append('email', this.email);
                params.append('vcode', this.vcode);
                this.axios.post("http://127.0.0.1:5000/user/register", params).then((res) => {
                    console.log(res.data)
                    console.log(typeof res.data)
                    if (res.data == 400) {
                        console.log(res.data)
                        this.$router.push('/')
                    } else if (res.data == 401) {
                        console.log(res.data)
                        this.tishi = "error information"
                        this.showTishi = true
                    }
                })
            }
        }
    }
}
</script>