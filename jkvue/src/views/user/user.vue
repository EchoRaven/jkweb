<template>
    <div>
        <!--这是用来修改头像的-->
        <div id="headshot_box">
            <input id="choose_p" type="file" @change="post_headshot" accept=".png, .jpg, .jpeg" />
            <button class="input_button" @click="p_input">选择图片</button>
            <p class="headtitle">头像效果</p>
            <img :src="tempshot" class="showhead" />
            <button class="closebutton" @click="closelist_c">关闭</button>
            <button class="ensurebutton" @click="closelist_e">确认</button>
        </div>
        <div id="change_abstract">
            <textarea id="change_abstract_input" placeholder="请输入新的简介" v-model="tempabstract">
            </textarea>
            <button class="closebutton" @click="a_closelist_c" id="b1">关闭</button>
            <button class="ensurebutton" @click="a_closelist_e" id="b2">确认</button>
        </div>
        <div id="userbox">
            <div class="head_box">
                <div class="header">
                    <div class="header_logo">
                        <div>
                            <h2>我的博客|</h2>
                            <h4>同舟共济</h4>
                        </div>
                    </div>
                    <div class="header_nav">
                        <ul class="clearfix">
                            <li class="have_second"><a>study</a>
                                <ul class="nav_second">
                                    <i></i>
                                    <li><a>science</a></li>
                                    <li><a>work</a></li>
                                    <li><a>arts</a></li>
                                    <li><a>news</a></li>
                                    <li><a>physics</a></li>
                                    <li><a>math</a></li>
                                    <li><a>music</a></li>
                                </ul>
                            </li>
                            <li class="have_second">
                                <a>daily life</a>
                                <ul class="nav_second">
                                    <i></i>
                                    <li><a>food</a></li>
                                    <li><a>school</a></li>
                                    <li><a>moive review</a></li>
                                    <li><a>travel</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                    <div class="header_nav_small_btn">
                        <span class="small_btn"></span>
                    </div>
                </div>
            </div>
            <div class="nav_hidden_zhanwei"></div>
            <div class="search_box">
                <div class="search">
                    <form name="searchform" class="search_form" method="post" action="[!--news.url--]e/search/index.php"
                        target="_blank">
                        <input type="text" class="search_text" name="keyboard" placeholder="输入关键字点击搜索">
                        <input type="hidden" name="tbname" value="news">
                        <input type="hidden" name="show" value="title">
                        <input type="hidden" name="tempid" value="1">
                        <input type="submit" class="search_btn" value="搜索一下">
                    </form>
                </div>
            </div>
            <div class="article_box clearfix">
                <div class="left">
                    <div class="article_content_box clearfix">
                        <div class="article_article_title">
                            <h3>我的文章</h3>
                        </div>
                        <h3 class="article_content_title">这里是文章的标题</h3>
                        <div class="article_author_count_box clearfix">
                            <i class="article_author_img" title="计科人">
                                <img :src="headshot" />
                            </i>
                            <a class="article_author" href="#">{{ username }}</a>
                            <p>发表时间：{{ create_time[page] }}</p>
                            <p>查看次数：{{ clicks[page] }}</p>
                            <p>点赞次数：{{ likes[page] }}</p>
                            <p>评论次数：{{ comments[page] }}</p>
                            <p>标签：{{ tags[page] }}</p>
                        </div>
                        <div class="article_content">
                            <div>
                                <mavon-editor class="md" :value="now_content" :subfield="prop.subfield"
                                    :defaultOpen="prop.defaultOpen" :toolbarsFlag="prop.toolbarsFlag"
                                    :editable="prop.editable" :scrollStyle="prop.scrollStyle" />
                            </div>
                        </div>

                        <div class="article_like_box">
                            <a href="#">喜欢的话点个赞吧！</a>
                        </div>


                        <div class="article_prev_next_box">
                            <a v-on:click="turn_to_pre">上一章：{{ pre_page() }}</a>
                            <a v-on:click="turn_to_nxt">下一章：{{ nxt_page() }}</a>
                        </div>
                    </div>

                    <div class="article_like_article">
                        <div class="article_article_title">
                            <h3>相关文章</h3>
                        </div>
                        <div class="article_like_list">
                            <a href="#">相似文章1</a>
                            <a href="#">相似文章2</a>
                            <a href="#">相似文章3</a>
                            <a href="#">相似文章4</a>
                            <a href="#">相似文章5</a>
                            <a href="#">相似文章6</a>
                        </div>
                    </div>
                    <div class="pinglun_box">
                        <div class="article_article_title">
                            <h3>文章评论</h3>
                        </div>
                    </div>
                </div>
                <div class="right">
                    <!--文章页关于我-->
                    <div class="right_box about_me_info">
                        <div class="about_me_info_touxiang">
                            <div @mouseenter="onMouseOver" @mouseleave="onMouseOut" @click="showlist">
                                <i class="about_me_line"></i>
                                <!--这个在mounted中确认-->
                                <img :src="headshot" id="headshot" />
                                <p id="change_headshot">更换头像</p>
                            </div>
                        </div>
                        <div>
                            <div class="about_me_text">
                                <h3>{{ username }}</h3>
                                <div @mouseenter="a_onMouseOver" @mouseleave="a_onMouseOut" @click="a_showlist">
                                    <p style="white-space: pre-line" id="abstract">
                                        {{ abstract }}
                                    </p>
                                </div>
                                <div id="submit">
                                    <!--将作者id，标题等信息传递到下一个页-->
                                    <button v-on:click="submit" class="create_button">开始创作</button>
                                </div>

                            </div>
                        </div>
                    </div>
                    <!--本栏推荐-->
                    <div class="right_box tuijian_moban">
                        <h3>本栏推荐</h3>
                        <div>
                            <ul>
                                <li><a href="#">科学</a></li>
                                <li><a href="#">计算机</a></li>
                                <li><a href="#">文学</a></li>
                                <li><a href="#">家庭</a></li>
                                <li><a href="#">食物</a></li>
                                <li><a href="#">旅行</a></li>

                            </ul>
                        </div>
                    </div>
                    <!--点击排行-->
                    <div class="right_box tuijian_moban">
                        <h3>排行榜</h3>
                        <div>
                            <ul>
                                <li><a href="#">top1</a></li>
                                <li><a href="#">top2</a></li>
                                <li><a href="#">top3</a></li>
                                <li><a href="#">top4</a></li>
                                <li><a href="#">top5</a></li>
                                <li><a href="#">top6</a></li>
                            </ul>
                        </div>
                    </div>
                    <!--友情链接-->
                    <div class="right_box youlian_list">
                        <h3>我的收藏</h3>
                        <div>
                            <ul>
                                <li><a href="#">收藏文章1</a></li>
                                <li><a href="#">收藏文章2</a></li>
                                <li><a href="#">收藏文章3</a></li>
                                <li><a href="#">收藏文章4</a></li>
                                <li><a href="#">收藏文章5</a></li>
                                <li><a href="#">收藏文章6</a></li>
                            </ul>
                        </div>
                    </div>


                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
