<!--
 @prettier
-->

<template>
  <div class="back">
    <div class="searchBox">
      <div class="searchBoxTitle">
        <b>搜索内容</b>
      </div>
      <div class="searchBar">
        <form action="" @submit="search()">
          <!--用submit可以实现回车搜索，很方便哦-->
          <input id="searchText" class="searchInput" v-model="searchContent" />
          <button id="searchBtn" class="searchButton" type="submit">
            搜索
          </button>
        </form>
      </div>
    </div>
    <div class="searchResultBox hide">
      <div v-for="(res, index) in searchResult" class="searchResult">
        <hr v-if="index > 0" />
        <div class="searchResultSingleBox">
          <div class="searchResultTitle">{{ res.title }}</div>
          <div class="searchResultDesc">{{ res.desc }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const chalk = require("chalk");
export default {
  data() {
    return {
      searchContent: "",
      searchResult: [
        {
          title: "你网速太慢啦",
          desc:
            "而且不应该看到这玩意儿的测试大汉当爱竞答三开韩海军爱当爱看档卡机海景昂丹卡还卡机方法拆所产爱o迪奥但奥迪偶爱较大大海爱思阿萨施耐庵静宁"
        },
        {
          title: "你网速太慢啦",
          desc:
            "而且不应该看到这玩意儿的测试大汉当爱竞答三开韩海军爱当爱看档卡机当爱竞答三开韩海军爱当爱看档卡机当爱竞答三开韩海军爱当爱看档卡机海景昂丹卡还卡机方法拆所产爱o迪奥但奥迪偶爱较大大海爱思阿萨施耐庵静宁"
        }
      ],
      haveResult: false
    };
  },
  mounted() {
    console.log(chalk.default.blue("Have a nice day!"));
  },
  methods: {
    search: function() {
      console.log(chalk.default.red("[Debug]") + "Search Button Clicked");
      let text = this.searchContent;
      /* 这里是要放ajax的 */
      this.changeLayout();
    },
    changeLayout: function() {
      console.log(chalk.default.red("[Debug]") + "Layout Changed");
      document.getElementsByClassName("searchBox")[0].classList.add("up");
      document
        .getElementsByClassName("searchResultBox")[0]
        .classList.remove("hide");
    }
  }
};
</script>

<style>
/* 搜索结果部分 */
.searchResultSingleBox:hover{
  background: rgb(194, 194, 194);
  transition-duration: 0.4s;
}
.searchResultSingleBox{
  border-radius: 8px;
  padding: 5px;
  transition-duration: 0.4s;
}
.searchResultTitle{
  margin: 5px 0 5px;
  font-size: large;
  font-weight: bold;
  max-lines: 1;
}
.searchResultDesc{
  font-size: 1em;
  font-weight: lighter;
  font-family: serif;
  max-lines: 2;
}
.searchResultBox.hide {
  visibility: hidden;
}
.searchResultBox {
  height: 400px;
  width: 600px;
  overflow: auto;
  margin: 0 auto 200px;
  padding: 20px;
  border-radius: 24px;
  background: #fff;
  box-shadow: 2px 2px 10px black;
  transition-duration: 0.5s;
}

/* 搜索栏部分 */
.searchBar {
  width: 100%;
  height: 40px;
  background: white;
  border-radius: 24px;
  box-shadow: 2px 2px 10px black;
}
.searchButton:active {
  background: rgb(0, 153, 153);
}
.searchButton:hover {
  transition-duration: 0.4s;
  background: aqua;
}
.searchButton {
  transition-duration: 0.4s;
  margin: 0px;
  width: 60px;
  background: rgb(0, 206, 206);
  font-weight: lighter;
  font-family: sans-serif;
  font-size: 1em;
  color: #fff;
  border: 0px;
  border-radius: 24px;
}
.searchInput {
  width: 480px;
  margin: 10px 15px auto 20px;
  font-size: 16px;
  background-color: transparent;
  border: 0px;
}
.searchBoxTitle {
  margin: 0 0 25px;
  font-size: xx-large;
  font-weight: bold;
  letter-spacing: 0.2rem;
  color: white;
  font-family: sans-serif;
  text-align: center;
}
.searchBox.up {
  margin: 40px auto 40px;
  transition-duration: 0.5s;
}
.searchBox {
  width: 600px;
  /* border: 2px solid grey; */
  margin: 200px auto;
}
.back {
  margin: 0;
  background: url("../../picture/background.jpg") no-repeat;
  background-size: cover;
  height: 100%;
  width: 100%;
  position: fixed;
  font-family: sans-serif;
}
</style>