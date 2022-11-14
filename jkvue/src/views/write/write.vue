<template>
    <div class="markdown">
        <div class="title_tags_submit">
            <input v-model="title" class="input_title" placeholder="请输入标题" />
            <button class="wtag_button" v-on:click="show_tag_list($event)">
                <!--标签筛选-->
                Tags
            </button>
            <div id="wtag_list" v-show="show_tag">
                <div v-for="(tg, index) in all_tags">
                    <button v-bind:id="tagid(index)" class="wctag_button" v-on:click="chooseTag($event)">
                        {{ tg }}
                    </button>
                </div>
            </div>
            <button v-press="handleClickLong" id="submit_icon">提交</button>
        </div>
        <div class="container">
            <mavon-editor v-model="content" ref="md" @imgAdd="$imgAdd" @change="change" style="min-height: 600px" />
        </div>
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import press from '../../../src/assets/js/press'
export default {
    name: "",
    props: [],
    components: {
        mavonEditor,
    },
    directives: {
        press
    },
    data() {
        return {
            show_tag: false,
            content: '',
            html: '',
            configs: {},
            title: '',
            uid: -1,
            timeOutEvent: 0, //记录触摸时长
            c_tags: [],
            //全部的标签
            all_tags: ["science", "study", "work", "food", "arts", "news", "cpu", "physics", "music", "math", "foreign", "daily", "school", "base"],
        }
    },
    methods: {
        // 将图片上传到服务器，返回地址替换到md中
        // 绑定@imgAdd event
        $imgAdd(pos, $file) {
            // 第一步.将图片上传到服务器.
            console.log($file);
            var formdata = new FormData();
            formdata.append('image', $file);
            formdata.append('uid', this.uid);
            formdata.append('title', this.title);
            this.$axios({
                url: 'http://127.0.0.1:5000/write/add_image',
                method: 'post',
                data: formdata
            }).then(res => {
                this.$refs.md.$img2Url(pos, res.data);
            })
        },
        // 所有操作都会被解析重新渲染
        change(value, render) {
            // render 为 markdown 解析后的结果[html]
            this.html = render;
        },
        // 提交
        submit() {
            //将html转移至数据库的content中
            if (this.title == null) {
                alert('请输入标题');
            }
            else {
                var tags = '';
                for (var i = 0; i < this.c_tags.length; ++i) {
                    tags += this.all_tags[this.c_tags[i]];
                    if (i != this.c_tags.length - 1) tags += ',';
                }
                console.log(tags);
                let params = new URLSearchParams();
                params.append('artical', this.html);
                params.append('title', this.title);
                params.append('uid', this.uid);
                params.append('tags', tags);
                this.$axios.post("http://127.0.0.1:5000/write/submit", params).then((res) => {
                    console.log(this.title);
                    console.log(this.uid);
                    console.log(tags);
                    console.log(this.html);
                    //接受返回值
                    if (res.data == 416) {
                        console.log("文章发布成功");
                        alert('文章发布成功!');
                        setTimeout(function () {
                            this.$router.push({ name: "user", params: { uid: this.uid } });
                        }.bind(this), 1000)
                    }
                    else {
                        console.log("文章发布失败");
                    }
                });
            }
        },
        handleClickLong() {
            this.submit();
        }, show_tag_list(event) {
            this.show_tag = !this.show_tag;
            var l = this.all_tags.length;
            for (var i = 0; i < l; ++i) {
                var tgname = 'tag' + i;
                var tg = document.getElementById(tgname).style;
                tg.marginLeft = 5 + 84 * (i % 5) + 'px';
                tg.marginTop = 9 + 49 * Math.floor(i / 5) + 'px';
            }
            if (this.show_tag == true) {
                var el = event.currentTarget;//获取了标签
                el.style.border = '2px solid rgb(31, 83, 226)';
                el.style.color = 'rgb(31, 83, 226)';
            } else {
                var el = event.currentTarget;//获取了标签
                el.style.border = '2px solid rgb(154, 151, 151)';
                el.style.color = 'rgb(154, 151, 151)';
            }
        }, tagid(index) {
            return "tag" + index;
        }, chooseTag(event) {
            //转化为Other
            //首先从el中获取标签序号
            var com = event.currentTarget;
            var el = com['id'];
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

                com.style.border = '2px solid rgb(31, 83, 226)';
                com.style.color = 'rgb(31, 83, 226)';
            }
            else {
                this.c_tags = this.c_tags.filter(function (item) {
                    return item != index;
                })
                com.style.border = '2px solid rgb(154, 151, 151)';
                com.style.color = 'rgb(154, 151, 151)';
            }
            console.log(this.c_tags);
        },
    },
    mounted() {
        this.title = this.$route.params.title;
        this.uid = this.$route.params.uid;
    },
}
</script>

<style>
.title_tags_submit {
    margin: 15px;
}

.input_title {
    outline: none;
    border: none;
    border-bottom: 2px solid rgb(154, 151, 151);
    font-size: 18px;
    height: 25px;
    width: 300px;
    margin-left: 50px;
    transition: all 0.5s;
}

.input_title:focus {
    border-bottom: 2px solid rgb(31, 83, 226);
    transition: all 0.5s;
}

#submit_icon {
    margin-left: 1000px;
    height: 40px;
    width: 80px;
    border-radius: 40px;
    font-size: 15px;
    background: url(../../picture/circle.png) no-repeat;
    background-size: 120%;
    background-position: -92px -25px;
    font-weight: bold;
    transition: all 0.5s;
}

#submit_icon:active {
    background-position: -10px -25px;
    transition: all 2s;
}

.wtag_button {
    outline: none;
    height: 40px;
    width: 80px;
    border-radius: 40px;
    font-size: 18px;
    font-weight: bold;
    position: fixed;
    transition: all 0.5s;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
}

.wctag_button {
    outline: none;
    height: 40px;
    width: 80px;
    border-radius: 40px;
    font-size: 18px;
    font-weight: bold;
    position: fixed;
    transition: all 0.5s;
    position: fixed;
    border: 2px solid rgb(154, 151, 151);
    color: rgb(154, 151, 151);
}

#wtag_list {
    margin-left: 355px;
    margin-top: 15px;
    z-index: 10000;
    height: 200px;
    width: 430px;
    background-color: rgb(255, 255, 255);
    position: fixed;
    border-radius: 20px;
    border: solid;
}
</style>