<template>
    <div>
        <div class="comment_box">
            <div class="sender">
                <!--评论内容-->
                <img :src="imgUrl" />
                <p>{{ title_info() }}</p>
            </div>
            <p style="white-space: pre-line" class="comment_content">{{ content }}</p>
            <div class="base_line">
                <div class="comment_time">
                    <p>{{ create_time }}</p>
                </div>
                <div class="comment_btn">
                    <button @click="send_comment">回复消息</button>
                </div>
                <div class="like_btn" @click="point_likes">
                    <img v-if="be_like" src="./like_yes.png">
                    <img v-else src="./like_no.png">
                </div>
                <p>{{ this.likes }}</p>
            </div>
            <div class="input_comment" v-show="show_input">
                <textarea placeholder="输入评论" :id="id"></textarea>
                <button :id="button_id()" @click="comment_this">发布</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "cline",
    inject: ['reload'],
    data() {
        return {
            imgUrl: "",
            username: "",
            show_input: false,
            to_name: "",
            be_like: false,
            likes: 0,
            likes_uid: [],
        }
    },
    props: {
        id: {
            type: Number,
            default: 0
        },
        fa: {
            type: Number,
            default: 0
        },
        cid: {
            type: Number,
            default: 0
        },
        likes_num: {
            type: Number,
            default: 0
        },
        content: {
            type: String,
            default: "没有内容",
        }, create_time: {
            type: String,
            default: "0-0-0",
        }, uid: {
            type: Number,
            default: 1,
        }, artid: {
            type: Number,
            default: 0,
        }, toid: {
            type: Number,
            default: 0,
        }, likes_list: {
            type: Array,
            default: [],
        }
    },
    mounted() {
        //开始时需要获取用户的头像
        let params = new URLSearchParams();
        params.append('uid', this.cid);
        this.$axios.post("http://127.0.0.1:5000/comment/get_sender", params).then((res) => {
            this.imgUrl = res.data['headshot'];
            this.username = res.data['username'];
        });
        let params_2 = new URLSearchParams();
        params_2.append('uid', this.toid);
        if (this.fa != 0) {
            this.$axios.post("http://127.0.0.1:5000/user/get_userinfo", params_2).then((res) => {
                this.to_name = res.data['username'];
            });
        }
        var textarea = document.getElementById(this.id);
        textarea.addEventListener('input', (e) => {
            textarea.style.height = '30px';
            textarea.style.height = e.target.scrollHeight + 'px';
            var button = document.getElementById(this.button_id());
            button.style.marginTop = (e.target.scrollHeight - 30) + 'px';
            if (textarea.value != "") button.style.backgroundColor = 'rgb(18,18,242)';
            else button.style.backgroundColor = 'rgb(168, 168, 253)';
        });
        this.likes = this.likes_num;
        this.likes_uid = this.likes_list;
        for (var i = 0; i < this.likes; ++i) {
            if (this.likes_uid[i] == this.uid) {
                this.be_like = true;
                break;
            }
        }
    },
    methods: {
        like_id() {
            return 'like' + this.id;
        }, comment_this() {
            var ele = document.getElementById(this.id);
            var itext = ele.value;
            if (itext == '') return;
            let params = new URLSearchParams();
            params.append('artid', this.artid);
            params.append('uid', this.uid);
            params.append('fa', this.fa);//传递这个的爸爸
            params.append('cid', this.cid);//传递这个的cid
            params.append('id', this.id);//传递这个的id
            params.append('content', itext);//传递这个的内容
            this.$axios.post("http://127.0.0.1:5000/comment/sent_comment", params).then((res) => {
                this.reload();
            });
            this.show_input = false;
        }, send_comment() {
            this.show_input = !this.show_input;
        }, title_info() {
            if (this.toid == 0) return this.username;
            else return this.username + " 回复 " + this.to_name;
        }, button_id() {
            return this.id + 'button';
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
            this.$axios.post("http://127.0.0.1:5000/comment/point_likes", params).then((res) => {
                console.log(res.data);
            });
            this.be_like = !this.be_like;
        }
    }
}
</script>

<style scoped>
.sender img {
    display: block;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    overflow: hidden;
    border: rgb(14, 26, 203) solid;
    margin-top: 2%;
    margin-left: 1%;
}

.sender {
    display: flex;
}

.sender p {
    font-weight: bolder;
    margin-left: 1%;
}

.comment_box {
    width: 100%;
}

.comment_content {
    margin-top: -2%;
    margin-left: 6.2%;
    width: 90%;
}

.comment_time {
    margin-top: -2%;
    margin-left: 6.2%;
    color: gray;
    font-size: 5px;
}

.base_line {
    display: flex;
}

.base_line .comment_btn {
    width: 100%;
    flex: 1;
    display: flex;
    justify-content: flex-end;
}

.base_line .comment_btn button {
    margin-top: -2%;
    margin-right: 10px;
    background-color: transparent;
    border: 0px;
    background: url(../../picture/comment.png) no-repeat;
    background-size: 80%;
    background-position: 0px -6px;
    color: transparent
}

.like_btn img {
    margin-top: -30%;
    background-size: 100%;
    height: 30px;
    width: 30px;
    margin-right: 0px;
}

.base_line p {
    margin-right: 190px;
    margin-top: -0.7%;
}

.input_comment textarea {
    margin-left: 6.3%;
    width: 60%;
    height: 30px;
    overflow: hidden;
    resize: none;
    min-height: 30px;
}

.input_comment button {
    z-index: 100;
    position: absolute;
    width: 50px;
    height: 25px;
    margin-left: -55px;
    margin-top: 5px;
    border-color: transparent;
    border-radius: 5px;
    color: white;
    font-weight: bolder;
    background-color: rgb(168, 168, 253);
}
</style>