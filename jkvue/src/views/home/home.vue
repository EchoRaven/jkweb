<template>

    <div class="home_board">
        <link rel="stylesheet" href="http://at.alicdn.com/t/font_1309180_m0vigzfu7y.css" />
        <form class="search_form">
            <div class="back"></div>
            <img id="logo" src="../../picture/mylogo.png" />
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
            <div id="raccoon" v-on:click="show_sbox"></div>
            <div id="boomcloud"></div>
            <div id="searchResult">
                <div v-for="(res, index) in searchResult" class="searchResult">
                    <hr v-if="index > 0" />
                    <div class="searchResultSingleBox" v-on:click="goto_page(searchResult[index])">
                        <div class="searchResultTitle">{{ searchTitle[index] }}</div>
                    </div>
                </div>
            </div>
            <div class="search-box">
                <input type="text" class="search-text" v-model="search_content" />
                <a class="search-btn" v-on:click="search">
                    <!--这个#号要改成正确的URL，到时候有文章了可以改的-->
                    <i class="iconfont iconchazhao"></i>
                </a>
            </div>
            <img :src="headshot" id="user" v-on:click="goto_user" />
        </form>
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
            title_list: [],
            headshot: "",
            searchResult: [],//这里直接储存文章序号
            searchTitle: [],//这里储存文章标题
            search_show: false,
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
        let params2 = new URLSearchParams();
        params2.append('uid', this.uid);
        this.$axios.post('http://127.0.0.1:5000/user/get_userinfo', params2).then(res => {
            this.headshot = res.data['headshot'];
        });
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
                com.style.backgroundColor = "#18c870";
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
                this.$router.push({ name: "write", params: { uid: this.uid } });
            }.bind(this), 1000)
        }, goto_user() {
            setTimeout(function () {
                this.$router.push({ name: "user", params: { uid: this.uid } });
            }.bind(this), 1000)
        }, search() {
            var tags = [];
            for (var i = 0; i < this.c_tags.length; ++i) {
                tags.push(this.all_tags[this.c_tags[i]]);
            }
            let params = new URLSearchParams();
            params.append('tags', tags);
            params.append('words', this.search_content);
            this.$axios.post("http://127.0.0.1:5000/search/get_search", params).then((res) => {
                this.searchResult = res.data['search_id'];
                this.searchTitle = res.data['search_title'];
                console.log(this.searchResult);
                console.log(this.searchTitle);
            })
            var n = 0;
            var timer = setInterval(() => {
                if (n == 0) {
                    document.getElementsByClassName('search-box')[0].style.visibility = 'hidden';
                    document.getElementById('searchResult').style.opacity = '100';
                    document.getElementById('searchResult').style.zIndex = '10';
                    n++;
                }
                else if (n <= 10) {
                    document.getElementsByClassName('search-box')[0].style.marginTop = (380 - 12 * n) + 'px';
                    n++;
                } else if (n == 11) {
                    document.getElementById('boomcloud').style.opacity = '100';
                    document.getElementById('boomcloud').style.zIndex = '100';
                    n++;
                } else if (n <= 79) {
                    n++;
                } else if (n == 80) {
                    document.getElementById('boomcloud').style.opacity = '0';
                    document.getElementById('boomcloud').style.zIndex = '-100';
                    n++;
                } else if (n <= 85) {
                    n++;
                } else if (n == 86) {
                    document.getElementById('raccoon').style.opacity = '100';
                    document.getElementById('raccoon').style.zIndex = '100';
                    n++;
                } else {
                    clearInterval(timer);
                }
            }, 10);
        },
        show_sbox() {
            console.log("return");
            var n = 0;
            var timer = setInterval(() => {
                if (n == 0) {
                    document.getElementsByClassName('search-box')[0].style.visibility = 'visible';
                    document.getElementById('raccoon').style.opacity = '0';
                    document.getElementById('raccoon').style.zIndex = '100';
                    n++;
                }
                else if (n <= 10) {
                    document.getElementsByClassName('search-box')[0].style.marginTop = (260 + 12 * n) + 'px';
                    n++;
                } else if (n <= 45) {
                    n++;
                } else if (n == 46) {
                    document.getElementById('searchResult').style.opacity = '0';
                    document.getElementById('searchResult').style.zIndex = '-10';
                    n++;
                } else {
                    clearInterval(timer);
                }
            }, 10);
        }
    }
}
</script>

