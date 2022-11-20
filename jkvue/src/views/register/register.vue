<template>
    <div class="reg_board">
        <video class="video-background" preload="auto" loop playsinline autoplay src="../../video/loginbck.mp4"
            muted="muted"></video>
        <button id="reg_ball" v-on:click="show_board">
            <span class="reg_title" v-show="show_reg">Register</span>
            <!--这同时也是username的按钮-->
        </button>
        <button id="reg_ball_1" v-show="show_ball">
            <!--这个是password的按钮-->
        </button>
        <button id="reg_ball_2" v-show="show_ball">
            <!--这个是email的按钮-->
        </button>
        <button id="reg_ball_3" v-show="show_ball" v-on:click="sendvcode">
            <!--这个同时也是sendvcode按钮-->
            <span class="reg_ball_3_title" v-show="show_reg_ball_3">Send Verificode</span>
        </button>
        <button id="reg_ball_4" v-show="show_ball">
            <!--这个是vcode的按钮-->
        </button>
        <button id="reg_ball_5" v-show="show_ball" v-on:click="register">
            <span class="reg_ball_5_title" v-show="show_reg_ball_5">Sign Up</span>
            <!--这个同时也是sign up按钮-->
        </button>
        <button id="reg_ball_6" v-show="show_ball" v-on:click="ToLogin">
            <span class="reg_ball_6_title" v-show="show_reg_ball_6">Go To Sign In</span>
            <!--这个同时也是sign in按钮-->
        </button>
        <form class="reg_form" v-show="show_b">
            <p class="Tishi" v-show="showregTishi">{{ regtishi }}</p>
            <input class="input" type="text" id="newusername" placeholder="username" v-model="username">
            <input class="input" type="password" id="newpassword" placeholder="password" v-model="password">
            <input class="input" type="text" id="newemail" placeholder="email" v-model="email">
            <input class="input" type="text" id="vcode" placeholder="vcode" v-model="vcode">
        </form>
    </div>
</template>

<script>
import { email } from 'is2';