export default {
    components: {
        mavonEditor,
    },
    data() {
        return {
            uid: -1,
            headshot: "",//这里存放头像的url
            tempshot: "",//这里存放临时头像的url
            username: "",//这里存放用户名
            abstract: "",//这里存放用户简介
            tempabstract: "",
            title: [],//这里储存文章标题
            content: [],//这里储存文章
            clicks: [],//这里储存点击数
            create_time: [],//这里储存创建时间
            comments: [],//这里存放评价数量
            likes: [],//这里储存点赞数量
            tags: [],//这里储存标签
            page: 0,//这里是页数
            now_content: "作者没有写过任何文章哦",//这里存放当前页面的信息
            total_page: 0,//这里存放总页数
        }
    },
    mounted() {
        this.uid = this.$route.params.uid;
        console.log(this.uid);
        let params = new URLSearchParams();
        params.append('uid', this.uid);
        this.$axios.post('http://127.0.0.1:5000/user/get_userinfo', params).then(res => {
            this.headshot = res.data['headshot'];
            this.tempshot = res.data['tempshot'];
            this.username = res.data['username'];
            this.abstract = res.data['abstract'];
            //这里做一个文本转化
            var ele = document.getElementById('abstract');
            ele.innerText = res.data['abstract'];
        });
        //刚开始要获取所有的该作者编写的网页属性,打包发过来
        this.$axios.post('http://127.0.0.1:5000/user/get_all_artical', params).then(res => {
            this.clicks = res.data['clicks'];
            this.comments = res.data['comments'];
            this.create_time = res.data['create_time'];
            this.likes = res.data['likes'];
            this.tags = res.data['tags'];
            this.title = res.data['title'];
            this.content = res.data['content'];
            this.now_content = this.content[this.page];
            this.total_page = this.comments.length;
        });
    }, computed: {
        prop() {
            let data = {
                subfield: false,// 单双栏模式
                defaultOpen: 'preview',//edit： 默认展示编辑区域 ， preview： 默认展示预览区域 
                editable: false,
                toolbarsFlag: false,
                scrollStyle: true
            }
            return data
        }
    },
    methods: {
        submit() {
            console.log(this.uid);
            setTimeout(function () {
                this.$router.push({ name: "write", params: { "uid": this.uid } });
            }.bind(this), 1000)
        },
        post_headshot(e) {
            console.log("上传头像");
            console.log(e.target.files[0]);
            var formdata = new FormData();
            var file = e.target.files[0];
            formdata.append('image', file);
            formdata.append('uid', this.uid);
            this.$axios({
                url: 'http://127.0.0.1:5000/user/post_headshot',
                method: 'post',
                data: formdata
            }).then(res => {
                this.tempshot = res.data['tempshot'];
                console.log(this.tempshot);
            })
        },
        onMouseOver() {
            var change_h = document.getElementById('change_headshot');
            var change_p = document.getElementById('headshot');
            change_p.style.filter = 'blur(2px)';
            change_h.style.opacity = '1';
        },
        // 鼠标移出
        onMouseOut() {
            var change_h = document.getElementById('change_headshot');
            var change_p = document.getElementById('headshot');
            change_p.style.filter = 'blur(0px)';
            change_h.style.opacity = '0';
        },
        showlist() {
            var hlist = document.getElementById('headshot_box');
            hlist.style.opacity = '1';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(4px)';
        },
        closelist_e() {
            var hlist = document.getElementById('headshot_box');
            hlist.style.opacity = '0';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(0px)';
            let params = new URLSearchParams();
            params.append('uid', this.uid);
            this.$axios.post('http://127.0.0.1:5000/user/ensure_headshot', params).then(res => {
                this.headshot = res.data['headshot'];
            })
        },
        closelist_c() {
            var hlist = document.getElementById('headshot_box');
            hlist.style.opacity = '0';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(0px)';
            let params = new URLSearchParams();
            params.append('uid', this.uid);
            this.$axios.post('http://127.0.0.1:5000/user/close_headshot', params).then(res => {
                this.tempshot = res.data['tempshot'];
            })
        }, p_input() {
            document.getElementById('choose_p').click()
        }, a_onMouseOver() {
            var hlist = document.getElementById('abstract');
            hlist.innerText = "修改简介请单击此处";
        },
        // 鼠标移出
        a_onMouseOut() {
            var hlist = document.getElementById('abstract');
            hlist.innerText = this.abstract;
        },
        a_showlist() {
            var hlist = document.getElementById('change_abstract');
            hlist.style.opacity = 1;
            hlist.style.zIndex = '2000';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(4px)';
        },
        a_closelist_e() {
            var hlist = document.getElementById('change_abstract');
            hlist.style.opacity = '0';
            hlist.style.zIndex = '0';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(0px)';
            var cai = document.getElementById('change_abstract_input');
            let params = new URLSearchParams();
            params.append('uid', this.uid);
            params.append('abstract', this.tempabstract);
            this.$axios.post('http://127.0.0.1:5000/user/change_abstract', params).then(res => {
                var ele = document.getElementById('abstract');
                ele.innerText = res.data;
                this.abstract = res.data;
            })
            var ele = document.getElementById('change_abstract_input');
            ele.value = "";
        },
        a_closelist_c() {
            var ele = document.getElementById('change_abstract_input');
            ele.value = "";
            var hlist = document.getElementById('change_abstract');
            hlist.style.opacity = '0';
            hlist.style.zIndex = '0';
            var ulist = document.getElementById('userbox');
            ulist.style.filter = 'blur(0px)';
        }, pre_page() {
            if (this.page == 0) {
                return '没有上一篇文章了哦';
            }
            return this.title[this.page - 1];
        }, nxt_page() {
            if (this.page == this.total_page - 1) {
                return '没有下一篇文章了哦';
            }
            return this.title[this.page + 1];
        }, turn_to_pre() {
            if (this.page == 0) return;
            this.page--;
            this.now_content = this.content[this.page];
        },
        turn_to_nxt() {
            if (this.page == this.total_page - 1) return;
            this.page++;
            this.now_content = this.content[this.page];
        }
    }
}
</script>

