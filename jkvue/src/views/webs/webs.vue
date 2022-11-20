<template>
    <div>
        <div class="back">{{ this.title }}</div>
        <img id="logo" src="../../picture/mylogo.png" />
        <img :src="headshot" id="user" v-on:click="goto_user" />
        <div class="artical_box">
            <div class="title_box">
                <h2>{{ this.title }}</h2>
                <p>{{ this.tags }}</p>
            </div>
            <mavon-editor class="md" :value="content" :subfield="prop.subfield" :defaultOpen="prop.defaultOpen"
                :toolbarsFlag="prop.toolbarsFlag" :editable="prop.editable" :scrollStyle="prop.scrollStyle" />
            <div class="see_likes">
                <img src="./eye.png">
                <p>{{ this.clicks }}</p>
                <div class="like_btn" @click="point_likes">
                    <img v-if="be_like" src="./like_yes.png">
                    <img v-else src="./like_no.png">
                </div>
                <p class="likes_num">{{ this.likes }}</p>
                <div class="collect_btn" @click="point_collect">
                    <img v-if="be_collect" src="./star_yes.png">
                    <img v-else src="./star_no.png">
                </div>
                <p class="collect_num">{{ this.collect_num }}</p>
            </div>
            <comment :artid="id" :uid="uid" class="co_box"></comment>
        </div>
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import comment from '../comment/comment.vue'
import 'mavon-editor/dist/css/index.css'
export default {
    components: {
        mavonEditor,
        comment,
    },
    data() {
        return {
            title: '',
            content: '<!DOCTYPE html><title>hahaha</title><body><p>hahaha</p></body>',
            id: Number(this.$route.params.id),
            uid: Number(this.$route.params.uid),
            headshot: "",
            clicks: 0,
            be_like: false,
            likes: 0,
            be_collect: false,
            likes_uid: [],
            collect_num: 0,
            collection: [],
            tags: [],
        }
    }, mounted() {
        //获取网页信息
        //content通过数据库获取
        let params = new URLSearchParams();
        params.append('id', this.id);
        this.$axios.post("http://127.0.0.1:5000/content", params).then((res) => {
            if (res.data['code'] == 414) {
                this.content = res.data['content'];
                this.title = res.data['title'];
                this.clicks = res.data['clicks'];
                this.likes = res.data['likes'];
                this.likes_uid = res.data['likes_uid'];
                this.collect_num = res.data['collect_num'];
                this.collection = res.data['collection'];
                this.tags = res.data['tags'];
                if (this.tags == "") this.tags = 'all';
                for (var i = 0; i < this.likes; ++i) {
                    if (this.likes_uid[i] == this.uid) {
                        this.be_like = true;
                        break;
                    }
                }
                for (var i = 0; i < this.collect_num; ++i) {
                    if (this.collection[i] == this.uid) {
                        this.be_collect = true;
                        break;
                    }
                }
            }
        })
        let params2 = new URLSearchParams();
        params2.append('uid', this.uid);
        this.$axios.post('http://127.0.0.1:5000/user/get_userinfo', params2).then(res => {
            this.headshot = res.data['headshot'];
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
    }, methods: {
        goto_user() {
            setTimeout(function () {
                this.$router.push({ name: "user", params: { uid: this.uid } });
            }.bind(this), 1000)
        }, point_likes() {
            //本地修改是否点赞的同时向服务器传递信息
            let params = new URLSearchParams();
            params.append('uid', this.uid);
            params.append('id', this.id);
            if (this.be_like == false) {
                this.likes_uid.push(this.uid);
                this.likes++;
                params.append('choose', true);
            } else {
                var newli = [];
                for (var i = 0; i < this.likes; ++i) {
                    if (this.likes_uid[i] != this.uid) {
                        newli.push(this.likes_uid[i]);
                    }
                }
                this.likes--;
                this.likes_uid = newli;
                params.append('choose', false);
            }
            this.$axios.post("http://127.0.0.1:5000/point_likes", params).then((res) => {
                console.log(res.data);
            });
            this.be_like = !this.be_like;
        }, point_collect() {
            let params = new URLSearchParams();
            params.append('uid', this.uid);
            params.append('id', this.id);
            if (this.be_collect == false) {
                this.collection.push(this.uid);
                this.collect_num++;
                params.append('choose', true);
            } else {
                var newli = [];
                for (var i = 0; i < this.likes; ++i) {
                    if (this.collection[i] != this.uid) {
                        newli.push(this.collection[i]);
                    }
                }
                this.collect_num--;
                this.collection = newli;
                params.append('choose', false);
            }
            this.$axios.post("http://127.0.0.1:5000/user/point_collect", params).then((res) => {
                console.log(res.data);
            });
            this.be_collect = !this.be_collect;
        }
    }
}
</script>
<style scoped>
.title_box {
    display: flex;
}

.title_box p {
    font-size: 5px;
    color: gray;
    margin-top: 40px;
    margin-left: 5px;
}

.back {
    background: url("../../picture/background.jpg") no-repeat;
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
    margin-top: -60px;
    z-index: -10;
}

.co_box {
    padding: 10px;
    margin-left: -10%;
    border-radius: 10px;
}

.artical_box {
    margin-top: 60px;
    padding: 10px;
    width: 70%;
    background-color: white;
    border: gray solid;
    margin-left: 15%;
    border-radius: 14px;
    box-shadow: 2px 2px 10px rgb(255, 255, 255);
}


.artical_box .title_box h2 {
    margin-left: 3%;
}

#logo {
    margin-top: -50px;
    margin-left: -5px;
    height: 60px;
    width: 80px;
    border-radius: 10px;
    position: fixed;
}

#user {
    background-size: contain;
    margin-top: -50px;
    margin-left: 1425px;
    height: 50px;
    width: 50px;
    border-radius: 50px;
    position: fixed;
    background-color: rgb(153, 227, 219);
    text-align: center;
    border: solid rgb(81, 255, 0) 3px;
}

.see_likes p {
    color: gray;
    font-size: 15px;
    margin-top: 16px;
}

.see_likes {
    box-shadow: 2px 2px 4px rgb(177, 177, 177);
    height: 40px;
    display: flex;
}

.see_likes img {
    margin-left: 20px;
    margin-top: 10px;
    height: 30px;
    width: 30px;
    opacity: 50%;
}
</style>