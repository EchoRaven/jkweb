<template>
    <div class="markdown">
        <div class="container">
            <mavon-editor v-model="content" ref="md" @imgAdd="$imgAdd" @change="change" style="min-height: 600px" />
            <button @click="submit">提交</button>
        </div>
    </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
export default {
    name: "",
    props: [],
    components: {
        mavonEditor,
    },
    data() {
        return {
            content: '',
            html: '',
            configs: {},
            title: '',
            uid: -1,
            tags: 'base',
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
            let params = new URLSearchParams();
            params.append('artical', this.html);
            params.append('title', this.title);
            params.append('uid', this.uid);
            params.append('tags', this.tags);
            this.$axios.post("http://127.0.0.1:5000/write/submit", params).then((res) => {
                console.log(this.title);
                console.log(this.uid);
                console.log(this.tags);
                console.log(this.html);
                //接受返回值
                if (res.data == 416) {
                    console.log("文章发布成功");
                }
                else {
                    console.log("文章发布失败");
                }
            });
        }
    },
    mounted() {
        this.title = this.$route.params.title;
        this.uid = this.$route.params.uid;
        console.log('标题' + this.title);
        console.log('用户' + this.uid);
    }
}
</script>