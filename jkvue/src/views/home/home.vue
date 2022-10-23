<template>
    <div class="home_board">
        <form class="search_form">
            <span id="logo">Logo</span>
            <!--搜索区域可以大一点-->
            <input type="text" class="input_search" v-model="search_content" />
            <span class="search_icon"></span>
            <span id="user">Us</span>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            search_content: "",
        }
    },
    methods: {
    }
}
</script>

<style>
.search_form {
    height: 80px;
    width: 100%;
    background: url("../../picture/search_board.png") no-repeat;
    background-size: cover;
    border-bottom: 10px;
    border-color: black;
}

* {
    margin: 0;
    padding: 0
}

#logo {
    margin-top: 15px;
    height: 50px;
    width: 100px;
    border-radius: 50px;
    position: fixed;
    background-color: white;
    text-align: center;
    font-size: 35px;
}

#user {
    margin-top: 15px;
    margin-left: 1600px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    background-color: white;
    text-align: center;
    font-size: 35px;
}

.input_search {
    border-color: white;
    margin-top: 15px;
    margin-left: 600px;
    height: 50px;
    width: 80px;
    border-radius: 50px;
    position: fixed;
    background-color: white;
    text-align: center;
    font-size: 25px;
    transition: width .5s;
    transition-delay: .1s;
}

.input_search:focus {
    width: 500px;
}

.search_icon {
    position: absolute;
    width: 40px;
    height: 40px;
    border-radius: 40px;
    margin-left: 608px;
    margin-top: 23px;
    background: url(../../picture/sbutton.png) no-repeat;
    background-size: 70%;
    background-position: 6px 7px;
    cursor: pointer;
}
</style>