<style>
#change_abstract_input {
    outline: none;
    border: none;
    border: 2px solid rgb(154, 151, 151);
    font-size: 18px;
    height: 25px;
    width: 250px;
    margin-left: 20px;
    transition: all 0.5s;
    margin-top: 25px;
    border-radius: 5px;
    height: 170px;
}

#b1 {
    margin-left: -250px;
    margin-top: 210px;
}

#b2 {
    margin-left: -115px;
    margin-top: 210px;
}

#change_abstract {
    left: 550px;
    top: 150px;
    height: 300px;
    width: 300px;
    border-radius: 10px;
    background-color: rgb(255, 255, 255);
    position: fixed;
    transition: all 0.5s;
    opacity: 0;
    border: 4px solid;
    border-color: rgb(110, 109, 109);
}

#choose_p {
    opacity: 0;
}

.headtitle {
    position: absolute;
    margin-top: 12px;
    margin-left: 113px;
    color: black;
    z-index: 2000;
    font-weight: bolder;
}

.input_button {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 60px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
    margin-left: 85px;
}

.input_button:hover {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 70px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(83, 39, 205);
    color: rgb(83, 39, 205);
}

.showhead {
    height: 140px;
    width: 140px;
    border-radius: 140px;
    margin-top: 100px;
    margin-left: -128px;
    border: 5px solid;
    border-color: #004FCB;
    position: fixed;
}

#userbox {
    filter: blur(0px);
    transition: all 0.5s;
}

.closebutton {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 60px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
    margin-top: 270px;
    margin-left: -45px;
    position: absolute;
}

.closebutton:hover {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 70px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(83, 39, 205);
    color: rgb(83, 39, 205);
}

.ensurebutton {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 60px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
    margin-top: 270px;
    margin-left: -188px;
    position: absolute;
}

.ensurebutton:hover {
    outline: none;
    height: 60px;
    width: 120px;
    border-radius: 70px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(83, 39, 205);
    color: rgb(83, 39, 205);
}


#headshot_box {
    left: 550px;
    top: 150px;
    height: 370px;
    width: 300px;
    border-radius: 10px;
    background-color: rgb(255, 255, 255);
    z-index: 1000;
    position: fixed;
    transition: all 0.5s;
    opacity: 0;
    border: 4px solid;
    border-color: rgb(110, 109, 109);
}

#change_headshot {
    opacity: 0;
    transition: all 0.5s;
    position: absolute;
    color: black;
    top: 70px;
    left: 117px;
    font-weight: bold;
}

#headshot {
    transition: all 0.5s;
}

#submit {
    width: 260px;
    height: 200px;
    padding: 30px;
    margin: 0px;
    line-height: 3;
    right: 0px;
    /* margin-top: 300px; */
    background-color: rgb(114, 196, 228);
    text-align: center;
    /* border-related properties */
    border: 10px solid rgb(223, 206, 206);
    background-clip: padding-box;
}

.create_button {
    outline: none;
    height: 70px;
    width: 140px;
    border-radius: 70px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
}

.create_button:hover {
    outline: none;
    height: 70px;
    width: 140px;
    border-radius: 70px;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.5s;
    border: 2px solid rgb(83, 39, 205);
    color: rgb(83, 39, 205);
}

#pp {
    align-items: center;
    display: flex;
    justify-content: center;

    /* Border */
    border: 0.25rem dashed #79828f;
    border-radius: 0.25rem;
}



.imgheadborder {
    position: relative;
    left: 5%;
    top: 20px;
    width: 10%;
    padding-top: 10%;
    margin-right: 3%;
    border-radius: 50%;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    z-Index: 0;
}

.imghead {
    position: absolute;
    left: 0px;
    top: 0px;
    border-radius: 50%;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    width: 100%;
    height: 100%;
    z-Index: 1;
}

.username {
    position: absolute;
    left: 20%;
    top: 40px;
    width: 10%;
    height: 40px;
    font-size: 30px;
}

.emailaddress {
    position: absolute;
    left: 20%;
    top: 80px;
    height: 10px;
    font-size: 18px;
}

html,
body,
ul,
li,
figure {
    margin: 0;
    padding: 0;
    border: none;
}

body {
    background: #f2f2f2;
    font: 16px "PingFang SC", "Microsoft Yahei", "Helvetica Neue", Helvetica, STHeiTi, sans-serif;
    color: #FFF;
}

body * {
    box-sizing: border-box;
}

li {
    list-style-type: none;
}

img {
    border: none;
}

ul {
    list-style: none;
}

input {
    outline: none;
}

a {
    cursor: pointer;
    text-decoration: none;
    color: #333;
}

.clearfix:after {
    content: "";
    display: block;
    height: 0;
    visibility: hidden;
    clear: both;
}

.clearfix {
    display: block;
}

h1,
h2,
h3,
h4,
p {
    margin: 0;
    padding: 0;
    text-align: justify;
}

a:hover {
    color: #004FCB;
}

/*瀛椾綋鑷姩鎷変几鍒板搴�*/
p {
    text-align: justify;
}

*:after,
*:before,
.nav_second,
.article li,
.clearfix,
footer,
.clearfix:after,
.self_info,
.self_info *,
.nav_second li a,
.article_list_link a,
.article_like_box a:hover,
.article_like_box a,
.article_like_article a,
.more {
    -webkit-transition: ease-in-out .5s;
    transition: ease-in-out .5s;
}

.have_second:hover:before {
    border-color: #004FCB;
}



/*澶撮儴瀵艰埅鍖哄煙*/

.head_box {
    width: 100%;
    height: 75px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
    border-left: none;
    border-right: none;
    position: relative;
    z-index: 999;
}

.head_box:before {
    background: #3A76BF;
    content: "";
    height: 5px;
    position: absolute;
    top: 0;
    width: 100%;
}

.header {
    width: 1100px;
    margin: 0 auto;
    height: 100%;
    line-height: 73px;
}


.header_logo {
    width: 25%;
    float: left;
    height: 100%;
    text-align: center;
}

.header_logo a {
    width: 100%;
    height: 100%;
    display: block;
}

.header_logo h2 {
    line-height: 50px;
    font-weight: normal;
    color: #3a76bf;
}

.header_logo h4 {
    line-height: 20px;
    font-weight: normal;
    color: #3a76bf;
}

.header_logo h2,
.header_logo h4 {
    display: inline-block;
}


.header_nav {
    width: 70%;
    float: left;
    height: 100%;
    line-height: 73px;
}

.header_nav>ul {
    padding-left: 20px;
}

.header_nav>ul>li {
    display: inline;
    float: left;
    height: 75px;
    position: relative;
    width: max-content;
}

