<template>
    <div>
        <Content :content="content" />
    </div>
</template>

<script>
import Content from '@/components/content.vue'
export default {
    components: {
        Content
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
        this.axios.post("http://127.0.0.1:5000/content", params).then((res) => {
            console.log(res.data['code']);
            if (res.data['code'] == 414) {
                this.content = res.data['content'];
            }
        })
    }, methods: {

    }
}
</script>
<style>
* {
    margin: 0;
    padding: 0;
}
</style>