<style scoped>
body {
    margin: 0px;
    padding: 0px;
}

.search_form {
    height: 80px;
    width: 100%;
    background: url("../../picture/search_board.png") no-repeat;
    background-size: cover;
    z-index: 1000000;
}

.back {
    /* height: 100%; */
    /* width: 100%; */
    background: url("../../picture/background.jpg") no-repeat;
    /* background-size: cover; */
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
}

* {
    margin: 0;
    padding: 0
}

#logo {
    margin-top: 10px;
    margin-left: 10px;
    height: 60px;
    width: 80px;
    border-radius: 10px;
    position: fixed;

}

/*右上角小人图标(117, 230, 216*/
#user {
    background-size: contain;
    margin-top: 15px;
    margin-left: 1440px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    background-color: rgb(153, 227, 219);
    text-align: center;
    border: solid rgb(81, 255, 0) 3px;
}

.search-box {
    position: absolute;
    margin-top: 380px;
    margin-left: 765px;
    transform: translate(-50%, -50%);
    background: #eff1eb;
    height: 40px;
    border-radius: 30px;
    /*圆角边框*/
    padding: 10px;
}

.search-box:hover>.search-text {
    width: 400px;
}

.search-box:hover>.search-btn {
    background: rgb(3, 6, 0);
    color: #f0f1f3;
}

.search-btn {

    color: rgb(255, 255, 255);
    /* float: right; */
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: #18c870;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.5s;
}

.search-text {
    border: none;
    background: none;
    outline: none;
    float: left;
    padding: 0;
    color: rgb(0, 1, 9);
    font-size: 20px;
    font-family: "Microsoft YaHei UI Light";
    transition: 0.5s;
    line-height: 40px;
    width: 0px;

}

/* Tags*/
.tag_button {

    border: none;
    margin-top: 430px;
    margin-left: 725px;
    height: 50px;
    width: 80px;
    font-size: 40px;
    border-radius: 50px;
    position: fixed;
    background-color: #2fa415;
    text-align: center;
}

#tag_list {
    height: 180px;
    width: 430px;
    margin-top: 500px;
    margin-left: 550px;
    background-color: rgb(255, 255, 255);
    position: fixed;
    border-radius: 20px;
    border: solid;
    border-color: burlywood;
    background: url(../../picture/button_board.png) no-repeat;
}

#searchResult {
    padding: 30px;
    height: 400px;
    width: 600px;
    border-radius: 24px;
    background: #fff;
    box-shadow: 2px 2px 10px black;
    transition-duration: 1s;
    position: fixed;
    margin-left: 445px;
    margin-top: 200px;
    z-index: -10;
    opacity: 0;
}

.searchResultSingleBox:hover {
    background: rgb(194, 194, 194);
    transition-duration: 0.4s;
}

.searchResultSingleBox {
    border-radius: 8px;
    padding: 5px;
    transition-duration: 0.4s;
}

.searchResultTitle {
    margin: 5px 0 5px;
    font-size: large;
    font-weight: bold;
    max-lines: 1;
}

.ctag_button {
    border-color: white;
    margin-top: 15px;
    margin-left: 500px;
    height: 40px;
    width: 80px;
    border-radius: 30px;
    position: fixed;
    background-color: #18c870;
    text-align: center;
}

.cbutton_name {
    font-size: 20px;
    color: white;
}

.button_name {
    font-size: 23px;
    color: white;
}

#raccoon {
    position: fixed;
    z-index: 100;
    height: 200px;
    width: 200px;
    background: url(../../picture/raccoon.png) no-repeat;
    background-size: 80%;
    transform: rotate(-8deg);
    margin-left: 700px;
    margin-top: 60px;
    opacity: 0;
    transition: 0.3s;
}

#boomcloud {
    position: fixed;
    z-index: 100;
    height: 200px;
    width: 200px;
    background: url(../../picture/boomcloud.png) no-repeat;
    background-size: 80%;
    opacity: 0;
    margin-left: 683px;
    margin-top: 69px;
    transition: 1.2s;
}
</style>