.have_second:before {
    position: absolute;
    content: "";
    top: 34px;
    right: 10px;
    width: 4px;
    height: 4px;
    border: 1px solid #999;
    border-right-width: 0;
    border-top-width: 0;
    transform: rotate(-45deg);
    -webkit-transform: rotate(-45deg);
    -moz-transform: rotate(-45deg);
    -o-transform: rotate(-45deg);
    -ms-transform: rotate(-45deg);
}

.have_second:hover:before {
    transform: rotate(135deg);
    -webkit-transform: rotate(135deg);
    -moz-transform: rotate(135deg);
    -o-transform: rotate(135deg);
    -ms-transform: rotate(135deg);
    top: 37px;
}

.header_nav>ul>li>a {
    height: 100%;
    display: block;
    padding: 0 20px;
}

.header_click {
    color: #004FCB;
}


/*.header_nav>ul>li:first-child a{padding:0 5px 0 40px;}*/
/*.header_nav>ul>li:last-child a{padding:0 0 0 5px;}*/

/*杩欓噷鏄紶鏍囨偓鍋滃埌鐖跺鑸� 瀛愬鑸殑閫忔槑搴︽樉绀哄嚭鏉ワ紝鍔ㄧ敾寤惰繜鏄�0.5绉�*/
.have_second:hover>.nav_second {
    opacity: 1;
    top: 73px;
    visibility: unset;
}

.nav_second {
    position: absolute;
    left: 0;
    top: 95px;
    background: #FFF;
    z-index: 9;
    visibility: hidden;
    white-space: nowrap;
    -webkit-box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.1);
    box-shadow: 4px 4px 4px 0 rgba(0, 0, 0, 0.1);
    opacity: 0;
}

.nav_second>i {
    position: absolute;
    top: -18px;
    left: 50%;
    margin-left: -10px;
    z-index: 10;
    border-width: 10px;
    border-style: solid;
    border-top-color: transparent;
    border-bottom-color: #FFF;
    border-right-color: transparent;
    border-left-color: transparent;
}

.nav_second li {
    font-size: 14px;
    overflow: hidden;
}

.nav_second li a {
    display: block;
    padding: 8px 20px;
    line-height: 30px;
    border-top: 1px #efefef solid;
}

.header_search {
    width: 5%;
    float: left;
    height: 100%;
    position: relative;
}

.header_search a {
    position: absolute;
    width: 100%;
    height: 100%;
}

.header_search_btn i {
    width: 30px;
    height: 30px;
    display: block;
    margin: 25px 0 0 10px;
    background: url("./img/search.png");
    background-size: 100% 100%;
}

.header_nav_small_btn {
    display: none;
}

/*搜索框*/
.search_box {
    width: 1100px;
    margin: 30px auto 20px auto;
    display: none;
}

.search {
    width: 500px;
    margin: 0 auto;
    height: 41px;
}

.search_form {
    position: relative;
}

.search_text {
    width: 400px;
    height: 38px;
    position: absolute;
    left: 0;
    border-radius: 4px;
    text-indent: 1em;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}

.search_btn {
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
    width: 90px;
    height: 38px;
    position: absolute;
    right: 0;
    background: #FFF;
    border-radius: 4px;
    color: #333;
}

.search_btn:hover {
    cursor: pointer;
}

.nav_hidden_zhanwei {
    display: none;
}

/*身体全部部分*/
.article_box {
    width: 1100px;
    margin: 30px auto;
}

/*左边文章部分*/
.left {
    width: 780px;
    float: left;
}


/*首页文章部分*/
.article_box_one {
    width: 100%;
    margin-bottom: 24px;
}

.index_article_title {
    padding: 16px 20px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}

.index_article_title h3 {
    font-weight: normal;
    display: block;
    width: 90%;
    float: left;
    color: #333;
}

.index_article_title a {
    display: block;
    width: 10%;
    float: right;
    font-size: 13px;
    text-align: right;
    color: #999;
    padding-top: 6px;
}

.index_article_title a:hover {
    color: #3a76bf;
}


.index_article {
    width: 100%;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
    border-top: none;
}

.index_article .article_list {
    width: 100%;
    display: block;
    border-bottom: 1px #efefef solid;
    padding: 20px 20px 20px 260px;
}

.index_article .article_list:last-child {
    border-bottom: none;
}

.index_article .article_list:nth-child(1) {
    border-top: 1px #efefef solid;
}

.index_article .article_list .article_list_img {
    display: inline-block;
    font-size: 0;
    /* float: left; */
    margin-left: -240px;
}

.index_article .article_list .article_list_img img {
    width: 226px;
    vertical-align: middle;
}

.index_article .article_list h3 {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #3a76bf;
    display: block;
    font-size: 16px;
    padding: 0 20px 10px 20px;
    font-weight: bold;
    line-height: 30px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
}

.index_article .article_list p {
    margin: 0 20px 10px 20px;
    font-size: 13px;
    color: #666;
    display: inline-block;
    height: 70px;
    text-overflow: ellipsis;
    overflow: hidden;
}

.index_article .article_list .article_list_link {
    padding: 0 20px;
    font-size: 13px;
}

/*鏂囩珷鐐瑰嚮鐜�*/
.article_list_count {
    color: #666;
    display: inline-block;
    text-indent: .5em;
    line-height: 18px;
}

.see_count {
    display: block;
    height: 20px;
    width: 20px;
    float: left;
    border-radius: 50%;
    background: #ecf0f1;
    box-shadow: inset 0px 2px 0px #bdc3c7;
    position: relative;
}

.see_count:before {
    content: "";
    width: 12px;
    height: 12px;
    background: #34495e;
    border-radius: 50%;
    position: absolute;
    left: 4px;
    top: 4px;
    box-shadow: inset 2px -2px 0px #2980b9, inset 0px 0px 0px 3.5px #3498db;
}

.see_count:after {
    content: "";
    width: 3px;
    height: 3px;
    background: #ffffff;
    border-radius: 50%;
    position: absolute;
    left: 10px;
    top: 7px;
}

/*鏂囩珷鐐硅禐鏁�*/
.article_list_like {
    color: #666;
    display: inline-block;
    text-indent: .5em;
    line-height: 18px;
    margin-left: 15px;
}

.like_count {
    display: block;
    height: 20px;
    width: 20px;
    float: left;
    position: relative;
}

.like_count:before {
    content: "";
    position: absolute;
    width: 11px;
    height: 18px;
    border-radius: 50% 50% 0 0;
    background: #e4b9b9;
    left: 10px;
    transform: rotate(-45deg);
    transform-origin: 0 100%;
    -webkit-transform: rotate(-45deg);
    -webkit-transform-origin: 0 100%;
    top: 0px;
}

