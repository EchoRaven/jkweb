<template>
    <div class="home_board">
        <form class="search_form">
            <span id="logo">Logo</span>
            <!--搜索区域可以大一点-->
            <button class="tag_button" v-on:click="show_tag_list">
                <!--标签筛选-->
                <p class="button_name">Tags</p>
            </button>
            <div id="tag_list" v-show="show_tag">
                <div v-for="(tg, index) in all_tags">
                    <button v-bind:id="tagid(index)" class="ctag_button" v-on:click="chooseTag($event)">
                        <p class="cbutton_name">{{ tg }}</p>
                    </button>
                </div>
            </div>
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
            show_tag: false,
            //选择的标签
            c_tags: [],
            //全部的标签
            all_tags: ["science", "study", "work", "food", "arts", "news", "cpu", "physics", "music", "math", "foreign", "daily", "school"],
        }
    },
    mounted() {
        console.log("create");
    },
    methods: {
        show_tag_list() {
            this.show_tag = !this.show_tag;
            var l = this.all_tags.length;
            for (var i = 0; i < l; ++i) {
                var tgname = 'tag' + i;
                var tg = document.getElementById(tgname).style;
                tg.marginLeft = 5 + 84 * (i % 5) + 'px';
                tg.marginTop = 5 + 43 * Math.floor(i / 5) + 'px';
            }
        }, tagid(index) {
            return "tag" + index;
        }, chooseTag(event) {
            var el = event.currentTarget['id'];//获取了标签
            console.log(el);
            //转化为Other
            //首先从el中获取标签序号
            var index = "";
            for (var i = 3; i < el.length; ++i) {
                index = index + el[i];
            }
            var check = 0;
            var l = this.c_tags.length;
            for (var i = 0; i < l; ++i) {
                if (this.c_tags[i] == index) {
                    check = 1;
                    break;
                }
            }
            if (check == 0) {
                this.c_tags.push(index);
                var com = document.getElementById(el);
                com.style.backgroundColor = "rgb(5, 111, 5)";
            }
            else {
                this.c_tags = this.c_tags.filter(function (item) {
                    return item != index;
                })
                var com = document.getElementById(el);
                com.style.backgroundColor = "rgb(7, 197, 7)";
            }
            console.log(this.c_tags);
        }
    }
}
</script>

<style>
.search_form {
    height: 80px;
    width: 100%;
    background: url("../../picture/search_board.png") no-repeat;
    background-size: cover;
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
    margin-left: 620px;
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

.tag_button {
    border-color: white;
    margin-top: 15px;
    margin-left: 500px;
    height: 50px;
    width: 100px;
    border-radius: 50px;
    position: fixed;
    background-color: rgb(7, 197, 7);
    text-align: center;
}

.ctag_button {
    border-color: white;
    margin-top: 15px;
    margin-left: 500px;
    height: 40px;
    width: 80px;
    border-radius: 30px;
    position: fixed;
    background-color: rgb(7, 197, 7);
    text-align: center;
}

.cbutton_name {
    font-size: 20px;
    color: white;
}

.button_name {
    font-size: 25px;
    color: white;
}

.input_search:focus {
    width: 500px;
}

.search_icon {
    position: absolute;
    width: 40px;
    height: 40px;
    border-radius: 40px;
    margin-left: 628px;
    margin-top: 23px;
    background: url(../../picture/sbutton.png) no-repeat;
    background-size: 70%;
    background-position: 6px 7px;
    cursor: pointer;
}

#divline {
    width: 400px;
    color: #987cb9;
    background-color: cadetblue;
    height: 1px;
    position: fixed;
    margin-left: 15px;
}

#tag_list {
    margin-top: 90px;
    height: 200px;
    width: 430px;
    margin-left: 500px;
    background-color: rgb(255, 255, 255);
    position: fixed;
    border-radius: 20px;
    border: solid;
    border-color: burlywood;
}
</style>