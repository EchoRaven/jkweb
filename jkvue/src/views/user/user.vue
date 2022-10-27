<template>
    <div>
        <!--将作者id，标题等信息传递到下一个页面-->
        <input v-model="title" />
        <button v-on:click="submit">submit</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            uid: -1,
            title: "",
        }
    },
    mounted() {
        this.uid = this.$route.params.uid;
        console.log(this.uid);
    },
    methods: {
        submit() {
            console.log(this.uid + " " + this.title);
            setTimeout(function () {
                this.$router.push({ name: "write", params: { "uid": this.uid, "title": this.title } });
            }.bind(this), 1000)
        }
    }
}
</script>

<style>

</style>