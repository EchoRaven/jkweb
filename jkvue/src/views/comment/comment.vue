<template>
    <div>
        <div class="comment_area">
            <!--这里是评论区的测试-->
            <!--评论区应当包括一级评论和二级评论-->
            <!--储存内容包括:文章id，点赞数，爸爸，内容，发布时间-->
            <div class="send_root">
                <textarea placeholder="对作品发表自己的评论吧" id="st"></textarea>
                <button @click="send_root" id="sb">发布</button>
            </div>
            <div id="comment_box" v-for="(index) in root">
                <cline :uid="uid" :id="id[index]" :cid="cid[index]" :fa="fa[index]" :content="content[index]"
                    :likes="likes[index]" :create_time="create_time[index]" :artid="artid" :toid="toid[index]" />
                <div v-for=" (idx) in c_tree[id[index]]">
                    <cline class="second_comment" :uid="uid" :id="id[idx]" :cid="cid[idx]" :fa="fa[idx]"
                        :content="content[idx]" :likes="likes[idx]" :create_time="create_time[idx]" :artid="artid"
                        :toid="toid[idx]" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import cline from './cline.vue'
export default {
    inject: ['reload'],
    components: {
        cline,
    },
    props: {
        uid: {
            type: Number,
            default: 1,
        }, artid: {
            type: Number,
            default: 1,
        },
    },
    data() {
        return {
            c_tree: [[]],//这是一个二维数组
            fa: [],
            id: [],
            likes: [],
            cid: [],
            content: [],
            root: [],//根
            create_time: [],
            toid: [],
        }
    },
    mounted() {
        //初始化的时候获取所有的关于该评论区的节点，并建立一棵树
        //根据文章获取所有的评论信息
        let params = new URLSearchParams();
        params.append('artid', this.artid);
        this.$axios.post("http://127.0.0.1:5000/comment/get_comment", params).then((res) => {
            //获取评论
            //逻辑是:先获取所有的信息，然后找到所有父亲为0的节点
            //然后建立一棵树
            this.fa = res.data['fa'];
            this.id = res.data['id'];
            this.likes = res.data['likes'];
            this.cid = res.data['uid'];
            this.content = res.data['content'];
            this.create_time = res.data['create_time'];
            this.toid = res.data['toid'];
            for (var i = 0; i < this.fa.length; ++i) {
                if (this.fa[i] == 0) this.root.push(i);//存入根
                var temp = [];
                for (var j = 0; j < this.fa.length; ++j) {
                    if (this.fa[j] == this.id[i]) {
                        temp.push(j);
                    }
                }
                this.c_tree.push(temp);
            }
        })
        var textarea = document.getElementById('st');
        textarea.addEventListener('input', (e) => {
            textarea.style.height = '30px';
            textarea.style.height = e.target.scrollHeight + 'px';
            var button = document.getElementById('sb');
            button.style.marginTop = (e.target.scrollHeight - 30) + 'px';
            if (textarea.value != "") button.style.backgroundColor = 'rgb(18,18,242)';
            else button.style.backgroundColor = 'rgb(168, 168, 253)';
        });
    },
    methods: {
        send_root() {
            var ele = document.getElementById('st');
            var itext = ele.value;
            if (itext == '') return;
            let params = new URLSearchParams();
            params.append('artid', this.artid);
            params.append('uid', this.uid);
            params.append('0', this.fa);//传递这个的爸爸
            params.append('0', this.cid);//传递这个的cid
            params.append('0', this.id);//传递这个的id
            params.append('content', itext);//传递这个的内容
            this.$axios.post("http://127.0.0.1:5000/comment/sent_comment", params).then((res) => {
                console.log(res.data);
                this.reload();
            });
        }
    }
}
</script>

<style>
.send_root {
    width: 700px;
    border: transparent;
}

.send_root textarea {
    margin-left: 2%;
    width: 70%;
    height: 30px;
    overflow: hidden;
    resize: none;
    min-height: 30px;
}

.send_root button {
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

#comment_box {
    width: 700px;
    border: transparent;
}

.second_comment {
    padding-left: 5%;
    box-sizing: border-box;
}

.comment_area {
    border: rgb(169, 168, 168) solid;
    padding-top: 20px;
    padding-bottom: 20px;
    width: 580px;
    margin-left: 25%;
    padding-left: 50px;
    border-radius: 10px;
}
</style>