.like_count:after {
    content: "";
    position: absolute;
    width: 11px;
    height: 18px;
    border-radius: 50% 50% 0 0;
    background: #e4b9b9;
    left: 2px;
    transform: rotate(45deg);
    transform-origin: 0 100%;
    -webkit-transform: rotate(45deg);
    -webkit-transform-origin: 0 100%;
    top: -8px;
}

.article_list_link a {
    color: #666;
    /* float: right; */
    display: inline-block;
}

.article_list_link a:hover {
    color: #3a76bf;
}

/*鏂囩珷绗簩绉嶆牱寮�*/
.article_box_two {
    width: 100%;
    margin-bottom: 20px;
}

.article_btn {
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
    border-top: none;
    margin-top: 1px;
    overflow: hidden;
}

.article_btn_nav>ul {
    border-bottom: 1px #ddd solid;
}

.article_btn_nav>ul li {
    display: inline-block;
    padding: 16px 20px;
    font-size: 17px;
    color: #333;
}

.article_btn_nav>ul li:hover {
    cursor: pointer;
    border-bottom: 1px solid #004FCB;
}


.article_btn_nav>ul li:first-child {
    border-bottom: 1px solid #004FCB;
    color: #004FCB;
}

.article_btn_box {
    width: 100%;
    display: block;
    padding: 10px 20px 20px 260px;
}


.article_btn_box_item_img {
    display: inline-block;
    font-size: 0;
    /* float: left; */
    margin-left: -240px;
}

.article_btn_box_item_img img {
    width: 226px;
}

/*瀛︿範绗旇涓嬮潰鐨勬爮鐩畊l涓€寮€濮嬫槸褰辫棌鐨� 閫氳繃js鐨勭偣鍑绘樉绀哄拰褰辫棌*/
.article_btn_box_item {
    display: none;
}

.article_btn_box_item:first-child {
    display: block;
}


/*鍒濆鏍峰紡杩欓噷闈㈢殑鏍峰紡 鏄粨鍚坖s瀹炵幇鐨勬晥鏋滐紝涓嬮潰鐨刲i鐨勬晥鏋滃叏閮ㄦ槸鐢眂ss瀹炵幇锛屼絾鏄乏渚х殑鍥剧墖鏄敱js鎺у埗瀹炵幇鐨�*/
.article_btn_box_item ul li {
    padding: 0 20px 0 20px;
    line-height: 32px;
    height: 32px;
    overflow: hidden;
}

/*杩欓噷ul涓嬬涓€涓猯i鍏冪礌寮€濮嬫椂鐨勬牱寮忚缃�*/
.article_btn_box_item ul li:first-child {
    height: 100%;
    background: #769cbf;
}

.article_btn_box_item ul li:first-child a {
    color: #333;
}

.article_btn_box_item ul li:first-child i {
    background: #FFF;
}

/*杩欓噷鏄紶鏍囩Щ鍏ュ埌ul涓嬬涓€涓猯i鍏冪礌鏃秎i鍏冪礌鐨勬牱寮�*/
.article_btn_box_item ul:hover li:first-child:hover {
    height: 100%;
    background: #769cbf;
}

.article_btn_box_item ul:hover li:first-child:hover a {
    color: #333;
}

.article_btn_box_item ul:hover li:first-child:hover i {
    background: #FFF;
}

/*杩欓噷li涓嬮潰绗竴涓厓绱犵粨鏉熸椂鎭㈠榛樿鐨勮缃�*/
.article_btn_box_item ul:hover li:first-child {
    height: 32px;
    background: none;
}

.article_btn_box_item ul:hover li:first-child a {
    color: #6f6f6f;
}

.article_btn_box_item ul:hover li:first-child i {
    background: #9a9a9a;
}


/*杩欓噷鏄痷l涓嬫瘡涓猯i鍏冪礌榧犳爣鍒掑叆鏃剁殑鐗规晥*/
.article_btn_box_item ul li:hover {
    height: 100%;
    background: #769cbf;
}

.article_btn_box_item ul li:hover a {
    color: #333;
}

.article_btn_box_item ul li:hover i {
    background: #FFF;
}





.article_btn_box_item ul li i {
    display: block;
    width: 20px;
    height: 20px;
    background: #9a9a9a;
    float: left;
    margin-top: 6px;
    margin-right: 20px;
    position: relative;
    font-style: normal;
}

.article_btn_box_item ul li i:before {
    position: absolute;
    left: 0;
    top: 0;
    font-size: 12px;
    color: #222;
    line-height: 20px;
    width: 20px;
    text-align: center;
}

.article_btn_box_item ul li:first-child i:before {
    content: "1";
}

.article_btn_box_item ul li:nth-child(2) i:before {
    content: "2";
}

.article_btn_box_item ul li:nth-child(3) i:before {
    content: "3";
}


.article_btn_box_item ul li a {
    display: block;
    color: #6f6f6f;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.article_btn_box_item ul li p {
    line-height: 24px;
    font-size: 14px;
    overflow: hidden;
    text-overflow: ellipsis;
    -webkit-box-orient: vertical;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    height: 48px;
}




.pagelist {
    text-align: center;
    color: #666;
    width: 100%;
    clear: both;
    margin: 20px 0 0;
    float: left;
}

.pagelist a {
    color: #666;
    margin: 0 5px 10px;
    padding: 5px 10px;
    background: #F7F7F7;
    display: inline-block;
}

.pagelist_active {
    background: #414d55 !important;
    color: #fff !important;
}




.more {
    padding: 10px 20px;
    display: block;
    margin: 0 auto;
    height: 50px;
    font-size: 20px;
    color: #3a76bf;
    border-radius: 10px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}

.more:hover {
    color: #FFF;
    background: #3a76bf;
}

/*鍒楄〃椤�*/
.list_article_title {
    margin-bottom: 10px;
    padding: 16px 20px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}

.list_article_title h3 {
    font-weight: normal;
    display: block;
    width: 100%;
    float: left;
    color: #3a76bf;
    border-bottom: 1px solid #ddd;
    padding-bottom: 5px;
    float: left;
}

.list_article_title p {
    display: block;
    margin: 5px 0 20px;
    background-color: #eee;
    font-size: 14px;
    color: #666;
    padding: 2px;
    font-weight: bold;
    float: left;
}


/*鏂囩珷椤�*/
.article_content_box {
    color: #666;
    font-size: 14px;
    padding: 20px;
    width: 100%;
    margin-bottom: 24px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
    border-top: none;
}

.article_article_title h3 {
    font-weight: normal;
    line-height: 30px;
    border-bottom: 1px solid #ddd;
    font-size: 18px;
    position: relative;
    color: #333;
}

