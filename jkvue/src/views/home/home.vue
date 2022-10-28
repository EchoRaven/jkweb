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
            <button id="user" v-on:click="goto_write">Us</button>
        </form>
        <!--推荐页-->
        <div class="recommand_board">
            <div class="recommand_li" v-for="(id, index) in recommand_list">
                <!--cover之后应有闪烁与方法效果-->
                <button v-bind:id="recommandid(index)" v-on:click="goto_page(id)" class="rec_button">
                    <!--这里应当放置的是标题与text内容-->
                    {{ form_title(title_list[index]) }}
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            search_content: "",
            show_tag: false,
            uid: -1,
            //选择的标签
            c_tags: [],
            //全部的标签
            all_tags: ["science", "study", "work", "food", "arts", "news", "cpu", "physics", "music", "math", "foreign", "daily", "school", "base"],
            //推荐列表
            recommand_list: [],
            title_list: []
        }
    },
    mounted() {
        //从数据库中请求，获取推荐列表
        //搜索和推荐的文章格式应当是标题+文章部分内容，这里先用标题代替
        //循环获取点击量前几个的文章
        this.uid = this.$route.params.uid;
        let params = new URLSearchParams();
        this.$axios.post("http://127.0.0.1:5000/recommand", params).then((res) => {
            console.log(res.data['code']);
            if (res.data['code'] == 410) {
                var datalist = res.data['arts']
                var titlelist = res.data['title']
                for (var i = 0; i < datalist.length; ++i) {
                    this.recommand_list.push(datalist[i]);
                    this.title_list.push(titlelist[i]);
                }
            }
        }, 10);
    },
    methods: {
        show_tag_list() {
            this.show_tag = !this.show_tag;
            var l = this.all_tags.length;
            for (var i = 0; i < l; ++i) {
                var tgname = 'tag' + i;
                var tg = document.getElementById(tgname).style;
                tg.marginLeft = 5 + 84 * (i % 5) + 'px';
                tg.marginTop = 9 + 49 * Math.floor(i / 5) + 'px';
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
        }, recommandid(index) {
            return 'reco' + index;
        }, form_title(tit) {
            var res = "";
            if (tit.length < 7) {
                res = tit;
            } else {
                for (var i = 0; i < 6; ++i) {
                    res += tit[i];
                }
                for (var i = 0; i < 3; ++i) {
                    res += '.';
                }
            }
            return res;
        }, goto_page(index) {
            setTimeout(function () {
                this.$router.push({ name: "webs", params: { id: index } });
            }.bind(this), 1000)
        }, goto_write() {
            setTimeout(function () {
                this.$router.push({ name: "user", params: { uid: this.uid } });
            }.bind(this), 1000)
        }
    }
}
</script>

<style>
.search_form {
    margin-top: -100px;
    position: fixed;
    height: 80px;
    width: 100%;
    background: url("../../picture/search_board.png") no-repeat;
    background-size: cover;
    z-index: 1000000;
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
    margin-left: 1400px;
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
    position: fixed;
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
    background: url(../../picture/button_board.png) no-repeat;
}

body {
    background: url(../../picture/home_board.png) no-repeat;
    background-size: cover;
}

.rec_button {
    background: url(../../picture/arrow.png) no-repeat;
    background-size: 230%;
    background-position: -50px -50px;
    height: 100px;
    width: 200px;
    font-size: 20px;
    font-weight: bolder;
    border-color: transparent;
    text-shadow: 2px 2px 5px red;
}

.rec_button:hover {
    height: 150px;
    width: 300px;
    font-size: 30px;
    animation: arrow_c 5s infinite alternate;
}

@keyframes arrow_c {
    0% {
        background: url(../../picture/arrow.png) no-repeat;
        background-size: 230%;
        background-position: -75px -75px;
        text-shadow: 2px 2px 5px red;
    }

    50% {
        background: url(../../picture/arrow_change.png) no-repeat;
        background-size: 100%;
        background-position: -40px -30px;
        text-shadow: -2px -2px 10px rgb(78, 219, 39);
    }

    100% {
        background: url(../../picture/arrow.png) no-repeat;
        background-size: 230%;
        background-position: -75px -75px;
        text-shadow: 2px 2px 5px red;
    }
}

.recommand_li {
    margin-top: 50px;
    margin-left: 100px;
    width: 900px;
    background-color: white;
}

.recommand_board {
    position: relative;
    margin-top: 100px;
}
</style>