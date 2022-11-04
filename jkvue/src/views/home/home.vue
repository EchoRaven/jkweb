<template>
    
    <div class="home_board">
        <link rel="stylesheet" href="http://at.alicdn.com/t/font_1309180_m0vigzfu7y.css"/>
        <form class="search_form">
            <div class="back"></div>
            <img id="logo" src="../../picture/mylogo.png"/>
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
            <div class="search-box">
                <input type="text" class="search-text" v-model="search_content"/>
                <a class="search-btn" href="#"><!--这个#号要改成正确的URL，到时候有文章了可以改的-->
                <i class="iconfont iconchazhao"></i>
                </a>
            </div>
            <button id="user" v-on:click="goto_user"></button>
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
    z-index: 1000000;
}
.back{
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
    background: url(../../picture/person.png) no-repeat;
    background-size: contain;
    margin-top: 15px;
    margin-left: 1480px;
    height: 30px;
    width: 25px;
    border-radius: 10px;
    position: fixed;
    background-color: rgb(153, 227, 219);
    text-align: center;
    font-size: 35px;
}

.search-box
{
    position: absolute;
    margin-top: 380px;
    margin-left: 765px;
    transform: translate( -50%,-50%);
    background: #eff1eb;
    height: 40px;
    border-radius: 30px; /*圆角边框*/
    padding: 10px;
}
.search-box:hover> .search-text
{
    width: 400px;
}
.search-box:hover> .search-btn
{
    background: rgb(3, 6, 0);
    color: #f0f1f3;
}
.search-btn
{

    color: rgb(255, 255, 255);
    /* float: right; */
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background:#18c870;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.5s;
}
.search-text
{
    border: none;
    background: none;
    outline: none;
    float: left;
    padding: 0;
    color: rgb(0, 1, 9);
    font-size: 20px;
    font-family: "Microsoft YaHei UI Light";
    transition: 0.5s;
    line-height:40px;
    width:  0px;

}

/* Tags*/ 
.tag_button {
    
    border:none;
    margin-top: 430px;
    margin-left: 740px;
    height: 30px;
    width: 50px;
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
    font-size: 15px;
    color: white;
}
</style>