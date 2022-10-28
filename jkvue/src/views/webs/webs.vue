<template>
    <div>
        <mavon-editor class="md" :value="content" :subfield="prop.subfield" :defaultOpen="prop.defaultOpen"
            :toolbarsFlag="prop.toolbarsFlag" :editable="prop.editable" :scrollStyle="prop.scrollStyle" />
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
            content: '<!DOCTYPE html><title>hahaha</title><body><p>hahaha</p></body>',
            id: 0,
        }
    }, mounted() {
        this.id = this.$route.params.id;
        console.log(this.id);
        //获取网页信息
        //content通过数据库获取
        let params = new URLSearchParams();
        params.append('id', this.id);
        this.$axios.post("http://127.0.0.1:5000/content", params).then((res) => {
            console.log(res.data['code']);
            if (res.data['code'] == 414) {
                this.content = res.data['content'];
                console.log(this.content);
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
* {
    margin: 0;
    padding: 0;
}
</style>