export default {
    data() {
        return {
            username: "",
            password: "",
            email: "",
            vcode: "",
            showregTishi: false,
            show_b: false,
            regtishi: "这里是提示",
            canclick: true,
            show_ball: false,
            show_reg_ball_3: false,
            show_reg_ball_5: false,
            show_reg_ball_6: false,
            show_reg: true,
        }
    },
    methods: {
        sendvcode() {
            if (this.email == "") {
                this.regtishi = "Please Input Email"
                this.showregTishi = true
                this.line_shake()
                console.log('empty email')
            } else {
                let params = new URLSearchParams();
                params.append('email', this.email);
                console.log(this.email)
                this.$axios.post("http://127.0.0.1:5000/user/mail", params).then((res) => {
                    console.log(res.data)
                    console.log(typeof res.data)
                    if (res.data == 406) {
                        console.log(res.data)
                        this.regtishi = "Fail To Send Mail"
                        this.showregTishi = True
                        this.line_shake()
                    } else if (res.data == 407) {
                        console.log(res.data)
                        this.regtishi = "Vcode Has Been Sent To Your Email"
                        this.showregTishi = true;
                    } else if (res.data == 408) {
                        this.regtishi = "The Email Is Already Registered"
                        this.showregTishi = true
                        this.line_shake()
                    } else if (res.data == 409) {
                        this.regtishi = "The Eail Format Is Incorrect"
                        this.showregTishi = true
                        this.line_shake()
                    }
                })
            }
        },
        register() {
            if (this.username == "" || this.password == "" || this.email == "" || this.vcode == "") {
                this.regtishi = "Please Input Infomation"
                this.showregTishi = true
                this.line_shake()
                console.log('empty cin')
            } else {
                let params = new URLSearchParams();
                params.append('username', this.username);
                params.append('password', this.password);
                params.append('email', this.email);
                params.append('vcode', this.vcode);
                this.$axios.post("http://127.0.0.1:5000/user/register", params).then((res) => {
                    console.log(res.data)
                    console.log(typeof res.data)
                    if (res.data == 400) {
                        this.regtishi = "Successful Register"
                        this.showregTishi = true
                        console.log(res.data)
                        this.$router.push('/')
                    } else if (res.data == 401) {
                        console.log(res.data)
                        this.regtishi = "Error Information"
                        this.showregTishi = true
                        this.line_shake()
                    }
                })
            }
        },
        show_board() {
            //分3段动画，第一个圈原地缩小，第二个到第四个圈弹跳出现，展开成登录界面
            var n1 = 0;//第一区间段的计时器
            var n2 = 0;//第二区间段的计时器
            var n3 = 0;//第三区间段的计时器
            var n4 = 0;//第四区间段的计时器
            var n5 = 0;//第五区间段的计时器
            if (this.canclick) {
                var timer = setInterval(() => {
                    this.show_reg = false;
                    if (n1 <= 25) {
                        reg_ball.style.height = (300 - n1 * 10) + 'px';
                        reg_ball.style.width = (300 - n1 * 10) + 'px';
                        reg_ball.style.radius = (300 - n1 * 10) + 'px';
                        n1++;
                    } else if (n2 <= 20) {
                        this.show_ball = true;
                        reg_ball_1.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n2 <= 40) {
                        reg_ball_2.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n2 <= 60) {
                        reg_ball_3.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n2 <= 80) {
                        reg_ball_4.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n2 <= 100) {
                        reg_ball_5.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n2 <= 120) {
                        reg_ball_6.style.marginTop = 50 + 5 * n2 + 'px';
                        n2++;
                    } else if (n3 <= 40) {
                        this.show_b = true;
                        reg_ball_3.style.width = (50 + 4 * n3) + 'px';
                        n3++;
                    } else if (n4 <= 40) {
                        this.show_reg_ball_3 = true;
                        reg_ball_5.style.width = (50 + 4 * n4) + 'px';
                        n4++;
                    } else if (n5 <= 40) {
                        this.show_reg_ball_5 = true;
                        reg_ball_6.style.width = (50 + 4 * n5) + 'px';
                        n5++;
                    } else {
                        this.show_reg_ball_6 = true;
                        clearInterval(timer);
                    }
                }, 10);
            }
            this.canclick = false;
        }, line_shake() {
            var n = 0;
            var timer = setInterval(() => {
                if (n <= 10) {
                    reg_ball.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_1.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_2.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_3.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_4.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_5.style.marginLeft = 550 + 5 * n + 'px';
                    reg_ball_6.style.marginLeft = 550 + 5 * n + 'px';
                    newusername.style.marginLeft = 620 + 5 * n + 'px';
                    newpassword.style.marginLeft = 620 + 5 * n + 'px';
                    newemail.style.marginLeft = 620 + 5 * n + 'px';
                    vcode.style.marginLeft = 620 + 5 * n + 'px';
                    n++;
                } else if (n <= 20) {
                    reg_ball.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_1.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_2.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_3.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_4.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_5.style.marginLeft = 650 - 5 * n + 'px';
                    reg_ball_6.style.marginLeft = 650 - 5 * n + 'px';
                    newusername.style.marginLeft = 720 - 5 * n + 'px';
                    newpassword.style.marginLeft = 720 - 5 * n + 'px';
                    newemail.style.marginLeft = 720 - 5 * n + 'px';
                    vcode.style.marginLeft = 720 - 5 * n + 'px';
                    n++;
                } else if (n <= 30) {
                    reg_ball.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_1.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_2.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_3.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_4.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_5.style.marginLeft = 450 + 5 * n + 'px';
                    reg_ball_6.style.marginLeft = 450 + 5 * n + 'px';
                    newusername.style.marginLeft = 520 + 5 * n + 'px';
                    newpassword.style.marginLeft = 520 + 5 * n + 'px';
                    newemail.style.marginLeft = 520 + 5 * n + 'px';
                    vcode.style.marginLeft = 520 + 5 * n + 'px';
                    n++;
                } else if (n <= 40) {
                    reg_ball.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_1.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_2.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_3.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_4.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_5.style.marginLeft = 750 - 5 * n + 'px';
                    reg_ball_6.style.marginLeft = 750 - 5 * n + 'px';
                    newusername.style.marginLeft = 820 - 5 * n + 'px';
                    newpassword.style.marginLeft = 820 - 5 * n + 'px';
                    newemail.style.marginLeft = 820 - 5 * n + 'px';
                    vcode.style.marginLeft = 820 - 5 * n + 'px';
                    n++;
                } else {
                    clearInterval(timer);
                }
            }, 3);
        },
        ToLogin() {
            this.$router.push("/")
        },
    }
}
</script>