.article_article_title h3:after {
    content: "";
    position: absolute;
    width: 60px;
    height: 2px;
    background: #004FCB;
    left: 0;
    bottom: -2px;
    -moz-transition: all .5s ease;
    -webkit-transition: all .5s ease;
    transition: all .5s ease;
}

.article_article_title h3:hover:after {
    width: 90px;
}

.article_article_title h3 span {
    display: block;
    float: right;
    font-size: 12px;
    color: #999;
}

.article_article_title h3 span a {
    color: #999;
}

.article_article_title h3 span a:hover {
    color: #004FCB;
}

.article_content_title {
    color: #3a76bf;
    font-weight: normal;
    font-size: 22px;
    margin-top: 20px;
}

.article_author_count_box {
    line-height: 34px;
    margin-top: 20px;
}

.article_author_img {
    display: block;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    float: left;
    overflow: hidden;
}

.article_author_img img {
    width: 100%;
    height: 100%;
}

.article_author {
    display: block;
    margin-left: 10px;
    float: left;
    color: #666;
}


.article_author_count_box p {
    display: block;
    float: left;
    margin-left: 10px;
    font-size: 13px;
}




.article_info {
    margin: 10px 0 20px 0;
    line-height: 30px;
    background-color: #eee;
    color: #666;
    padding: 10px 10px;
}

.article_content {
    overflow: hidden;
    width: 100%;
    line-height: 30px;
    padding-top: 20px;
}

.article_content img {
    display: block;
    max-width: 100% !important;
    height: auto !important;
    margin: auto;
}

.article_link_box {
    margin: 40px 0 40px;
}

.article_link {
    display: block;
    background-color: #eee;
    font-size: 14px;
    color: #666;
    padding: 2px 0 2px 16px;
    font-weight: bold;
    margin-bottom: 20px;
    line-height: 30px;
}

.article_link_one {
    padding: 0 16px 20px 16px;
    line-height: 30px;
}

.article_link_one h3 {
    font-size: 14px;
    color: #666;
    font-weight: bold;
}

.article_link_one a {
    color: #666;
}

.article_link_one a:hover {
    color: #004FCB;
}

.article_end {
    border-top: 1px solid #eee;
    margin: 40px 0;
    width: 100%;
    float: left;
    padding: 5px 16px;
}

.article_end a {
    color: #004FCB;
}

.article_like_box {
    text-align: center;
    float: left;
    width: 100%;
    margin: 40px 0;
}

.article_like_box a {
    display: inline-block;
    height: 50px;
    width: auto;
    background: #3a76bf;
    line-height: 50px;
    padding: 0 10px;
    border-radius: 8px;
    color: #FFF;
}

.article_like_box a:hover {
    background: #e4b9b9
}

.article_prev_next_box {
    margin-top: 20px;
    border-top: 1px dashed #eee;
    padding: 20px 0 0 0;
    float: left;
    width: 100%;
}

