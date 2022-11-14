<template>
    <div>
        <div class="artical_box">
            <mavon-editor class="md" :value="content" :subfield="prop.subfield" :defaultOpen="prop.defaultOpen"
                :toolbarsFlag="prop.toolbarsFlag" :editable="prop.editable" :scrollStyle="prop.scrollStyle" />
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
            content: '<!DOCTYPE html><title>hahaha</title><body><p>hahaha</p></body>',
            id: Number(this.$route.params.id),
            uid: Number(this.$route.params.uid),
        }
    }, mounted() {
        //获取网页信息
        //content通过数据库获取
        let params = new URLSearchParams();
        params.append('id', this.id);
        this.$axios.post("http://127.0.0.1:5000/content", params).then((res) => {
            if (res.data['code'] == 414) {
                this.content = res.data['content'];
            }
        })
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
}
</script>
<style>
.co_box {
    padding: 10px;
    margin-left: -10%;
}

.artical_box {
    margin-top: 30px;
    padding: 10px;
    width: 70%;
    border: gray solid;
    margin-left: 15%;
}
</style>