<style scoped>
@import"register_style.css";

/*引入css文件 */
@keyframes flashing {
    0% {
        box-shadow: 0px 0px 0px cyan;
        border-color: aliceblue;
    }

    50% {
        box-shadow: 0px 0px 40px cyan;
        border-color: aliceblue;
    }

    100% {
        box-shadow: 0px 0px 0px cyan;
        border-color: aliceblue;
    }

}

#reg_ball {
    background: url(../../picture/earth.jpg) repeat-x 0 0;
    /*引入地球图片作为背景*/
    margin-top: 50px;
    height: 300px;
    width: 300px;
    margin-left: 550px;
    position: fixed;
    border-radius: 300px;
    animation: flashing 2s infinite alternate, loop 20s linear infinite;
    /*地球自转动画*/
    color: rgb(73, 64, 64);
}

.reg_form {
    position: fixed;
}

/*字体修改 */
.reg_title {
    color: aliceblue;
    font-size: 60px;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    animation: focus-in-contract-bck 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}

#reg_ball_1 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

#reg_ball_2 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

#reg_ball_3 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

#reg_ball_4 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

#reg_ball_5 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

#reg_ball_6 {
    margin-top: 50px;
    margin-left: 550px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    animation: flashing 2s infinite alternate;
}

.login_form {
    margin-top: 0px;
    margin-left: 0px;
    height: 0;
    width: 0;
}

.Tishi {
    margin-top: 5px;
    margin-left: 560px;
    height: 30px;
    width: 800px;
    font-size: 20px;
    color: rgb(154, 151, 151);
    position: fixed;
}

.reg_ball_3_title {
    font-size: 25px;
    color: cornflowerblue;
    text-align: center;
}

.reg_ball_5_title {
    font-size: 25px;
    color: cornflowerblue;
    text-align: center;
}

.reg_ball_6_title {
    font-size: 25px;
    color: cornflowerblue;
    text-align: center;
}

body {
    display: block;
    margin: 0px;
    margin-top: 0px;
    margin-right: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    background-color: black;
}

#newusername {
    margin-top: 55px;
    margin-left: 620px;
    position: fixed;
    border: none;
    border-bottom: 2px solid rgb(154, 151, 151);
    font-size: 30px;
    color: rgb(154, 151, 151);
    background-color: black;
}

#newpassword {
    margin-top: 155px;
    margin-left: 620px;
    border: none;
    position: fixed;
    border-bottom: 2px solid rgb(154, 151, 151);
    font-size: 30px;
    color: rgb(154, 151, 151);
    background-color: black;
}

#newemail {
    margin-top: 255px;
    margin-left: 620px;
    border: none;
    position: fixed;
    border-bottom: 2px solid rgb(154, 151, 151);
    font-size: 30px;
    color: rgb(154, 151, 151);
    background-color: black;
}

#vcode {
    margin-top: 455px;
    margin-left: 620px;
    border: none;
    position: fixed;
    border-bottom: 2px solid rgb(154, 151, 151);
    font-size: 30px;
    color: rgb(154, 151, 151);
    background-color: black;
}

.video-background {
    position: fixed;
    overflow: hidden;
    background-size: cover;
}
</style>