.article_prev_next_box a {
    display: block;
    width: 50%;
    height: 100%;
    float: left;
    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.article_prev_next_box a:nth-child(1) {
    border-right: 1px solid #666;
}


/*鏂囩珷椤电浉浼兼枃绔�*/
.article_like_article {
    color: #666;
    font-size: 14px;
    padding: 20px;
    width: 100%;
    margin-bottom: 24px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;

}

.article_like_article a {
    display: block;
    line-height: 26px;
    font-size: 16px;
    position: relative;
    padding-left: 25px;
    height: 26px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.article_like_list {
    margin-top: 10px;
}

.article_like_article a:hover {
    text-decoration: underline;
}

.article_like_article a:before {
    position: absolute;
    top: 35%;
    left: 5px;
    content: "";
    width: 8px;
    height: 8px;
    display: block;
    border-radius: 50%;
    background: rgb(58, 118, 191);
}


/*鏂囩珷椤佃瘎璁�*/

.pinglun_box {
    padding: 20px;
    width: 100%;
    margin-bottom: 24px;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}






/*鍙宠竟鑷垜浠嬬粛鍙婃枃绔犳帹鑽愰儴鍒�*/
.right {
    width: 300px;
    float: right;
}

.right_box {
    overflow: hidden;
    margin-bottom: 24px;
    background: #f8f8fa;
    border: 1px #fff solid;
    box-shadow: 0 0 3px #ddd;
    -webkit-box-shadow: 0 1px 3px #ddd;
}



/*鍙充晶鑷垜浠嬬粛*/
.self_info img,
.self_info_scroll_bottom img {
    width: 100%;
    padding: 12px;
    margin: 0;
    display: block
}

.self_info_text {
    padding: 10px 20px 20px 20px;
    font-size: 12px;
    color: #666;
}

.self_info_text h3 {
    font-size: 22px;
    font-weight: normal;
    color: #3a76bf;
    margin-bottom: 8px;
}

.self_info_text p {
    margin-bottom: 15px;
    line-height: 22px;
}

.self_info_text p:nth-child(1) {
    margin-top: 20px;
}

.self_info_text a {
    color: #3a76bf;
}

/*鍙充晶鑷垜浠嬬粛闅愯棌鐨勯儴鍒�*/
.self_info_scroll_bottom {
    position: fixed;
    right: 0;
    top: 0;
    z-index: -9;
    width: 300px;
    opacity: 0;
}

/*鍙充晶鏂囩珷椤佃嚜鎴戜粙缁嶅奖钘忕殑閮ㄥ垎*/
.about_me_info_scroll_bottom {
    position: fixed;
    right: 0;
    top: 0;
    z-index: -9;
    width: 300px;
    opacity: 0;
}


/*鍙充晶浜岀淮鐮侀儴鍒�*/
.self_erweima h3,
.tuijian_moban h3,
.youlian_list h3 {
    padding: 15px 20px;
    border-bottom: 1px #efefef solid;
    font-size: 18px;
    color: #333;
    font-weight: normal;
}

.self_zuoyoum h3 {
    padding: 22px 20px;
    font-size: 18px;
    color: #333;
    font-weight: normal;
}

.self_erweima img {
    padding: 12px;
    display: block;
    max-width: 50%;
    margin: 0 auto;
}

.tuijian_moban div {
    padding: 10px 20px 12px 20px;
    font-size: 13px;
    color: #666;
}

.tuijian_moban div ul {
    overflow: hidden;
}

.tuijian_moban div ul li {
    margin-top: 17.4px;
    ;
    position: relative;
    padding-left: 30px;
    line-height: 20px;
    font-size: 15px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.tuijian_moban div ul li:before {
    position: absolute;
    text-indent: .4em;
    top: 0;
    left: 0;
    background: #414d55;
    width: 20px;
    height: 20px;
    display: block;
    font-size: 14px;
    color: #fff;
}

.tuijian_moban div ul li:nth-child(1):before,
.tuijian_moban div ul li:nth-child(2):before,
.tuijian_moban div ul li:nth-child(3):before {
    background: #3a76bf;
    color: #FFF;
}

.tuijian_moban div ul li:nth-child(1):before {
    content: "1";
}

.tuijian_moban div ul li:nth-child(2):before {
    content: "2";
}

.tuijian_moban div ul li:nth-child(3):before {
    content: "3";
}

.tuijian_moban div ul li:nth-child(4):before {
    content: "4";
}

.tuijian_moban div ul li:nth-child(5):before {
    content: "5";
}

.tuijian_moban div ul li:nth-child(6):before {
    content: "6";
}

.tuijian_moban div ul li a {
    color: #666;
}

.tuijian_moban div ul li a:hover {
    color: #3a76bf;
}



.youlian_list div {
    padding: 10px 20px 12px 20px;
    font-size: 13px;
    color: #666;
}

.youlian_list div ul {
    overflow: hidden;
}

.youlian_list div ul li {
    margin-top: 17.4px;
    ;
    position: relative;
    padding-left: 30px;
    line-height: 20px;
    font-size: 15px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.youlian_list div ul li:before {
    position: absolute;
    top: 35%;
    left: 5px;
    content: "";
    width: 8px;
    height: 8px;
    display: block;
    border-radius: 50%;
    background: rgb(58, 118, 191);
}




.about_me_info_touxiang {
    height: 80px;
    background: #414d55;
    position: relative;
}

.about_me_line {
    display: block;
    position: absolute;
    width: 80px;
    height: 80px;
    left: 50%;
    margin-left: -40px;
    top: 80px;
    margin-top: -40px;
    border-radius: 50%;
    overflow: hidden;
    border-width: 3px;
    border-style: solid;
    border-top-color: #f25022;
    border-right-color: #f25022;
    border-bottom-color: #ffb901;
    border-left-color: #ffb901;
    transform: rotate(-45deg);
}

.about_me_info_touxiang img {
    display: block;
    position: absolute;
    width: 74px;
    height: 74px;
    left: 50%;
    margin-left: -37px;
    top: 80px;
    margin-top: -37px;
    border-radius: 50%;
    overflow: hidden;
}

.about_me_text {
    background: #3c85b9;
    padding: 55px 20px 20px 20px;
    font-size: 13px;
    text-align: center
}

.about_me_text h3 {
    text-align: center;
    font-size: 22px;
    font-weight: normal;
    margin-bottom: 20px;
}


.about_me_text p {
    text-align: center;
    line-height: 30px;
}

.about_me_text img {
    margin-top: 20px;
}


/*鍏充簬鎴戠晫闈�*/
.me_box {
    width: 1100px;
    margin: 30px auto;
    background: #f8f8fa;
    box-shadow: 0 1px 3px #ddd;
    border: 1px #fff solid;
    -webkit-box-shadow: 0 1px 3px #ddd;
}

/*.me_box1{padding: 20px;}*/

.me_box_title {
    height: 100px;
    background: #414d55;
    line-height: 100px;
    padding: 0 20px;
}

.me_box_title>img {
    /* float: left; */
    display: inline-block;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    overflow: hidden;
    margin-top: 10px;
    border: 3px solid rgba(255, 255, 255, .9)
}

.me_box_title>h3 {
    display: inline-block;
    margin-left: 15px;
    /* float: left; */
    font-size: 22px;
}


.me_box_text {
    background: #d7d7d7;
}

.me_box_title_title {
    padding: 10px 30px;
    background: #3c85b9;
    font-size: 18px;
}

.me_box_text_div {
    padding: 10px 30px;
    color: #555;
    font-size: 14px;
    line-height: 25px;
}

.me_box_text_div img {
    max-width: 100%;
}

.footer_box {
    width: 100%;
    background: #414d55;
    z-index: 101;
    position: relative;
    border-top: #3a76bf 10px solid;
    margin-top: 0;
    padding: 30px 0;
    color: #ddd;
    font-size: 14px;
    font-family: "PingFang SC", "Microsoft Yahei", "Helvetica Neue", Helvetica, STHeiTi, sans-serif;
}

.footer {
    width: 1100px;
    margin: 0 auto;
    height: 100%;
}

.footer_img {
    overflow: hidden;
    float: left;
    margin-right: 20px;
}

.footer_img ul li {
    float: left;
    margin: 0 10px;
    text-align: center;
}

.footer_img ul li img {
    width: 100px;
    height: 100px;
    display: block;
}

.footer_text p i {
    font-weight: bold;
    color: #3a76bf;
    font-style: normal
}

.footer_text p {
    margin-bottom: 5px;
}







/*鎵嬫満绔�*/
@media (max-width: 1099px) {

    /*鎵嬫満椤甸潰瀵艰埅*/
    .head_box {
        width: 100%;
        background: #1C2327;
        height: 50px;
        border: none;
        position: fixed;
        top: 0;
    }

    .head_box:before {
        display: none;
    }

    .header {
        width: 95%;
        margin: 0 auto;
        height: 100%;
        line-height: 56px;
    }

    .header_logo {
        width: 75%;
        float: left;
        height: 100%;
        text-align: left;
    }

    .header_logo h2 {
        color: #FFF;
    }

    .header_logo h4 {
        color: #FFF;
    }

    .header_nav {
        position: fixed;
        top: 50px;
        width: 100%;
        height: auto;
        right: 0;
        background: rgba(0, 0, 0, 0.3);
        display: none;
        z-index: 11;
    }

    .header_nav>ul>li {
        display: block;
        height: auto;
        line-height: 2.5;
        width: 50%;
        background: #f8f8fa;
        margin-left: 48%;
    }

    .have_second:before {
        display: none;
    }

    .have_second:hover:before {
        display: none;
    }

    .header_nav>ul>li>a {
        height: 100%;
        display: block;
        width: 100%;
        text-align: center;
        padding: 0;
        font-size: 15px;
    }

    .nav_second {
        position: unset !important;
        overflow: hidden;
        left: 0;
        top: 0;
        background: #f2f2f2;
        z-index: 9;
        width: 100%;
        display: block;
        visibility: unset;
        opacity: 1;
    }

    .nav_second i {
        display: none;
    }

    .nav_second li {
        height: 30px;
        line-height: 30px;
        font-size: 14px;
        width: 100%;
    }

    .nav_second li a {
        height: 100%;
        width: 100%;
        display: block;
        padding: 0;
        text-align: center;
    }

    /*鎵嬫満椤甸潰鎼滅储鎸夐挳*/
    .header_search {
        width: 50px;
        float: left;
        height: 100%;
        position: relative;
    }

    .header_search a {
        position: absolute;
        width: 100%;
        height: 100%;
    }

    .header_search i {
        width: 34px;
        height: 35px;
        display: block;
        margin: 12px 0 0 8px;
        background: url("./img/search_small.png");
        background-size: 100% 100%;
    }

    /*鎵嬫満椤甸潰鐨勫鑸寜閽� 涓夋í鍙樹竴脳*/
    .header_nav_small_btn {
        display: block;
        width: 35px;
        float: right;
        height: 38px;
        margin-top: 12px;
    }

    .header_nav_small_btn .small_btn {
        width: 100%;
        height: 4px;
        background: #fff;
        display: block;
        margin-top: 15px;
        position: relative;
    }

    .header_nav_small_btn .small_btn:before,
    .header_nav_small_btn .small_btn:after {
        content: '';
        display: block;
        width: 100%;
        height: 4px;
        position: absolute;
        background: #fff;
        -webkit-transition-property: margin, -webkit-transform;
        transition-property: margin, -webkit-transform;
        transition-property: margin, transform;
        transition-property: margin, transform, -webkit-transform;
        -webkit-transition-duration: 300ms;
        transition-duration: 300ms;
    }

    .small_btn:before {
        margin-top: -12px;
    }

    .small_btn:after {
        margin-top: 12px;
    }

    .click_small_btn .small_btn {
        background: none;
    }

    .click_small_btn .small_btn:before,
    .click_small_btn .small_btn:after {
        content: '';
        display: block;
        width: 100%;
        height: 4px;
        position: absolute;
        background: #fff;
    }

    .click_small_btn .small_btn:before {
        margin-top: 0;
        -webkit-transform: rotate(-45deg);
        transform: rotate(-45deg);
    }

    .click_small_btn .small_btn:after {
        margin-top: 0;
        -webkit-transform: rotate(45deg);
        transform: rotate(45deg);
    }

    /*鎼滅储妗�*/
    .search_box {
        width: 96%;
        margin: 20px auto 20px auto;
        display: none;
    }

    .search {
        width: 100%;
        margin: 0 auto;
        height: 41px;
    }

    .search_form {
        position: relative;
    }

    .search_text {
        width: 77%;
        height: 38px;
        position: absolute;
        left: 0;
        border-radius: 4px;
        text-indent: 1em;
        box-shadow: 0 1px 3px #ddd;
        border: 1px #fff solid;
        -webkit-box-shadow: 0 1px 3px #ddd;
    }

    .search_btn {
        width: 20%;
        height: 38px;
        position: absolute;
        right: 0;
        background: #FFF;
        border-radius: 4px;
        color: #333;
        box-shadow: 0 1px 3px #ddd;
        border: 1px #fff solid;
        -webkit-box-shadow: 0 1px 3px #ddd;
    }

    .search_btn:hover {
        cursor: pointer;
    }

    .nav_hidden_zhanwei {
        display: block;
        height: 50px;
    }

    /*banner閮ㄥ垎*/
    .banner_box {
        width: 96%;
        height: 222px;
        background: #f8f8fa;
        box-shadow: 0 1px 3px #ddd;
        border: 1px #fff solid;
        -webkit-box-shadow: 0 1px 3px #ddd;
        margin: 10px auto 10px auto;
    }

    /*韬綋閮ㄥ垎*/
    .article_box {
        width: 96%;
        margin: 10px auto;
    }

    .article .article_list h3 {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .index_article_title h3 {
        width: 80%;
    }

    .index_article_title a {
        width: 15%;
    }

    .article_btn_box_item ul li a {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .me_box {
        width: 96%;
        margin: 20px auto;
    }

    .me_box_title {
        padding: 0 10px;
    }

    .me_box_title_title {
        padding: 10px 20px;
    }

    .me_box_text_div {
        padding: 10px 20px;
    }






    .right {
        display: none;
    }

    .left {
        width: 100%;
        margin: 0 auto;
    }

    .footer_box {
        width: 100%;
        margin-top: 20px;
    }

    .footer {
        width: 96%;
        margin: 0 auto;
    }
}

@media (max-width: 767px) {
    .header_nav ul {
        padding-left: 0;
    }

    .header_logo {
        width: 80%;
        float: left;
        height: 100%;
        text-align: left;
    }

    .header_search {
        width: 40px;
        float: left;
        height: 100%;
        position: relative;
    }

    .header_search a {
        position: absolute;
        width: 100%;
        height: 100%;
    }

    .header_search_btn i {
        width: 30px;
        height: 30px;
        display: block;
        margin: 13px 0 0 5px;
        background: url("./img/search_small.png");
        background-size: 100% 100%;
    }

    .header_nav_small_btn {
        display: block;
        width: 28px;
        float: right;
        height: 36px;
        margin-top: 10px;
    }

    .small_btn:before {
        margin-top: -10px;
    }

    .small_btn:after {
        margin-top: 10px;
    }

    .banner_box {
        height: 158px;
    }

    .index_article .article_list {
        width: 100%;
        display: block;
        padding: 20px 0 20px 0;
    }

    .index_article .article_list .article_list_img {
        display: inline-block;
        font-size: 0;
        /* float: left; */
        margin-left: 0;
        width: 100%;
    }

    .index_article .article_list .article_list_img img {
        width: 100%;
        padding: 0 20px 10px 20px;
        vertical-align: middle;
    }

    .article_btn_nav {
        overflow-x: auto;
        padding: 0 0 16px 0;
    }

    .article_btn_nav>ul {
        width: 800px;
        overflow-x: scroll;
    }

    .article_btn_box {
        padding: 10px 20px 20px 20px;
    }

    .article_btn_box_item_img {
        width: 100%;
        margin-left: 0;
        margin-bottom: 10px;
    }

    .article_btn_box_item_img img {
        width: 100%;
    }

    .article_btn_box_item ul li a {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .footer_img {
        overflow: hidden;
        width: 100%;
        margin-right: 0;
        text-align: center;
        float: left;
    }

    .footer_img ul {
        display: inline-block;
        margin: 0 auto;
    }

    .footer_img ul li img {
        width: 170px;
        height: 170px;
    }

    .footer_text {
        float: left;
        padding: 20px 20px 0 20px;
    }
}

@media (max-width: 376px) {
    .header_nav_small_btn {
        width: 24px;
    }

    .header_logo h2 {
        font-size: 22px;
    }

    .header_logo h4 {
        font-size: 16px;
    }

    .footer_img ul li img {
        width: 160px;
        height: 160px;
    }
}

@media (max-width: 362px) {
    .footer_img ul li img {
        width: 150px;
        height: 150px;
    }
}
</style>